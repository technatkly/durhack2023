from taipy.gui import Gui, notify, navigate, Markdown
import pandas as pd

budget_md = page = """
<|toggle|theme|>

<<<<<<< HEAD
# Getting started with Taipy GUI
=======
priceList = [9.84, 20.00, 60.00, 7.24, 2.61, 8.78, 4.35, 10.00, 5.17, 9.83]
spending_df = pd.DataFrame({
    "Category": ["Expense", "Savings", "Income", "Expense", "Expense", "Expense", "Expense", "Savings", "Expense", "Expense"],
    "Item": ["food", "part time job", "Parents", "textbook", "leisure", "textbook", "transportation", "part time job", "food", "tutoring"],
    "price": [f'£{price:.2f}' for price in priceList],
    "total balance": ['-', '+', '+', '-', '-', '-', '-', '+', '-', '-'],
})
>>>>>>> 7fd5825e6338836df549270d31af0c092638f9ca

<|layout|columns=1 1|
<|
My text: <|{text}|>

Enter a word:
<|{text}|input|>
<|Analyze|button|on_action=local_callback|>
|>

<<<<<<< HEAD

<|Table|expandable|
<|{dataframe}|table|width=100%|>
|>
|>

<|layout|columns=1 1 1|
## Positive <|{np.mean(dataframe['Score Pos'])}|text|format=%.2f|raw|>

## Neutral <|{np.mean(dataframe['Score Neu'])}|text|format=%.2f|raw|>

## Negative <|{np.mean(dataframe['Score Neg'])}|text|format=%.2f|raw|>
|>

<|{dataframe}|chart|type=bar|x=Text|y[1]=Score Pos|y[2]=Score Neu|y[3]=Score Neg|y[4]=Overall|color[1]=green|color[2]=grey|color[3]=red|type[4]=line|>
"""
=======
    notify(state, "S", f"Added a new row.")
>>>>>>> 7fd5825e6338836df549270d31af0c092638f9ca
