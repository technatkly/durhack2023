from taipy.gui import Gui, notify, navigate, Markdown
import pandas as pd
import numpy as np

budget_md =  """
<h1> Deciding your budget </h1>
<|{state}|slider|min=1|max=100|> <p> </p> £<|{state}|> in total 
 <p> </p>
<|{state}|input|> is set, check your balance
<p> </p>
<|submit|button|on_action=on_button_action|>
<p> </p>
Your total balance is  <|1000-{state}|>
"""

def on_button_action(state):   
    state.text = "Button Pressed"
    notify(state, 'info', f'The text is: {state.text}')

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = "According to your set budget, you have __ money left"
        return


text = "My budget"


