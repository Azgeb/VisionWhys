# AI Prompts
PROMPT_CONCISE = '''
You are an autonomous vehicle analyzing your environment through a camera feed. Based on the provided image, you have decided to come to a complete stop and not proceed further. Your task involves multiple steps:
Analyze the image thoroughly and provide a detailed explanation of your decision. Identify all relevant visual or contextual factors (e.g., pedestrians, roadblocks, other vehicles, traffic signs) that contributed to your choice to stop.
Select the single most critical object or region in the image that had the greatest influence on this decision.
Output the precise (x, y) coordinates of the center point of that object/region. This point must reflect the actual geometric center of the object or the most relevant part of it in terms of safety (e.g., pedestrian torso, vehicle body, etc.).
Justify clearly why this center point is correct, including how it was determined (e.g., bounding box center, contour centroid), and why this location best represents the core of the influencing factor.
Finally, output the center point in the following format, on a new line:
Rank 1 Center Point: (x, y)
'''

PROMPT_DETAILED = '''
You are an autonomous vehicle analyzing your environment through a camera feed. Based on the provided image, you have decided to come to a complete stop and not proceed further.

Your task:

1. Analyze the image and identify **the three most significant objects or regions** that contributed to the stop decision, ranked by importance:

   * **1** = most significant
   * **2** = second most significant
   * **3** = third most significant

2. For each object, output the **precise (x, y) coordinates of its center point**. This point should reflect the geometric center or the most safety-relevant part (e.g., pedestrian torso, vehicle body, sign face).

3. Format your final output **exactly** like this:
```
Rank 1 Center Point: (x1, y1)
Rank 2 Center Point: (x2, y2)
Rank 3 Center Point: (x3, y3)
```

Only include these three lines in the final output. Do not include any extra text or commentary.
'''

# Dictionary of available prompts
AVAILABLE_PROMPTS = {
    "concise": PROMPT_CONCISE,
    "detailed": PROMPT_DETAILED
}

# Model configuration
MODEL_CONFIG = {
    "repo_name": "cyan2k/molmo-7B-D-bnb-4bit",
    "arguments": {
        "device_map": "auto", 
        "torch_dtype": "auto", 
        "trust_remote_code": True
    }
}

# Visualization settings
HIGHLIGHT_SETTINGS = {
    1: {"radius": 200, "color": (0, 0, 255), "opacity": 0.5},    # Red for most critical
    2: {"radius": 150, "color": (0, 165, 255), "opacity": 0.4},  # Orange for second
    3: {"radius": 100, "color": (0, 255, 255), "opacity": 0.3},  # Yellow for third
}

# Image analysis settings
PROXIMITY_THRESHOLD = 0.15  # Default threshold for point filtering