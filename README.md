<p align="center">
  <img src="https://raw.githubusercontent.com/tailpyscss2/tailpyscss-framework/main/docs/assets/logos/tailpyscss_logo_snake_wind.png" alt="TailPySCSS Logo" width="200"/>
</p>

# TailPySCSS v0.5.0: The Frontend Engine

[![Analysis & Tests](https://github.com/tailpyscss2/tailpyscss-framework/actions/workflows/main.yml/badge.svg)](https://github.com/tailpyscss2/tailpyscss-framework/actions/workflows/main.yml)
[![PyPI - Version](https://img.shields.io/pypi/v/tailpyscss)](https://pypi.org/project/tailpyscss/)
[![Python Version](https://img.shields.io/pypi/pyversions/tailpyscss)](https://pypi.org/project/tailpyscss/)
[![License](https://img.shields.io/github/license/tailpyscss2/tailpyscss-framework)](https://img.shields.io/github/license/tailpyscss2/tailpyscss-framework)

> **"Build Modern UI in Python. No Node.js. No npm. No Webpack."**

TailPySCSS is a **Python-Native CSS Engine**. It gives you the power of utility classes (like Tailwind) and the structure of components (like Bootstrap) without the nightmare of a Node.js build pipeline.

It compiles SCSS to CSS directly in Python. It scans your Python code for usage. It treeshakes unused styles by default.

---

## 🔥 Creating UI in Python (New in v0.5.0)

Forget writing HTML classes manually. Use the new **Python Component Library**:

```python
from tailpyscss.ui import Card, Button, Input, Switch

def view():
    return Card(
        Input(placeholder="Enter email"),
        Switch(label="Enable Notifications"),
        Button("Save Changes", variant="primary")
    )
```

**What happens?**
1.  **The Scanner** detects you used `Card`, `Input`, and `Switch`.
2.  **The Engine** compiles *only* the CSS needed for those 3 components.
3.  **The Output** is a tiny, optimized CSS file (**~9 KB** for small apps).

---

## 🚀 Features

### 1. Zero Node.js Dependency
Stop fighting `package.json`, `node_modules`, and `webpack.config.js`. TailPySCSS is 100% Python.
*   **Install**: `pip install tailpyscss`
*   **Run**: `tailpyscss build`

### 2. The Context Engine (Tree Shaking)
We don't include 500KB of unused CSS. If you don't use the `Table` component in your Python code, its CSS is **not generated**.
*   **Base Size**: ~9 KB (Utilities only)
*   **Full Suite**: ~19 KB (All 30+ components)

### 3. The Component Library (30+ Elements)
Batteries included. Neon-ready. Glassmorphism-ready.
*   **Essentials**: `Button`, `Card`, `Badge`, `Alert`, `Navbar`, `Hero`.
*   **Forms**: `Input`, `Select`, `Checkbox`, `Radio`, `Switch`, `File`.
*   **Overlay**: `Modal`, `Toast`, `Tooltip`, `Popover`.
*   **Navigation**: `Tabs`, `Sidebar`, `Pagination`, `Breadcrumb`.

### 4. The Vibe Engine (Dynamic Theming)
Change your entire app's feel with one config line.
```python
# tailpy_config.py
config = {
    "vibe": "neon"  # Options: 'flat', 'glass', 'neon'
}
```

---

## ⚡ Quick Start

### 1. Install
```bash
pip install tailpyscss
```

### 2. Initialize
```bash
tailpyscss init
```
Creates `tailpy_config.py` and `styles/` folder.

### 3. Build & Watch
```bash
# Watch for changes (0.1s response time)
tailpyscss watch
```

---

## 🛠️ Configuration

Configure colors, spacing, and vibes in pure Python:

```python
# tailpy_config.py
config = {
    "colors": {
        "primary": "#3b82f6",  # Blue
        "secondary": "#ec4899" # Pink
    },
    "vibe": "glass"
}
```

## 📚 Comparisons

| Feature | TailPySCSS (v2) | Tailwind JIT | Bootstrap 5 |
| :--- | :--- | :--- | :--- |
| **Tech Stack** | **Python (Pip)** | Node.js (Npm) | SASS |
| **Setup Time** | **1 Minute** | 10-20 Minutes | 5 Minutes |
| **Dependencies** | **0** | 100+ (Node modules) | 0 (if CDN) |
| **Output Size** | **~9 KB - 19 KB** | ~3 KB - 10 KB | ~200 KB + JS |
| **Tree Shaking** | **Yes (Component)** | Yes (Class) | Manual Only |

---

## 📄 License
MIT License. **100% Open Source.**
Created by [Abdi Abdikarim](https://github.com/CABDUWAHAAB).
