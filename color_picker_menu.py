#!/usr/bin/env python3
"""
ANSI Color Picker - Interactive Menu Interface

A user-friendly interface for exploring ANSI color codes and their applications.
This menu-driven tool provides easy access to all features of the ANSI color picker.

Usage:
    python color_picker_menu.py
"""

import os
import sys
import re
import subprocess
try:
    # Try relative import first (when used as part of a package)
    from .ansi_color_picker import (
        enable_windows_ansi, colorize, ALL_COLORS, BASIC_COLORS, BRIGHT_COLORS,
        RGB_CUBE_COLORS, GRAYSCALE_COLORS, print_basic_colors, print_extended_colors,
        print_truecolor_samples, print_color_details, print_code_examples,
        preview_colors, print_header
    )
except ImportError:
    # Fall back to direct import (when run as a script)
    import os
    import sys
    # Add the parent directory to sys.path
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from ANSI_colors.ansi_color_picker import (
        enable_windows_ansi, colorize, ALL_COLORS, BASIC_COLORS, BRIGHT_COLORS,
        RGB_CUBE_COLORS, GRAYSCALE_COLORS, print_basic_colors, print_extended_colors,
        print_truecolor_samples, print_color_details, print_code_examples,
        preview_colors, print_header
    )

# Enable ANSI colors
ANSI_ENABLED = enable_windows_ansi()

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    """Print the main menu."""
    clear_screen()
    print_header("ANSI Color Picker - Interactive Menu")
    
    print("\nSelect an option:")
    print(colorize("1. View Basic Colors (16 standard colors)", "36"))
    print(colorize("2. View Extended Color Palette (256 colors)", "36"))
    print(colorize("3. View True Color Samples (24-bit RGB)", "36"))
    print(colorize("4. Color Details & Information", "36"))
    print(colorize("5. Text Preview with Custom Colors", "36"))
    print(colorize("6. Python Code Examples", "36"))
    print(colorize("7. Color Combination Explorer", "36"))
    print(colorize("8. Exit", "36"))
    
    return input("\nEnter your choice (1-8): ")

def color_details_menu():
    """Menu for exploring details of specific colors."""
    while True:
        clear_screen()
        print_header("Color Details & Information")
        
        print("\nSelect a color category:")
        print(colorize("1. Basic Colors (0-7)", "36"))
        print(colorize("2. Bright Colors (8-15)", "36"))
        print(colorize("3. RGB Cube Colors (16-231)", "36"))
        print(colorize("4. Grayscale Colors (232-255)", "36"))
        print(colorize("5. Enter a specific color number (0-255)", "36"))
        print(colorize("6. Return to main menu", "36"))
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            display_color_group(BASIC_COLORS, "Basic Colors", 0)
        elif choice == '2':
            display_color_group(BRIGHT_COLORS, "Bright Colors", 8)
        elif choice == '3':
            display_rgb_cube_colors()
        elif choice == '4':
            display_color_group(GRAYSCALE_COLORS, "Grayscale Colors", 232)
        elif choice == '5':
            try:
                color_num = int(input("\nEnter color number (0-255): "))
                if 0 <= color_num < 256:
                    clear_screen()
                    print_color_details(color_num)
                    input("\nPress Enter to continue...")
                else:
                    print("\nInvalid color number. Must be between 0 and 255.")
                    input("\nPress Enter to continue...")
            except ValueError:
                print("\nInvalid input. Please enter a number.")
                input("\nPress Enter to continue...")
        elif choice == '6':
            return
        else:
            print("\nInvalid choice. Please try again.")
            input("\nPress Enter to continue...")

def display_color_group(colors, title, start_index):
    """Display a group of colors with their details."""
    clear_screen()
    print_header(title)
    
    for i, color in enumerate(colors):
        color_num = start_index + i
        fg_sample = colorize("Text", color.ansi_fg)
        bg_sample = colorize("Text", None, color.ansi_bg)
        
        print(f"\nColor {color_num}: {color.name}")
        print(f"  ANSI Codes: \\033[{color.ansi_fg}m (FG), \\033[{color.ansi_bg}m (BG)")
        print(f"  RGB: {color.rgb}, Hex: {color.hex}")
        print(f"  Samples: {fg_sample} {bg_sample}")
    
    input("\nPress Enter to continue...")

def display_rgb_cube_colors():
    """Display the RGB cube colors in a structured way."""
    clear_screen()
    print_header("RGB Cube Colors (16-231)")
    
    print("\nThe RGB cube consists of 216 colors arranged in a 6×6×6 cube.")
    print("Each color is a combination of Red, Green, and Blue values.")
    
    # Display a simplified representation of the cube
    print("\nColor number format: 16 + (36 × r) + (6 × g) + b")
    print("Where r, g, b are values from 0 to 5")
    
    # Show a sample of the cube
    print("\nSample of the RGB cube (first 36 colors):")
    for r in range(1):  # Just show the first layer
        for g in range(6):
            print()
            for b in range(6):
                color_num = 16 + (r * 36) + (g * 6) + b
                color = RGB_CUBE_COLORS[color_num - 16]
                bg_color = colorize(f" {color_num:3d} ", None, color.ansi_bg)
                print(f"{bg_color}", end=" ")
    
    print("\n\nTo see details for a specific color, use option 5 in the previous menu.")
    input("\nPress Enter to continue...")

def text_preview_menu():
    """Menu for previewing text with custom colors."""
    while True:
        clear_screen()
        print_header("Text Preview with Custom Colors")
        
        print("\nOptions:")
        print(colorize("1. Use color numbers (0-255)", "36"))
        print(colorize("2. Use RGB values", "36"))
        print(colorize("3. Return to main menu", "36"))
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            try:
                fg = input("\nEnter foreground color number (0-255, or leave empty for default): ")
                bg = input("Enter background color number (0-255, or leave empty for default): ")
                text = input("Enter text to preview (or leave empty for default): ")
                
                fg = int(fg) if fg else None
                bg = int(bg) if bg else None
                text = text if text else "Hello, ANSI colors!"
                
                clear_screen()
                preview_colors(fg, bg, text)
                input("\nPress Enter to continue...")
            except ValueError:
                print("\nInvalid input. Please enter valid numbers.")
                input("\nPress Enter to continue...")
        elif choice == '2':
            try:
                fg_input = input("\nEnter foreground RGB values (r,g,b or leave empty for default): ")
                bg_input = input("Enter background RGB values (r,g,b or leave empty for default): ")
                text = input("Enter text to preview (or leave empty for default): ")
                
                fg = fg_input if fg_input else None
                bg = bg_input if bg_input else None
                text = text if text else "Hello, ANSI colors!"
                
                clear_screen()
                preview_colors(fg, bg, text)
                input("\nPress Enter to continue...")
            except ValueError:
                print("\nInvalid input. Please enter valid RGB values.")
                input("\nPress Enter to continue...")
        elif choice == '3':
            return
        else:
            print("\nInvalid choice. Please try again.")
            input("\nPress Enter to continue...")

def color_combination_explorer():
    """Interactive tool to explore foreground and background color combinations."""
    clear_screen()
    print_header("Color Combination Explorer")
    
    print("\nThis tool helps you explore different combinations of foreground and background colors.")
    print("Use arrow keys to navigate, 'q' to quit.")
    
    # Create a grid of color combinations
    fg_colors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    bg_colors = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    # Print the grid header
    print("\n     ", end="")
    for bg in bg_colors:
        print(f"BG{bg:2d} ", end="")
    print()
    
    # Print the grid
    for fg in fg_colors:
        print(f"FG{fg:2d} ", end="")
        for bg in bg_colors:
            fg_code = ALL_COLORS[fg].ansi_fg
            bg_code = ALL_COLORS[bg].ansi_bg
            print(colorize("Ab", fg_code, bg_code), end=" ")
        print()
    
    print("\nExtended combinations:")
    print("Try combinations like FG=196 (bright red) with BG=46 (bright green):")
    fg, bg = 196, 46
    fg_code = ALL_COLORS[fg].ansi_fg
    bg_code = ALL_COLORS[bg].ansi_bg
    print(colorize("Sample Text", fg_code, bg_code))
    
    print("\nOr FG=51 (cyan) with BG=90 (dark gray):")
    fg, bg = 51, 90
    fg_code = ALL_COLORS[fg].ansi_fg
    bg_code = ALL_COLORS[bg].ansi_bg
    print(colorize("Sample Text", fg_code, bg_code))
    
    input("\nPress Enter to continue...")

def main():
    """Main function."""
    if not ANSI_ENABLED:
        print("Warning: ANSI color codes may not be supported in this terminal.")
        input("Press Enter to continue anyway...")
    
    while True:
        choice = print_menu()
        
        if choice == '1':
            clear_screen()
            print_basic_colors()
            input("\nPress Enter to continue...")
        elif choice == '2':
            clear_screen()
            print_extended_colors()
            input("\nPress Enter to continue...")
        elif choice == '3':
            clear_screen()
            print_truecolor_samples()
            input("\nPress Enter to continue...")
        elif choice == '4':
            color_details_menu()
        elif choice == '5':
            text_preview_menu()
        elif choice == '6':
            clear_screen()
            print_code_examples()
            input("\nPress Enter to continue...")
        elif choice == '7':
            color_combination_explorer()
        elif choice == '8':
            clear_screen()
            print("Thank you for using the ANSI Color Picker!")
            sys.exit(0)
        else:
            print("\nInvalid choice. Please try again.")
            input("\nPress Enter to continue...")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("\nProgram terminated by user.")
        sys.exit(0)