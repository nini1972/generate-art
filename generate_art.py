import datetime
import random

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

# Functions to map hour to color and rotation
hour_color = lambda h: f"color palette with hue shift of {h * 15} degrees"
rotation_angle = lambda h: h * 15  # rotation based on hour

# Step 2: Get current day and hour
now = datetime.datetime.now()
current_day = now.strftime("%A")
current_hour = now.hour

# Step 3: Generate the art prompt
prompt = (
    f"Generative digital artwork with {day_map[current_day]} and {hour_color(current_hour)}, "
    f"rotated {rotation_angle(current_hour)} degrees, modern digital art style."
)

# Step 4: Simulate image generation API call
# In a real scenario, here we would call an API like DALL·E or Stable Diffusion with the prompt.
# For now, we'll simulate by generating a mock image URL.
mock_image_id = random.randint(1000, 9999)
mock_image_url = f"https://example.com/generated_art_{mock_image_id}.png"

# Step 5: Print confirmation message
print("✅ Artwork generated successfully!")
print(f"Prompt used: {prompt}")
print(f"Mock Image URL: {mock_image_url}")
