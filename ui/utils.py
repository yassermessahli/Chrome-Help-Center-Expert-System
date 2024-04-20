import webbrowser


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
