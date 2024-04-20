import tkinter as tkinter

import customtkinter as tk

import ui.globals as g
import ui.widgets as w
from ui.constants import constants
from ui.routing import Routes
from ui.utils import solution_and_explanation


def result_page():
    # before doing anything, clear the content in this page, remove all widgets
    for widget in Routes.result_page.winfo_children():
        widget.pack_forget()

    page = Routes.result_page

    w.GapH(page, height=20).pack()

    result, solution, link, explanation = solution_and_explanation()

    if solution is None:
        render_no_solution()
    else:
        render_solution(result, solution, link, explanation)

    w.GapH(page, height=20).pack()

    # button to go back to the welcome page
    home_button = tk.CTkButton(
        page,
        text="Return to Home",
        fg_color=constants.blue600,
        height=50,
        width=300,
        command=lambda: Routes.go_to(Routes.welcome_page, run_function=g.reset),
    )
    home_button.pack(pady=10, padx=20)

    w.GapH(page, height=60).pack()


def render_solution(result, solution, link, explanation):
    page = Routes.result_page

    title = tk.CTkLabel(
        page,
        text="We found a solution for your problem!",
        font=("Product Sans", 18),
        text_color=constants.grey700,
        anchor=tkinter.W,
    )
    title.pack(anchor=tkinter.W, padx=20)

    subtitle = tk.CTkLabel(
        page,
        text=f"Problem Code: {result}",
        font=("Product Sans", 16),
        text_color=constants.blue600,
        anchor=tkinter.W,
    )
    subtitle.pack(anchor=tkinter.W, padx=20)

    w.GapH(page, height=10).pack()

    w.SolutionCard(
        page,
        text=solution,
        link=link,
    ).pack(expand=True, fill="both", padx=20)

    w.GapH(page, height=20).pack()

    w.OtherSolutionCard(
        page,
        text=explanation,
    ).pack(expand=True, fill="both", padx=20)


def render_no_solution():
    page = Routes.result_page
    w.GapH(page, height=Routes.app.winfo_screenheight() // 6).pack()
    tk.CTkLabel(
        page,
        text="We couldn't find a solution for your problem.\nPlease contact Google Chrome Technical Support.",
        font=("Product Sans", 18),
        text_color=constants.grey700,
    ).pack()
