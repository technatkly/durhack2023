from taipy.gui import Gui, navigate
from pages.index import index_md
from pages.budget import budget_md
from pages.categories import categories_md
from pages.academy import academy_md
from pages.settings import settings_md

text = "Original text"

# icon_insight = "<|html|<img src="../Image/insight_icon.jpg" alt="Description of the image" width="300" height="200">|>"

root_md = "<|menu|lov={[('index', 'Quick Insight')), ('budget', 'Your Budget'), ('categories', 'The Categories'), ('academy', 'Your Academy'), ('settings', 'Settings')]}|on_action=on_menu|>"

pages = {
    "/": root_md,
    "index": index_md,
    "budget": budget_md,
    "categories": categories_md,
    "academy": academy_md,
    "settings": settings_md
}


def on_menu(state, action, payload):
    page = payload["args"][0]
    navigate(state, page)


Gui(pages=pages).run(run_browser=False, use_reloader=True, port=3000)
