# TailPySCSS UI Components

> **Pre-Built Components with Python Integration**

A showcase of the built-in UI components available in TailPySCSS with both HTML and Python usage examples.

---

## Available Components

### Navbar
Fixed-top navigation with brand, links, and actions.

**HTML:**
```html
<nav ui="navbar">
    <div class="max-w-7xl mx-auto flex justify-between items-center px-6">
        <a href="/" class="font-bold text-2xl">Brand</a>
        <div class="flex gap-6">
            <a href="/docs">Docs</a>
            <a href="/about">About</a>
        </div>
    </div>
</nav>
```

---

### Card
Container component with shadow and rounded corners.

**HTML:**
```html
<div ui="card" class="p-6">
    <h3 class="text-xl font-bold mb-2">Card Title</h3>
    <p class="text-gray-600">Card content goes here.</p>
</div>
```

**Python:**
```python
from tailpyscss.ui import Card

Card(
    title="Card Title",
    content="Card content goes here.",
    classes="p-6"
)
```

---

### Button
Styled button with variants.

**HTML:**
```html
<button ui="button" class="bg-indigo-600 text-white">
    Primary Button
</button>
```

**Python:**
```python
from tailpyscss.ui import Button

Button("Click Me", variant="primary")
```

---

### Input
Form input with label and validation states.

**HTML:**
```html
<div ui="input">
    <label for="email">Email</label>
    <input type="email" id="email" placeholder="you@example.com">
</div>
```

---

### Switch
Toggle switch component.

**HTML:**
```html
<label ui="switch">
    <input type="checkbox">
    <span>Enable Notifications</span>
</label>
```

**Python:**
```python
from tailpyscss.ui import Switch

Switch(label="Enable Notifications", checked=True)
```

---

### Badge
Small status indicator.

**HTML:**
```html
<span ui="badge" class="bg-green-100 text-green-800">Active</span>
```

---

### Alert
Notification message box.

**HTML:**
```html
<div ui="alert" class="bg-blue-50 text-blue-800 p-4 rounded">
    <strong>Info:</strong> This is an informational message.
</div>
```

---

### Tabs
Tabbed content navigation.

**HTML:**
```html
<div ui="tabs">
    <div class="tab-list">
        <button class="tab active">Tab 1</button>
        <button class="tab">Tab 2</button>
    </div>
    <div class="tab-content">
        <div class="tab-panel active">Content 1</div>
        <div class="tab-panel">Content 2</div>
    </div>
</div>
```

---

### Sidebar
Sticky navigation sidebar.

**HTML:**
```html
<aside ui="sidebar" class="w-64">
    <h3>Navigation</h3>
    <ul>
        <li><a href="#section1">Section 1</a></li>
        <li><a href="#section2">Section 2</a></li>
    </ul>
</aside>
```

---

### Hero
Large header section.

**HTML:**
```html
<section ui="hero" class="text-center py-20">
    <h1 class="text-5xl font-bold mb-4">Welcome</h1>
    <p class="text-xl text-gray-600 mb-8">Build amazing things.</p>
    <button class="bg-indigo-600 text-white px-6 py-3 rounded-lg">
        Get Started
    </button>
</section>
```

---

## Tree Shaking

Components are only included in your CSS if you use them. Add the `ui="..."` attribute to enable tree shaking:

```html
<!-- This component's CSS will be included -->
<div ui="card">...</div>

<!-- This won't include any component CSS -->
<div class="bg-white p-4">...</div>
```

---

## Customization

Override component styles in `styles/main.scss`:

```scss
[ui="button"] {
    border-radius: 9999px; // Fully rounded buttons
    font-weight: 700;
}
```

---

**See the [full documentation](docs.md) for more details.**
