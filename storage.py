def save_expenses(expenses):
    with open("expenses.txt", "w", encoding="utf-8") as file:
        for expense in expenses:
            line = f"{expense['category']};{expense['amount']};{expense['note']}\n"
            file.write(line)


def load_expenses():
    expenses = []
    try:
        with open("expenses.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts =  line.strip().split(";")                 
                expense = {
                    "category": parts[0],         
                    "amount": float(parts[1]),           
                    "note": parts[2]              
                }
                expenses.append(expense)
    except FileNotFoundError:
        pass                                 
    return expenses