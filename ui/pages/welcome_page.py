import tkinter as tkinter

import customtkinter as tk

import widgets as w
from constants import constants
from routing import Routes


def welcome_page():
    page = Routes.welcome_page

    w.GapH(page, height=40).pack()
    w.ImageWidget(page, image_path=constants.chrome_logo, scale=0.6).pack()
    w.GapH(page, height=20).pack()

    title1 = tk.CTkLabel(
        page,
        text="Google Chrome Technical\nSupport Expert System",
        font=("Product Sans", 28),
        text_color=constants.grey800,
    )
    title1.pack()

    w.GapH(page, height=20).pack()

    title2 = tk.CTkLabel(
        page,
        text="How can we help you?",
        font=("Product Sans", 20),
        text_color=constants.grey700,
    )
    title2.pack()

    w.GapH(page, height=20).pack()

    page.grid_columnconfigure(0, weight=1)  # Weight for column 0
    page.grid_columnconfigure(1, weight=1)  # Weight for column 1 (adjust if needed)

    for category in constants.categories:
        w.Card(
            page,
            category,
        ).pack(padx=20, pady=6, expand=True, fill=tkinter.X)

    w.GapH(page, height=40).pack()
