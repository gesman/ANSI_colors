# ANSI Color Viewer

A Python utility for exploring and visualizing ANSI 256-color combinations in the terminal.

## Overview

`colors.py` is a command-line tool that helps developers visualize and experiment with ANSI color codes for terminal applications. It displays a grid of color combinations based on specified background and foreground colors, making it easy to choose the perfect color scheme for your terminal applications.

## Features

- Display combinations of background and foreground colors
- Support for 9 color families (gray, red, green, yellow, blue, magenta, cyan, white, black)
- Cross-platform compatibility (Windows, macOS, Linux)
- Example code snippets for using the displayed colors in your own Python applications
- User-friendly command-line interface

## Installation

No installation required! Simply download the `colors.py` script and run it with Python 3:

```bash
# Clone the repository or download the script
git clone https://github.com/gesman/ANSI_colors.git
# Or just download colors.py directly

# Make the script executable (Linux/macOS)
chmod +x colors.py
```

## Requirements

- Python 3.x
- No external dependencies required

## Usage

```bash
python colors.py [background_color] [foreground_color]
```

Where `background_color` and `foreground_color` are one of the following:
- gray
- red
- green
- yellow
- blue
- magenta
- cyan
- white
- black

If no arguments are provided, the script defaults to gray background and gray foreground.

### Examples

```bash
# Display combinations of red background with yellow foreground
python colors.py red yellow

# Display combinations of blue background with white foreground
python colors.py blue white

# Default display (gray on gray)
python colors.py
```

## Output Example

When you run the script, you'll see:

1. A usage banner showing available colors
2. A grid displaying various shade combinations of the selected background and foreground colors
3. An example Python code snippet showing how to use the displayed colors in your own code

The output will look similar to this (text representation):

```
──────────────────────────────────────────────────────
Usage: colors.py BG_COLOR FG_COLOR
Colors: gray, red, green, yellow, blue, magenta, cyan, white, black
Example: python colors.py red yellow
──────────────────────────────────────────────────────

🔷 Background: red    🔶 Foreground: yellow

 B= 52 F=100   B= 88 F=100   B=124 F=100   B=160 F=100   B=196 F=100  

 B= 52 F=142   B= 88 F=142   B=124 F=142   B=160 F=142   B=196 F=142  

 B= 52 F=184   B= 88 F=184   B=124 F=184   B=160 F=184   B=196 F=184  

 B= 52 F=190   B= 88 F=190   B=124 F=190   B=160 F=190   B=196 F=190  

 B= 52 F=226   B= 88 F=226   B=124 F=226   B=160 F=226   B=196 F=226  

 B= 52 F=227   B= 88 F=227   B=124 F=227   B=160 F=227   B=196 F=227  

 B= 52 F=229   B= 88 F=229   B=124 F=229   B=160 F=229   B=196 F=229  

 B= 52 F=230   B= 88 F=230   B=124 F=230   B=160 F=230   B=196 F=230  

 B= 52 F=231   B= 88 F=231   B=124 F=231   B=160 F=231   B=196 F=231  


Example Python print with ANSI codes:

    print("\033[48;5;124m\033[38;5;184m Hello ANSI World \033[0m")
Output:
    Hello ANSI World 
```

Each cell in the grid shows the specific ANSI color codes used for that combination.

## Understanding ANSI Color Codes

The script uses the ANSI 256-color mode, which allows for a wide range of colors in terminal applications. The format for these codes is:

- `\033[38;5;XXXm` - Sets the foreground (text) color
- `\033[48;5;XXXm` - Sets the background color
- `\033[0m` - Resets all formatting

Where `XXX` is a number between 0 and 255 representing a specific color.

The color ranges used in this script are:
- Gray shades: 232-255
- Red shades: 52, 88, 124, 160, 196, 203, 210, 217, 224
- Green shades: 22, 28, 34, 40, 46, 82, 118, 154, 190
- Yellow shades: 100, 142, 184, 190, 226, 227, 229, 230, 231
- Blue shades: 17, 18, 19, 20, 21, 27, 33, 39, 45, 81
- Magenta shades: 53, 89, 125, 161, 201, 207, 213, 219, 225
- Cyan shades: 23, 30, 37, 44, 51, 87, 123, 159, 195
- White: 255
- Black: 16

## Technical Details

### Windows Compatibility

The script includes special handling for Windows terminals, which traditionally have limited ANSI color support. It uses the Windows API through `ctypes` to enable ANSI escape sequence processing in the console.

### Special Cases

- Black text is displayed on a white background to make it visible
- White text is displayed on a black background for contrast
- When black is selected as a background or foreground color, only shade 16 is used

## How It Works

1. The script defines color shade ranges for each supported color
2. When executed, it parses command-line arguments to determine the requested colors
3. It generates a grid showing combinations of the selected background and foreground colors
4. For each combination, it displays the exact ANSI codes used
5. It provides an example Python code snippet using a middle shade from each selected color

## Use Cases

- Designing color schemes for terminal applications
- Learning about ANSI color codes and terminal formatting
- Testing terminal color compatibility across different platforms
- Selecting visually appealing and accessible color combinations

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests if you have suggestions for improvements or bug fixes.

## License

[Include license information here]

## Author

[Include author information here]