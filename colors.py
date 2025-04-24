#!/usr/bin/env python3
import sys, os

COLOR_SHADES = {
    'gray': list(range(232, 256)),
    'red': [52, 88, 124, 160, 196, 203, 210, 217, 224],
    'green': [22, 28, 34, 40, 46, 82, 118, 154, 190],
    'yellow': [100, 142, 184, 190, 226, 227, 229, 230, 231],
    'blue': [17, 18, 19, 20, 21, 27, 33, 39, 45, 81],
    'magenta': [53, 89, 125, 161, 201, 207, 213, 219, 225],
    'cyan': [23, 30, 37, 44, 51, 87, 123, 159, 195],
    'white': [255],
    'black': [16],  # treated specially in logic
}

def print_usage():
    print("──────────────────────────────────────────────────────")
    print("Usage: colors.py BG_COLOR FG_COLOR")
    
    # Print each color name in its respective color
    print("Colors: ", end="")
    color_names = list(COLOR_SHADES.keys())
    for i, color in enumerate(color_names):
        if color == 'black':
            # Use white background for black text to make it visible
            shade = 255
            print(f"\033[48;5;{shade}m\033[38;5;16m{color}\033[0m", end="")
        elif color == 'white':
            # Use black background for white text
            shade = 16
            print(f"\033[48;5;{shade}m\033[38;5;255m{color}\033[0m", end="")
        else:
            # Use middle shade of each color
            shade = COLOR_SHADES[color][len(COLOR_SHADES[color])//2]
            print(f"\033[38;5;{shade}m{color}\033[0m", end="")
            
        # Add comma separator except for the last item
        if i < len(color_names) - 1:
            print(", ", end="")
    print()
    
    print("Example: python colors.py red yellow")
    print("──────────────────────────────────────────────────────\n")

def print_color_grid(bg_color, fg_color):
    if bg_color not in COLOR_SHADES or fg_color not in COLOR_SHADES:
        print(f"\n❌ Invalid color(s): '{bg_color}', '{fg_color}'\n")
        return

    bg_fixed = bg_color == 'black'
    fg_fixed = fg_color == 'black'

    bg_shades = [16] if bg_fixed else COLOR_SHADES[bg_color][::2]  # backgrounds in steps of 2
    fg_shades = [16] if fg_fixed else COLOR_SHADES[fg_color]

    print(f"\n🔷 Background: {bg_color}    🔶 Foreground: {fg_color}\n")
    for fg in fg_shades:
        for bg in bg_shades:
            bg_code = 16 if bg_fixed else bg
            fg_code = 16 if fg_fixed else fg
            print(f"\033[48;5;{bg_code}m\033[38;5;{fg_code}m B={bg_code:3} F={fg_code:3} \033[0m", end='  ')
        print("\n")

    # Example usage print
    sample_bg = bg_shades[len(bg_shades)//2] if not bg_fixed else 16
    sample_fg = fg_shades[len(fg_shades)//2] if not fg_fixed else 16
    print("\nExample Python print with ANSI codes:\n")
    print(f'    print("\\033[48;5;{sample_bg}m\\033[38;5;{sample_fg}m Hello ANSI World \\033[0m")')
    print("Output:")
    print(f"    \033[48;5;{sample_bg}m\033[38;5;{sample_fg}m Hello ANSI World \033[0m\n")

def _enable_windows_ansi():
    if os.name == 'nt':
        try:
            import ctypes
            k32 = ctypes.windll.kernel32
            h = k32.GetStdHandle(-11)
            mode = ctypes.c_ulong()
            if k32.GetConsoleMode(h, ctypes.byref(mode)):
                k32.SetConsoleMode(h, mode.value | 0x0004)
        except Exception:
            pass

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    _enable_windows_ansi()
    clear_screen()
    print_usage()

    if len(sys.argv) != 3:
        print_color_grid('gray', 'gray')  # default
    else:
        bg = sys.argv[1].lower()
        fg = sys.argv[2].lower()
        print_color_grid(bg, fg)
