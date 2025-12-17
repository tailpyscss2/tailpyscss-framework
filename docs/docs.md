# TailPySCSS Documentation

> **The Complete Manual for Python Developers**

TailPySCSS is a pure-Python CSS framework that gives you utility classes (like Tailwind) and component structure (like Bootstrap) without Node.js.

---

## 📚 Quick Links

- [Installation](#installation)
- [CLI Commands](#cli-commands)
- [Methodologies](#methodologies)
- [Framework Integrations](#framework-integrations)
- [Advanced Topics](#advanced-topics)

---

## Why TailPySCSS?

Modern web development forces Python developers into the JavaScript ecosystem. TailPySCSS breaks this dependency:

- 🚫 **No Node.js**: No `npm install`, no `package.json`, no `node_modules`
- ⚡ **Zero Runtime**: Build-time tool that generates static CSS
- 🐍 **Framework Agnostic**: Works with Flask, Django, FastAPI, Streamlit
- 🎨 **SCSS Power**: Built on LibSass with full SCSS support
- 🌲 **Tree Shaking**: Only generates CSS for classes you use

---

## Installation

```bash
pip install tailpyscss
```

Verify installation:
```bash
tailpyscss --version
# tailpyscss, version 0.5.3
```

---

## CLI Commands

### 1. Initialize Project

Run once to scaffold the directory structure:

```bash
tailpyscss init
```

Creates:
- `static/css/styles.css` - Generated CSS output
- `styles/main.scss` - Your custom SCSS
- `tailpy_config.py` - Configuration file

### 2. Watch Mode (Development)

Watches for changes and rebuilds CSS instantly:

```bash
tailpyscss watch
```

### 3. Build (Production)

One-time optimized build with minification:

```bash
tailpyscss build
```

---

## Methodologies

### The Pro Way: BEM + Utilities

For scalable projects, use BEM for structure and utilities for modifiers:

**HTML:**
```html
<div class="card card--featured">
    <div class="card__header">
        <h2 class="text-xl font-bold">Title</h2>
    </div>
</div>
```

**SCSS:**
```scss
.card {
    background: white;
    border-radius: 0.5rem;
    
    &--featured {
        border: 2px solid theme('colors.indigo.500');
    }
    
    &__header {
        padding: 1.5rem;
    }
}
```

### The Rapid Way: Utility-First

For prototypes and simple pages:

```html
<button class="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700">
    Click Me
</button>
```

---

## Framework Integrations

### Flask

```python
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
```

```html
<!-- templates/base.html -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
```

### Django

```python
# settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
```

```html
<!-- templates/base.html -->
{% load static %}
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
```

### FastAPI

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
```

### Streamlit

```python
import streamlit as st

def load_css():
    with open("static/css/styles.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css()
```

---

## Advanced Topics

### Configuration

Customize colors, spacing, and breakpoints in `tailpy_config.py`:

```python
config = {
    "colors": {
        "primary": "#4f46e5",
        "secondary": "#ec4899"
    },
    "screens": {
        "sm": "640px",
        "md": "768px",
        "lg": "1024px"
    }
}
```

### Custom SCSS

Import custom SCSS files in `styles/main.scss`:

```scss
@import "variables";
@import "components/navbar";

body {
    font-family: 'Inter', sans-serif;
}
```

### Dark Mode

Use CSS variables:

```scss
:root {
    --bg-primary: #ffffff;
    --text-primary: #111827;
}

[data-theme="dark"] {
    --bg-primary: #111827;
    --text-primary: #f9fafb;
}
```

---

## Production Deployment

The `build` command automatically:
- ✅ Minifies CSS (via LibSass compressed output)
- ✅ Tree-shakes unused classes
- ✅ Generates optimized output

### Docker Example

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install tailpyscss
RUN tailpyscss build

CMD ["gunicorn", "app:app"]
```

---

## Support

- 📖 [Full Documentation](https://tailpyscss2.github.io/tailpyscss-framework/)
- 🐛 [GitHub Issues](https://github.com/tailpyscss2/tailpyscss-framework/issues)
- 💬 [Discussions](https://github.com/tailpyscss2/tailpyscss-framework/discussions)

---

**Built with ❤️ for Python developers who refuse to use Node.js.**
