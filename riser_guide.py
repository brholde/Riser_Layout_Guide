import tkinter as tk
from PIL import Image, ImageTk
import os
import sys

def resource_path(relative_path):
    """
    Get the absolute path to the resource, works for both development and frozen (PyInstaller) environments.
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Riser layouts for different dimensions
# Each key is the width, and the value is a dictionary with height as keys
# and a list of lists representing the riser layout.

# 1 = long side (8 ft) of riser riser oriented horizontally
# 2 = long side (8 ft) of riser riser oriented vertically

# LIMITS:
# Risers - 24
stage_layouts = {
    6: {
        8: [
            ["1"]
        ],
        16: [
            ["1", "1"]
        ],
        24: [
            ["1", "1", "1"]
        ],
        32: [
            ["1", "1", "1", "1"]
        ],
        40: [
            ["1", "1", "1", "1", "1"]
        ],
        48: [
            ["1", "1", "1", "1", "1", "1"]
        ],
        56: [
            ["1", "1", "1", "1", "1", "1", "1"]
        ],
        64: [
            ["1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        72: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        80: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        88: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        96: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        104: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        112: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        120: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        128: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        136: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        144: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        152: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        160: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        168: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        176: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        184: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        192: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ]
    },
    12: {
        8: [
            ["2", "2"]
        ],
        16: [
            ["1", "1"],
            ["1", "1"]
        ],
        24: [
            ["1", "1", "1"],
            ["1", "1", "1"]
        ],
        32: [
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"]
        ],
        40: [
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"]
        ],
        48: [
            ["1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1"]
        ],
        56: [
            ["1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1"]
        ],
        64: [
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        72: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        80: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        88: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
        96: [
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
        ],
    },
    18: {
        8: [
            ["2", "2", "2"]
        ],
        16: [
            ["2", "2", "2"],
            ["2", "2", "2"]
        ],
        24: [
            ["1", "1", "1"],
            ["1", "1", "1"],
            ["1", "1", "1"]
        ],
        32: [
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"]
        ],
        40: [
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"]
        ],
        48: [
            ["1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1"]
        ],
        56: [
            ["1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1"]
        ],
        64: [
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1", "1", "1"]
        ]
    },
    24: {
        8: [
            ["2", "2", "2", "2"]
        ],
        16: [
            ["2", "2", "2", "2"],
            ["2", "2", "2", "2"]
        ],
        24: [
            ["1", "1", "1"],
            ["1", "1", "1"],
            ["1", "1", "1"],
            ["1", "1", "1"]
        ],
        32: [
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"]
        ],
        40: [
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"]
        ],
        48: [
            ["1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1", "1"]
        ]
    },
    30: {
        8: [
            ["2", "2", "2", "2", "2"]
        ],
        16: [
            ["2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2"]
        ],
        24: [
            ["2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2"]
        ],
        32: [
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"],
            ["1", "1", "1", "1"]
        ],
    },
    36: {
        8: [
            ["2", "2", "2", "2", "2", "2"]
        ],
        16: [
            ["2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2"]
        ],
        24: [
            ["2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2"]
        ],
        32: [
            ["2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2"]
        ],
    },
    42: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2"]
        ],
        16: [
            ["2", "2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2", "2"]
        ],
        24: [
            ["2", "2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2", "2"]
        ],
    },
    48: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2", "2"]
        ],
        16: [
            ["2", "2", "2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2", "2", "2"]
        ],
        24: [
            ["2", "2", "2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2", "2", "2"]
        ]
    },
    54: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ],
        16: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ]
    },
    60: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ],
        16: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ]
    },
    66: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ],
        16: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ]
    },
    72: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ],
        16: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ]
    },
    78: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ]
    },
    84: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ]
    },
    90: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ]
    },
    96: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ]
    },
    102: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ]
    },
    108: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ]
    },
    114: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ]
    },
    120: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ]
    },
    126: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ]
    },
    132: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ]
    },
    138: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ]
    },
    144: {
        8: [
            ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"]
        ]
    }
}





# Helper functions ____________________________________________________________
def get_stage_layout(length, width):
    """
    Returns the stage layout for the given length and width if it exists.
    Raises a ValueError if no layout is found.
    """
    if length in stage_layouts and width in stage_layouts[length]:
        return stage_layouts[length][width]
    elif width in stage_layouts and length in stage_layouts[width]:
        return stage_layouts[width][length]
    else:
        raise ValueError(f"No layout found for dimensions {length}x{width}.")

def find_closest_layout(length, width):
    """
    Chooses the layout with the minimal sum of absolute differences in dimensions.
    Considers both (length, width) and (width, length) in stage_layouts.
    """
    closest = None
    min_diff = None
    for l in stage_layouts:
        for w in stage_layouts[l]:
            # Check (l, w)
            diff = abs(l - length) + abs(w - width)
            if min_diff is None or diff <= min_diff:
                min_diff = diff
                closest = (l, w)
            # Check (w, l) if not the same
            if l != w:
                diff_swapped = abs(w - length) + abs(l - width)
                if diff_swapped <= min_diff:
                    min_diff = diff_swapped
                    closest = (w, l)
    return closest





# GUI _______________________________________________________________
large_font = ("Helvetica", 22, "bold")
app_font = ("Helvetica", 20)

root = tk.Tk()
root.title("Ben's Riser Layout Guide")
root.geometry("800x500")
root.resizable(True, True)

icon_image = tk.PhotoImage(file=resource_path("images/logo.png"))
root.iconphoto(False, icon_image)


# Create canvas + scrollbar
canvas_frame = tk.Frame(root)
canvas_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(canvas_frame)

# Vertical scrollbar
v_scrollbar = tk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=v_scrollbar.set)

# Horizontal scrollbar
h_scrollbar = tk.Scrollbar(canvas_frame, orient="horizontal", command=canvas.xview)
canvas.configure(xscrollcommand=h_scrollbar.set)

# Pack scrollbars
v_scrollbar.pack(side="right", fill="y")
h_scrollbar.pack(side="bottom", fill="x")
canvas.pack(side="left", fill="both", expand=True)


# Scrollable content frame inside canvas
content_frame = tk.Frame(canvas)
canvas_window = canvas.create_window((0, 0), window=content_frame, anchor="n")

# Use grid with stretchable spacers
content_frame.grid_rowconfigure(0, weight=1)
content_frame.grid_columnconfigure(0, weight=1)
content_frame.grid_columnconfigure(2, weight=1)

center_frame = tk.Frame(content_frame)
center_frame.grid(row=0, column=1, pady=20)




# Make scrolling work
def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
content_frame.bind("<Configure>", on_configure)

def center_content(event):
    canvas_width = event.width
    content_width = content_frame.winfo_reqwidth()
    x = max((canvas_width - content_width) // 2, 0)
    canvas.coords(canvas_window, x, 0)
    canvas.configure(scrollregion=canvas.bbox("all"))






canvas.bind("<Configure>", center_content)


# Allow mousewheel scrolling
def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
canvas.bind_all("<MouseWheel>", on_mousewheel)  # Windows/macOS
canvas.bind_all("<Button-4>", lambda e: canvas.yview_scroll(-1, "units"))  # Linux
canvas.bind_all("<Button-5>", lambda e: canvas.yview_scroll(1, "units"))

# Shift + mousewheel for horizontal scroll
def on_shift_mousewheel(event):
    canvas.xview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<Shift-MouseWheel>", on_shift_mousewheel)


input_frame = tk.Frame(center_frame)
input_frame.pack(pady=20)

debug_frame = tk.Frame(center_frame)
debug_frame.pack(pady=10)
debug_label = tk.Label(debug_frame, text="Debug Output", font=("Helvetica", 18))
debug_label.pack()

diagram_canvas = tk.Frame(center_frame)
diagram_canvas.pack(pady=40)

for row in range(2):
    for col in range(2):
        cell = tk.Label(diagram_canvas, font=app_font)
        cell.grid(row=row, column=col, padx=5, pady=5)

diagram_frame = tk.Frame(diagram_canvas)
diagram_frame.grid(row=0, column=1, sticky="n")

horizontal_arrow = tk.Canvas(diagram_canvas)
horizontal_arrow.grid(row=1, column=1, sticky="n")

vertical_arrow = tk.Canvas(diagram_canvas)
vertical_arrow.grid(row=0, column=0, sticky="n")
vertical_arrow.create_line(50, 10, 50, 250, arrow=tk.BOTH, width=2)

image_library = {
}

# Load and resize images for stage layouts
riser_horizontal = Image.open(resource_path("images/horizontal.png"))
resized_riser_horizontal = riser_horizontal.resize((112, 84))
image_library[1] = ImageTk.PhotoImage(resized_riser_horizontal)
riser_vertical = Image.open(resource_path("images/vertical.png"))
resized_riser_vertical =  riser_vertical.resize((84, 112))
image_library[2] = ImageTk.PhotoImage(resized_riser_vertical)


#GUI Logic
def generate_diagram(xdim, ydim):
    """
    Generates a stage layout diagram based on the given dimensions.
    Also updates the vertical arrow to match height dynamically.
    """

    # Force longer dimension to be horizontal (width), shorter to be vertical (height)
    if xdim >= ydim:
        long = xdim
        short = ydim
    else:
        long = ydim
        short = xdim

    # Clear previous diagram
    for widget in diagram_frame.winfo_children():
        widget.destroy()
    vertical_arrow.delete("all")  # Clear old arrow
    horizontal_arrow.delete("all")  # Clear old arrow

    try:
        layout = get_stage_layout(long, short)
        debug_label.config(text=f"Layout for {long} x {short}:", fg="darkgreen")
    except ValueError:
        closest = find_closest_layout(long, short)
        layout = get_stage_layout(*closest)
        debug_label.config(text=f"No layout available for {long} x {short}. Closest is: {closest[0]} x {closest[1]}", fg="maroon")

    # Layout each row
    row_heights = []
    row_widths = []
    for r, row in enumerate(layout):
        row_frame = tk.Frame(diagram_frame)
        row_frame.grid(row=r, column=0, pady=2, sticky="w")
        max_height = 0
        total_row_width = 0
        for c, cell in enumerate(row):
            cell_value = int(cell)
            img = image_library.get(cell_value, None)
            if img:
                width = img.width()
                height = img.height()
                max_height = max(max_height, height)
                total_row_width += width + 4  # account for horizontal padding
            label = tk.Label(row_frame, text=cell, font=app_font, image=img, borderwidth=2)
            label.grid(row=0, column=c, padx=2, pady=2)
        row_heights.append(max_height)
        row_widths.append(total_row_width)

    total_height = sum(row_heights) + (len(row_heights) - 1) * 4  # account for vertical padding
    max_width = max(row_widths) if row_widths else 0

    # Update vertical arrow canvas height
    vertical_arrow.config(width=60, height=total_height + 20)

    # Draw vertical arrow centered
    vertical_arrow.create_line(30, 10, 30, total_height + 10, arrow=tk.BOTH, width=3)
    # Find the outermost key (length) used to get the layout
    try:
        if closest[0] in stage_layouts and closest[1] in stage_layouts[closest[0]]:
            outer_key = closest[0]
        elif closest[1] in stage_layouts and closest[0] in stage_layouts[closest[1]]:
            outer_key = closest[1]
        else:
            # If closest was used, get it from closest
            outer_key = closest[0]
    except Exception:
        outer_key = long  # fallback



    # --- Horizontal arrow under diagram ---
    # Place the horizontal arrow under the diagram, matching the diagram width
    horizontal_arrow.config(width=max_width + 20, height=60)
    # Draw horizontal arrow centered vertically in the canvas
    y_center = 30
    horizontal_arrow.create_line(10, y_center, max_width + 10, y_center, arrow=tk.BOTH, width=3)
    # Find the outermost key (width) used to get the layout
    try:
        if closest[0] in stage_layouts and closest[1] in stage_layouts[closest[0]]:
            width_key = closest[1]
        elif closest[1] in stage_layouts and closest[0] in stage_layouts[closest[1]]:
            width_key = closest[0]
        else:
            width_key = closest[1]
    except Exception:
        width_key = short  # fallback

    if width_key >= outer_key:
        horizontal_arrow.create_text((max_width + 20) // 2, y_center + 20, text=f"{width_key} ft", font=app_font)
        vertical_arrow.create_text(15, (total_height + 20) // 2, text=f"{outer_key} ft", angle=90, font=app_font)
    else:
        horizontal_arrow.create_text((max_width + 20) // 2, y_center + 20, text=f"{outer_key} ft", font=app_font)
        vertical_arrow.create_text(15, (total_height + 20) // 2, text=f"{width_key} ft", angle=90, font=app_font)

    canvas.configure(scrollregion=canvas.bbox("all"))


def on_spin_change(*args):
    try:
        length = int(length_var.get())
        width = int(width_var.get())

        generate_diagram(length, width)
    except ValueError:
        pass

length_var = tk.StringVar(value="8")
width_var = tk.StringVar(value="6")

length_var.trace_add("write", on_spin_change)
width_var.trace_add("write", on_spin_change)




# Length Label
length_label = tk.Label(input_frame, text="Length:", font=large_font)
length_label.grid(row=0, column=0, padx=5)
# Empty label for spacing
tk.Label(input_frame, text="").grid(row=0, column=1)
# Width Label
width_label = tk.Label(input_frame, text="Width:", font=large_font)
width_label.grid(row=0, column=2)

# Length Spinbox
length_spin = tk.Spinbox(input_frame, from_=1, to=300, width=10, justify='center', font=app_font, textvariable=length_var)
length_spin.grid(row=1, column=0, padx=(0, 5))
# 'x' label between spinboxes
x_label = tk.Label(input_frame, text="x", font=app_font)
x_label.grid(row=1, column=1)
# Width Spinbox
width_spin = tk.Spinbox(input_frame, from_=1, to=300, width=10, justify='center', font=app_font, textvariable=width_var)
width_spin.grid(row=1, column=2, padx=(5,0))





def __main__():
    root.mainloop()

if __name__ == "__main__":
    __main__()