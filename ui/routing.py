import customtkinter as tk

from ui.constants import constants


class Routes:
    app = tk.CTk()

    width = 800
    height = app.winfo_screenheight() - 200
    x = int((app.winfo_screenwidth() / 2) - (width / 2))
    y = int((app.winfo_screenheight() / 2) - (height / 2))
    app.geometry(f"{width}x{height}+{x}+{y}")

    app.title("Google Chrome Technical Support")
    # app.iconbitmap(constants.fav_icon)

    # Configure the root window's grid (weights for full size)
    app.grid_columnconfigure(0, weight=1)  # Weight for column 0
    app.grid_rowconfigure(0, weight=1)  # Weight for row 0

    welcome_page = tk.CTkScrollableFrame(
        app,
        fg_color=constants.grey100,
        height=height,
    )
    second_page = tk.CTkScrollableFrame(
        app,
        fg_color=constants.grey100,
        height=height,
    )
    question_page = tk.CTkScrollableFrame(
        app,
        fg_color=constants.grey100,
        height=height,
    )
    result_page = tk.CTkScrollableFrame(
        app,
        fg_color=constants.grey100,
        height=height,
    )

    def go_to(page: tk.CTkScrollableFrame, run_function: callable = None):
        for route in Routes.routes:
            route.grid_forget()
        
        if run_function:
            run_function()
        page.grid(row=0, column=0, sticky="nsew")
        page.tkraise()

    welcome_page.grid(row=0, column=0, sticky="nsew")

    routes = [
        welcome_page,
        second_page,
        question_page,
        result_page,
    ]
