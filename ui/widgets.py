import tkinter
import tkinter as tkinter

import awesometkinter as atk
import customtkinter as tk
from PIL import Image

import ui.globals as g
import ui.utils as utils
import ui.widgets as w
from ui.constants import constants
from ui.pages.question_page import question_page as question_page_function
from ui.routing import Routes


## Spacing
class GapH(tk.CTkFrame):
    def __init__(self, master, height=10, **kwargs):
        super().__init__(
            master,
            height=height,
            width=0,
            fg_color=constants.grey100,
            bg_color=constants.grey100,
            **kwargs,
        )


class GapW(tk.CTkFrame):
    def __init__(self, master, width=10, **kwargs):
        super().__init__(master, width=width, height=0, **kwargs)


## Label
class CTkLabel(tk.CTkLabel):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


## Divider
class DividerH(tk.CTkFrame):
    def __init__(self, master, height=2, **kwargs):
        super().__init__(master, height=height, bg_color="grey", **kwargs)


class DividerV(tk.CTkFrame):
    def __init__(self, master, width=2, **kwargs):
        super().__init__(master, width=width, bg_color="grey", **kwargs)


## Image
class ImageWidget(tk.CTkLabel):
    def __init__(self, master, image_path, scale=1, **kwargs):
        image_file = Image.open(image_path)
        image_size = (int(image_file.size[0] * scale), int(image_file.size[1] * scale))
        image_utility = tk.CTkImage(image_file, size=image_size)
        super().__init__(master, image=image_utility, text="", **kwargs)


## a card widget
# Design a simple card with image, title and a button.
# do it in python using customtkinter package.
# Don'te create a class, write code directly.
# keep it simple.


class Card(tk.CTkFrame):
    def __init__(
        self,
        master,
        category,
        index,
        title_color=constants.grey800,
        description_color=constants.grey600,
        **kwargs,
    ):
        image_path = category["icon"]
        bg_color = category["color"]
        title = category["title"]
        description = category["description"]

        super().__init__(
            master,
            fg_color=constants.grey50,
            border_color=bg_color,
            border_width=2,
            **kwargs,
        )

        # Image on the left
        image_label = ImageWidget(self, image_path=image_path, scale=0.5)
        image_label.pack(side="left", padx=20, pady=4)

        # Frame to hold title, description, and button
        content_frame = tk.CTkFrame(
            self,
            fg_color=constants.grey50,
        )
        content_frame.pack(
            side="left", fill="both", expand=True, padx=10, pady=6, anchor=tkinter.W
        )

        # Title, description, and button within the content frame
        title_label = tk.CTkLabel(
            content_frame,
            text=title,
            font=("Product Sans", 19),
            text_color=title_color,
        )
        title_label.pack(padx=5, expand=True, anchor=tkinter.W)

        description_label = tk.CTkLabel(
            content_frame,
            text=description,
            font=("Product Sans", 14),
            text_color=description_color,
        )
        description_label.pack(padx=5, expand=True, anchor=tkinter.W)

        def on_click():
            g.category_index = index
            Routes.go_to(Routes.question_page, run_function=question_page_function)

        button = tk.CTkButton(
            self,
            text="Get Help",
            fg_color=bg_color,
            text_color=constants.grey800,
            hover=False,
            command=on_click,
        )
        button.pack(pady=8, padx=8, anchor=tkinter.S, side="right")


## radio button
class RadioListTile(tk.CTkRadioButton):
    def __init__(
        self,
        master,
        text,
        value,
        variable,
        **kwargs,
    ):
        super().__init__(
            master,
            text=text,
            value=value,
            variable=variable,
            hover=True,
            hover_color=constants.blue600,
            border_color=constants.grey800,
            text_color=constants.grey800,
            **kwargs,
        )


## solution card
# a simple card with a title saying "Solution",
# a description, and a button saying "Next Question"
# a button to continue searching on Google.com
# this card will be used in the result page.
# it should be a class.
# the class should be named SolutionCard.
# background color should be a light green and the title color should be dark green.
# the button color should be dark green.
# the text color should be grey800.


class SolutionCard(tk.CTkFrame):
    def __init__(
        self,
        master,
        text,
        link,
        **kwargs,
    ):
        super().__init__(
            master,
            fg_color=constants.green100,
            **kwargs,
        )

        solution_icon = ImageWidget(
            self, image_path="./ui/assets/solution.png", scale=0.6
        )
        solution_icon.pack(side="left", padx=20, pady=30, anchor=tkinter.NW)

        w.GapH(self, height=20).pack()

        # Title
        title_label = tk.CTkLabel(
            self,
            text="Solution",
            font=("Product Sans", 30),
            text_color=constants.green600,
        )
        title_label.pack(pady=10, padx=20, anchor=tkinter.W, expand=True)

        # Description
        description_label = tk.CTkLabel(
            self,
            text=text,
            font=("Product Sans", 17),
            text_color=constants.grey700,
            justify="left",
            anchor="w",
            wraplength=450,
        )
        description_label.pack(fill="both", padx=20, pady=10, expand=True)

        # Google Search Button
        google_button = tk.CTkButton(
            self,
            text=utils.shorten_text(f"More info on {link}"),
            fg_color=constants.green600,
            command=lambda: utils.open_url(link),
        )
        google_button.pack(pady=10, anchor=tkinter.W, padx=20)

        w.GapH(self, height=20).pack()


class OtherSolutionCard(tk.CTkFrame):
    def __init__(
        self,
        master,
        text,
        **kwargs,
    ):
        super().__init__(
            master,
            fg_color=constants.grey300,
            **kwargs,
        )

        w.GapH(self, height=20).pack()

        # Title
        title_label = tk.CTkLabel(
            self,
            text="How we found this solution?",
            font=("Product Sans", 20),
            text_color=constants.grey600,
        )
        title_label.pack(pady=10, padx=20, anchor=tkinter.W, expand=True)

        # Description
        description_label = tk.CTkLabel(
            self,
            text=text,
            font=("Product Sans", 17),
            text_color=constants.grey700,
            justify="left",
            anchor="w",
        )
        description_label.pack(fill="both", padx=20, pady=10, expand=True)

        w.GapH(self, height=20).pack()
