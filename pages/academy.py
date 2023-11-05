from pages.categories import totalExpense
expense = totalExpense
budget = 150


def score():
    if expense / budget <= 0.8:
        return 100
    else:
        return 100 ** (1.8 - expense / budget)


runScore = score()

academy_md = f"""
## Your Academy

### You did very well!
### You score <|{runScore:.0f}|>

Expense: <|{expense}|> <p> </p>
Budget: <|{budget}|> <p> </p>
"""
expense = 700
budget = 600
