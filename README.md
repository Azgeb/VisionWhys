# VisionWhys

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.11.0-green.svg)
![Transformers](https://img.shields.io/badge/Transformers-4.48.2-orange.svg)

A computer vision tool that leverages multimodal AI to analyze aerial scenes and identify objects that caused an autonomous vehicle to arrive at a certain decision.

## 🚀 Features

- Identifies and ranks critical objects in aerial scenes
- Extracts precise coordinates of objects causing a decisions
- Visualizes results with color-coded highlights
- Supports multiple analysis strategies

## 📋 Requirements

- Python 3.10+
- PyTorch with CUDA support
- OpenCV
- Transformers library
- Other dependencies listed in `requirements.txt`

## 🛠️ Installation

1. Clone this repository:

```bash
git clone https://github.com/Azgeb/VisionWhys
cd VisionWhys
```

2. Create a virtual environment:

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔍 Usage

Run the main script and follow the interactive prompts:

```bash
python main.py
```

You'll be asked to:
1. Enter the path to an image file
2. Select a prompt strategy (concise or detailed)

### Example:

```
Model loaded successfully. Enter image paths to analyze or type 'exit' to quit.
Enter the path to the image (or type 'exit' to quit): data/images/stop/stop1.jpg
Select prompt strategy ['concise', 'detailed'] [default: concise]: detailed
```

The program will then:
- Analyze the image with the selected AI model
- Extract ranked coordinates of critical objects
- Display the image with highlighted objects

## ⚙️ How It Works

1. **Image Analysis**: The program uses the [cyan2k/molmo-7B-D-bnb-4bit](https://huggingface.co/cyan2k/molmo-7B-D-bnb-4bit) multimodal model to analyze images
2. **Object Detection**: The AI identifies and ranks objects based on their importance for a decision
3. **Coordinate Extraction**: Coordinates are parsed from the AI's text response
4. **Visualization**: Objects are highlighted with color-coded circles based on their rank (points that are too close together get ignored).

## ⚙️ Configuration

You can customize the behavior in `config/config.py`:

- **Prompt Strategies**: Modify `PROMPT_CONCISE` or `PROMPT_DETAILED` to change how the AI interprets images
- **Model Selection**: Change the model in `MODEL_CONFIG`
- **Visualization**: Adjust highlight colors, sizes and opacity in `HIGHLIGHT_SETTINGS`
- **Object Filtering**: Modify `PROXIMITY_THRESHOLD` to control how close objects can be without getting ignored

## 📁 Project Structure

```
├── main.py              # Main application script
├── config/
│   └── config.py        # Configuration settings
├── data/
│   └── images/          # Test images organized by category
│       ├── left/
│       ├── right/
│       └── stop/
└── requirements.txt     # Dependencies
```

## 🔧 Advanced Usage

- Add more prompts in `config/config.py` by extending the `AVAILABLE_PROMPTS` dictionary
- Modify the highlight visualization by changing parameters in `HIGHLIGHT_SETTINGS`
- Add your own image directories under `data/images` for different scenarios

## 📝 License

MIT License
Copyright (c) 2025 Azgeb