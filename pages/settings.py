settings_md = """
## Settings
Notification: <|{value}|toggle|lov=On;Off|> <p></p>
Volume: <|{value}|toggle|lov=On;Off|><p></p>
Location: <|{value}|toggle|lov=On;Off|><p></p>
User: <|{value}|toggle|lov=Student; Parents|unselected_value=No Value|><p></p>
Logout: <|{value}|toggle|lov=Yes;No|><p></p>
Save Data: <|{content}|file_download|don't bypass_preview|>
"""
value = "Volume"
