import ast
import tkinter as tkinter

import customtkinter as tk

import ui.globals as g
import ui.widgets as w
from ui.categories import categories
from ui.constants import constants
from ui.pages.result_page import result_page as result_page_function
from ui.pages.welcome_page import welcome_page as welcome_page_function
from ui.routing import Routes


def question_page():
    # before doing anything, clear the content in this page, remove all widgets
    for widget in Routes.question_page.winfo_children():
        widget.pack_forget()

    category = categories[g.category_index]
    questions = category["questions"]
    category_name = category["title"]
    radio_vars = [tk.StringVar(value="Null") for _ in questions]
    current_index = 0
    total_questions = len(questions)
    page = Routes.question_page

    def next_question():
        nonlocal current_index
        radio_value = radio_vars[current_index].get()
        radio_dict = ast.literal_eval(radio_value)
        value = radio_dict["value"]
        g.answers.append(value)
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
            widget.pack(
                pady=5,
                padx=60,
                expand=True,
                fill=tkinter.X,
                anchor=tkinter.W,
            )

    all_pages_content = [
        page_content(index, questions, category_name, radio_vars, page, next_question)
        for index in range(total_questions)
    ]

    # Render the first question
    render_question(0)


def page_content(
    index: int,
    questions: list,
    category_name: str,
    radio_vars: list,
    page: tkinter.Tk,
    next_question: callable,
):
    total_questions = len(questions)

    def reset_and_go_to_welcome_page():
        g.reset()
        Routes.go_to(Routes.welcome_page, run_function=welcome_page_function)

    return [
        # spacing
        w.GapH(page, height=20),
        # category icon
        w.ImageWidget(page, image_path=categories[g.category_index]["icon"], scale=0.5),
        # title
        tk.CTkLabel(
            page,
            text=category_name,
            font=("Product Sans", 20),
            text_color=categories[g.category_index]["button_color"],
        ),
        # subtitle
        tk.CTkLabel(
            page,
            text=f"Question {index + 1}/{total_questions}",
            font=("Product Sans", 17),
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
            width=300,
            command=next_question,
        ),
        # next home button
        tk.CTkButton(
            page,
            text="Home",
            height=40,
            width=300,
            border_color=constants.grey500,
            text_color=constants.grey500,
            border_width=2,
            fg_color=constants.grey50,
            hover=False,
            command=reset_and_go_to_welcome_page,
        ),
        # spacing
        w.GapH(page, height=60),
    ]
