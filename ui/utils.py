import webbrowser

import ui.globals as g
from expert_system.engine import run
from ui.advice import advice as advice_list
from ui.categories import categories


def miles_to_km(input_entry, result_label):
    miles = parse_string_to_double(input_entry.get())
    if miles is None:
        result_label.configure(text="Result: Please enter a valid number")
        return
    km = miles * 1.60934
    result_label.configure(text=f"Result: {km} km")


def parse_string_to_double(string):
    try:
        res = float(string)
        if res < 0:
            return None
        return res
    except ValueError:
        return None


def open_url(url="https://www.google.com/"):
    webbrowser.open(url, new=0, autoraise=True)


def explanation_format(expdict):
    exp = list(expdict.values())
    res = ""
    for i, level in enumerate(exp):
        res += f"{i+1}) Level {i+1}:\n"
        for item in level:
            res += f"    - {item}\n"
        if i < len(exp) - 1:
            res += "\n==>\n\n"
    return res


def result_format(result):
    try:
        return list(result.values())[0]
    except:  # noqa: E722
        return None


def solution_and_explanation():
    try:
        category_name = categories[g.category_index]["title"]
        result, explanation = run(category_name, g.answers)

        if result is None:
            return None, None, None, None

        result_formatted = result_format(result)
        if result_formatted is None:
            return None, None, None, None
        explanation_formatted = explanation_format(explanation)

        # convertin result to advice

        advice_cat = advice_list[category_name]
        # print(advice_cat.keys())
        # print(result_formatted)
        advice = advice_cat[str(result_formatted)]
        return result_formatted, advice["advice"], advice["link"], explanation_formatted
    except:  # noqa: E722
        return None, None, None, None


def shorten_text(text, max_length=50):
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text