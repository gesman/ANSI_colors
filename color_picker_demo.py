#!/usr/bin/env python3
"""
ANSI Color Picker - Quick Demo

This script demonstrates the key features of the ANSI color picker tool
with visual examples of different color modes and combinations.

Run this script to get a quick overview of what the color picker can do.
"""

import os
import time
import sys
try:
    # Try relative import first (when used as part of a package)
    from .ansi_color_picker import (
        enable_windows_ansi, colorize, ALL_COLORS, BASIC_COLORS, BRIGHT_COLORS,
        RGB_CUBE_COLORS, GRAYSCALE_COLORS, print_header, rgb_to_ansi_truecolor
    )
except ImportError:
    # Fall back to direct import (when run as a script)
    import os
    import sys
    # Add the parent directory to sys.path
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from ANSI_colors.ansi_color_picker import (
        enable_windows_ansi, colorize, ALL_COLORS, BASIC_COLORS, BRIGHT_COLORS,
        RGB_CUBE_COLORS, GRAYSCALE_COLORS, print_header, rgb_to_ansi_truecolor
    )

# Enable ANSI colors
ANSI_ENABLED = enable_windows_ansi()

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_delay(text, delay=0.03):
    """Print text with a slight delay between characters for a typing effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def demo_intro():
    """Display an introduction to the demo."""
    clear_screen()
    print_header("ANSI Color Picker - Quick Demo")
    
    print_with_delay("\nWelcome to the ANSI Color Picker demonstration!")
    print_with_delay("This demo will show you the key features of the tool.")
    print_with_delay("Let's explore the colorful world of terminal text...\n")
    
    time.sleep(1)

def demo_basic_colors():
    """Demonstrate the basic 16 colors."""
    print_header("Basic 16 Colors")
    
    print("\nStandard Colors (30-37 for foreground, 40-47 for background):")
    for i, color in enumerate(BASIC_COLORS):
        fg_code = color.ansi_fg
        bg_code = color.ansi_bg
        print(f"{colorize(f'{color.name:12}', fg_code)} - "
              f"FG: \\033[{fg_code}m, BG: \\033[{bg_code}m, "
              f"RGB: {color.rgb}, Hex: {color.hex}")
    
    print("\nBright Colors (90-97 for foreground, 100-107 for background):")
    for i, color in enumerate(BRIGHT_COLORS):
        fg_code = color.ansi_fg
        bg_code = color.ansi_bg
        print(f"{colorize(f'{color.name:12}', fg_code)} - "
              f"FG: \\033[{fg_code}m, BG: \\033[{bg_code}m, "
              f"RGB: {color.rgb}, Hex: {color.hex}")
    
    print("\nText Formatting:")
    print(f"{colorize('Bold', bold=True)} - \\033[1m")
    print(f"{colorize('Underline', underline=True)} - \\033[4m")
    print(f"{colorize('Reverse', reverse=True)} - \\033[7m")
    print(f"{colorize('Bold + Underline', bold=True, underline=True)} - \\033[1;4m")
    
    input("\nPress Enter to continue...")

def demo_extended_colors():
    """Demonstrate the extended 256-color palette."""
    clear_screen()
    print_header("Extended 256-Color Palette")
    
    print("\nThe extended palette includes 256 colors:")
    print("- Colors 0-15: Basic and bright colors")
    print("- Colors 16-231: 6×6×6 RGB color cube")
    print("- Colors 232-255: Grayscale colors")
    
    print("\nSample from the RGB cube:")
    # Display a small sample of the RGB cube
    for r in range(2):
        for g in range(3):
            print()
            for b in range(6):
                color_num = 16 + (r * 36) + (g * 6) + b
                color = RGB_CUBE_COLORS[color_num - 16]
                bg_color = colorize(f" {color_num:3d} ", None, color.ansi_bg)
                print(f"{bg_color}", end=" ")
    
    print("\n\nSample from the grayscale range:")
    for i in range(0, 24, 3):  # Show every 3rd grayscale color
        color_num = 232 + i
        color = GRAYSCALE_COLORS[i]
        bg_color = colorize(f" {color_num:3d} ", None, color.ansi_bg)
        print(f"{bg_color}", end=" ")
    
    print("\n\nUsage example:")
    color_num = 202  # A nice orange
    color = ALL_COLORS[color_num]
    print(f"{colorize('This is color 202 (orange)', color.ansi_fg)}")
    print(f"ANSI code: \\033[38;5;{color_num}m for foreground, \\033[48;5;{color_num}m for background")
    
    input("\nPress Enter to continue...")

def demo_truecolor():
    """Demonstrate 24-bit true color."""
    clear_screen()
    print_header("24-bit True Color (RGB)")
    
    print("\nTrue color allows specifying exact RGB values (0-255 for each component).")
    print("Format: \\033[38;2;R;G;Bm for foreground, \\033[48;2;R;G;Bm for background")
    
    print("\nRGB Gradient Examples:")
    
    # Red gradient
    print("\nRed gradient (varying red component):")
    for r in range(0, 256, 32):
        fg_code = rgb_to_ansi_truecolor(r, 0, 0)
        bg_code = rgb_to_ansi_truecolor(r, 0, 0, background=True)
        print(f"{colorize('■', fg_code)}", end="")
    print(f" - Red (0-255, 0, 0)")
    
    # Green gradient
    print("\nGreen gradient (varying green component):")
    for g in range(0, 256, 32):
        fg_code = rgb_to_ansi_truecolor(0, g, 0)
        bg_code = rgb_to_ansi_truecolor(0, g, 0, background=True)
        print(f"{colorize('■', fg_code)}", end="")
    print(f" - Green (0, 0-255, 0)")
    
    # Blue gradient
    print("\nBlue gradient (varying blue component):")
    for b in range(0, 256, 32):
        fg_code = rgb_to_ansi_truecolor(0, 0, b)
        bg_code = rgb_to_ansi_truecolor(0, 0, b, background=True)
        print(f"{colorize('■', fg_code)}", end="")
    print(f" - Blue (0, 0, 0-255)")
    
    # Rainbow
    print("\nRainbow colors:")
    rainbow_colors = [
        (255, 0, 0),    # Red
        (255, 127, 0),  # Orange
        (255, 255, 0),  # Yellow
        (0, 255, 0),    # Green
        (0, 0, 255),    # Blue
        (75, 0, 130),   # Indigo
        (148, 0, 211)   # Violet
    ]
    
    for r, g, b in rainbow_colors:
        bg_code = rgb_to_ansi_truecolor(r, g, b, background=True)
        print(colorize("  ", None, bg_code), end="")
    print(" - Rainbow")
    
    # Example text with RGB colors
    print("\nExample text with RGB colors:")
    r, g, b = 255, 128, 0  # Orange
    fg_code = rgb_to_ansi_truecolor(r, g, b)
    bg_code = rgb_to_ansi_truecolor(0, 0, 128, background=True)  # Dark blue background
    print(colorize("RGB Orange text (255,128,0) on dark blue background (0,0,128)", fg_code, bg_code))
    
    input("\nPress Enter to continue...")

def demo_text_effects():
    """Demonstrate various text effects and combinations."""
    clear_screen()
    print_header("Text Effects and Combinations")
    
    print("\nCombining colors and formatting:")
    
    # Bold colored text
    print(colorize("Bold red text", "31", bold=True))
    print(colorize("Bold green text", "32", bold=True))
    print(colorize("Bold blue text", "34", bold=True))
    
    # Underlined colored text
    print(colorize("Underlined cyan text", "36", underline=True))
    print(colorize("Underlined magenta text", "35", underline=True))
    print(colorize("Underlined yellow text", "33", underline=True))
    
    # Foreground and background combinations
    print(colorize("White text on red background", "37", "41"))
    print(colorize("Black text on green background", "30", "42"))
    print(colorize("Yellow text on blue background", "33", "44"))
    
    # 256-color combinations
    print(colorize("Color 208 (orange) on color 27 (blue)", "38;5;208", "48;5;27"))
    print(colorize("Color 118 (green) on color 54 (purple)", "38;5;118", "48;5;54"))
    print(colorize("Color 226 (yellow) on color 18 (dark blue)", "38;5;226", "48;5;18"))
    
    # RGB color combinations
    orange_fg = rgb_to_ansi_truecolor(255, 128, 0)
    blue_bg = rgb_to_ansi_truecolor(0, 0, 128, background=True)
    print(colorize("RGB orange on RGB dark blue", orange_fg, blue_bg))
    
    pink_fg = rgb_to_ansi_truecolor(255, 105, 180)
    teal_bg = rgb_to_ansi_truecolor(0, 128, 128, background=True)
    print(colorize("RGB pink on RGB teal", pink_fg, teal_bg))
    
    input("\nPress Enter to continue...")

def demo_practical_examples():
    """Show practical examples of using colors in terminal applications."""
    clear_screen()
    print_header("Practical Examples")
    
    # Example 1: Error/Warning/Success messages
    print("\n1. Status Messages:")
    print(colorize("ERROR: File not found", "31", bold=True))
    print(colorize("WARNING: Disk space low", "33", bold=True))
    print(colorize("SUCCESS: Operation completed", "32", bold=True))
    print(colorize("INFO: Processing data", "36"))
    
    # Example 2: Syntax highlighting
    print("\n2. Simple Syntax Highlighting:")
    code = """def calculate_total(items):
    \"\"\"Calculate the total price with tax.\"\"\"
    total = 0
    for item in items:
        total += item.price * (1 + TAX_RATE)
    return total"""
    
    # Very simple syntax highlighting
    highlighted = code
    highlighted = highlighted.replace("def ", colorize("def ", "38;5;208"))
    highlighted = highlighted.replace("return ", colorize("return ", "38;5;208"))
    highlighted = highlighted.replace("for ", colorize("for ", "38;5;208"))
    highlighted = highlighted.replace("in ", colorize("in ", "38;5;208"))
    highlighted = highlighted.replace("\"\"\"", colorize("\"\"\"", "38;5;28"))
    highlighted = highlighted.replace("Calculate the total price with tax.", 
                                     colorize("Calculate the total price with tax.", "38;5;28"))
    highlighted = highlighted.replace("items", colorize("items", "38;5;75"))
    highlighted = highlighted.replace("item", colorize("item", "38;5;75"))
    highlighted = highlighted.replace("total", colorize("total", "38;5;75"))
    highlighted = highlighted.replace("price", colorize("price", "38;5;75"))
    highlighted = highlighted.replace("TAX_RATE", colorize("TAX_RATE", "38;5;208"))
    
    print(highlighted)
    
    # Example 3: Progress bar
    print("\n3. Progress Bar:")
    total = 20
    for i in range(total + 1):
        progress = i / total
        bar_length = 30
        filled_length = int(bar_length * progress)
        bar = colorize('█' * filled_length, "32") + colorize('░' * (bar_length - filled_length), "90")
        percent = colorize(f"{int(100 * progress)}%", "36", bold=True)
        
        sys.stdout.write(f"\rProgress: {bar} {percent}")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")
    
    # Example 4: Table with colored rows
    print("\n4. Colored Table:")
    print(colorize("ID  | Name      | Status   | Score", "97", "44", bold=True))
    print(colorize("001 | Alice     | Active   | 95", "92"))
    print(colorize("002 | Bob       | Inactive | 82", "91"))
    print(colorize("003 | Charlie   | Active   | 88", "92"))
    print(colorize("004 | David     | Pending  | 76", "93"))
    
    input("\nPress Enter to continue...")

def demo_conclusion():
    """Show conclusion and next steps."""
    clear_screen()
    print_header("Conclusion")
    
    print_with_delay("\nThank you for exploring the ANSI Color Picker demo!")
    print_with_delay("To continue exploring, try these tools:")
    
    print("\n1. " + colorize("ansi_color_picker.py", "92", bold=True) + 
          " - Command-line tool with various display modes")
    print("   Example: python ansi_color_picker.py --mode=extended")
    
    print("\n2. " + colorize("color_picker_menu.py", "92", bold=True) + 
          " - Interactive menu-based interface")
    print("   Example: python color_picker_menu.py")
    
    print("\n3. Check " + colorize("README_color_picker.md", "92", bold=True) + 
          " for comprehensive documentation")
    
    print("\nHappy coloring your terminal applications!")
    
    print("\n" + colorize("═" * 60, "38;5;39"))
    rainbow_text = "ANSI COLOR PICKER"
    rainbow_colors = [196, 202, 226, 82, 33, 57, 129, 165]
    
    for i, char in enumerate(rainbow_text):
        color_idx = i % len(rainbow_colors)
        color_code = f"38;5;{rainbow_colors[color_idx]}"
        print(colorize(char, color_code, bold=True), end="")
    print("\n" + colorize("═" * 60, "38;5;39"))

def main():
    """Run the demo."""
    if not ANSI_ENABLED:
        print("Warning: ANSI color codes may not be supported in this terminal.")
        print("The demo may not display correctly.")
        input("Press Enter to continue anyway...")
    
    try:
        demo_intro()
        demo_basic_colors()
        demo_extended_colors()
        demo_truecolor()
        demo_text_effects()
        demo_practical_examples()
        demo_conclusion()
    except KeyboardInterrupt:
        clear_screen()
        print("\nDemo terminated by user.")
        sys.exit(0)

if __name__ == '__main__':
    main()