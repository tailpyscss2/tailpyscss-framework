# TailPySCSS Practical Guides

> **Production-Ready Patterns and Best Practices**

Real-world component patterns, dark mode implementation, and responsive design strategies.

---

## Component Patterns

### Production Navbar

A responsive navbar with logo, links, and mobile menu:

**HTML:**
```html
<nav class="navbar">
    <div class="navbar__container max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
        <a href="/" class="navbar__logo text-2xl font-bold text-gray-900">
            MyApp
        </a>

        <!-- Desktop Links -->
        <div class="navbar__links hidden md:flex gap-6">
            <a href="/features" class="text-gray-600 hover:text-indigo-600">Features</a>
            <a href="/pricing" class="text-gray-600 hover:text-indigo-600">Pricing</a>
        </div>

        <!-- CTA Button -->
        <a href="/signup" class="hidden md:block bg-indigo-600 text-white px-4 py-2 rounded-lg">
            Sign Up
        </a>
    </div>
</nav>
```

**SCSS:**
```scss
.navbar {
    background: white;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    position: sticky;
    top: 0;
    z-index: 50;
}
```

---

### Accessible Forms

Forms with validation and error states:

```html
<form class="form max-w-md mx-auto p-6 bg-white rounded-lg shadow">
    <div class="form__group mb-4">
        <label for="email" class="block text-sm font-bold text-gray-700 mb-2">
            Email Address
        </label>
        <input 
            type="email" 
            id="email" 
            class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500"
            required
        >
        <p class="form__error text-red-600 text-sm mt-1 hidden">
            Please enter a valid email
        </p>
    </div>

    <button type="submit" class="w-full bg-indigo-600 text-white py-3 rounded-lg font-bold">
        Submit
    </button>
</form>
```

---

## Dark Mode Implementation

### Setup CSS Variables

```scss
/* styles/main.scss */
:root {
    --bg-primary: #ffffff;
    --text-primary: #111827;
    --border: #e5e7eb;
}

[data-theme="dark"] {
    --bg-primary: #111827;
    --text-primary: #f9fafb;
    --border: #374151;
}

body {
    background-color: var(--bg-primary);
    color: var(--text-primary);
}
```

### JavaScript Toggle

```javascript
const toggleDarkMode = () => {
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    html.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
};

// Load saved theme
const savedTheme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-theme', savedTheme);
```

### Toggle Button

```html
<button onclick="toggleDarkMode()" class="p-2 rounded-lg bg-gray-200 dark:bg-gray-700">
    🌙 Toggle Dark Mode
</button>
```

---

## Responsive Design Strategy

### Mobile-First Approach

Start with mobile layout, enhance for desktop:

```html
<!-- Mobile: Stack vertically -->
<!-- Tablet (md): 2 columns -->
<!-- Desktop (lg): 4 columns -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
    <div class="bg-white p-4 rounded-lg shadow">Card 1</div>
    <div class="bg-white p-4 rounded-lg shadow">Card 2</div>
    <div class="bg-white p-4 rounded-lg shadow">Card 3</div>
    <div class="bg-white p-4 rounded-lg shadow">Card 4</div>
</div>
```

### Responsive Typography

```scss
h1 {
    font-size: 2rem;      // Mobile: 32px
    
    @media (min-width: 768px) {
        font-size: 3rem;  // Tablet: 48px
    }
    
    @media (min-width: 1024px) {
        font-size: 4rem;  // Desktop: 64px
    }
}
```

---

## Best Practices

### ✅ Do This

- Use BEM for component structure
- Use utilities for modifiers (colors, spacing)
- Keep HTML semantic and readable
- Test on multiple screen sizes

### ❌ Don't Do This

- Don't use 50+ utility classes on one element
- Don't hardcode colors (use `tailpy_config.py`)
- Don't ignore SCSS (use it for complex logic)

---

**See [docs.md](docs.md) for full framework documentation.**
