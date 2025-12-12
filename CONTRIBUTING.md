# Contributing to TailPySCSS

Thank you for your interest in contributing! This document explains how to modify the framework source code itself (the Python generators).

## Project Architecture

The core logic is located in `tailpyscss/generators/`. We use an OOP approach:

*   **`base.py`**: The abstract base class.
*   **`colors.py`**: Generates color classes (`text-`, `bg-`, `border-`).
*   **`layout.py`**: Flexbox, Grid, Sizing, Positioning.
*   **`typography.py`**: Fonts and Text alignment.
*   **`spacing.py`**: Margins and Padding.

## Development Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/tailpyscss.git
    cd tailpyscss
    ```

2.  **Install in Editable Mode**:
    This allows you to change Python code and test it immediately without reinstalling.
    ```bash
    pip install -e .
    ```

## Adding a New Utility

To add a new CSS feature (e.g., Opacity):

1.  Open `tailpyscss/generators/layout.py` (or create a new file).
2.  Add the logic to the `generate()` method or create a new Generator class.
3.  If adding a new class, register it in `tailpyscss/generator.py` inside the `generator_classes` list.

## Testing Your Changes

1.  Create a test folder (e.g., `test_site`).
2.  Run the build command:
    ```bash
    cd test_site
    python -m tailpyscss.cli build
    ```
3.  Inspect `static/css/output.css` to verify your new CSS rules appear.
