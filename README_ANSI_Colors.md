# ANSI Colors Project

This project provides a comprehensive set of tools for exploring and using ANSI color codes in terminal applications.

## Project Structure

The project is organized as follows:

```
PYTHON/
├── ansi_colors_tool.py         # Wrapper script for easy access to all tools
├── ANSI_colors/                # Main package directory
│   ├── __init__.py             # Package initialization
│   ├── ansi_color_picker.py    # Main command-line tool
│   ├── color_picker_menu.py    # Interactive menu interface
│   ├── color_picker_demo.py    # Demonstration script
│   ├── ansi_colors.py          # Utility module for using colors
│   ├── color_example.py        # Real-world examples
│   └── README_color_picker.md  # Detailed documentation
```

## Quick Start

The easiest way to use the tools is through the wrapper script:

```bash
# Show help
python ansi_colors_tool.py help

# Run the command-line color picker
python ansi_colors_tool.py picker --mode=basic

# Run the interactive menu
python ansi_colors_tool.py menu

# Run the demonstration script
python ansi_colors_tool.py demo

# Run the example application
python ansi_colors_tool.py example
```

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

## Using the Utility Module in Your Projects

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

## Documentation

For detailed documentation, see the [README_color_picker.md](ANSI_colors/README_color_picker.md) file in the ANSI_colors directory.