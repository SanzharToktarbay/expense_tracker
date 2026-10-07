from expense_tracker.utils import get_number
from expense_tracker.storage import save_expenses, load_expenses
# from rich.console import Console
# from rich.table import Table


def show_menu():
    print("\n=== Учёт расходов ===")
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Итоги по категориям")
    print("4. Статистика")
    print("0. Выход")


def add_expense(expenses):
    category = input("Категория: ").strip().lower()
    amount = get_number("Сумма: ")
    note = input("Описание: ").strip()
    expenses.append({"category": category, "amount": amount, "note": note})
    print("Расход добавлен.") 


def show_expenses(expenses):
    if not expenses:
        print("Расходов пока нет.")
        return

    print("\n=== Все расходы ===")
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['category']}: {expense['amount']:.0f} тенге — {expense['note']}")


def show_by_category(expenses):
    if not expenses:
        print("Расходов пока нет.")
        return

    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        category_totals[category] = category_totals.get(category, 0) + amount

    print("\n=== Итоги по категориям ===")
    for category, total in category_totals.items():
        print(f"{category}: {total:.0f} тенге")


def show_stats(expenses):
    if not expenses:
        print("Расходов пока нет.")
        return

    amounts = []
    for expense in expenses:
        amounts.append(expense["amount"])

    total = sum(amounts)  
    count = len(amounts)   
    biggest = max(amounts) 
    average = total / count 

    print("\n=== Статистика ===")
    print(f"Всего потрачено: {total:.0f} тенге")
    print(f"Количество расходов: {count}")              
    print(f"Самый большой расход: {biggest:.0f} тенге")   
    print(f"Средний расход: {average:.0f} тенге")


expenses = load_expenses()

while True:
    show_menu()
    choice = input("Выберите действие: ").strip()

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":                           
        show_expenses(expenses)
    elif choice == "3":
        show_by_category(expenses)
    elif choice == "4":
        show_stats(expenses)
    elif choice == "0":
        print("До свидания!")
        save_expenses(expenses)
        break
    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")