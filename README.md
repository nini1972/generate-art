# Generate Art

An art generator tool that creates artwork based on the current day and time.

## Features

- **Fetches current day and hour** - Automatically gets the current time
- **Day → Semantic Concept Mapping**:
  - Monday: structured geometric shapes
  - Tuesday: minimalist lines
  - Wednesday: balanced symmetry
  - Thursday: dynamic abstract flow
  - Friday: playful colorful patterns
  - Saturday: organic nature-inspired
  - Sunday: calm watercolor tones
- **Hour → Numeric Influence**:
  - Rotation angle (0-345°)
  - Color hue shift
  - Size scaling
  - Saturation and brightness
  - Shape complexity
- **Generates AI art prompts** for use with DALL·E, Stable Diffusion, etc.
- **Directly draws artwork** using the Pillow graphics library

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the art generator:

```bash
python generate_art.py
```

This will:
1. Get the current day and hour
2. Generate an AI art prompt based on the mappings
3. Create an actual artwork image in the `output/` folder
4. Display the prompt and file location

## Example Output

```
✅ Artwork generated successfully!
Day: Friday
Hour: 14:00
Day Concept: playful colorful patterns
Hour Influence: rotation=210°, hue_shift=210°
Prompt used: Generative digital artwork with playful colorful patterns and color palette with hue shift of 210 degrees, rotated 210 degrees, modern digital art style.
Mock Image URL: https://example.com/generated_art_1234.png
Generated Image: output/artwork_20231128_140000.png
```

## Running Tests

```bash
python test_generate_art.py
```

## How It Works

### Day Mapping
Each day of the week is mapped to a unique artistic concept:

| Day | Concept | Shape Style |
|-----|---------|-------------|
| Monday | structured | rectangles |
| Tuesday | minimalist | lines |
| Wednesday | balanced | symmetry |
| Thursday | dynamic | curves |
| Friday | playful | circles |
| Saturday | organic | blobs |
| Sunday | calm | waves |

### Hour Influence
The current hour (0-23) influences:
- **Angle**: `hour × 15` degrees (0° to 345°)
- **Size**: 50% to 100% scaling
- **Saturation**: Higher during midday
- **Brightness**: Simulates daylight (peaks at noon)
- **Complexity**: 3-10 elements based on time
- **Opacity**: 150-255 transparency level

