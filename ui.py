"""
Driving Towards Tomorrow
Main User Interface
"""

from nicegui import ui

from config import *
from content import *


# ==========================================================
# PAGE
# ==========================================================

@ui.page("/")
def create_homepage():

    load_assets()

    create_navbar()

    create_hero()

    create_about()

    create_timeline()

    create_working()

    create_benefits()

    create_prototype()

    create_comparison()

    create_future()

    create_team()

    create_footer()


# ==========================================================
# LOAD STATIC FILES
# ==========================================================

def load_assets():

    ui.add_head_html("""
<link rel="stylesheet" href="/static/style.css">
""")

    ui.add_body_html("""
<script src="/static/script.js"></script>
""")


# ==========================================================
# NAVIGATION BAR
# ==========================================================

def create_navbar():

    with ui.header().classes("navbar"):

        with ui.row().classes(
            "navbar-container"
        ):

            ui.label(
                APP_TITLE
            ).classes(
                "logo"
            )

            with ui.row().classes(
                "nav-links"
            ):

                ui.link(
                    "Home",
                    "#hero"
                )

                ui.link(
                    "About",
                    "#about"
                )

                ui.link(
                    "Timeline",
                    "#timeline"
                )

                ui.link(
                    "Benefits",
                    "#benefits"
                )

                ui.link(
                    "Future",
                    "#future"
                )

                ui.link(
                    "Team",
                    "#team"
                )


# ==========================================================
# HERO
# ==========================================================

def create_hero():

    with ui.column().classes(
        "hero"
    ):

        ui.element("div").classes(
            "sun"
        )

        ui.label(

            HERO["title"]

        ).classes(

            "hero-title"

        )

        ui.label(

            HERO["subtitle"]

        ).classes(

            "hero-subtitle"

        )

        ui.label(

            APP_DESCRIPTION

        ).classes(

            "hero-description"

        )

        ui.button(

            HERO["button"],

            on_click=lambda:

            ui.run_javascript("""

document.getElementById(
'about'
).scrollIntoView(
{
behavior:'smooth'
}
);

""")

        ).classes(

            "hero-button"

        )

        ui.image(

            "/static/images/solar_car.svg"

        ).classes(

            "solar-car"

        )


# ==========================================================
# ABOUT
# ==========================================================

def create_about():

    with ui.column().classes(
        "section"
    ):

        ui.html(

            '<div id="about"></div>'

        )

        ui.label(

            ABOUT["title"]

        ).classes(

            "section-title"

        )

        with ui.card().classes(

            "glass-card"

        ):

            ui.label(

                ABOUT["text"]

            ).classes(

                "section-text"

            )
            # ==========================================================
# TIMELINE
# ==========================================================

def create_timeline():

    with ui.column().classes("section"):

        ui.html('<div id="timeline"></div>')

        ui.label(
            "Evolution of Solar Cars"
        ).classes(
            "section-title"
        )

        ui.label(
            "A quick look at some important milestones."
        ).classes(
            "section-subtitle"
        )

        with ui.column().classes("timeline"):

            for event in TIMELINE:

                with ui.card().classes(
                    "glass-card timeline-card"
                ):

                    ui.label(
                        event["year"]
                    ).classes(
                        "timeline-year"
                    )

                    ui.label(
                        event["title"]
                    ).classes(
                        "timeline-title"
                    )

                    ui.label(
                        event["description"]
                    ).classes(
                        "timeline-description"
                    )


# ==========================================================
# HOW IT WORKS
# ==========================================================

def create_working():

    with ui.column().classes("section"):

        ui.label(
            "How Solar Powered Cars Work"
        ).classes(
            "section-title"
        )

        ui.label(
            "Energy flows from the sun to the wheels."
        ).classes(
            "section-subtitle"
        )

        with ui.row().classes(
            "working-flow"
        ):

            steps = [

                ("☀️", "Sun"),

                ("🔆", "Solar Panels"),

                ("🔋", "Battery"),

                ("⚡", "Motor"),

                ("🚗", "Car")

            ]

            for icon, text in steps:

                with ui.card().classes(
                    "glass-card flow-card"
                ):

                    ui.label(
                        icon
                    ).classes(
                        "flow-icon"
                    )

                    ui.label(
                        text
                    ).classes(
                        "flow-title"
                    )


# ==========================================================
# BENEFITS
# ==========================================================

def create_benefits():

    with ui.column().classes("section"):

        ui.html('<div id="benefits"></div>')

        ui.label(
            "Benefits"
        ).classes(
            "section-title"
        )

        ui.label(
            "Why solar powered vehicles are important."
        ).classes(
            "section-subtitle"
        )

        with ui.row().classes(
            "benefits-grid"
        ):

            for benefit in BENEFITS:

                with ui.card().classes(
                    "glass-card benefit-card"
                ):

                    ui.label(
                        benefit["icon"]
                    ).classes(
                        "benefit-icon"
                    )

                    ui.label(
                        benefit["title"]
                    ).classes(
                        "benefit-title"
                    )

                    ui.label(
                        benefit["description"]
                    ).classes(
                        "benefit-description"
                    )
                    # ==========================================================
# PROTOTYPE
# ==========================================================

def create_prototype():

    with ui.column().classes("section"):

        ui.label(
            "Project Prototype"
        ).classes(
            "section-title"
        )

        ui.label(
            "A simple working model demonstrating how a solar powered car operates."
        ).classes(
            "section-subtitle"
        )

        with ui.row().classes(
            "prototype-container"
        ):

            ui.image(
                "/static/images/solar_car.svg"
            ).classes(
                "prototype-image"
            )

            with ui.column().classes(
                "prototype-info"
            ):

                ui.label(
                    "Prototype Features"
                ).classes(
                    "card-title"
                )

                features = [

                    "Solar Panel",

                    "Rechargeable Battery",

                    "DC Motor",

                    "Lightweight Chassis",

                    "Eco-Friendly Design"

                ]

                for feature in features:

                    ui.label(
                        f"✅ {feature}"
                    ).classes(
                        "feature-item"
                    )


# ==========================================================
# COMPARISON
# ==========================================================

def create_comparison():

    with ui.column().classes("section"):

        ui.label(
            "Vehicle Comparison"
        ).classes(
            "section-title"
        )

        ui.label(
            "Comparing Petrol, Electric and Solar Vehicles."
        ).classes(
            "section-subtitle"
        )

        columns = [

            {
                "name": "Vehicle",
                "label": "Vehicle",
                "field": "Vehicle"
            },

            {
                "name": "Fuel",
                "label": "Fuel",
                "field": "Fuel"
            },

            {
                "name": "Pollution",
                "label": "Pollution",
                "field": "Pollution"
            },

            {
                "name": "Running Cost",
                "label": "Running Cost",
                "field": "Running Cost"
            }

        ]

        ui.table(

            columns=columns,

            rows=COMPARISON

        ).classes(

            "comparison-table"

        )


# ==========================================================
# FUTURE
# ==========================================================

def create_future():

    with ui.column().classes("section"):

        ui.html(
            '<div id="future"></div>'
        )

        ui.label(
            "Future Scope"
        ).classes(
            "section-title"
        )

        ui.label(
            "Solar vehicle technology continues to improve every year."
        ).classes(
            "section-subtitle"
        )

        with ui.column().classes(
            "future-list"
        ):

            for item in FUTURE:

                with ui.card().classes(
                    "glass-card future-card"
                ):

                    ui.label(
                        f"🚀 {item}"
                    ).classes(
                        "future-item"
                    )
                    # ==========================================================
# TEAM
# ==========================================================

def create_team():

    with ui.column().classes("section"):

        ui.html('<div id="team"></div>')

        ui.label(
            "Project Team"
        ).classes(
            "section-title"
        )

        ui.label(
            "Created as a school project."
        ).classes(
            "section-subtitle"
        )

        with ui.card().classes(
            "glass-card"
        ):

            ui.label(
                "Driving Towards Tomorrow\nSolar Powered Cars"
            ).classes(
                "section-text"
            )


# ==========================================================
# FOOTER
# ==========================================================

def create_footer():

    with ui.footer().classes("footer"):

        ui.label(
            "© 2026 Driving Towards Tomorrow | Solar Powered Cars"
        ).classes(
            "footer-text"
        ) 
