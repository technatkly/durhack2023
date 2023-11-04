from taipy.gui import Gui, notify, navigate

text = "Original text"

root_md="<|menu|lov={[('index', 'Quick Insight'), ('budget', 'Your Budget'), ('categories', 'The Categories'), ('academy', 'Your Academy'), ('settings', 'Settings')]}|on_action=on_menu|>"

index_md = """
# Home

My text: <|{text}|>

<|{text}|input|>

<|Run local|button|on_action=on_button_action|>
"""

budget_md = "## Your Budget"
categories_md = "## The Categories"
academy_md = "## Your Academy"
settings_md = "## Settings"

pages = {
    "/": root_md,
    "index": index_md,
    "budget": budget_md,
    "categories": categories_md,
    "academy": academy_md,
    "settings": settings_md
}

def on_button_action(state):
    notify(state, 'info', f'The text is: {state.text}')
    state.text = "Button Pressed"

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return

def on_menu(state, action, payload):
    page = payload["args"][0]
    navigate(state, page)

Gui(pages=pages).run(run_browser=False, use_reloader=True, port=3000)

