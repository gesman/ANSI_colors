#!/usr/bin/env python3
"""
ANSI Colors Utility Module

A lightweight utility for easily adding ANSI colors to terminal output in Python scripts.
This module provides simple functions and constants for working with terminal colors.

Usage:
    from ansi_colors import *
    
    print(red("This text is red"))
    print(bg_blue("Blue background"))
    print(bold(green("Bold green text")))
    print(underline(yellow("Underlined yellow text")))
    print(rgb(255, 128, 0, "Orange text"))
    print(bg_rgb(0, 0, 128, "Text with dark blue background"))
"""

import os
import sys
import ctypes
from functools import wraps

# Enable ANSI escapes on Windows consoles
def enable_windows_ansi():
    """Enable ANSI escape sequences on Windows."""
    if os.name == 'nt':
        try:
            k32 = ctypes.windll.kernel32
            h = k32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
            mode = ctypes.c_ulong()
            if k32.GetConsoleMode(h, ctypes.byref(mode)):
                # ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
                k32.SetConsoleMode(h, mode.value | 0x0004)
                return True
        except Exception:
            pass
    return os.name != 'nt'  # True if not Windows (likely supports ANSI)

# Call this at startup
ANSI_ENABLED = enable_windows_ansi()

# ANSI escape sequence constants
ESC = '\033['
RESET = f'{ESC}0m'

# Text formatting
BOLD = f'{ESC}1m'
DIM = f'{ESC}2m'
ITALIC = f'{ESC}3m'
UNDERLINE = f'{ESC}4m'
BLINK = f'{ESC}5m'
REVERSE = f'{ESC}7m'
HIDDEN = f'{ESC}8m'
STRIKETHROUGH = f'{ESC}9m'

# Basic foreground colors
BLACK = f'{ESC}30m'
RED = f'{ESC}31m'
GREEN = f'{ESC}32m'
YELLOW = f'{ESC}33m'
BLUE = f'{ESC}34m'
MAGENTA = f'{ESC}35m'
CYAN = f'{ESC}36m'
WHITE = f'{ESC}37m'
DEFAULT_FG = f'{ESC}39m'

# Basic background colors
BG_BLACK = f'{ESC}40m'
BG_RED = f'{ESC}41m'
BG_GREEN = f'{ESC}42m'
BG_YELLOW = f'{ESC}43m'
BG_BLUE = f'{ESC}44m'
BG_MAGENTA = f'{ESC}45m'
BG_CYAN = f'{ESC}46m'
BG_WHITE = f'{ESC}47m'
DEFAULT_BG = f'{ESC}49m'

# Bright foreground colors
BRIGHT_BLACK = f'{ESC}90m'
BRIGHT_RED = f'{ESC}91m'
BRIGHT_GREEN = f'{ESC}92m'
BRIGHT_YELLOW = f'{ESC}93m'
BRIGHT_BLUE = f'{ESC}94m'
BRIGHT_MAGENTA = f'{ESC}95m'
BRIGHT_CYAN = f'{ESC}96m'
BRIGHT_WHITE = f'{ESC}97m'

# Bright background colors
BG_BRIGHT_BLACK = f'{ESC}100m'
BG_BRIGHT_RED = f'{ESC}101m'
BG_BRIGHT_GREEN = f'{ESC}102m'
BG_BRIGHT_YELLOW = f'{ESC}103m'
BG_BRIGHT_BLUE = f'{ESC}104m'
BG_BRIGHT_MAGENTA = f'{ESC}105m'
BG_BRIGHT_CYAN = f'{ESC}106m'
BG_BRIGHT_WHITE = f'{ESC}107m'

def colorize(text, *args):
    """Apply ANSI color codes to text.
    
    Args:
        text: The text to colorize
        *args: Any number of ANSI color codes to apply
        
    Returns:
        The colorized text string
    """
    if not ANSI_ENABLED or not args:
        return text
    
    return ''.join(args) + text + RESET

# Basic color functions
def black(text): return colorize(text, BLACK)
def red(text): return colorize(text, RED)
def green(text): return colorize(text, GREEN)
def yellow(text): return colorize(text, YELLOW)
def blue(text): return colorize(text, BLUE)
def magenta(text): return colorize(text, MAGENTA)
def cyan(text): return colorize(text, CYAN)
def white(text): return colorize(text, WHITE)

# Bright color functions
def bright_black(text): return colorize(text, BRIGHT_BLACK)
def bright_red(text): return colorize(text, BRIGHT_RED)
def bright_green(text): return colorize(text, BRIGHT_GREEN)
def bright_yellow(text): return colorize(text, BRIGHT_YELLOW)
def bright_blue(text): return colorize(text, BRIGHT_BLUE)
def bright_magenta(text): return colorize(text, BRIGHT_MAGENTA)
def bright_cyan(text): return colorize(text, BRIGHT_CYAN)
def bright_white(text): return colorize(text, BRIGHT_WHITE)

# Background color functions
def bg_black(text): return colorize(text, BG_BLACK)
def bg_red(text): return colorize(text, BG_RED)
def bg_green(text): return colorize(text, BG_GREEN)
def bg_yellow(text): return colorize(text, BG_YELLOW)
def bg_blue(text): return colorize(text, BG_BLUE)
def bg_magenta(text): return colorize(text, BG_MAGENTA)
def bg_cyan(text): return colorize(text, BG_CYAN)
def bg_white(text): return colorize(text, BG_WHITE)

# Bright background color functions
def bg_bright_black(text): return colorize(text, BG_BRIGHT_BLACK)
def bg_bright_red(text): return colorize(text, BG_BRIGHT_RED)
def bg_bright_green(text): return colorize(text, BG_BRIGHT_GREEN)
def bg_bright_yellow(text): return colorize(text, BG_BRIGHT_YELLOW)
def bg_bright_blue(text): return colorize(text, BG_BRIGHT_BLUE)
def bg_bright_magenta(text): return colorize(text, BG_BRIGHT_MAGENTA)
def bg_bright_cyan(text): return colorize(text, BG_BRIGHT_CYAN)
def bg_bright_white(text): return colorize(text, BG_BRIGHT_WHITE)

# Style functions
def bold(text): return colorize(text, BOLD)
def dim(text): return colorize(text, DIM)
def italic(text): return colorize(text, ITALIC)
def underline(text): return colorize(text, UNDERLINE)
def blink(text): return colorize(text, BLINK)
def reverse(text): return colorize(text, REVERSE)
def hidden(text): return colorize(text, HIDDEN)
def strikethrough(text): return colorize(text, STRIKETHROUGH)

# 256-color functions
def color256(n, text):
    """Apply a color from the 256-color palette."""
    if not 0 <= n <= 255:
        raise ValueError(f"Color index must be between 0 and 255, got {n}")
    return colorize(text, f'{ESC}38;5;{n}m')

def bg_color256(n, text):
    """Apply a background color from the 256-color palette."""
    if not 0 <= n <= 255:
        raise ValueError(f"Color index must be between 0 and 255, got {n}")
    return colorize(text, f'{ESC}48;5;{n}m')

# RGB color functions
def rgb(r, g, b, text):
    """Apply an RGB foreground color."""
    if not all(0 <= c <= 255 for c in (r, g, b)):
        raise ValueError(f"RGB values must be between 0 and 255, got ({r}, {g}, {b})")
    return colorize(text, f'{ESC}38;2;{r};{g};{b}m')

def bg_rgb(r, g, b, text):
    """Apply an RGB background color."""
    if not all(0 <= c <= 255 for c in (r, g, b)):
        raise ValueError(f"RGB values must be between 0 and 255, got ({r}, {g}, {b})")
    return colorize(text, f'{ESC}48;2;{r};{g};{b}m')

# Composite functions for combining styles
def style(text, fg=None, bg=None, bold_=False, underline_=False, reverse_=False):
    """Apply multiple styles at once.
    
    Args:
        text: The text to style
        fg: Foreground color code or function
        bg: Background color code or function
        bold_: Whether to make the text bold
        underline_: Whether to underline the text
        reverse_: Whether to reverse the colors
        
    Returns:
        The styled text
    """
    # Start with the text
    result = text
    
    # Apply foreground color if provided
    if fg:
        if callable(fg):
            # If fg is a function (like red, green, etc.)
            result = fg(result)
        else:
            # If fg is a color code string
            result = colorize(result, fg)
    
    # Apply background color if provided
    if bg:
        if callable(bg):
            # If bg is a function (like bg_red, bg_green, etc.)
            result = bg(result)
        else:
            # If bg is a color code string
            result = colorize(result, bg)
    
    # Apply other styles
    if bold_:
        result = bold(result)
    if underline_:
        result = underline(result)
    if reverse_:
        result = reverse(result)
    
    return result

# Function decorators for styling function output
def colored_output(color_func):
    """Decorator to apply a color function to the output of another function."""
    @wraps(color_func)
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                return color_func(result)
            return result
        return wrapper
    return decorator

# Example usage of the decorator:
# @colored_output(red)
# def get_error_message():
#     return "An error occurred"

# Utility functions
def strip_ansi(text):
    """Remove ANSI escape sequences from a string."""
    import re
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def supports_color():
    """Check if the current terminal supports color."""
    return ANSI_ENABLED

def print_color_table():
    """Print a table of available colors."""
    print("Basic colors (30-37):")
    for i, func in enumerate([black, red, green, yellow, blue, magenta, cyan, white], 30):
        print(f"{i}: {func(f'Color {i}')}")
    
    print("\nBright colors (90-97):")
    for i, func in enumerate([bright_black, bright_red, bright_green, bright_yellow, 
                             bright_blue, bright_magenta, bright_cyan, bright_white], 90):
        print(f"{i}: {func(f'Color {i}')}")
    
    print("\nSample 256-color palette:")
    for i in range(0, 256, 16):
        for j in range(16):
            if i + j < 256:
                print(color256(i + j, f"{i+j:3d}"), end=" ")
        print()

if __name__ == "__main__":
    # Show examples when run directly
    print("\nANSI Colors Utility Examples:\n")
    
    print("Basic colors:")
    print(black("Black"), red("Red"), green("Green"), yellow("Yellow"), 
          blue("Blue"), magenta("Magenta"), cyan("Cyan"), white("White"))
    
    print("\nBright colors:")
    print(bright_black("Bright Black"), bright_red("Bright Red"), 
          bright_green("Bright Green"), bright_yellow("Bright Yellow"),
          bright_blue("Bright Blue"), bright_magenta("Bright Magenta"), 
          bright_cyan("Bright Cyan"), bright_white("Bright White"))
    
    print("\nBackground colors:")
    print(bg_black("Black BG"), bg_red("Red BG"), bg_green("Green BG"), 
          bg_yellow("Yellow BG"), bg_blue("Blue BG"), bg_magenta("Magenta BG"), 
          bg_cyan("Cyan BG"), bg_white("White BG"))
    
    print("\nText styles:")
    print(bold("Bold"), dim("Dim"), italic("Italic"), underline("Underline"), 
          blink("Blink"), reverse("Reverse"), strikethrough("Strikethrough"))
    
    print("\nCombinations:")
    print(bold(red("Bold Red")), bg_blue(yellow("Yellow on Blue")), 
          underline(bright_green("Underlined Bright Green")))
    
    print("\n256-color mode:")
    print(color256(196, "Color 196 (bright red)"), 
          color256(46, "Color 46 (bright green)"),
          color256(21, "Color 21 (blue)"),
          color256(208, "Color 208 (orange)"))
    
    print("\nRGB colors:")
    print(rgb(255, 128, 0, "RGB Orange"), 
          rgb(128, 0, 128, "RGB Purple"),
          bg_rgb(0, 0, 128, "RGB Dark Blue Background"))
    
    print("\nComplex styling:")
    print(style("Custom Style", RED, BG_YELLOW, bold_=True, underline_=True))
    
    print("\nFor more examples and a color table, run:")
    print(cyan("  python -c 'from ansi_colors import print_color_table; print_color_table()'"))