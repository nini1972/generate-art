# Generate AI Art with GPT Image

This version uses OpenAI's GPT Image API (`gpt-image-1`) to generate artwork based on day and time mappings.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your OpenAI API key:**
   
   **Option 1: Environment Variable (Recommended)**
   ```powershell
   # Windows PowerShell
   $env:OPENAI_API_KEY = "your-api-key-here"
   
   # Or set permanently in Windows
   setx OPENAI_API_KEY "your-api-key-here"
   ```
   
   **Option 2: Direct in Code**
   Edit `generate_ai_art.py` and replace:
   ```python
   client = OpenAI()
   ```
   with:
   ```python
   client = OpenAI(api_key="your-api-key-here")
   ```

## Usage

Run the AI art generator:

```bash
python generate_ai_art.py
```

This will:
1. Get the current day and hour
2. Generate an AI art prompt based on the mappings plus any extra keywords you pass in
3. Call OpenAI's GPT Image API to create the artwork (unless you run `--dry-run`)
4. Download and save the image to `output/ai_artwork_YYYYMMDD_HHMMSS.png`

You can tailor the experience with command-line flags:

```
python generate_ai_art.py --keywords "sunset, neon" --style Surrealism --quality hd --size 1792x1024 --dry-run
```

### Command-Line Options

- `--keywords`: Add extra keywords or themes to the prompt
- `--style`: Override the randomly chosen style (choose from the documented list)
- `--quality`: Request `standard` (default) or `hd` quality
- `--size`: Choose `1024x1024`, `1792x1024`, or `1024x1792`
- `--model`: Select the OpenAI image model (defaults to `gpt-image-1`)
- `--dry-run`: Print the generated prompt and estimated cost without hitting the API
- `--seed`: Provide a seed to reproduce the same style & mood choices

## Example Output

```
✅ Prompt generated: Generative digital artwork with playful colorful patterns and color palette with hue shift of 240 degrees, rotated 240 degrees, modern digital art style.
Day: Friday
Hour: 16:00
Generating image with GPT Image API...
✅ Image generated successfully!
Image URL: https://oaidalleapiprodscus.blob.core.windows.net/...
✅ Artwork saved locally as: output/ai_artwork_20251128_165341.png
```

## Configuration

### Model Options
- `gpt-image-1` – GPT Image endpoint (successor to the previous OpenAI image models)

### Quality Options
- `standard` – Standard quality (default)
- `hd` – High definition (available on GPT Image)

### Size Options
- `1024x1024` – Square (default)
- `1792x1024` – Landscape
- `1024x1792` – Portrait

## Cost Estimate

**GPT Image (`gpt-image-1`):**
- Standard quality (1024x1024): ~$0.04 per image
- HD quality (1024x1024): ~$0.08 per image

## Features

✅ **Local image saving** - Images are automatically downloaded and saved to `output/` folder  
✅ **Error handling** - Graceful error messages if API fails  
✅ **Timestamp naming** - Files named with timestamp for organization  
✅ **Environment variable support** - Secure API key management  
✅ **Command-line control** - Customize keywords, style, size, quality, and run `--dry-run` costing  
✅ **Progress feedback** - Clear console output during generation  

## Differences from Local Version

| Feature | `generate_art.py` | `generate_ai_art.py` |
|---------|-------------------|----------------------|
| Requires API | ❌ No | ✅ Yes (OpenAI) |
| Cost | Free | ~$0.04 per image |
| Quality | Good | Excellent (AI-generated) |
| Speed | Instant | ~10-30 seconds |
| Offline | ✅ Works offline | ❌ Requires internet |
| Customization | Algorithmic patterns | AI interpretation |

## Troubleshooting

**Error: OpenAI API key not found**
- Set the `OPENAI_API_KEY` environment variable
- Or modify the code to include your API key directly

**Error: Rate limit exceeded**
- Wait a few minutes and try again
- Check your OpenAI API usage limits

**Error: Insufficient credits**
- Add credits to your OpenAI account at platform.openai.com

## Next Steps

Once you have your API key:
1. Set it as an environment variable
2. Run `python generate_ai_art.py`
3. Check the `output/` folder for your AI-generated artwork!
