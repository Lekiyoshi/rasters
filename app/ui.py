import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from ttkwidgets import TickScale


class MainUI(ttk.Frame):  # TODO: Subdivide into smaller components? This class is getting bloated...
    def __init__(self, parent):
        super().__init__(parent, padding=8)
        self.pack(fill=tk.BOTH, expand=True)

        # Styles
        self.style = ttk.Style()
        self.style.theme_use("default")

        #
        #
        # Tabs (for each primitive type to raster)
        self.tabs = ttk.Notebook(self)
        self.tabs.pack(expand=True)

        self.fr_tab_line = ttk.Frame(self.tabs)
        self.fr_tab_line.pack(fill=tk.BOTH, expand=True)
        self.fr_tab_circle = ttk.Frame(self.tabs)
        self.fr_tab_circle.pack(fill=tk.BOTH, expand=True)
        self.fr_tab_bezier = ttk.Frame(self.tabs)
        self.fr_tab_bezier.pack(fill=tk.BOTH, expand=True)

        self.tabs.add(self.fr_tab_line, text="Line")
        self.tabs.add(self.fr_tab_circle, text="Circle")
        self.tabs.add(self.fr_tab_bezier, text="Bezier Curve")

        #
        # Slider widgets toolbar ('Line' tab)
        self.fr_line_toolbar = ttk.Frame(self.fr_tab_line)
        self.fr_line_toolbar.grid(row=0, column=0, padx=4, pady=(4, 8), sticky=tk.NSEW)

        # Sliders for P1 coordinates
        self.fr_p1_sliders = ttk.LabelFrame(self.fr_line_toolbar, padding=4, text="P1")
        self.fr_p1_sliders.grid(row=0, column=0, padx=(0, 8), sticky=tk.W)

        # P1.x slider
        self.fr_p1x = ttk.Frame(self.fr_p1_sliders)
        self.fr_p1x.grid(row=0, column=0, sticky=tk.NSEW)

        self.p1x_label = ttk.Label(self.fr_p1x, text="X:")
        self.p1x_label.grid(row=0, column=0, padx=(0, 2))
        self.p1x_var = tk.IntVar(self.fr_p1x)
        self.p1x_scale = TickScale(
            self.fr_p1x,
            orient=tk.HORIZONTAL,
            length=80,
            from_=0,
            to=39,
            resolution=1,
            variable=self.p1x_var,
            showvalue=True
        )
        self.p1x_scale.set(0)
        self.p1x_scale.grid(row=0, column=1)

        # Separator
        self.sep = ttk.Separator(self.fr_p1_sliders, orient=tk.VERTICAL)
        self.sep.grid(row=0, column=1, padx=4, sticky=tk.NS)

        # P1.y slider
        self.fr_p1y = ttk.Frame(self.fr_p1_sliders)
        self.fr_p1y.grid(row=0, column=2, sticky=tk.NSEW)

        self.p1y_label = ttk.Label(self.fr_p1y, text="Y:")
        self.p1y_label.grid(row=0, column=0, padx=(0, 2))

        self.p1y_var = tk.IntVar(self.fr_p1y)
        self.p1y_scale = TickScale(
            self.fr_p1y,
            orient=tk.HORIZONTAL,
            length=80,
            from_=0,
            to=39,
            resolution=1,
            variable=self.p1y_var,
            showvalue=True
        )
        self.p1y_scale.set(0)
        self.p1y_scale.grid(row=0, column=1)

        # Sliders for P2 coordinates
        self.fr_p2_sliders = ttk.LabelFrame(self.fr_line_toolbar, padding=4, text="P2")
        self.fr_p2_sliders.grid(row=0, column=1, padx=(0, 0), sticky=tk.W)

        # P2.x slider
        self.fr_p2x = ttk.Frame(self.fr_p2_sliders)
        self.fr_p2x.grid(row=0, column=0, sticky=tk.NSEW)

        self.p2x_label = ttk.Label(self.fr_p2x, text="X:")
        self.p2x_label.grid(row=0, column=0, padx=(0, 2))

        self.p2x_var = tk.IntVar(self.fr_p2x)
        self.p2x_scale = TickScale(
            self.fr_p2x,
            orient=tk.HORIZONTAL,
            length=80,
            from_=0,
            to=39,
            resolution=1,
            variable=self.p2x_var,
            showvalue=True
        )
        self.p2x_scale.set(39)
        self.p2x_scale.grid(row=0, column=1)

        # Separator
        self.sep = ttk.Separator(self.fr_p2_sliders, orient=tk.VERTICAL)
        self.sep.grid(row=0, column=1, padx=4, sticky=tk.NS)

        # P2.y slider
        self.fr_p2y = ttk.Frame(self.fr_p2_sliders)
        self.fr_p2y.grid(row=0, column=2, sticky=tk.NSEW)

        self.p2y_label = ttk.Label(self.fr_p2y, text="Y:")
        self.p2y_label.grid(row=0, column=0, padx=(0, 2))

        self.p2y_var = tk.IntVar(self.fr_p2y)
        self.p2y_scale = TickScale(
            self.fr_p2y,
            orient=tk.HORIZONTAL,
            length=80,
            from_=0,
            to=39,
            resolution=1,
            variable=self.p2y_var,
            showvalue=True
        )
        self.p2y_scale.set(39)
        self.p2y_scale.grid(row=0, column=1)

        #
        # Raster options dropdown menu ('Line' tab)
        self.fr_line_options = ttk.Frame(self.fr_tab_line)
        self.fr_line_options.grid(row=1, column=0, padx=4, pady=(0, 8), sticky=tk.NSEW)

        self.line_options_label = ttk.Label(self.fr_line_options, text="Raster options:")
        self.line_options_label.grid(row=0, column=0, padx=(0, 4), sticky=tk.W)
        self.line_options_var = tk.StringVar(self)
        self.line_options_list = ["Analítico", "DDA", "Bresenham", "Analítico + DDA"]
        self.line_options_menu = ttk.OptionMenu(
            self.fr_line_options,
            self.line_options_var,
            self.line_options_list[0],
            *self.line_options_list
        )
        self.line_options_menu.grid(row=0, column=1, sticky=tk.W)

        #
        # Slider widgets toolbar ('Circle' tab)
        self.fr_circle_toolbar = ttk.Frame(self.fr_tab_circle)
        self.fr_circle_toolbar.grid(row=0, column=0, padx=4, pady=(4, 8), sticky=tk.NSEW)

        # Sliders for cincunference parameters
        self.fr_circle_sliders = ttk.LabelFrame(self.fr_circle_toolbar, padding=4, text="Parameters")
        self.fr_circle_sliders.grid(row=0, column=0, padx=(0, 8), sticky=tk.W)

        # X_c slider
        self.fr_xc = ttk.Frame(self.fr_circle_sliders)
        self.fr_xc.grid(row=0, column=0, sticky=tk.NSEW)

        self.xc_label = ttk.Label(self.fr_xc, text="Xc:")
        self.xc_label.grid(row=0, column=0, padx=(0, 2))
        self.xc_var = tk.IntVar(self.fr_xc)
        self.xc_scale = TickScale(
            self.fr_xc,
            orient=tk.HORIZONTAL,
            length=80,
            from_=0,
            to=39,
            resolution=1,
            variable=self.xc_var,
            showvalue=True
        )
        self.xc_scale.set(19)
        self.xc_scale.grid(row=0, column=1)

        # Separator
        self.sep = ttk.Separator(self.fr_circle_sliders, orient=tk.VERTICAL)
        self.sep.grid(row=0, column=1, padx=4, sticky=tk.NS)

        # Y_c slider
        self.fr_yc = ttk.Frame(self.fr_circle_sliders)
        self.fr_yc.grid(row=0, column=2, sticky=tk.NSEW)

        self.yc_label = ttk.Label(self.fr_yc, text="Yc:")
        self.yc_label.grid(row=0, column=0, padx=(0, 2))
        self.yc_var = tk.IntVar(self.fr_yc)
        self.yc_scale = TickScale(
            self.fr_yc,
            orient=tk.HORIZONTAL,
            length=80,
            from_=0,
            to=39,
            resolution=1,
            variable=self.yc_var,
            showvalue=True
        )
        self.yc_scale.set(19)
        self.yc_scale.grid(row=0, column=1)

        # Separator
        self.sep = ttk.Separator(self.fr_circle_sliders, orient=tk.VERTICAL)
        self.sep.grid(row=0, column=3, padx=4, sticky=tk.NS)

        # Radius slider
        self.fr_radius = ttk.Frame(self.fr_circle_sliders)
        self.fr_radius.grid(row=0, column=4, sticky=tk.NSEW)

        self.radius_label = ttk.Label(self.fr_radius, text="Radius:")
        self.radius_label.grid(row=0, column=0, padx=(0, 2))

        self.radius_var = tk.IntVar(self.fr_radius)
        self.radius_scale = TickScale(
            self.fr_radius,
            orient=tk.HORIZONTAL,
            length=80,
            from_=0,
            to=39,
            resolution=1,
            variable=self.radius_var,
            showvalue=True
        )
        self.radius_scale.set(19)
        self.radius_scale.grid(row=0, column=1)

        #
        # Raster options dropdown menu ('Circle' tab)
        self.fr_circle_options = ttk.Frame(self.fr_tab_circle)
        self.fr_circle_options.grid(row=1, column=0, padx=4, pady=(0, 8), sticky=tk.NSEW)

        self.circle_options_label = ttk.Label(self.fr_circle_options, text="Raster options:")
        self.circle_options_label.grid(row=0, column=0, padx=(0, 4), sticky=tk.W)
        self.circle_options_var = tk.StringVar(self)
        self.circle_options_list = ["Paramétrico", "Simétrico", "Paramétrico + Simétrico"]
        self.circle_options_menu = ttk.OptionMenu(
            self.fr_circle_options,
            self.circle_options_var,
            self.circle_options_list[0],
            *self.circle_options_list
        )
        self.circle_options_menu.grid(row=0, column=1, sticky=tk.W)

        #
        # Display canvas
        self.fr_img_view = ttk.Frame(self.fr_tab_line, borderwidth=1, relief=tk.SUNKEN)
        self.fr_img_view.grid(row=2, column=0, padx=4, pady=(0, 4), sticky=tk.NSEW)

        self.canvas = tk.Canvas(self.fr_img_view, borderwidth=-2)
        self.canvas.config(width=320, height=320)
        self.canvas.pack()

        self.photoimage = None

    def update_canvas(self, image: Image):
        self.canvas.delete("all")
        self.photoimage = ImageTk.PhotoImage(image)  # Reference needed to prevent gargabe collection
        self.canvas.create_image(0, 0, image=self.photoimage, anchor=tk.NW)
