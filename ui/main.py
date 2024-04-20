import tkinter

import customtkinter as tk
import customtkinter as tk

import utils as utils
import widgets as w
from pages.question_page import question_page
from pages.second_page import second_page
from pages.welcome_page import welcome_page
from pages.result_page import result_page
from routing import Routes


tk.set_default_color_theme("./theme.json")
tk.set_appearance_mode("light")

answers = ["Extensions(High)", "Ram(Slow)", "BrowsingExperience(Slow)", "Tabs(High)"]

result, explanation = run("HardWare", answers)

print("result:")
print(result)
print("explanation:")
print(explanation)


# Render pages
welcome_page()
second_page()
question_page()
result_page()


Routes.welcome_page.tkraise()

Routes.app.mainloop()
