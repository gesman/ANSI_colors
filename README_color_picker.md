# ANSI Color Picker Tool

A comprehensive tool for exploring and using ANSI color codes in terminal applications.

## Features

- **Visual Color Display**: See all available foreground and background color combinations
- **Complete Color Information**: View ANSI escape sequences, RGB values, and hex codes for each color
- **Organized Color Categories**: Browse colors by category (basic, bright, grayscale, RGB cube)
- **Multiple Display Modes**: Toggle between different visualization options
- **Code Examples**: Learn how to implement colors using Python libraries (colorama, rich, direct ANSI)
- **Text Preview**: Visualize custom text with chosen color combinations
- **Interactive Interface**: User-friendly menu system for easy navigation
- **Utility Module**: Lightweight module for easily adding colors to your Python applications
- **Example Application**: Real-world examples of using colors in terminal applications

## Color Categories

The tool organizes colors into the following categories:

1. **Basic Colors (0-7)**: The standard 8 colors available in most terminals
2. **Bright Colors (8-15)**: Brighter versions of the basic 8 colors
3. **RGB Cube Colors (16-231)**: A 6×6×6 cube of colors representing RGB combinations
4. **Grayscale Colors (232-255)**: 24 shades of gray from near-black to near-white

## Components

The ANSI Color Picker Tool consists of the following components:

1. **ansi_color_picker.py** - The main command-line tool for exploring colors
2. **color_picker_menu.py** - An interactive menu-based interface
3. **color_picker_demo.py** - A demonstration of key features with visual examples
4. **ansi_colors.py** - A lightweight utility module for using colors in your applications
5. **color_example.py** - Real-world examples of using colors in terminal applications

## Installation

All the ANSI color picker tools are located in the `PYTHON/ANSI_colors` directory. A wrapper script `ansi_colors_tool.py` is provided in the `PYTHON` directory for easy access to all the tools.

## Usage

### Wrapper Script

The easiest way to use the tools is through the wrapper script:

```bash
python ansi_colors_tool.py [tool] [options]
```

Available tools:
- `picker` - Run the command-line color picker
- `menu` - Run the interactive menu interface
- `demo` - Run the demonstration script
- `example` - Run the example application
- `help` - Show help message

Examples:

```bash
# Show basic 16 colors
python ansi_colors_tool.py picker --mode=basic

# Run the interactive menu
python ansi_colors_tool.py menu

# Run the demo
python ansi_colors_tool.py demo

# Run the example application
python ansi_colors_tool.py example
```

### Direct Usage

You can also run the tools directly from the ANSI_colors directory:

```bash
# Command-line color picker
python ANSI_colors/ansi_color_picker.py [options]

# Interactive menu
python ANSI_colors/color_picker_menu.py

# Demo script
python ANSI_colors/color_picker_demo.py

# Example application
python ANSI_colors/color_example.py
```

### Color Picker Options

When using the color picker (either through the wrapper or directly), the following options are available:

- `--mode=<mode>`: Display mode (basic, extended, truecolor, examples, preview)
- `--fg=<color>`: Set foreground color for preview (0-255 or r,g,b)
- `--bg=<color>`: Set background color for preview (0-255 or r,g,b)
- `--text=<text>`: Custom text for preview
- `--help`: Show help message

Examples:

```bash
# Show basic 16 colors
python ansi_colors_tool.py picker --mode=basic

# Show extended 256-color palette
python ansi_colors_tool.py picker --mode=extended

# Preview text with specific colors
python ansi_colors_tool.py picker --mode=preview --fg=196 --bg=46 --text="Custom colored text"

# Preview with RGB colors
python ansi_colors_tool.py picker --mode=preview --fg=255,128,0 --bg=0,0,128 --text="RGB colors"

# Show details for a specific color
python ansi_colors_tool.py picker --mode=196
```

### Interactive Menu Interface

For a more user-friendly experience, use the menu-based interface:

```bash
python ansi_colors_tool.py menu
```

This provides an interactive menu system to explore all features of the color picker.

### Demo Script

To see a guided tour of the tool's capabilities:

```bash
python ansi_colors_tool.py demo
```

### Using the Utility Module

The `ansi_colors.py` module provides a simple way to add colors to your Python applications:

```python
# If using the module directly from the ANSI_colors directory
from PYTHON.ANSI_colors.ansi_colors import red, green, blue, bold, underline

# Or if you've installed the package
from ANSI_colors import red, green, blue, bold, underline

# Basic usage
print(red("This text is red"))
print(green("This text is green"))

# Combining styles
print(bold(blue("This text is bold and blue")))
print(underline(red("This text is underlined and red")))

# Using RGB colors
# If using the module directly from the ANSI_colors directory
from PYTHON.ANSI_colors.ansi_colors import rgb, bg_rgb
# Or if you've installed the package
from ANSI_colors import rgb, bg_rgb

print(rgb(255, 128, 0, "This text is orange"))
print(bg_rgb(0, 0, 128, "This text has a dark blue background"))
```

### Example Application

For real-world examples of using colors in terminal applications:

```bash
python ansi_colors_tool.py example
```

This demonstrates:
- Colored logging
- Status messages
- Progress indicators
- Data visualization
- Interactive menus

## ANSI Color Codes Reference

### Basic Format

ANSI escape sequences follow this format:
```
\033[<code>m
```

Where `<code>` is one or more numeric codes separated by semicolons.

### Common Codes

- **Text Formatting**:
  - `0`: Reset all formatting
  - `1`: Bold
  - `2`: Dim
  - `3`: Italic
  - `4`: Underline
  - `7`: Reverse (swap foreground/background)

- **Basic Foreground Colors** (30-37):
  - `30`: Black
  - `31`: Red
  - `32`: Green
  - `33`: Yellow
  - `34`: Blue
  - `35`: Magenta
  - `36`: Cyan
  - `37`: White

- **Basic Background Colors** (40-47):
  - `40`: Black
  - `41`: Red
  - `42`: Green
  - `43`: Yellow
  - `44`: Blue
  - `45`: Magenta
  - `46`: Cyan
  - `47`: White

- **Bright Foreground Colors** (90-97):
  - `90`: Bright Black (Gray)
  - `91`: Bright Red
  - `92`: Bright Green
  - `93`: Bright Yellow
  - `94`: Bright Blue
  - `95`: Bright Magenta
  - `96`: Bright Cyan
  - `97`: Bright White

- **Bright Background Colors** (100-107):
  - `100`: Bright Black (Gray)
  - `101`: Bright Red
  - `102`: Bright Green
  - `103`: Bright Yellow
  - `104`: Bright Blue
  - `105`: Bright Magenta
  - `106`: Bright Cyan
  - `107`: Bright White

### 256-Color Mode

For 256-color mode, use:
- Foreground: `38;5;<n>` where n is 0-255
- Background: `48;5;<n>` where n is 0-255

Example: `\033[38;5;208m` for orange text (color 208)

### True Color (24-bit RGB)

For true color (24-bit RGB), use:
- Foreground: `38;2;<r>;<g>;<b>` where r,g,b are 0-255
- Background: `48;2;<r>;<g>;<b>` where r,g,b are 0-255

Example: `\033[38;2;255;128;0m` for RGB orange text

## Python Code Examples

### Direct ANSI Sequences

```python
# Basic usage
print("\033[31mRed text\033[0m")
print("\033[1;32mBold green text\033[0m")
print("\033[3;33mItalic yellow text\033[0m")
print("\033[4;34mUnderlined blue text\033[0m")
print("\033[45mMagenta background\033[0m")
print("\033[1;36;44mBold cyan text on blue background\033[0m")

# 256-color mode
print("\033[38;5;208mOrange text (color 208)\033[0m")
print("\033[48;5;27mBackground color 27\033[0m")

# True color (24-bit)
print("\033[38;2;255;128;0mRGB orange text\033[0m")
print("\033[48;2;0;128;255mRGB blue background\033[0m")
```

### Using Colorama

```python
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
```

### Using Rich

```python
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
```

## Terminal Compatibility

- **Windows**: ANSI colors are supported in modern Windows terminals (Windows 10+) with the Windows Terminal, PowerShell, or Command Prompt. The tool automatically enables ANSI support on Windows.
- **macOS/Linux**: Most terminals on macOS and Linux have excellent ANSI color support.
- **True Color Support**: Not all terminals support 24-bit true color. If colors appear incorrect, your terminal might be limited to 256 colors or less.

## Tips for Using Colors Effectively

1. **Maintain Readability**: Ensure text remains readable by choosing appropriate color combinations
2. **Use Sparingly**: Too many colors can be distracting; use them to highlight important information
3. **Consider Accessibility**: Some color combinations may be difficult for colorblind users to distinguish
4. **Test in Different Terminals**: Colors may appear differently across various terminal emulators
5. **Provide Fallbacks**: When using advanced color features, consider providing fallbacks for terminals with limited support

## Troubleshooting

- **Colors Not Displaying**: Some terminals may not support ANSI colors or may have them disabled
- **Incorrect Colors**: Your terminal might not support the color mode you're using (try 256-color mode instead of true color)
- **Garbled Output**: If you see escape sequences as text, your terminal doesn't support ANSI codes
- **Windows Issues**: On older Windows versions, you may need to use colorama or another library for proper color support

## Using Colors in Your Projects

The `ansi_colors.py` utility module is designed to be easily integrated into your own Python projects:

### Method 1: Copy the module

1. Copy the `PYTHON/ANSI_colors/ansi_colors.py` file to your project directory
2. Import the functions you need:
   ```python
   from ansi_colors import red, green, bold, underline
   ```
3. Use the functions to add color to your terminal output:
   ```python
   print(red("Error: File not found"))
   print(green("Success: Operation completed"))
   ```

### Method 2: Use the package

1. Add the ANSI_colors directory to your Python path
2. Import the functions from the package:
   ```python
   from PYTHON.ANSI_colors import red, green, bold, underline
   ```
3. Use the functions to add color to your terminal output:
   ```python
   print(red("Error: File not found"))
   print(green("Success: Operation completed"))
   ```

The module provides:
- Basic color functions (red, green, blue, etc.)
- Background color functions (bg_red, bg_green, etc.)
- Text style functions (bold, underline, italic, etc.)
- 256-color mode functions (color256, bg_color256)
- True color RGB functions (rgb, bg_rgb)
- Utility functions for combining styles and checking terminal support

See `color_example.py` for comprehensive examples of how to use these functions in real-world applications.