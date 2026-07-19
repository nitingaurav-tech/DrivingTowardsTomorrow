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
                "/static/images/prototype.jpg"
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

        ui.label("Project Team").classes("section-title")

        ui.label(
            "Meet the team behind Driving Towards Tomorrow"
        ).classes("section-subtitle")

        members = [
            (
                "DB",
                "Dwij Bharadwaj",
                "Roll No. 14",
                "Website • PPT • Project File",
            ),
            (
                "LN",
                "Lavith Nagpal",
                "Roll No. 22",
                "Project File • Question Box",
            ),
            (
                "RA",
                "Rudraksh Aashri",
                "Roll No. 28",
                "Prototype Model • Survey",
            ),
            (
                "DB",
                "Daksh Bharadwaj",
                "Roll No. 11",
                "Log Book",
            ),
        ]

        with ui.row().style(
            "width:100%; justify-content:center; gap:28px; "
            "flex-wrap:wrap; margin-top:40px;"
        ):

            for initials, name, roll, work in members:

                with ui.card().style(
                    "width:290px; min-height:360px; padding:28px; "
                    "border-radius:20px; text-align:center; "
                    "background:#ffffff; color:#081426;"
                ):

                    ui.label(initials).style(
                        "width:110px; height:110px; border-radius:50%; "
                        "background:#ffd34d; color:#081426; "
                        "display:flex; align-items:center; "
                        "justify-content:center; margin:0 auto 20px auto; "
                        "font-size:32px; font-weight:800;"
                    )

                    ui.label(name).style(
                        "color:#081426; font-size:22px; "
                        "font-weight:700; margin-bottom:8px;"
                    )

                    ui.label(roll).style(
                        "color:#465368; font-size:16px; "
                        "margin-bottom:12px;"
                    )

                    ui.separator().style(
                        "background:#d8dee8; width:100%; margin:14px 0;"
                    )

                    ui.label("Contribution").style(
                        "color:#081426; font-size:17px; "
                        "font-weight:700; margin-top:8px;"
                    )

                    ui.label(work).style(
                        "color:#465368; font-size:15px; "
                        "line-height:1.5; text-align:center;"
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
