"""
Driving Towards Tomorrow
Main Application
"""

from nicegui import app, ui
import os
# Import the webpage so the @ui.page("/") decorator is registered
import ui as website_ui
app.add_static_files("/static", "static")

def main() -> None:
    ui.run(
        title="Driving Towards Tomorrow",
        favicon="☀️",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        reload=False,
    )


if __name__ in {"__main__", "__mp_main__"}:
    main()
