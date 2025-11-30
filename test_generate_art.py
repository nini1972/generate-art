"""
Tests for the art generator tool.
"""

import datetime
import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from generate_art import (
    day_map,
    day_colors,
    day_shapes,
    time_color,
    time_rotation,
    time_influence,
    generate_prompt,
    generate_artwork
)


def test_day_map():
    """Test that all days are mapped to concepts."""
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        assert day in day_map, f"{day} not in day_map"
        assert isinstance(day_map[day], str), f"{day} mapping is not a string"
    print("✅ test_day_map passed")


def test_day_colors():
    """Test that all days have color palettes."""
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        assert day in day_colors, f"{day} not in day_colors"
        assert len(day_colors[day]) >= 3, f"{day} should have at least 3 colors"
        for color in day_colors[day]:
            assert len(color) == 3, f"Color should be RGB tuple"
            assert all(0 <= c <= 255 for c in color), f"Color values should be 0-255"
    print("✅ test_day_colors passed")


def test_day_shapes():
    """Test that all days have shape mappings."""
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        assert day in day_shapes, f"{day} not in day_shapes"
        assert isinstance(day_shapes[day], str), f"{day} shape is not a string"
    print("✅ test_day_shapes passed")


def test_time_color():
    """Test time to color mapping function."""
    # Test a few times
    times = [
        datetime.datetime(2023, 1, 1, 0, 0, 0),
        datetime.datetime(2023, 1, 1, 12, 30, 0),
        datetime.datetime(2023, 1, 1, 23, 59, 59)
    ]
    for t in times:
        result = time_color(t)
        assert "hue shift" in result, f"time_color({t}) should contain 'hue shift'"
    print("✅ test_time_color passed")


def test_time_rotation():
    """Test time to rotation angle mapping."""
    # Test a few times
    times = [
        datetime.datetime(2023, 1, 1, 0, 0, 0),
        datetime.datetime(2023, 1, 1, 12, 30, 0),
        datetime.datetime(2023, 1, 1, 23, 59, 59)
    ]
    for t in times:
        angle = time_rotation(t)
        assert 0 <= angle < 360, f"Rotation angle {angle} should be between 0 and 360"
    print("✅ test_time_rotation passed")


def test_time_influence():
    """Test time influence calculations."""
    # Test a few times
    times = [
        datetime.datetime(2023, 1, 1, 0, 0, 0),
        datetime.datetime(2023, 1, 1, 12, 30, 0),
        datetime.datetime(2023, 1, 1, 23, 59, 59)
    ]
    
    for t in times:
        influence = time_influence(t)
        
        assert "angle" in influence, "influence should have 'angle'"
        assert "size" in influence, "influence should have 'size'"
        assert "saturation" in influence, "influence should have 'saturation'"
        assert "brightness" in influence, "influence should have 'brightness'"
        assert "complexity" in influence, "influence should have 'complexity'"
        assert "opacity" in influence, "influence should have 'opacity'"
        
        assert 0 <= influence["angle"] < 360, f"angle should be 0-360"
        assert 0.5 <= influence["size"] <= 1.0, f"size should be between 0.5 and 1.0"
        assert 0 <= influence["saturation"] <= 1.0, f"saturation should be between 0 and 1.0"
        assert 0 <= influence["brightness"] <= 1.0, f"brightness should be between 0 and 1.0"
        # Complexity range changed in new implementation
        assert influence["complexity"] > 0, f"complexity should be positive"
        assert 150 <= influence["opacity"] <= 255, f"opacity should be between 150 and 255"
    
    print("✅ test_time_influence passed")


def test_generate_prompt():
    """Test prompt generation for all days and times."""
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    t = datetime.datetime(2023, 1, 1, 12, 0, 0)
    
    for day in days:
        prompt = generate_prompt(day, t)
        assert day_map[day] in prompt, f"Prompt should contain day concept"
        assert "digital artwork" in prompt.lower(), f"Prompt should mention digital artwork"
    
    print("✅ test_generate_prompt passed")


def test_generate_artwork():
    """Test artwork generation."""
    import tempfile
    
    days = ["Monday", "Friday", "Sunday"]  # Test a few representative days
    t = datetime.datetime(2023, 1, 1, 12, 0, 0)
    
    for day in days:
        # Generate artwork without saving
        image = generate_artwork(day, t, width=200, height=150)
        assert image is not None, f"Image should not be None for {day}"
        assert image.size == (200, 150), f"Image size should be 200x150"
    
    # Test saving to file
    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = os.path.join(tmpdir, "test_artwork.png")
        image = generate_artwork("Friday", t, output_path=output_path)
        assert os.path.exists(output_path), "Output file should exist"
    
    print("✅ test_generate_artwork passed")


def run_all_tests():
    """Run all tests."""
    print("\n🧪 Running tests for generate_art.py\n")
    print("=" * 50)
    
    test_day_map()
    test_day_colors()
    test_day_shapes()
    test_time_color()
    test_time_rotation()
    test_time_influence()
    test_generate_prompt()
    test_generate_artwork()
    
    print("=" * 50)
    print("\n✅ All tests passed!\n")


if __name__ == "__main__":
    run_all_tests()
