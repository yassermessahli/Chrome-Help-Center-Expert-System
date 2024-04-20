import tkinter as tkinter

import customtkinter as tk

import widgets as w
from constants import constants
from globals import answers
from routing import Routes


def result_page():
    # before doing anything, clear the content in this page, remove all widgets
    for widget in Routes.result_page.winfo_children():
        widget.pack_forget()

    page = Routes.result_page

    w.GapH(page, height=20).pack()

    print(f"====================\nAnswers: {answers}\n====================")

    # show answers
    tk.CTkLabel(
        page,
        text="Your answers:",
        font=("Product Sans", 18),
        text_color=constants.grey700,
    ).pack()
    for answer in answers:
        tk.CTkLabel(
            page,
            text=answer,
            font=("Product Sans", 16),
            text_color=constants.grey700,
        ).pack(pady=5)

    # a button to clear the answers
    clear_button = tk.CTkButton(
        page,
        text="Clear Answers",
        fg_color=constants.red600,
        height=50,
        width=200,
        command=lambda: answers.clear(),
    )
    clear_button.pack(pady=10, padx=20)

    title2 = tk.CTkLabel(
        page,
        text="We found a solution for your problem!",
        font=("Product Sans", 18),
        text_color=constants.grey700,
    )
    title2.pack()

    w.GapH(page, height=10).pack()

    w.SolutionCard(page).pack(expand=True, fill="both", padx=20)

    w.GapH(page, height=20).pack()

    w.OtherSolutionCard(page).pack(expand=True, fill="both", padx=20)

    w.GapH(page, height=20).pack()

    # button to go back to the welcome page
    home_button = tk.CTkButton(
        page,
        text="Return to Home",
        fg_color=constants.blue600,
        height=50,
        width=200,
        command=lambda: Routes.go_to(Routes.welcome_page, run_function=answers.clear),
    )
    home_button.pack(pady=10, padx=20)

    w.GapH(page, height=60).pack()
