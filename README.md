# Orientation Mate for ComfyUI

A simple scaling node for ComfyUI, allowing the changing of the length of the input's longest edge. This node is designed to streamline the process of preparing images for various tasks and control over your image dimensions.

- **Author:** Darren Davies (aka dugdiamond)
- **GitHub:** https://github.com/dugdiamond6-afk
- **Version:** 1.0

---

## What Is This?

**Orientation Mate** is a lightweight scaling node for ComfyUI. Perfect for quickly finding the new dimensions, scale-factor, aspect ratio and shortest edge, clamped to multiples of 16 pixels to make it more tensor friendly.

Use it for:
* Preparing source images for latents or KSamplers
* Streamlining workflows that require image dimension control

---

## Features
* **Image Handling:**
    * Takes image or video input.
* **Smart UX:**
    * Node auto-evaluates the given input value and clamps it to the nearest higher multiple of 16.

---

## Installation

Clone this repository into your `custom_nodes` folder.

```bash
git clone https://github.com/dugdiamond6-afk/ComfyUI-Orientation_Mate.git
```

Your folder should look like:

```bash
ComfyUI/
--- custom_nodes/
------ ComfyUI-OrientationMate/
--------- __init__.py
--------- orientation_mate.py
--------- (other files)
```

Restart ComfyUI to load the new node.

There are no extra dependencies - it works out of the box.

---

Basic Usage

1. Add the Orientaion Mate node from the node search menu.
2. Connect an image source (e.g., Load Image) to the input.
3. Connect outputs to the required dots
4. Run the graph.
5. #self-explanatory!

---

Known Limitations
- None

---

Notes

This extension is experimental and under active development. Use at your own risk, especially in production workflows.

Back up your projects frequently. Feedback, bug reports, and suggestions are always welcome - but expect breakage, quirks, and rough edges. This tool does what I need right now; future updates may be irregular depending on available time.

---

Version History

- **1.0** Initial release

---


License & Usage Terms

Copyright (c) 2026 Darren Davies (aka dugdiamond)

This project is source-available, but not open-source under a standard open-source license, and not freeware.
You may use and experiment with it freely, and any results you create with it are yours to use however you like.
However:

Redistribution, resale, rebranding, or claiming authorship of this code or extension is strictly prohibited without explicit written permission.

Use at your own risk. No warranties or guarantees are provided.

The only official repository for this project is: https://github.com/dugdiamond6-afk/ComfyUI-Orientation_Mate

---

Author

Created by https://github.com/dugdiamond6-afk
