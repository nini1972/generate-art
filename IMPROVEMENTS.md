# Project Improvement Ideas

Here are some ideas to make the art generation even more dynamic, unique, and interesting. We can explore these when you return.

---

### For `generate_art.py` (Local Geometric Art)

1.  **Increase Granularity for Uniqueness**
    -   **Goal**: Ensure no two images are ever the same.
    -   **How**: Incorporate minutes, seconds, and even milliseconds into the logic that determines shape properties (position, size, color, rotation).
    -   **Example**: `seed = now.hour * 3600 + now.minute * 60 + now.second`

2.  **More Complex Generative Algorithms**
    -   **Goal**: Create more sophisticated and visually interesting patterns.
    -   **How**: Introduce advanced algorithms beyond simple shapes.
        -   **Perlin Noise**: For organic, flowing textures (like clouds or marble).
        -   **Voronoi Diagrams**: For creating cell-like structures.
        -   **Fractal Trees**: For generating natural, branching patterns.
        -   **Reaction-Diffusion**: For simulating patterns found in nature (like animal prints).

3.  **Dynamic Color Palettes**
    -   **Goal**: Move beyond fixed color schemes for more varied and harmonious results.
    -   **How**: Generate color palettes on the fly based on color theory, seeded by the exact timestamp.
        -   **Methods**: Complementary, triadic, analogous, or split-complementary colors.
        -   **Library**: Use a library like `colormath` or `colorspacious` to help with calculations.

4.  **External Configuration File**
    -   **Goal**: Make it easy to experiment with parameters without changing the code.
    -   **How**: Move settings into a `config.json` or `config.yaml` file.
    -   **Parameters**: Image `width`, `height`, `complexity`, `opacity_range`, `size_range`, etc.

---

### For `generate_ai_art.py` (AI-Powered Art with GPT Image)

1.  **Advanced Prompt Engineering for Variety (completed)**
    -   **Status**: Already delivers randomized art styles, moods, and now accepts user-supplied keywords.
    -   **Future idea**: We could still layer in season/month cues or holiday themes for more context.

2.  **User-Defined Keywords via Command-Line (implemented)**
    -   `--keywords` allows you to inject any extra themes you want alongside the day-based concept.

3.  **Expose API Parameters (implemented)**
    -   Use `--style`, `--quality`, `--size`, `--model`, and `--seed` to experiment with different GPT Image configurations.

4.  **Cost Estimation and Dry-Run Mode (implemented)**
    -   `--dry-run` prints the prompt plus estimated cost for the desired quality without charging your account.

5.  **Next idea**
    -   Automatically detect the current season, month, or nearby holiday and add it to the prompt so the visuals feel tied to a specific moment in time.

---

We can pick any of these to work on when you're back!
