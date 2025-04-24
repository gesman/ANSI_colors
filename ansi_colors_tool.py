#!/usr/bin/env python3
"""
ANSI Colors Tool - Wrapper Script

This script provides easy access to the ANSI color picker tools.
It allows running the tools without having to navigate to the ANSI_colors directory.

Usage:
    python ansi_colors_tool.py [tool] [options]

Tools:
    picker      - Run the command-line color picker
    menu        - Run the interactive menu interface
    demo        - Run the demonstration script
    example     - Run the example application
    help        - Show this help message

Examples:
    python ansi_colors_tool.py picker --mode=basic
    python ansi_colors_tool.py menu
    python ansi_colors_tool.py demo
    python ansi_colors_tool.py example
"""

import os
import sys
import importlib.util
import subprocess

def show_help():
    """Show the help message."""
    print(__doc__)

def run_module(module_name, args=None):
    """Run a module from the ANSI_colors package."""
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the module
    module_path = os.path.join(script_dir, f'{module_name}.py')
    
    # Check if the module exists
    if not os.path.exists(module_path):
        print(f"Error: Module '{module_name}' not found at {module_path}")
        return False
    
    # Run the module as a script
    cmd = [sys.executable, module_path]
    if args:
        cmd.extend(args)
    
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running {module_name}: {e}")
        return False

def main():
    """Main function."""
    # Parse command-line arguments
    if len(sys.argv) < 2:
        show_help()
        return
    
    tool = sys.argv[1].lower()
    args = sys.argv[2:] if len(sys.argv) > 2 else []
    
    if tool == 'picker':
        run_module('ansi_color_picker', args)
    elif tool == 'menu':
        run_module('color_picker_menu', args)
    elif tool == 'demo':
        run_module('color_picker_demo', args)
    elif tool == 'example':
        run_module('color_example', args)
    elif tool in ['help', '--help', '-h']:
        show_help()
    else:
        print(f"Unknown tool: {tool}")
        show_help()

if __name__ == '__main__':
    main()