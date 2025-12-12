<p align="center">
  <img src="assets/logos/tailpyscss_logo_snake_wind.png" alt="TailPySCSS Logo" width="200"/>
</p>

# TailPySCSS Documentation

Welcome to the official documentation for **TailPySCSS**.

## Introduction
TailPySCSS is a Python-native Utility CSS framework designed to work seamlessly with Flask, Django, and other Python web frameworks. It eliminates the need for Node.js, `npm`, or complex build pipelines.

## Documentation

- **[Feature Overview](features.md)**: See what's included in v0.4.1.
- **[Class Reference](reference.md)**: Full guide to all generated CSS utility classes.

## Installation

```bash
pip install tailpyscss
```

## Quick Links
- [GitHub Repository](https://github.com/tailpyscss-tech/tailpyscss-framework)
- [PyPI Package](https://pypi.org/project/tailpyscss/)

## Guide

### 1. Project Initialization
```bash
tailpyscss init
```

### 2. Configuration
Edit `tailpy_config.py` to define your design system tokens.

### 3. Usage
Use SCSS @apply within your `styles/main.scss` file:

```scss
.btn {
    @apply px-4 py-2 bg-primary text-white rounded;
}
```

### 4. Build
```bash
tailpyscss build
```

## Advanced
- **Universal Bridge**: Import `tailpyscss_theme` in Python to access your colors and config variables.
- **Security**: The configuration loader enforces strict sanitization to prevent injection attacks.
