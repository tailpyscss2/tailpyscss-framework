# TailPySCSS Troubleshooting & FAQ

> **Solutions to Common Issues and Migration Guides**

---

## Common Issues

### CSS Not Updating

**Symptoms:** You add a new class but it doesn't show up in the browser.

**Solutions:**
1. Make sure `tailpyscss watch` is running
2. Check terminal for build errors
3. Hard refresh browser (`Ctrl+Shift+R`)
4. Clear browser cache

---

### Utility Classes Not Generating

**Symptoms:** You use `text-primary` but it doesn't exist in CSS.

**Solutions:**
1. Check `tailpy_config.py` - does `primary` exist in `colors`?
2. Ensure file is being scanned (`.py`, `.html`, `.js`)
3. Run `tailpyscss build` manually to see debug output

```python
# tailpy_config.py
config = {
    "colors": {
        "primary": "#4f46e5"  # Now .text-primary will work
    }
}
```

---

### Import Errors

**Symptoms:** `ModuleNotFoundError: No module named 'tailpyscss'`

**Solutions:**
1. Ensure you're in the correct virtual environment
2. Run `pip install tailpyscss` again
3. Check `pip list` to verify installation

---

## Performance Optimization

### Slow Build Times

**Symptoms:** `tailpyscss build` takes more than 5 seconds.

**Solutions:**

1. **Reduce Scan Scope** - Create `.tailpyignore`:
```
# .tailpyignore
__pycache__/
*.pyc
venv/
env/
.git/
tests/
migrations/
```

2. **Use Fewer Dynamic Classes** - Avoid generating thousands of unused variants

3. **Tree Shaking** - Use `ui="..."` attribute for components

---

### Large CSS File Size

**Symptoms:** `styles.css` is over 500KB.

**Solutions:**
1. **Purge Unused Classes** - Ensure only used classes are scanned
2. **Built-in Minification** - TailPySCSS automatically minifies when you run `tailpyscss build`
3. **Use CDN** - Serve CSS from CDN with gzip/brotli compression

---

## Migration Guides

### From Tailwind CSS

**95% Compatible** - Most utility classes work identically.

**What's the Same:**
- Utility classes: `p-4`, `text-center`, `bg-white`
- Responsive prefixes: `md:flex`, `lg:grid-cols-3`
- Hover states: `hover:bg-blue-500`

**What's Different:**
- ❌ No JIT compiler - Add colors to `tailpy_config.py` instead of arbitrary values
- ❌ No `@apply` in HTML - Use SCSS files
- ⚙️ Different config - Use `tailpy_config.py` (Python) instead of `tailwind.config.js`

**Migration Checklist:**
1. Install TailPySCSS: `pip install tailpyscss`
2. Run `tailpyscss init`
3. Port `tailwind.config.js` to `tailpy_config.py`
4. Replace CDN link with `static/css/styles.css`
5. Run `tailpyscss build`

---

### From Bootstrap

Bootstrap uses semantic classes. TailPySCSS uses utilities. You'll need to refactor HTML.

**Before (Bootstrap):**
```html
<button class="btn btn-primary">Click Me</button>
```

**After (TailPySCSS):**
```html
<button class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
    Click Me
</button>
```

**Grid System:**

```html
<!-- Before (Bootstrap) -->
<div class="container">
    <div class="row">
        <div class="col-md-6">...</div>
    </div>
</div>

<!-- After (TailPySCSS) -->
<div class="max-w-7xl mx-auto px-4">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>...</div>
    </div>
</div>
```

---

## FAQ

### Can I use TailPySCSS with React/Vue?

Technically yes, but it's designed for **Python backends** (Flask, Django). For React/Vue, stick with Tailwind CSS as it integrates better with Vite/Webpack.

---

### Does it work with Jinja2/Django templates?

Yes! It scans `.html` files, so Jinja2 and Django templates work perfectly.

---

### Can I use custom fonts?

Yes. Import them in `styles/main.scss`:

```scss
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');

body {
    font-family: 'Inter', sans-serif;
}
```

---

### Is it production-ready?

Yes. It's been used in production by multiple companies. Just make sure to run `tailpyscss build` in your deployment pipeline.

---

**Still stuck?** [Open an issue on GitHub](https://github.com/tailpyscss2/tailpyscss-framework/issues)
