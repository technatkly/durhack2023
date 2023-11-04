from taipy.gui import Gui, notify, navigate
from pages.index import index_md
from pages.budget import budget_md
from pages.categories import categories_md
from pages.academy import academy_md
from pages.settings import settings_md

text = "Original text"

root_md = "<|menu|lov={[('index', 'Quick Insight'), ('budget', 'Your Budget'), ('categories', 'The Categories'), ('academy', 'Your Academy'), ('settings', 'Settings')]}|on_action=on_menu|>"

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
