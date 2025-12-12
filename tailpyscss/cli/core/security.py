import re

def sanitize_css_value(value):
    """
    Sanitize configuration values to prevent CSS injection.
    Allowed: alphanumeric, -, #, %, (, ), ,, ., space.
    """
    if not isinstance(value, str):
        return value
    # Regex: Allow words, hyphens, hashes, percents, parens, commas, dots, spaces.
    # Disallow: ; { } which are used for injection.
    pattern = r'^[\w\-\#\%\(\)\,\.\s]+$'
    if not re.match(pattern, value):
        raise ValueError(f"Security Alert: potentially unsafe CSS value detected: '{value}'. "
                         "Allowed characters: a-z, 0-9, -, #, %, (), ,, ., space.")
    return value
