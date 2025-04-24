"""
ANSI Colors Package

A comprehensive package for exploring and using ANSI color codes in terminal applications.

This package includes:
- ansi_color_picker.py: Main tool for exploring ANSI colors
- color_picker_menu.py: Interactive menu interface
- color_picker_demo.py: Demonstration of key features
- ansi_colors.py: Utility module for using colors in applications
- color_example.py: Real-world examples of using colors

For more information, see README_color_picker.md
"""

# Import main components for easy access
from .ansi_colors import (
    # Basic colors
    black, red, green, yellow, blue, magenta, cyan, white,
    bright_black, bright_red, bright_green, bright_yellow,
    bright_blue, bright_magenta, bright_cyan, bright_white,
    
    # Background colors
    bg_black, bg_red, bg_green, bg_yellow, bg_blue, bg_magenta, bg_cyan, bg_white,
    bg_bright_black, bg_bright_red, bg_bright_green, bg_bright_yellow,
    bg_bright_blue, bg_bright_magenta, bg_bright_cyan, bg_bright_white,
    
    # Styles
    bold, dim, italic, underline, blink, reverse, hidden, strikethrough,
    
    # Advanced coloring
    color256, bg_color256, rgb, bg_rgb,
    
    # Utility functions
    style, strip_ansi, supports_color, print_color_table
)

# Version information
__version__ = '1.0.0'