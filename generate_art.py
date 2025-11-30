import datetime
import random
import math
import os
from PIL import Image, ImageDraw

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

# Day to color palette mapping
day_colors = {
    "Monday": [(44, 62, 80), (52, 73, 94), (127, 140, 141), (149, 165, 166)],
    "Tuesday": [(41, 128, 185), (52, 152, 219), (236, 240, 241), (189, 195, 199)],
    "Wednesday": [(39, 174, 96), (46, 204, 113), (26, 188, 156), (22, 160, 133)],
    "Thursday": [(155, 89, 182), (142, 68, 173), (52, 152, 219), (41, 128, 185)],
    "Friday": [(241, 196, 15), (243, 156, 18), (231, 76, 60), (155, 89, 182)],
    "Saturday": [(26, 188, 156), (52, 152, 219), (155, 89, 182), (231, 76, 60)],
    "Sunday": [(230, 243, 255), (179, 217, 255), (128, 191, 255), (77, 166, 255)]
}

# Day to shape drawing function mapping
day_shapes = {
    "Monday": "rectangles",
    "Tuesday": "lines",
    "Wednesday": "symmetry",
    "Thursday": "curves",
    "Friday": "circles",
    "Saturday": "organic",
    "Sunday": "waves"
}


def time_color(t):
    """Map time to color description."""
    total_minutes = t.hour * 60 + t.minute
    return f"color palette with hue shift of {total_minutes % 360} degrees"


def time_rotation(t):
    """Map time to rotation angle."""
    total_seconds = t.hour * 3600 + t.minute * 60 + t.second
    return (total_seconds // 10) % 360


def time_influence(t):
    """Calculate numeric influences based on exact time."""
    # Calculate a normalized time value (0.0 to 1.0) based on the full day
    total_seconds = t.hour * 3600 + t.minute * 60 + t.second + t.microsecond / 1000000
    seconds_in_day = 24 * 3600
    normalized = total_seconds / seconds_in_day
    
    # Use microsecond for extra randomness in complexity
    micro_factor = t.microsecond / 1000000
    
    return {
        "angle": (total_seconds // 10) % 360,
        "size": 0.5 + (normalized * 0.5),
        "saturation": 0.3 + (math.sin(normalized * math.pi) * 0.7),
        "brightness": 0.3 + ((t.hour if t.hour <= 12 else 24 - t.hour) / 12) * 0.7,
        "complexity": int(3 + (normalized + micro_factor) * 10),
        "opacity": int(150 + normalized * 105)
    }


def generate_prompt(day, t):
    """Generate an AI art prompt based on day and time."""
    prompt = (
        f"Generative digital artwork with {day_map[day]} and {time_color(t)}, "
        f"rotated {time_rotation(t)} degrees, modern digital art style."
    )
    return prompt


def draw_rectangles(draw, width, height, colors, influence):
    """Draw structured geometric rectangles (Monday style)."""
    count = influence["complexity"]
    for i in range(count):
        x = random.randint(0, width)
        y = random.randint(0, height)
        w = int(50 * influence["size"] + random.randint(20, 80))
        h = int(40 * influence["size"] + random.randint(15, 60))
        color = colors[i % len(colors)] + (influence["opacity"],)
        draw.rectangle([x, y, x + w, y + h], fill=color)


def draw_lines(draw, width, height, colors, influence):
    """Draw minimalist lines (Tuesday style)."""
    count = influence["complexity"] * 2
    for i in range(count):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        angle_rad = math.radians(influence["angle"] + random.randint(-30, 30))
        length = int(100 * influence["size"] + random.randint(50, 150))
        x2 = x1 + int(length * math.cos(angle_rad))
        y2 = y1 + int(length * math.sin(angle_rad))
        color = colors[i % len(colors)] + (influence["opacity"],)
        draw.line([x1, y1, x2, y2], fill=color, width=3)


def draw_symmetry(draw, width, height, colors, influence):
    """Draw balanced symmetrical shapes (Wednesday style)."""
    count = influence["complexity"]
    center_x = width // 2
    for i in range(count):
        offset_x = random.randint(20, width // 3)
        y = random.randint(50, height - 50)
        size = int(30 * influence["size"] + random.randint(10, 40))
        color = colors[i % len(colors)] + (influence["opacity"],)
        # Draw on both sides for symmetry
        draw.ellipse([center_x - offset_x - size, y - size, 
                      center_x - offset_x + size, y + size], fill=color)
        draw.ellipse([center_x + offset_x - size, y - size, 
                      center_x + offset_x + size, y + size], fill=color)


def draw_curves(draw, width, height, colors, influence):
    """Draw dynamic abstract curves (Thursday style)."""
    count = influence["complexity"]
    for i in range(count):
        points = []
        x = random.randint(0, width // 2)
        y = random.randint(0, height)
        for j in range(5):
            x += random.randint(30, 100)
            y += random.randint(-50, 50)
            y = max(0, min(height, y))
            points.append((x, y))
        color = colors[i % len(colors)] + (influence["opacity"],)
        if len(points) >= 2:
            draw.line(points, fill=color, width=4)


def draw_circles(draw, width, height, colors, influence):
    """Draw playful colorful circles (Friday style)."""
    count = influence["complexity"] * 2
    for i in range(count):
        x = random.randint(0, width)
        y = random.randint(0, height)
        r = int(20 * influence["size"] + random.randint(10, 50))
        color = colors[i % len(colors)] + (influence["opacity"],)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=color)


def draw_organic(draw, width, height, colors, influence):
    """Draw organic nature-inspired shapes (Saturday style)."""
    count = influence["complexity"]
    for i in range(count):
        # Draw irregular polygon (organic blob)
        center_x = random.randint(50, width - 50)
        center_y = random.randint(50, height - 50)
        points = []
        num_points = random.randint(6, 10)
        for j in range(num_points):
            angle = (2 * math.pi / num_points) * j
            r = int(30 * influence["size"] + random.randint(10, 40))
            px = center_x + int(r * math.cos(angle))
            py = center_y + int(r * math.sin(angle))
            points.append((px, py))
        color = colors[i % len(colors)] + (influence["opacity"],)
        if len(points) >= 3:
            draw.polygon(points, fill=color)


def draw_waves(draw, width, height, colors, influence):
    """Draw calm wave patterns (Sunday style)."""
    count = influence["complexity"]
    for i in range(count):
        y_base = int(height / (count + 1) * (i + 1))
        points = []
        for x in range(0, width, 10):
            y = y_base + int(30 * math.sin(x * 0.02 + i))
            points.append((x, y))
        color = colors[i % len(colors)] + (influence["opacity"],)
        if len(points) >= 2:
            draw.line(points, fill=color, width=5)


def generate_artwork(day, time_obj, width=800, height=600, output_path=None):
    """Generate artwork directly using the graphics library."""
    
    # Seed random with exact time for uniqueness
    random.seed(time_obj.timestamp())
    
    colors = day_colors[day]
    influence = time_influence(time_obj)
    shape_type = day_shapes[day]
    
    # Create image with gradient background
    image = Image.new("RGBA", (width, height), (255, 255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    # Draw background gradient
    base_color = colors[0]
    for y in range(height):
        ratio = y / height
        r = int(base_color[0] + (255 - base_color[0]) * ratio * 0.3)
        g = int(base_color[1] + (255 - base_color[1]) * ratio * 0.3)
        b = int(base_color[2] + (255 - base_color[2]) * ratio * 0.3)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    # Create overlay for shapes
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    
    # Draw shapes based on day
    shape_functions = {
        "rectangles": draw_rectangles,
        "lines": draw_lines,
        "symmetry": draw_symmetry,
        "curves": draw_curves,
        "circles": draw_circles,
        "organic": draw_organic,
        "waves": draw_waves
    }
    
    shape_func = shape_functions.get(shape_type, draw_circles)
    shape_func(overlay_draw, width, height, colors, influence)
    
    # Composite the overlay onto the base image
    image = Image.alpha_composite(image, overlay)
    
    # Convert to RGB for saving as PNG
    final_image = image.convert("RGB")
    
    # Rotate based on hour influence (subtle rotation)
    rotation = influence["angle"] % 10 - 5  # Small rotation: -5 to +5 degrees
    if rotation != 0:
        final_image = final_image.rotate(rotation, expand=False, fillcolor=(255, 255, 255))
    
    # Save if output path provided
    if output_path:
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        final_image.save(output_path)
    
    return final_image


def main():
    """Main function to run the art generator."""
    # Step 2: Get current day and time
    now = datetime.datetime.now()
    current_day = now.strftime("%A")
    
    # Step 3: Generate the art prompt
    prompt = generate_prompt(current_day, now)

    # Step 4: Generate actual artwork using graphics library
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join(output_dir, f"artwork_{timestamp}.png")
    
    generate_artwork(current_day, now, output_path=output_path)

    # Step 5: Print confirmation message
    print("✅ Artwork generated successfully!")
    print(f"Day: {current_day}")
    print(f"Time: {now.strftime('%H:%M:%S')}")
    print(f"Day Concept: {day_map[current_day]}")
    print(f"Time Influence: rotation={time_rotation(now)}°, hue_shift={time_color(now)}")
    print(f"AI Art Prompt: {prompt}")
    print(f"Generated Image: {output_path}")


if __name__ == "__main__":
    main()
