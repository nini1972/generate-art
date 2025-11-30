import argparse
import base64
import datetime
import os
import random
import sys
import requests
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
try:
    client = OpenAI()  # Automatically reads from OPENAI_API_KEY
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("API key not found")
except Exception:
    print("❌ Error: OpenAI API key not found.")
    print("Please add OPENAI_API_KEY to your .env file or environment variables.")
    print("OPENAI_API_KEY=sk-proj-...")
    sys.exit(1)

# Step 1: Define mappings for day and hour
day_map = {
    "Monday": "structured geometric shapes",
    "Tuesday": "minimalist lines",
    "Wednesday": "balanced symmetry",
    "Thursday": "dynamic abstract flow",
    "Friday": "playful colorful patterns",
    "Saturday": "organic nature-inspired",
    "Sunday": "calm watercolor tones"
}

# Additional creative elements for AI prompt
art_styles = [
    "Cyberpunk", "Watercolor", "Oil Painting", "3D Render", "Abstract Expressionism",
    "Surrealism", "Pop Art", "Minimalist", "Impressionist", "Digital Glitch Art",
    "Synthwave", "Ukiyo-e", "Art Nouveau", "Cubism", "Low Poly"
]

descriptors = [
    "ethereal", "vibrant", "dark", "minimalist", "intricate", "chaotic", "serene",
    "geometric", "organic", "futuristic", "retro", "dreamlike", "gloomy", "neon",
    "pastel", "gritty", "whimsical", "majestic"
]

def hour_color(h):
    return f"color palette with hue shift of {h * 15} degrees"


def rotation_angle(h):
    return h * 15


def _get_attr_or_key(obj, name):
    if isinstance(obj, dict):
        return obj.get(name)
    return getattr(obj, name, None)

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Generate unique GPT Image art that depends on the day and time."
    )
    parser.add_argument("--keywords", help="Comma-separated keywords to add to the prompt", default="")
    parser.add_argument("--style", choices=art_styles, help="Override the randomly chosen art style")
    parser.add_argument("--quality", choices=["low", "medium", "high", "auto"], default="auto",
                        help="Image quality to request from GPT Image")
    parser.add_argument("--size", choices=["1024x1024", "1792x1024", "1024x1792"],
                        default="1024x1024", help="Image size to request")
    parser.add_argument("--model", default="gpt-image-1", help="Model to send to the OpenAI API")
    parser.add_argument("--dry-run", action="store_true",
                        help="Print the prompt and estimated cost without calling the API")
    parser.add_argument("--seed", type=int, help="Seed the random generator for reproducible prompts")
    return parser.parse_args()

def build_prompt(day, hour, style, desc1, desc2, keywords):
    keywords_fragment = ""
    if keywords:
        keywords_fragment = f" Additional keywords: {', '.join(keywords)}."

    return (
        f"Generative digital artwork with {day_map[day]} and {hour_color(hour)}, "
        f"rotated {rotation_angle(hour)} degrees. Style: {style}. Mood: {desc1} and {desc2}.{keywords_fragment}"
    )

def estimate_cost(quality):
    pricing = {
        "low": 0.02,
        "medium": 0.04,
        "high": 0.08,
        "auto": 0.04
    }
    return pricing.get(quality, 0.04)

def main():
    args = parse_arguments()

    if args.seed is not None:
        random.seed(args.seed)

    now = datetime.datetime.now()
    current_day = now.strftime("%A")
    current_hour = now.hour

    style = args.style or random.choice(art_styles)
    desc1, desc2 = random.sample(descriptors, 2)
    keywords = [kw.strip() for kw in args.keywords.split(",") if kw.strip()]

    prompt = build_prompt(current_day, current_hour, style, desc1, desc2, keywords)

    print(f"✅ Prompt generated: {prompt}")
    print(f"Day: {current_day}")
    print(f"Hour: {current_hour}:00")
    print(f"Style: {style}, Quality: {args.quality}, Size: {args.size}")

    if args.dry_run:
        cost_per_image = estimate_cost(args.quality)
        print("🧪 Dry run mode enabled — no API call will be made.")
        print(f"Estimated cost: ${cost_per_image:.2f} (quality={args.quality})")
        return

    print(f"Generating image with GPT Image API ({args.model})...")

    try:
        response = client.images.generate(
            model=args.model,
            prompt=prompt,
            size=args.size,
            quality=args.quality,
            n=1
        )

        image_info = response.data[0]
        image_url = _get_attr_or_key(image_info, "url")
        image_data = None

        if image_url:
            print("✅ Image generated successfully!")
            print(f"Image URL: {image_url}")

            image_response = requests.get(image_url, timeout=30)
            image_response.raise_for_status()
            image_data = image_response.content
        elif b64_json := _get_attr_or_key(image_info, "b64_json"):
            print("✅ Image generated successfully (inline base64 payload).")
            image_data = base64.b64decode(b64_json)
        else:
            raise ValueError("No URL or base64 payload returned from API.")

        output_dir = "output"
        os.makedirs(output_dir, exist_ok=True)

        timestamp = now.strftime("%Y%m%d_%H%M%S")
        file_name = os.path.join(output_dir, f"ai_artwork_{timestamp}.png")

        with open(file_name, "wb") as f:
            f.write(image_data)

        print(f"✅ Artwork saved locally as: {file_name}")
    except Exception as e:
        print(f"❌ Error generating or saving artwork: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()