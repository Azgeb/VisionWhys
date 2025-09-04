# AI Prompts
PROMPT_CONCISE = '''
You are an autonomous driving vehicle not only on established paths, analyzing a camera frame. You decided to come to a full stop rather than to continue for 5 meters:

1. Based on the input image, determine whether this decision was correct for the next 5 meters of movement.
2. Explain the decision in 2–4 sentences, focusing only on the input image.
3. Identify the single most critical object/region justifying a full stop (if correct).
4. Provide its center point as percentages of the image width/height:

   * Origin = top-left, x% → right, y% → down.
   * Round to 1 decimal place.

**Rules (rural-optimized):**

* Do not speculate or guess.
* If the path is partially unclear but shows usable continuation, prefer "correct."
* For multiple objects, prioritize the one **directly in the drivable path**. If tied, pick the closest.
* Do not infer beyond what is visible.

---

**Final Output Format (sections in order):**

```
Decision is: [CORRECT | INCORRECT]

Reasoned Decision:
[2–4 sentence explanation]

Most Critical Object/Region:
[Description]

Center-Point Determination:
* Coordinates (%): (x = ##.#%, y = ##.#%)
* Why: [Short justification]

Rank 1 Center Point: (x%, y%)
```


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