academy_md = """
<h1> Your Score: </h1> <p> </p>
<|{score}|>
<p> </p>
Expense: <|{expense}|> <p> </p>
Budget: <|{budget}|> <p> </p>
"""
expense = 700
budget = 600

def score():
    if expense/budget >= 0.8:
        return 100
    else:
      return 100^(1.8-expense/budget)
    
