categories_md = "## Your Expenses in Category"
from taipy.gui import Gui, notify, navigate, Markdown
import pandas as pd

costList = [9.84, 20.00, 60.00, 7.24, 2.61, 8.78, 4.35, 10.00, 5.17, 9.83]
spending_df = pd.DataFrame({
    "Category": ["Expense", "Savings", "Income", "Expense", "Expense", "Expense", "Expense", "Savings", "Expense",
                 "Expense"],
    "Item": ["food", "part time job", "Parents", "textbook", "leisure", "textbook", "transportation", "part time job",
             "food", "tutoring"],
    "Cost": [f'£{price:.2f}' for price in costList]
})

totalExpense = sum(costList)


def spending_df_on_add(state, var_name, payload):
    empty_row = pd.DataFrame([[None for _ in state.spending_df.columns]], columns=state.spending_df.columns)
    state.spending_df = pd.concat([empty_row, state.spending_df], axis=0, ignore_index=True)

    notify(state, "S", f"Added a new expense.")


categories_md = Markdown(f"<|{spending_df}|table|filter=True|on_add=spending_df_on_add|> Total = £<|{totalExpense}|>")
