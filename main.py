import tkinter

import customtkinter as tk
import customtkinter as tk

import ui.utils as utils
import ui.widgets as w
from ui.pages.question_page import question_page
from ui.pages.second_page import second_page
from ui.pages.welcome_page import welcome_page
from ui.pages.result_page import result_page
from ui.routing import Routes
from expert_system.engine import run



tk.set_default_color_theme("./ui/theme.json")
tk.set_appearance_mode("light")

# Render pages
welcome_page()
second_page()
question_page()
result_page()

Routes.welcome_page.tkraise()

Routes.app.mainloop()
