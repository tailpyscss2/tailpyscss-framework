<p align="center">
  <img src="https://raw.githubusercontent.com/tailpyscss2/tailpyscss-framework/main/docs/assets/logos/tailpyscss_logo_snake_wind.png" alt="TailPySCSS Logo" width="200"/>
</p>

# TailPySCSS v0.4.5

![PyPI - Version](https://img.shields.io/pypi/v/tailpyscss)
![PyPI - Downloads](https://img.shields.io/pypi/dm/tailpyscss)
![License](https://img.shields.io/github/license/tailpyscss2/tailpyscss-framework)
![Build Status](https://img.shields.io/github/actions/workflow/status/tailpyscss2/tailpyscss-framework/python-package.yml)

**The Python-Native Utility CSS Engine for Clean HTML**

TailPySCSS is a **Python-powered TailwindCSS alternative** without Node.js. It is a lightweight **utility-first CSS framework** designed specifically for Python developers (Flask, Django, FastAPI).

If you are looking for a **Python styling framework** or a pure Python **UI framework**, this is it. Unlike traditional tools, this is a **Node-less CSS engine** that compiles **SCSS** to CSS directly in Python. It perfectly integrates with Jinja2 templates, keeping your project 100% Pythonic.

**100% Python. 100% Open Source.**

**Created by [Abdi Abdikarim](https://github.com/CABDUWAHAAB)**

---

## 🚀 New in v0.4.0 (The 3x Bundle)
*   **Universal Python Bridge**: Automatically generates `tailpyscss_theme.py` effectively synching your frontend design tokens with your Python backend (Flask/Django/FastAPI).
*   **Smart Config**: Validated Python-based configuration (`tailpy_config.py`) with 100% Security Sanitization preventing CSS injections.
*   **Performance Core**: Smart MD5 Caching & 0.1s Watch Debounce for instant feedback.

## 📦 Installation

You can install TailPySCSS via pip or from source.

### Option 1: Install via PyPI
```bash
pip install tailpyscss
```

### Option 2: Install from Source (Development)
If you want to contribute or modify the framework:
```bash
pip install -e .
```

### Auto-Setup for Windows
The installation attempts to automatically run:
```bash
python -m tailpyscss.cli setup-path
```
This adds the generic Python `Scripts` folder to your Windows PATH so you can use the `tailpyscss` command globally.

> [!NOTE]
> **Command not found?**
> If the automatic setup failed and Windows can't find the `tailpyscss` command, run the setup manually:
> ```bash
> python -m tailpyscss.cli setup-path
> ```
> Then restart your terminal.

## ⚡ Quick Start

### 1. Initialize
Go to your project folder and run:

```bash
tailpyscss init
```
*(Or use `python -m tailpyscss.cli init`)*

This creates:
*   `tailpy_config.py` (Your Python-based Settings!)
*   `styles/` folder (Your SCSS)

### 2. Build or Watch
To build once:
```bash
tailpyscss build
```

To watch for changes (0.1s response time):
```bash
tailpyscss watch
```

### 3. The Universal Bridge (Backend Magic)
When you run build, we generate `tailpyscss_theme.py`. Use it in your Python code!

```python
import tailpyscss_theme

print(tailpyscss_theme.COLORS['primary']) 
# Output: #3b82f6 (Synced directly from your CSS logic!)
```

### 4. The Core Philosophy: Clean HTML & BEM
The main objective of TailPySCSS is to separate structure (HTML) from implementation (CSS). Instead of cluttering your HTML with classes, use **SCSS BEM** and the custom `@apply` directive.

**Your SCSS (`styles/main.scss`):**
```scss
.card {
    @apply flex flex-col bg-white p-6 rounded-lg shadow-lg;

    &__header {
        @apply text-2xl font-bold text-dark mb-4;
    }

    &__button {
        @apply px-4 py-2 bg-primary text-white rounded hover:bg-secondary transition-colors;
    }
}
```

---

## ⚙️ Configuration (`tailpy_config.py`)
We now use **Native Python** for configuration. Pure dynamic power.

```python
config = {
    "colors": {
        "primary": "#3b82f6",
        "secondary": "#ec4899",
        "dark": "#1f2937",
        "light": "#f3f4f6"
    },
    # ... screens, spacing, typography
}
```

> [!IMPORTANT]
> **Security Guarantee**: All configuration values are strictly sanitized. Attempts to inject CSS (e.g., `"; body { display: none }"`) will raise a `Security Alert` and stop the build.

---

## 📚 Documentation

*   [**Class Reference**](https://github.com/tailpyscss2/tailpyscss-framework/blob/main/docs/reference.md): Valid list of all generated classes.
*   [**Contributing Guide**](https://github.com/tailpyscss2/tailpyscss-framework/blob/main/CONTRIBUTING.md): How to develop the framework itself.
*   [**Security Policy**](https://github.com/tailpyscss2/tailpyscss-framework/blob/main/SECURITY.md): Reporting vulnerabilities.

---

## 📄 License

MIT License. Free for commercial and private use.
