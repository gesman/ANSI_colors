#!/usr/bin/env python3
"""
ANSI Colors Example Application

This script demonstrates how to use the ansi_colors utility module
in a real-world application scenario.

It includes examples of:
- Colored logging
- Status messages
- Progress indicators
- Data visualization
- Interactive menus
"""

import os
import sys
import time
import random
from datetime import datetime

# Import the ansi_colors utility module
try:
    # Try relative import first (when used as part of a package)
    from .ansi_colors import (
        # Basic colors
        red, green, yellow, blue, cyan, magenta, white, black,
        bright_red, bright_green, bright_yellow, bright_blue,
        bright_white, bright_cyan,
        
        # Background colors
        bg_red, bg_green, bg_blue, bg_yellow, bg_black,
        
        # Styles
        bold, underline, reverse,
        
        # Advanced coloring
        color256, bg_color256, rgb, bg_rgb,
        
        # Utility functions
        style, strip_ansi
    )
except ImportError:
    # Fall back to direct import (when run as a script)
    import os
    import sys
    # Add the parent directory to sys.path
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from ANSI_colors.ansi_colors import (
        # Basic colors
        red, green, yellow, blue, cyan, magenta, white, black,
        bright_red, bright_green, bright_yellow, bright_blue,
        bright_white, bright_cyan,
        
        # Background colors
        bg_red, bg_green, bg_blue, bg_yellow, bg_black,
        
        # Styles
        bold, underline, reverse,
        
        # Advanced coloring
        color256, bg_color256, rgb, bg_rgb,
        
        # Utility functions
        style, strip_ansi
    )

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def log_message(level, message):
    """Print a formatted log message with appropriate coloring."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if level == 'INFO':
        level_str = cyan(f'[{level}]')
    elif level == 'WARNING':
        level_str = yellow(f'[{level}]')
    elif level == 'ERROR':
        level_str = red(f'[{level}]')
    elif level == 'SUCCESS':
        level_str = green(f'[{level}]')
    elif level == 'DEBUG':
        level_str = magenta(f'[{level}]')
    else:
        level_str = f'[{level}]'
    
    print(f"{bold(timestamp)} {level_str} {message}")

def show_status_messages():
    """Demonstrate colored status messages."""
    print(bold(underline("\nColored Status Messages:")))
    
    log_message('INFO', 'System starting up')
    log_message('DEBUG', 'Loading configuration from config.json')
    log_message('WARNING', 'Disk space is running low (15% remaining)')
    log_message('ERROR', 'Failed to connect to database server')
    log_message('SUCCESS', 'User data successfully imported')
    
    # Direct styling examples
    print()
    print(bg_red(white(' CRITICAL ')), "System temperature exceeding safe limits")
    print(bg_green(black(' OK ')), "All services running normally")
    print(bg_yellow(black(' PENDING ')), "Waiting for external API response")
    print(bg_blue(white(' INFO ')), "Background task scheduled for midnight")

def show_progress_indicators():
    """Demonstrate progress indicators with colors."""
    print(bold(underline("\nProgress Indicators:")))
    
    # Simple progress bar
    total = 20
    print("\nDownloading updates:")
    for i in range(total + 1):
        progress = i / total
        bar_length = 30
        filled_length = int(bar_length * progress)
        
        # Color the progress bar based on completion percentage
        if progress < 0.3:
            bar = red('█' * filled_length) + '░' * (bar_length - filled_length)
        elif progress < 0.6:
            bar = yellow('█' * filled_length) + '░' * (bar_length - filled_length)
        else:
            bar = green('█' * filled_length) + '░' * (bar_length - filled_length)
        
        percent = bright_white(f"{int(100 * progress)}%")
        
        sys.stdout.write(f"\r[{bar}] {percent}")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")
    
    # Spinner with changing colors
    print("Processing data:")
    spinner_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    colors = [red, yellow, green, cyan, blue, magenta]
    
    for i in range(30):
        char_idx = i % len(spinner_chars)
        color_idx = i % len(colors)
        
        spinner = colors[color_idx](spinner_chars[char_idx])
        sys.stdout.write(f"\r{spinner} Processing... ")
        sys.stdout.flush()
        time.sleep(0.1)
    
    print(green("Done!"))

def show_data_visualization():
    """Demonstrate data visualization with colors."""
    print(bold(underline("\nData Visualization:")))
    
    # Bar chart
    print("\nMonthly Sales (Bar Chart):")
    data = [
        ("Jan", 120),
        ("Feb", 85),
        ("Mar", 140),
        ("Apr", 70),
        ("May", 95),
        ("Jun", 110),
    ]
    
    max_value = max(item[1] for item in data)
    scale_factor = 40 / max_value
    
    for month, value in data:
        bar_length = int(value * scale_factor)
        
        # Color based on value
        if value < 80:
            bar_color = red
        elif value < 100:
            bar_color = yellow
        else:
            bar_color = green
        
        bar = bar_color('█' * bar_length)
        print(f"{cyan(month):4} │ {bar} {value}")
    
    # Heat map
    print("\nServer Load Heat Map (Last 24 Hours):")
    hours = list(range(24))
    loads = [random.uniform(0, 100) for _ in range(24)]
    
    for i, (hour, load) in enumerate(zip(hours, loads)):
        # Color based on load
        if load < 30:
            block = bg_color256(22, '  ')  # Dark green
        elif load < 60:
            block = bg_color256(220, '  ')  # Yellow
        elif load < 80:
            block = bg_color256(208, '  ')  # Orange
        else:
            block = bg_color256(196, '  ')  # Red
        
        hour_str = f"{hour:02d}:00"
        load_str = f"{load:.1f}%"
        print(f"{hour_str} {block} {load_str}")

def show_interactive_menu():
    """Demonstrate an interactive colored menu."""
    print(bold(underline("\nInteractive Menu:")))
    
    menu_items = [
        ("View Dashboard", "Display system dashboard"),
        ("Manage Users", "Add, edit, or remove users"),
        ("System Settings", "Configure system parameters"),
        ("Run Diagnostics", "Check system health"),
        ("Exit", "Quit the application")
    ]
    
    print("\nPlease select an option:")
    
    for i, (title, description) in enumerate(menu_items, 1):
        # Highlight the menu number
        number = bright_yellow(f"{i}")
        
        # Style the title based on the option
        if i == len(menu_items):  # Exit option
            title_str = bright_red(title)
        else:
            title_str = bright_green(title)
        
        # Description in a muted color
        desc_str = cyan(f"- {description}")
        
        print(f"  {number}. {title_str} {desc_str}")
    
    # Simulate selection
    selected = 4
    print(f"\n{yellow('Selected:')} {bright_green(menu_items[selected-1][0])}")
    
    # Show a dialog box
    print("\n" + "┌" + "─" * 50 + "┐")
    print("│" + bold(bright_blue(" System Diagnostics ")).center(50) + "│")
    print("│" + " " * 50 + "│")
    print("│" + " Running diagnostics, please wait...".ljust(50) + "│")
    print("│" + " " * 50 + "│")
    print("│" + green(" ✓ CPU: Normal").ljust(50) + "│")
    print("│" + green(" ✓ Memory: Normal").ljust(50) + "│")
    print("│" + yellow(" ⚠ Disk Space: 85% used").ljust(50) + "│")
    print("│" + green(" ✓ Network: Connected").ljust(50) + "│")
    print("│" + " " * 50 + "│")
    print("│" + bright_green(" Diagnostics completed successfully! ").center(50) + "│")
    print("└" + "─" * 50 + "┘")

def main():
    """Main function to run the demo."""
    clear_screen()
    
    # Title
    title = "ANSI Colors Example Application"
    print("\n" + "=" * 60)
    print(style(title, bright_yellow, bold_=True).center(60))
    print("=" * 60)
    
    print("\nThis example demonstrates how to use the ansi_colors utility")
    print("module in various real-world application scenarios.")
    
    # Run the demonstrations
    show_status_messages()
    show_progress_indicators()
    show_data_visualization()
    show_interactive_menu()
    
    # Conclusion
    print("\n" + "=" * 60)
    print(bold(bright_cyan("Thank you for exploring the ANSI Colors examples!")))
    print("Check out the source code to see how these effects were created.")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExample terminated by user.")
        sys.exit(0)