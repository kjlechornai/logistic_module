"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
from typing import List


class Inventory(pc.State):
    """The app state."""

    cat_abbr: List[str] = ["STA", "PLU", "ELE", "VEH"]
    options: List[str] = ["Inventory Item", "Purchasing Item", "Sales Item"]

    pass


class InventoryTable(pc.Model, Table=True):
    pass


def add_new_item_header():
    return pc.center(
        pc.text("Item Data", flex="2"),
        pc.icon(tag="minus", border="1px solid white", padding="2px"),
        pc.icon(tag="close", border="1px solid white", padding="2px"),
        pc.icon(tag="close", border="1px solid white", padding="2px"),
        color="white",
        font_weight="700",
        height="50px",
        width="100%",
        bg="teal",
        display="flex",
        align_items="center",
        justify_content="center",
        padding="5px",
    )


def add_new_item_middle():
    return pc.center(
        pc.hstack(
            pc.vstack(
                pc.flex(
                    pc.text(
                        "Item No.", color="blue", font_size="0.75rem", width="150px"
                    ),
                    pc.spacer(),
                    pc.select(Inventory.cat_abbr, font_size="0.75rem", height="2rem"),
                    pc.spacer(),
                    pc.input(height="2rem"),
                    pc.spacer(),
                    border_bottom="1px solid gray",
                    align="center",
                ),
                pc.flex(
                    pc.text(
                        "Description", color="blue", font_size="0.75rem", width="200px"
                    ),
                    pc.spacer(),
                    pc.input(height="2rem"),
                    pc.spacer(),
                    border_bottom="1px solid gray",
                    align="center",
                ),
                pc.spacer(),
                pc.flex(
                    pc.text(
                        "Foreign Name", font_size="0.75rem", color="blue", width="200px"
                    ),
                    pc.spacer(),
                    pc.input(height="2rem"),
                    pc.spacer(),
                    border_bottom="1px solid gray",
                    align="center",
                ),
                pc.flex(
                    pc.text(
                        "Item Type", font_size="0.75rem", color="blue", width="350px"
                    ),
                    pc.select(Inventory.cat_abbr, font_size="0.75rem", height="2rem"),
                    pc.spacer(),
                    border_bottom="1px solid gray",
                    align="center",
                ),
                pc.flex(
                    pc.text(
                        "Item Group", color="blue", font_size="0.75rem", width="350px"
                    ),
                    pc.select(Inventory.cat_abbr, font_size="0.75rem", height="2rem"),
                    pc.spacer(),
                    border_bottom="1px solid gray",
                    align="center",
                ),
                pc.flex(
                    pc.text(
                        "UOM Group", color="blue", font_size="0.75rem", width="350px"
                    ),
                    pc.select(Inventory.cat_abbr, font_size="0.75rem", height="2rem"),
                    pc.spacer(),
                    border_bottom="1px solid gray",
                    align="center",
                ),
                pc.flex(
                    pc.text(
                        "Price List", color="blue", font_size="0.75rem", width="350px"
                    ),
                    pc.select(
                        Inventory.cat_abbr,
                        font_size="0.75rem",
                        height="2rem",
                    ),
                    pc.spacer(),
                    border_bottom="1px solid gray",
                    align="center",
                ),
                # pc.hstack(pc.text("Item Description"), pc.input()),
                # margin_auto="0",
                padding="20px",
                border_right="2px solid gray",
                width="80%",
            ),
            pc.flex(
                pc.checkbox(
                    Inventory.options[0],
                    font_weight="bold",
                ),
                pc.checkbox(Inventory.options[1], font_weight="bold"),
                pc.checkbox(Inventory.options[2], font_weight="bold"),
                width="150px",
                direction="column",
                justify="start",
                align="start",
                height="50px",
            ),
            display="flex",
            justify_content="space_between",
        )
    )


def add_new_item_menu():
    return pc.flex(
        pc.box(
            "General",
            font_size="0.75rem",
            border="1px solid skyblue",
            _hover={"cursor": "pointer"},
        ),
        pc.spacer(),
        pc.box(
            "Purchasing Data",
            font_size="0.75rem",
            border="1px solid skyblue",
            _hover={"cursor": "pointer"},
        ),
        pc.spacer(),
        pc.box(
            "Sales Data",
            font_size="0.75rem",
            border="1px solid skyblue",
            _hover={"cursor": "pointer"},
        ),
        pc.spacer(),
        pc.box(
            "Inventory Data",
            font_size="0.75rem",
            border="1px solid skyblue",
            _hover={"cursor": "pointer"},
        ),
        pc.spacer(),
        pc.box(
            "Planning Data",
            font_size="0.75rem",
            border="1px solid skyblue",
            _hover={"cursor": "pointer"},
        ),
        pc.spacer(),
        pc.box(
            "Production Data",
            font_size="0.75rem",
            border="1px solid skyblue",
            _hover={"cursor": "pointer"},
        ),
        pc.spacer(),
        pc.box(
            "Properties",
            font_size="0.75rem",
            border="1px solid skyblue",
            _hover={"cursor": "pointer"},
        ),
        pc.spacer(),
        pc.box(
            "Attachments",
            font_size="0.75rem",
            border="1px solid skyblue",
            _hover={"cursor": "pointer"},
        ),
        pc.spacer(),
        justify="center",
        align="center",
        width="100%",
        spacing="1px",
        padding="20px",
    )


def general_data():
    return pc.flex(
        pc.spacer(),
        pc.checkbox(
            "Withholding Tax Liable",
            size="sm",
            width="100%",
        ),
        pc.spacer(),
        pc.spacer(),
        pc.spacer(),
        pc.spacer(),
        pc.spacer(),
        pc.spacer(),
        pc.checkbox("Do Not Apply Discount Groups", size="sm", width="100%"),
        pc.flex(
            pc.text(
                "Manufacturer",
                font_size="0.75rem",
                width="300px",
            ),
            pc.spacer(),
            pc.select(
                Inventory.cat_abbr,
                placeholder="- No Manufacturer",
                font_size="0.75rem",
                height="2rem",
            ),
            pc.spacer(),
            align="center",
            width="350px",
        ),
        pc.flex(
            pc.text(
                "Additional Identifier",
                font_size="0.75rem",
                width="300px",
            ),
            pc.spacer(),
            pc.input(height="2rem"),
            pc.spacer(),
            align="center",
            width="350px",
        ),
        pc.flex(
            pc.text(
                "Shipping Type",
                font_size="0.75rem",
                width="300px",
            ),
            pc.spacer(),
            pc.select(
                # Inventory.cat_abbr,
                font_size="0.75rem",
                height="2rem",
            ),
            pc.spacer(),
            align="center",
            width="350px",
        ),
        pc.text("Serial and Batch Numbers", text_decoration="underline", as_="small"),
        pc.flex(
            pc.text(
                "Manage Item By",
                font_size="0.75rem",
                width="300px",
            ),
            pc.spacer(),
            pc.select(
                # cat_abbr,
                placeholder="None",
                font_size="0.75rem",
                height="2rem",
            ),
            pc.spacer(),
            align="center",
            width="350px",
        ),
        pc.flex(
            pc.flex(
                pc.radio("Active"),
                pc.radio("Inactive"),
                pc.radio("Advanced"),
                display="flex",
                direction="column",
                width="150px",
            ),
            pc.flex(
                pc.text(
                    "From",
                    font_size="0.75rem",
                    width="100px",
                ),
                pc.spacer(),
                pc.input(height="2rem"),
                pc.spacer(),
                align="center",
                width="200px",
            ),
            pc.flex(
                pc.text(
                    "To",
                    font_size="0.75rem",
                    width="100px",
                ),
                pc.spacer(),
                pc.input(height="2rem"),
                pc.spacer(),
                align="center",
                width="200px",
            ),
            pc.flex(
                pc.text(
                    "Remarks",
                    font_size="0.75rem",
                    width="100px",
                ),
                pc.spacer(),
                pc.input(height="2rem"),
                pc.spacer(),
                align="center",
                width="200px",
            ),
        ),
        pc.flex(
            pc.box(width="60%"),
            pc.flex(
                pc.flex(
                    pc.text(
                        "Country/Region Of Origin",
                        font_size="0.75rem",
                        width="300px",
                    ),
                    pc.spacer(),
                    pc.input(height="2rem"),
                    pc.spacer(),
                    align="center",
                ),
                pc.flex(
                    pc.text(
                        "Standard Item Identification",
                        font_size="0.75rem",
                        width="300px",
                    ),
                    pc.spacer(),
                    pc.input(height="2rem"),
                    pc.spacer(),
                    align="center",
                ),
                pc.flex(
                    pc.text(
                        "Commodity Classification",
                        font_size="0.75rem",
                        width="300px",
                    ),
                    pc.spacer(),
                    pc.input(height="2rem"),
                    pc.spacer(),
                    align="center",
                ),
                width="500px",
                direction="column",
            ),
            justify="center",
            align="left",
            spacing="50px",
            width="100%",
        ),
        pc.flex(
            pc.button("Add", margin="10px", bg="steelblue", color="white"),
            pc.button("Cancel", margin="10px", bg="steelblue", color="white"),
            justify="start",
            align="center",
            width="300px",
        ),
        direction="column",
        justify="center",
        align="left",
        padding="10px",
        width="100%",
    )


@pc.route(route="/", title="Index Home")
def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            add_new_item_header(),
            add_new_item_middle(),
            add_new_item_menu(),
            general_data(),
            border="2px solid black",
        ),
        bg="lightblue",
        width="100%",
        height="100%",
    )


# Add state and page to the app.
app = pc.App(state=Inventory)
app.compile()
