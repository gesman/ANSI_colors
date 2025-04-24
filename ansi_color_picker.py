#!/usr/bin/env python3
"""
ANSI Color Picker Tool

A comprehensive tool for exploring and using ANSI color codes in terminal applications.
Features:
- Visual display of all standard and extended color combinations
- Shows ANSI escape sequences, RGB values, and hex codes
- Organized by color categories (basic, bright, grayscale, RGB cube)
- Multiple display modes
- Code examples for Python libraries (colorama, rich, direct ANSI)
- Text preview with custom color combinations

Usage:
    python ansi_color_picker.py [options]

Options:
    --mode=<mode>       Display mode: basic, extended, truecolor, examples, preview
                        (default: basic)
    --fg=<color>        Set foreground color for preview (0-255 or r,g,b)
    --bg=<color>        Set background color for preview (0-255 or r,g,b)
    --text=<text>       Custom text for preview (default: "Hello, ANSI colors!")
    --help              Show this help message
"""

import os
import sys
import re
import ctypes
from collections import namedtuple

# Enable ANSI escapes on Windows consoles
def enable_windows_ansi():
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

# Color definitions
Color = namedtuple('Color', ['name', 'ansi_fg', 'ansi_bg', 'rgb', 'hex'])

# Basic 8 colors
BASIC_COLORS = [
    Color('Black',        '30', '40', (0, 0, 0),       '#000000'),
    Color('Red',          '31', '41', (170, 0, 0),     '#AA0000'),
    Color('Green',        '32', '42', (0, 170, 0),     '#00AA00'),
    Color('Yellow',       '33', '43', (170, 85, 0),    '#AA5500'),
    Color('Blue',         '34', '44', (0, 0, 170),     '#0000AA'),
    Color('Magenta',      '35', '45', (170, 0, 170),   '#AA00AA'),
    Color('Cyan',         '36', '46', (0, 170, 170),   '#00AAAA'),
    Color('White',        '37', '47', (170, 170, 170), '#AAAAAA'),
]

# Bright versions of the 8 basic colors
BRIGHT_COLORS = [
    Color('Bright Black',   '90', '100', (85, 85, 85),     '#555555'),
    Color('Bright Red',     '91', '101', (255, 85, 85),    '#FF5555'),
    Color('Bright Green',   '92', '102', (85, 255, 85),    '#55FF55'),
    Color('Bright Yellow',  '93', '103', (255, 255, 85),   '#FFFF55'),
    Color('Bright Blue',    '94', '104', (85, 85, 255),    '#5555FF'),
    Color('Bright Magenta', '95', '105', (255, 85, 255),   '#FF55FF'),
    Color('Bright Cyan',    '96', '106', (85, 255, 255),   '#55FFFF'),
    Color('Bright White',   '97', '107', (255, 255, 255),  '#FFFFFF'),
]

# Generate 216 colors of the 6x6x6 RGB cube (colors 16-231)
RGB_CUBE_COLORS = []
for r in range(6):
    for g in range(6):
        for b in range(6):
            color_num = 16 + (r * 36) + (g * 6) + b
            # Calculate RGB values (0, 95, 135, 175, 215, 255)
            rgb_r = 0 if r == 0 else (r * 40 + 55)
            rgb_g = 0 if g == 0 else (g * 40 + 55)
            rgb_b = 0 if b == 0 else (b * 40 + 55)
            hex_color = f'#{rgb_r:02X}{rgb_g:02X}{rgb_b:02X}'
            name = f'Color {color_num}'
            RGB_CUBE_COLORS.append(Color(name, f'38;5;{color_num}', f'48;5;{color_num}', 
                                         (rgb_r, rgb_g, rgb_b), hex_color))

# Generate 24 grayscale colors (colors 232-255)
GRAYSCALE_COLORS = []
for i in range(24):
    color_num = 232 + i
    # Calculate grayscale value (8, 18, 28, ..., 238)
    gray_value = 8 + i * 10
    hex_color = f'#{gray_value:02X}{gray_value:02X}{gray_value:02X}'
    name = f'Gray {color_num}'
    GRAYSCALE_COLORS.append(Color(name, f'38;5;{color_num}', f'48;5;{color_num}', 
                                 (gray_value, gray_value, gray_value), hex_color))

# All 256 colors
ALL_COLORS = BASIC_COLORS + BRIGHT_COLORS + RGB_CUBE_COLORS + GRAYSCALE_COLORS

def colorize(text, fg=None, bg=None, bold=False, underline=False, reverse=False):
    """Apply ANSI color codes to text."""
    if not ANSI_ENABLED:
        return text
    
    codes = []
    if fg:
        codes.append(fg)
    if bg:
        codes.append(bg)
    if bold:
        codes.append('1')
    if underline:
        codes.append('4')
    if reverse:
        codes.append('7')
    
    if not codes:
        return text
    
    return f"{ESC}{';'.join(codes)}m{text}{RESET}"

def rgb_to_ansi_truecolor(r, g, b, background=False):
    """Convert RGB values to 24-bit ANSI color code."""
    code = '48;2' if background else '38;2'
    return f"{code};{r};{g};{b}"

def rgb_to_hex(r, g, b):
    """Convert RGB values to hex color code."""
    return f"#{r:02X}{g:02X}{b:02X}"

def print_header(title):
    """Print a formatted header."""
    width = 80
    print("\n" + "=" * width)
    print(f"{title:^{width}}")
    print("=" * width)

def print_basic_colors():
    """Display the 16 basic colors (8 standard + 8 bright)."""
    print_header("Basic 16 Colors (Standard + Bright)")
    
    # Print column headers
    print("\nColor Name".ljust(20), "FG Code".ljust(10), "BG Code".ljust(10), 
          "RGB".ljust(15), "Hex".ljust(10), "Sample".ljust(20))
    print("-" * 80)
    
    # Print standard colors
    for color in BASIC_COLORS + BRIGHT_COLORS:
        fg_sample = colorize("Text", color.ansi_fg)
        bg_sample = colorize("Text", None, color.ansi_bg)
        rgb_str = f"({color.rgb[0]}, {color.rgb[1]}, {color.rgb[2]})"
        
        print(f"{color.name.ljust(20)} "
              f"{('\\033[' + color.ansi_fg + 'm').ljust(10)} "
              f"{('\\033[' + color.ansi_bg + 'm').ljust(10)} "
              f"{rgb_str.ljust(15)} "
              f"{color.hex.ljust(10)} "
              f"{fg_sample} {bg_sample}")

def print_color_grid(colors, title, columns=8):
    """Print a grid of colors with their information."""
    print_header(title)
    
    for i, color in enumerate(colors):
        if i % columns == 0:
            print()
        
        # Print color block and number
        bg_color = colorize(f" {i+16:3d} ", None, color.ansi_bg)
        print(f"{bg_color}", end=" ")
        
        # Print newline after last column
        if (i + 1) % columns == 0 or i == len(colors) - 1:
            print()

def print_extended_colors():
    """Display the extended 256-color palette."""
    print_header("Extended 256-Color Palette")
    
    # Print 16 basic colors
    print("\n--- Basic 16 Colors (0-15) ---")
    for i, color in enumerate(BASIC_COLORS + BRIGHT_COLORS):
        if i % 8 == 0:
            print()
        bg_color = colorize(f" {i:3d} ", None, color.ansi_bg)
        print(f"{bg_color}", end=" ")
        if (i + 1) % 8 == 0:
            print()
    
    # Print 6x6x6 RGB cube (216 colors)
    print("\n\n--- 6x6x6 RGB Cube (16-231) ---")
    # Print in a more organized way to show the cube structure
    for r in range(6):
        for g_block in range(3):  # Split into 2 rows for better display
            print()
            for g in range(2):
                g_val = g + g_block * 2
                for b in range(6):
                    color_num = 16 + (r * 36) + (g_val * 6) + b
                    color = RGB_CUBE_COLORS[color_num - 16]
                    bg_color = colorize(f" {color_num:3d} ", None, color.ansi_bg)
                    print(f"{bg_color}", end=" ")
                print("  ", end="")  # Separate the two g-value groups
            print()
        print()  # Extra line between r-value groups
    
    # Print grayscale colors
    print("\n--- Grayscale (232-255) ---")
    for i, color in enumerate(GRAYSCALE_COLORS):
        if i % 8 == 0:
            print()
        color_num = 232 + i
        bg_color = colorize(f" {color_num:3d} ", None, color.ansi_bg)
        print(f"{bg_color}", end=" ")
        if (i + 1) % 8 == 0 or i == len(GRAYSCALE_COLORS) - 1:
            print()

def print_color_details(color_num):
    """Print detailed information about a specific color."""
    if 0 <= color_num < 16:
        color = (BASIC_COLORS + BRIGHT_COLORS)[color_num]
    elif 16 <= color_num < 232:
        color = RGB_CUBE_COLORS[color_num - 16]
    elif 232 <= color_num < 256:
        color = GRAYSCALE_COLORS[color_num - 232]
    else:
        print(f"Invalid color number: {color_num}")
        return
    
    print_header(f"Color {color_num}: {color.name}")
    print(f"\nANSI Codes:")
    print(f"  Foreground: \\033[{color.ansi_fg}m")
    print(f"  Background: \\033[{color.ansi_bg}m")
    print(f"\nRGB Values: {color.rgb}")
    print(f"Hex Code: {color.hex}")
    
    print("\nSamples:")
    print(f"  Text with foreground: {colorize('Sample Text', color.ansi_fg)}")
    print(f"  Text with background: {colorize('Sample Text', None, color.ansi_bg)}")
    print(f"  Bold text: {colorize('Sample Text', color.ansi_fg, bold=True)}")
    print(f"  Underlined text: {colorize('Sample Text', color.ansi_fg, underline=True)}")
    print(f"  Reversed text: {colorize('Sample Text', color.ansi_fg, reverse=True)}")
    
    # Show combinations with other colors
    print("\nCombinations with other colors:")
    for i, other in enumerate([0, 7, 15, 226, 21, 201, 46, 231]):  # Selected contrasting colors
        other_color = ALL_COLORS[other] if other < len(ALL_COLORS) else BASIC_COLORS[0]
        print(f"  With color {other}: "
              f"{colorize('Text', color.ansi_fg, other_color.ansi_bg)} "
              f"{colorize('Text', other_color.ansi_fg, color.ansi_bg)}")

def print_truecolor_samples():
    """Display samples of 24-bit true color."""
    print_header("24-bit True Color Samples")
    
    print("\nGradients:")
    
    # Red gradient
    print("\nRed Gradient:")
    for i in range(0, 256, 16):
        bg_color = rgb_to_ansi_truecolor(i, 0, 0, background=True)
        print(colorize(f" {i:3d} ", bg_color), end=" ")
    print()
    
    # Green gradient
    print("\nGreen Gradient:")
    for i in range(0, 256, 16):
        bg_color = rgb_to_ansi_truecolor(0, i, 0, background=True)
        print(colorize(f" {i:3d} ", bg_color), end=" ")
    print()
    
    # Blue gradient
    print("\nBlue Gradient:")
    for i in range(0, 256, 16):
        bg_color = rgb_to_ansi_truecolor(0, 0, i, background=True)
        print(colorize(f" {i:3d} ", bg_color), end=" ")
    print()
    
    # Gray gradient
    print("\nGray Gradient:")
    for i in range(0, 256, 16):
        bg_color = rgb_to_ansi_truecolor(i, i, i, background=True)
        print(colorize(f" {i:3d} ", bg_color), end=" ")
    print()
    
    # Rainbow
    print("\nRainbow:")
    for i in range(0, 360, 20):
        # Convert HSV to RGB (simplified, with S=V=1)
        h = i / 60
        sector = int(h)
        frac = h - sector
        
        if sector == 0:
            r, g, b = 255, int(255 * frac), 0
        elif sector == 1:
            r, g, b = int(255 * (1 - frac)), 255, 0
        elif sector == 2:
            r, g, b = 0, 255, int(255 * frac)
        elif sector == 3:
            r, g, b = 0, int(255 * (1 - frac)), 255
        elif sector == 4:
            r, g, b = int(255 * frac), 0, 255
        else:
            r, g, b = 255, 0, int(255 * (1 - frac))
        
        bg_color = rgb_to_ansi_truecolor(r, g, b, background=True)
        print(colorize(f" {i:3d}° ", bg_color), end=" ")
    print()
    
    # Small color matrix
    print("\nColor Matrix (Red × Green, Blue=128):")
    size = 8  # 8×8 matrix
    for r in range(size):
        print()
        r_val = int(r * 255 / (size - 1))
        for g in range(size):
            g_val = int(g * 255 / (size - 1))
            bg_color = rgb_to_ansi_truecolor(r_val, g_val, 128, background=True)
            print(colorize("  ", bg_color), end="")
    print()

def print_code_examples():
    """Display code examples for using ANSI colors in Python."""
    print_header("Python Code Examples for Terminal Colors")
    
    # Direct ANSI sequences
    print("\n--- Direct ANSI Escape Sequences ---")
    print("""
# Basic usage
print("\\033[31mRed text\\033[0m")
print("\\033[1;32mBold green text\\033[0m")
print("\\033[3;33mItalic yellow text\\033[0m")
print("\\033[4;34mUnderlined blue text\\033[0m")
print("\\033[45mMagenta background\\033[0m")
print("\\033[1;36;44mBold cyan text on blue background\\033[0m")

# 256-color mode
print("\\033[38;5;208mOrange text (color 208)\\033[0m")
print("\\033[48;5;27mBackground color 27\\033[0m")

# True color (24-bit)
print("\\033[38;2;255;128;0mRGB orange text\\033[0m")
print("\\033[48;2;0;128;255mRGB blue background\\033[0m")
""")
    
    # Colorama examples
    print("\n--- Using Colorama Library ---")
    print("""
from colorama import init, Fore, Back, Style

# Initialize colorama (required on Windows)
init()

# Basic colors
print(Fore.RED + "Red text")
print(Back.GREEN + "Green background")
print(Fore.BLUE + Back.YELLOW + "Blue text on yellow background")
print(Style.BRIGHT + "Bright text")
print(Style.DIM + "Dim text")

# Reset all formatting
print(Style.RESET_ALL + "Normal text")

# Combine styles
print(Fore.MAGENTA + Back.CYAN + Style.BRIGHT + "Bright magenta on cyan" + Style.RESET_ALL)
""")
    
    # Rich examples
    print("\n--- Using Rich Library ---")
    print("""
from rich import print
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table

# Simple colored text
print("[bold red]Bold red text[/bold red]")
print("[blue on yellow]Blue text on yellow background[/blue on yellow]")

# Using Console for more control
console = Console()
console.print("RGB colors", style="rgb(255,128,0)")
console.print("Named colors", style="deep_sky_blue1")

# Styled Text object
text = Text("Gradient text")
text.stylize("bold magenta", 0, 8)
text.stylize("yellow", 8, 13)
console.print(text)

# Tables with colors
table = Table(title="Colored Table")
table.add_column("Name", style="cyan")
table.add_column("Value", style="magenta")
table.add_row("Item 1", "[green]Active[/green]")
table.add_row("Item 2", "[red]Inactive[/red]")
console.print(table)

# Panels
console.print(Panel("Styled panel content", 
                   title="Title", 
                   subtitle="Subtitle",
                   style="green"))
""")
    
    # Custom color function
    print("\n--- Custom Color Function ---")
    print("""
def colorize(text, fg=None, bg=None, bold=False, underline=False):
    \"\"\"Apply ANSI color codes to text.\"\"\"
    codes = []
    
    if fg:
        if isinstance(fg, tuple) and len(fg) == 3:  # RGB tuple
            codes.append(f"38;2;{fg[0]};{fg[1]};{fg[2]}")
        elif isinstance(fg, int) and 0 <= fg < 256:  # 256-color
            codes.append(f"38;5;{fg}")
        else:  # Basic color code
            codes.append(fg)
    
    if bg:
        if isinstance(bg, tuple) and len(bg) == 3:  # RGB tuple
            codes.append(f"48;2;{bg[0]};{bg[1]};{bg[2]}")
        elif isinstance(bg, int) and 0 <= bg < 256:  # 256-color
            codes.append(f"48;5;{bg}")
        else:  # Basic color code
            codes.append(bg)
    
    if bold:
        codes.append('1')
    if underline:
        codes.append('4')
    
    if not codes:
        return text
    
    return f"\\033[{';'.join(codes)}m{text}\\033[0m"

# Examples
print(colorize("Basic red text", "31"))
print(colorize("256-color text", 202))
print(colorize("RGB color text", (255, 128, 0)))
print(colorize("Text with background", "97", "44"))
print(colorize("RGB background", None, (0, 128, 255)))
print(colorize("Bold underlined text", "32", bold=True, underline=True))
""")

def preview_colors(fg_color=None, bg_color=None, text="Hello, ANSI colors!"):
    """Preview text with specified foreground and background colors."""
    print_header("Color Preview")
    
    if not fg_color and not bg_color:
        print("\nNo colors specified. Showing sample combinations:")
        
        # Show some sample combinations
        combinations = [
            (1, None), (None, 3), (4, 7), (15, 0), 
            (196, None), (None, 46), (51, 196), (226, 18)
        ]
        
        for fg, bg in combinations:
            fg_code = ALL_COLORS[fg].ansi_fg if fg is not None else None
            bg_code = ALL_COLORS[bg].ansi_bg if bg is not None else None
            
            fg_desc = f"fg={fg}" if fg is not None else "default fg"
            bg_desc = f"bg={bg}" if bg is not None else "default bg"
            
            print(f"\n{fg_desc}, {bg_desc}:")
            print(colorize(text, fg_code, bg_code))
        
        return
    
    # Parse color specifications
    fg_code = None
    bg_code = None
    
    if fg_color:
        if ',' in fg_color:  # RGB format
            try:
                r, g, b = map(int, fg_color.split(','))
                fg_code = rgb_to_ansi_truecolor(r, g, b)
                print(f"\nForeground: RGB({r},{g},{b}) - Hex: {rgb_to_hex(r, g, b)}")
            except ValueError:
                print(f"Invalid RGB format for foreground: {fg_color}")
        else:  # Color number
            try:
                color_num = int(fg_color)
                if 0 <= color_num < len(ALL_COLORS):
                    fg_code = ALL_COLORS[color_num].ansi_fg
                    print(f"\nForeground: Color {color_num} - {ALL_COLORS[color_num].name}")
                else:
                    print(f"Invalid color number for foreground: {color_num}")
            except ValueError:
                print(f"Invalid color specification for foreground: {fg_color}")
    
    if bg_color:
        if ',' in bg_color:  # RGB format
            try:
                r, g, b = map(int, bg_color.split(','))
                bg_code = rgb_to_ansi_truecolor(r, g, b, background=True)
                print(f"Background: RGB({r},{g},{b}) - Hex: {rgb_to_hex(r, g, b)}")
            except ValueError:
                print(f"Invalid RGB format for background: {bg_color}")
        else:  # Color number
            try:
                color_num = int(bg_color)
                if 0 <= color_num < len(ALL_COLORS):
                    bg_code = ALL_COLORS[color_num].ansi_bg
                    print(f"Background: Color {color_num} - {ALL_COLORS[color_num].name}")
                else:
                    print(f"Invalid color number for background: {color_num}")
            except ValueError:
                print(f"Invalid color specification for background: {bg_color}")
    
    print("\nPreview:")
    print(colorize(text, fg_code, bg_code))
    
    # Show code to reproduce
    print("\nCode to reproduce:")
    if ',' in str(fg_color) or ',' in str(bg_color):
        print("# Using 24-bit true color")
        fg_part = f"\\033[{fg_code}m" if fg_code else ""
        bg_part = f"\\033[{bg_code}m" if bg_code else ""
        print(f'print("{fg_part}{bg_part}{text}\\033[0m")')
    else:
        fg_part = f"\\033[{fg_code}m" if fg_code else ""
        bg_part = f"\\033[{bg_code}m" if bg_code else ""
        print(f'print("{fg_part}{bg_part}{text}\\033[0m")')

def parse_args():
    """Parse command line arguments."""
    args = {
        'mode': 'basic',
        'fg': None,
        'bg': None,
        'text': "Hello, ANSI colors!",
    }
    
    for arg in sys.argv[1:]:
        if arg == '--help':
            print(__doc__)
            sys.exit(0)
        elif arg.startswith('--mode='):
            args['mode'] = arg[7:]
        elif arg.startswith('--fg='):
            args['fg'] = arg[5:]
        elif arg.startswith('--bg='):
            args['bg'] = arg[5:]
        elif arg.startswith('--text='):
            args['text'] = arg[7:]
    
    return args

def main():
    """Main function."""
    args = parse_args()
    
    if not ANSI_ENABLED:
        print("Warning: ANSI color codes may not be supported in this terminal.")
    
    if args['mode'] == 'basic':
        print_basic_colors()
    elif args['mode'] == 'extended':
        print_extended_colors()
    elif args['mode'] == 'truecolor':
        print_truecolor_samples()
    elif args['mode'] == 'examples':
        print_code_examples()
    elif args['mode'] == 'preview':
        preview_colors(args['fg'], args['bg'], args['text'])
    elif args['mode'].isdigit():
        # If mode is a number, show details for that color
        print_color_details(int(args['mode']))
    else:
        print(f"Unknown mode: {args['mode']}")
        print("Use --help for usage information.")
    
    # Always show usage hint at the end
    print("\nTip: Try different modes with --mode=<mode>")
    print("Available modes: basic, extended, truecolor, examples, preview")
    print("Or use a color number (0-255) to see details for that specific color")

if __name__ == '__main__':
    main()