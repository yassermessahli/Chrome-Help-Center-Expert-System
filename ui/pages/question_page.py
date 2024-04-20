import tkinter as tkinter

import customtkinter as tk

import ui.widgets as w
from ui.categories import categories
from ui.constants import constants
from ui.globals import answers
from ui.pages.result_page import result_page as result_page_function
from ui.routing import Routes
import ast


def question_page(category_index: int = 0):
    # before doing anything, clear the content in this page, remove all widgets
    for widget in Routes.question_page.winfo_children():
        widget.pack_forget()

    category = categories[category_index]
    questions = category["questions"]
    radio_vars = [tk.StringVar(value="Null") for _ in questions]
    current_index = 0
    total_questions = len(questions)
    page = Routes.question_page

    def next_question():
        nonlocal current_index
        radio_value = radio_vars[current_index].get()
        radio_dict = ast.literal_eval(radio_value)
        value = radio_dict["value"]
        answers.append(value)
        current_index += 1
        if current_index < total_questions:
            render_question(current_index)
        else:
            Routes.go_to(Routes.result_page, run_function=result_page_function)

    def render_question(index: int):
        if index > 0:
            # forget the previous content
            for widget in all_pages_content[index - 1]:
                widget.pack_forget()

        # pack the updated content
        for widget in all_pages_content[index]:
            widget.pack(pady=5)

    all_pages_content = [
        page_content(index, questions, radio_vars, page, next_question)
        for index in range(total_questions)
    ]

    # Render the first question
    render_question(0)


def page_content(
    index: int,
    questions: list,
    radio_vars: list,
    page: tkinter.Tk,
    next_question: callable,
):
    total_questions = len(questions)
    return [
        # spacing
        w.GapH(page, height=Routes.app.winfo_screenheight() // 10),
        # title
        tk.CTkLabel(
            page,
            text=f"Question {index + 1}/{total_questions}",
            font=("Product Sans", 20),
            text_color=constants.grey700,
        ),
        # spacing
        w.GapH(page, height=10),
        # question
        tk.CTkLabel(
            page,
            text=questions[index]["question"],
            font=("Product Sans", 18),
            wraplength=600,
            text_color=constants.grey800,
        ),
        # spacing
        w.GapH(page, height=10),
        # radio buttons
        *[
            w.RadioListTile(
                page,
                text=option["text"],
                value=option,
                variable=radio_vars[index],
            )
            for option in questions[index]["options"]
        ],
        # spacing
        w.GapH(page, height=20),
        # next button
        tk.CTkButton(
            page,
            text="Next Question",
            height=40,
            command=next_question,
        ),
        # spacing
        w.GapH(page, height=60),
    ]
