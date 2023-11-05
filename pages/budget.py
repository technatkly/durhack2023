from taipy.gui import Gui, notify, navigate, Markdown
from pages.categories import totalExpense
import pandas as pd
import numpy as np

totalBudget = 200


def on_button_action(state):
    state.text = "Button Pressed"
    totalBudget = state
    notify(state, 'info', f'The text is: {state.text}')


text = "My budget"

budget_md = """
# Set your budget on this slider:
<|{state}|slider|min=1|max=200|>

Your budget will be set to £<|{state}|> 
<p></p>
<|submit|button|on_action=on_button_action|>

-----
Budget of this month:   £<|{state}|>
Budget left:            £<|{state}-{totalExpense}|>
"""
