import cv2
import re
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig
from PIL import Image
import config.config as config

# Load processor and model
processor = AutoProcessor.from_pretrained(config.MODEL_CONFIG["repo_name"], **config.MODEL_CONFIG["arguments"])
model = AutoModelForCausalLM.from_pretrained(config.MODEL_CONFIG["repo_name"], **config.MODEL_CONFIG["arguments"])

def ask_ai(prompt, image):
    inputs = processor.process(images=[image], text=prompt)
    inputs = {k: v.to(model.device).unsqueeze(0) for k, v in inputs.items()}
    output = model.generate_from_batch(
        inputs,
        GenerationConfig(max_new_tokens=500, stop_strings="<|endoftext|>"),  # Increased tokens for 3 objects
        tokenizer=processor.tokenizer,
    )
    generated_tokens = output[0, inputs["input_ids"].size(1):]
    return processor.tokenizer.decode(generated_tokens, skip_special_tokens=True)

def extract_ranked_points(text, proximity_threshold=0.15):  # 5% of image dimension is default
    """Extract the three ranked center points, ignoring points too close to each other"""
    potential_points = []
    filtered_points = []
    
    # Match the simplified format from the prompt
    pattern = r"Rank (\d+) Center Point: \((\d+\.\d+), (\d+\.\d+)\)"
    matches = re.finditer(pattern, text)
    
    # Collect all potential points
    for match in matches:
        rank = int(match.group(1))
        x_percent = float(match.group(2)) / 100  # Convert to percentage
        y_percent = float(match.group(3)) / 100  # Convert to percentage
        
        potential_points.append({
            "rank": rank,
            "description": f"Object #{rank}",
            "coordinates": (x_percent, y_percent)
        })
    
    # Sort by rank (1 is highest priority)
    potential_points.sort(key=lambda p: p["rank"])
    
    # Filter out points that are too close to higher-ranked points
    for point in potential_points:
        too_close = False
        for existing_point in filtered_points:
            # Calculate Euclidean distance as percentage of image dimensions
            x1, y1 = point["coordinates"]
            x2, y2 = existing_point["coordinates"]
            distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
            
            if distance < proximity_threshold:
                too_close = True
                print(f"Ignoring point at {point['coordinates']} (rank {point['rank']}) - " 
                      f"too close to existing point at {existing_point['coordinates']} (rank {existing_point['rank']})")
                break
        
        if not too_close:
            filtered_points.append(point)
    
    return filtered_points

def load_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image from '{image_path}'")
    return img

def highlight_ranked_objects(image, ranked_points):
    """Highlight multiple objects with different colors based on their rank"""
    result = image.copy()
    height, width = image.shape[:2]
    
    for point in ranked_points:
        rank = point["rank"]
        settings = config.HIGHLIGHT_SETTINGS.get(rank)
        if not settings:
            continue
            
        # Convert normalized coordinates to pixel coordinates
        x_percent, y_percent = point["coordinates"]
        center_point = (int(x_percent * width), int(y_percent * height))
        
        # Create a mask for this object
        mask = image.copy()
        mask[:] = 0
        cv2.circle(mask, center_point, settings["radius"], settings["color"], -1)
        
        # Add label with rank and description
        label = f"#{rank}: {point['description']}"
        cv2.putText(mask, label, 
                    (center_point[0] - settings["radius"]//2, center_point[1] - settings["radius"] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, settings["color"], 2)
        
        # Blend the mask with the current result
        result = cv2.addWeighted(result, 1.0, mask, settings["opacity"], 0)
    
    return result

def display_image(image, window_name="Analyzed Scene"):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def analyze_image(image_path, prompt):
    img = load_image(image_path)
    if img is None:
        print("Error: Could not load image for analysis")
        return

    # Get AI response
    response = ask_ai(prompt, Image.open(image_path))
    print("AI Response:", response)
    
    # Extract all ranked points
    ranked_points = extract_ranked_points(response)
    
    if not ranked_points:
        print("Error: Could not extract any center points from analysis")
        return
    
    print(f"Found {len(ranked_points)} significant objects:")
    for point in ranked_points:
        print(f"Rank {point['rank']}: {point['description']} at {point['coordinates']}")
    
    # Highlight all objects and display
    highlighted_img = highlight_ranked_objects(img, ranked_points)
    display_image(highlighted_img, "Analyzed Scene - Ranked Objects")

def main():
    print("Model loaded successfully. Enter image paths to analyze or type 'exit' to quit.")
    while True:
        image_path = input("Enter the path to the image (or type 'exit' to quit): ").strip()
        if image_path.lower() == 'exit':
            print("Exiting the program.")
            break
        prompt_key = input(f"Select prompt strategy {list(config.AVAILABLE_PROMPTS.keys())} [default: concise]: ").strip().lower()
        if not prompt_key:
            prompt_key = "concise"
        analyze_image(image_path, config.AVAILABLE_PROMPTS[prompt_key])

if __name__ == "__main__":
    main()