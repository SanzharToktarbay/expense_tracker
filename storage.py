import json


def save_expenses(expenses):
    with open("expenses.json", "w", encoding="utf-8") as file:
        json.dump(expenses, file, ensure_ascii=False, indent=2)


def load_expenses():
    try:
        with open("expenses.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []