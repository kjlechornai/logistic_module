"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
from typing import List


class Inventory(pc.State):
    """The app state."""

    cat_abbr: List[str] = ["STA", "PLU", "ELE", "VEH"]
    options: List[str] = ["Inventory Item", "Purchasing Item", "Sales Item"]
    item_type: List[str] = ["Item", "Service", "Works"]
    uom_group: List[str] = ["Litres", "Kilos", "Packs"]
    item_group: List[str] = ["Stock", "Fixed Assets", "Project Items", "Tools"]
    price_list: List[str] = [
        "Price List 01",
        "Last Evaluated Price",
        "Last Purchase Price",
        "Moving Average Price",
    ]


class InventoryTable(pc.Model, table=True):
    item_no: str
    item_desciption: str
    item_category: str
    item_uom: str
    item_pricelist: str
    item_type: str


def purchase_request_header():
    return pc.center(
        pc.text("Purchase Request", flex="2"),
        pc.icon(
            tag="minus",
            color="teal",
            bg="white",
            font_size="1.25rem",
            w="25px",
            h="25px",
            border="1.5px solid white",
            border_radius="1rem",
            padding="3px",
        ),
        pc.icon(
            tag="copy",
            color="teal",
            bg="white",
            font_size="1.25rem",
            w="25px",
            h="25px",
            border="1.5px solid white",
            border_radius="1rem",
            padding="3px",
        ),
        pc.icon(
            tag="close",
            color="teal",
            bg="white",
            font_size="1.25rem",
            w="25px",
            h="25px",
            border="1.5px solid white",
            border_radius="1rem",
            padding="3px",
        ),
        color="white",
        font_weight="700",
        height="50px",
        width="100%",
        bg="steelblue",
        display="flex",
        align_items="center",
        justify_content="center",
        padding="1em",
    )


def add_new_item_header():
    return pc.center(
        pc.text("Item Data", flex="2"),
        pc.icon(
            tag="minus",
            color="teal",
            bg="white",
            font_size="1.25rem",
            w="25px",
            h="25px",
            border="1.5px solid white",
            border_radius="1rem",
            padding="3px",
        ),
        pc.icon(
            tag="copy",
            color="teal",
            bg="white",
            font_size="1.25rem",
            w="25px",
            h="25px",
            border="1.5px solid white",
            border_radius="1rem",
            padding="3px",
        ),
        pc.icon(
            tag="close",
            color="teal",
            bg="white",
            font_size="1.25rem",
            w="25px",
            h="25px",
            border="1.5px solid white",
            border_radius="1rem",
            padding="3px",
        ),
        color="white",
        font_weight="700",
        height="50px",
        width="100%",
        bg="teal",
        display="flex",
        align_items="center",
        justify_content="center",
        padding="1em",
    )


def add_new_item_middle():
    return pc.center(
        pc.hstack(
            pc.flex(
                pc.flex(
                    pc.text(
                        "Item No.",
                        font_size="0.75rem",
                        font_weight="700",
                        width="200px",
                        text_align="left",
                    ),
                    pc.select(
                        Inventory.cat_abbr,
                        font_size="0.75rem",
                        height="1.75rem",
                        border="None",
                        bg="lightseagreen",
                        margin="2px",
                    ),
                    pc.input(
                        height="1.75rem",
                        border="None",
                        border_bottom="1px solid gray",
                        margin="2px",
                    ),
                    justify="end",
                    align="end",
                ),
                pc.flex(
                    pc.text(
                        "Description",
                        font_size="0.75rem",
                        font_weight="700",
                        width="200px",
                        text_align="left",
                    ),
                    pc.spacer(),
                    pc.input(
                        height="1.75rem",
                        border="None",
                        border_bottom="1px solid gray",
                        margin="2px",
                    ),
                    justify="end",
                    align="end",
                ),
                pc.flex(
                    pc.text(
                        "Foreign Name",
                        font_size="0.75rem",
                        font_weight="700",
                        width="200px",
                    ),
                    pc.spacer(),
                    pc.input(
                        height="1.75rem",
                        border="None",
                        border_bottom="1px solid gray",
                        margin="2px",
                    ),
                    justify="end",
                    align="end",
                ),
                pc.flex(
                    pc.text(
                        "Item Type",
                        font_size="0.75rem",
                        font_weight="700",
                        width="350px",
                    ),
                    pc.select(
                        Inventory.item_type,
                        font_size="0.75rem",
                        height="1.75rem",
                        border="None",
                        bg="lightseagreen",
                        margin="2px",
                    ),
                    justify="end",
                    align="end",
                ),
                pc.flex(
                    pc.text(
                        "Item Group",
                        font_size="0.75rem",
                        font_weight="700",
                        width="350px",
                    ),
                    pc.select(
                        Inventory.item_group,
                        font_size="0.75rem",
                        height="1.75rem",
                        border="None",
                        bg="lightseagreen",
                        margin="2px",
                    ),
                    justify="end",
                    align="end",
                ),
                pc.flex(
                    pc.text(
                        "UOM Group",
                        font_size="0.75rem",
                        font_weight="700",
                        width="350px",
                    ),
                    pc.select(
                        Inventory.uom_group,
                        placeholder="pcs",
                        font_size="0.75rem",
                        height="1.75rem",
                        border="None",
                        bg="lightseagreen",
                        margin="2px",
                    ),
                    justify="end",
                    align="end",
                ),
                pc.flex(
                    pc.text(
                        "Price List",
                        font_size="0.75rem",
                        font_weight="700",
                        width="350px",
                    ),
                    pc.select(
                        Inventory.price_list,
                        font_size="0.75rem",
                        height="1.75rem",
                        border="None",
                        bg="lightseagreen",
                        margin="2px",
                    ),
                    justify="end",
                    align="end",
                ),
                # pc.hstack(pc.text("Item Description"), pc.input()),
                # margin_auto="0",
                padding="20px",
                border_right="2px solid gray",
                width="100%",
                justify="center",
                align="left",
                direction="column",
                spacing="2px",
            ),
            pc.flex(
                pc.checkbox(
                    Inventory.options[0],
                    size="sm",
                ),
                pc.checkbox(Inventory.options[1], size="sm"),
                pc.checkbox(Inventory.options[2], size="sm"),
                width="150px",
                direction="column",
                justify="start",
                align="left",
            ),
            display="flex",
            justify_content="flex_start",
        )
    )


def pr_middle():
    return pc.center(
        pc.hstack(
            pc.flex(
                pc.flex(
                    pc.text(
                        "Requester",
                        font_size="0.75rem",
                        width="200px",
                        text_align="left",
                    ),
                    pc.box(
                        pc.select(
                            placeholder="user",
                            font_size="0.75rem",
                            height="1.5rem",
                            border="None",
                        ),
                        bg="steelblue",
                        w="150px",
                        border="1px solid gray",
                        border_radius="5px",
                    ),
                    pc.input(
                        height="1.75rem",
                        w="200px",
                        border_radius="0px",
                        border="None",
                        border_bottom="1px solid gray",
                        margin="2px",
                    ),
                    justify="end",
                    align="end",
                    padding="1px",
                ),
                pc.flex(
                    pc.text(
                        "Requester name",
                        font_size="0.75rem",
                        width="200px",
                        text_align="left",
                    ),
                    pc.spacer(),
                    pc.input(
                        height="1.75rem",
                        w="250px",
                        border_radius="0px",
                        border="None",
                        border_bottom="1px solid gray",
                        margin="2px",
                    ),
                    justify="end",
                    align="end",
                    padding="1px",
                ),
                pc.flex(
                    pc.text(
                        "Branch",
                        font_size="0.75rem",
                        width="200px",
                    ),
                    pc.spacer(),
                    pc.box(
                        pc.select(
                            placeholder="Site",
                            font_size="0.75rem",
                            height="1.5rem",
                            border="None",
                        ),
                        bg="steelblue",
                        w="150px",
                        border="1px solid gray",
                        border_radius="5px",
                    ),
                    justify="end",
                    align="end",
                    padding="1px",
                ),
                pc.flex(
                    pc.text(
                        "Department",
                        font_size="0.75rem",
                        width="200px",
                    ),
                    pc.input(
                        height="1.75rem",
                        w="250px",
                        border_radius="0px",
                        border="None",
                        border_bottom="1px solid gray",
                        margin="2px",
                    ),
                    justify="end",
                    align="end",
                    padding="1px",
                ),
                pc.flex(
                    pc.box(
                        pc.checkbox(
                            "Send Email if PO or GRPO is added",
                        ),
                        w="100%",
                        font_size="0.75rem",
                    ),
                    # pc.text(
                    #     "Send Email if PO or GRPO is added",
                    #     font_size="0.75rem",
                    #     width="350px",
                    #     text_align="left",
                    # ),
                    justify="start",
                    align="start",
                    padding="1px",
                ),
                pc.flex(
                    pc.text(
                        "Email address",
                        font_size="0.75rem",
                        width="350px",
                    ),
                    pc.input(
                        height="1.75rem",
                        border="None",
                        w="250px",
                        border_radius="0px",
                        border_bottom="1px solid gray",
                        margin="2px",
                    ),
                    justify="end",
                    align="end",
                    padding="1px",
                ),
                # pc.hstack(pc.text("Item Description"), pc.input()),
                # margin_auto="0",
                padding="0px 100px 0px 20px",
                width="40%",
                justify="start",
                align="left",
                direction="column",
            ),
            pc.flex(pc.box(), w="30%"),
            pc.flex(
                pc.flex(
                    pc.text(
                        "No.",
                        font_size="0.75rem",
                        width="150px",
                        text_align="left",
                    ),
                    pc.box(
                        pc.select(
                            placeholder="PR",
                            font_size="0.75rem",
                            height="1.5rem",
                            border="None",
                        ),
                        bg="steelblue",
                        w="150px",
                        border="1px solid gray",
                        border_radius="5px",
                    ),
                    pc.input(
                        height="1.75rem",
                        w="150px",
                        border_radius="0px",
                        border="None",
                        border_bottom="1px solid gray",
                        margin="2px",
                    ),
                    justify="end",
                    align="end",
                    padding="2px",
                ),
                pc.flex(
                    pc.text(
                        "Status",
                        font_size="0.75rem",
                        width="200px",
                        text_align="left",
                    ),
                    pc.spacer(),
                    pc.input(
                        height="1.75rem",
                        border="None",
                        border_bottom="1px solid gray",
                        margin="2px",
                    ),
                    justify="end",
                    align="end",
                ),
                pc.flex(
                    pc.text(
                        "Posting Date",
                        font_size="0.75rem",
                        width="200px",
                    ),
                    pc.spacer(),
                    pc.input(
                        height="1.75rem",
                        border="None",
                        border_radius="0px",
                        border_bottom="1px solid gray",
                        margin="2px",
                    ),
                    justify="end",
                    align="end",
                ),
                pc.flex(
                    pc.text(
                        "Valid Until",
                        font_size="0.75rem",
                        width="200px",
                        text_align="left",
                    ),
                    pc.spacer(),
                    pc.input(
                        height="1.75rem",
                        border="None",
                        border_bottom="1px solid gray",
                        border_radius="0px",
                        margin="2px",
                    ),
                    justify="end",
                    align="end",
                ),
                pc.flex(
                    pc.text(
                        "Document Date",
                        font_size="0.75rem",
                        width="200px",
                    ),
                    pc.spacer(),
                    pc.input(
                        height="1.75rem",
                        border="None",
                        border_bottom="1px solid gray",
                        border_radius="0px",
                        margin="2px",
                    ),
                    justify="end",
                    align="end",
                ),
                pc.flex(
                    pc.text(
                        "Required Date",
                        font_size="0.75rem",
                        width="200px",
                    ),
                    pc.spacer(),
                    pc.input(
                        height="1.75rem",
                        border="None",
                        border_bottom="1px solid gray",
                        border_radius="0px",
                        margin="2px",
                    ),
                    justify="end",
                    align="end",
                ),
                # pc.hstack(pc.text("Item Description"), pc.input()),
                # margin_auto="0",
                padding="20px",
                padding_top="0px",
                width="30%",
                justify="right",
                align="right",
                direction="column",
                spacing="2px",
            ),
            display="flex",
            justify_content="flex_start",
            w="100%",
        ),
        w="100%",
    )


def add_new_item_menu():
    return pc.responsive_grid(
        pc.box(
            "General",
            font_size="0.65rem",
            border="1px solid rgba(0,0,0,0.5)",
            text_align="center",
            _hover={"cursor": "pointer"},
        ),
        pc.box(
            "Purchasing Data",
            font_size="0.65rem",
            border="1px solid rgba(0,0,0,0.5)",
            _hover={"cursor": "pointer"},
            text_align="center",
        ),
        pc.box(
            "Sales Data",
            font_size="0.65rem",
            border="1px solid rgba(0,0,0,0.5)",
            _hover={"cursor": "pointer"},
            text_align="center",
        ),
        pc.box(
            "Inventory Data",
            font_size="0.65rem",
            border="1px solid rgba(0,0,0,0.5)",
            _hover={"cursor": "pointer"},
            text_align="center",
        ),
        pc.box(
            "Planning Data",
            font_size="0.65rem",
            border="1px solid rgba(0,0,0,0.5)",
            _hover={"cursor": "pointer"},
            text_align="center",
        ),
        pc.box(
            "Production Data",
            font_size="0.65rem",
            border="1px solid rgba(0,0,0,0.5)",
            _hover={"cursor": "pointer"},
            text_align="center",
        ),
        pc.box(
            "Properties",
            font_size="0.65rem",
            border="1px solid rgba(0,0,0,0.5)",
            _hover={"cursor": "pointer"},
            text_align="center",
        ),
        pc.box(
            "Attachments",
            font_size="0.65rem",
            border="1px solid rgba(0,0,0,0.5)",
            _hover={"cursor": "pointer"},
            text_align="center",
        ),
        columns=[8],
        width="100%",
        # spacing="1",
        bg="rgba(0,0,0,0.1)",
        border="1px solid rgba(0,0,0,0.5)",
        border_radius="5px",
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
                height="1.75rem",
                border="None",
                bg="lightseagreen",
                margin="2px",
            ),
            pc.spacer(),
            align="center",
            width="350px",
            padding_top="30px",
        ),
        pc.flex(
            pc.text(
                "Additional Identifier",
                font_size="0.75rem",
                width="300px",
            ),
            pc.spacer(),
            pc.input(
                height="1.75rem",
                border="None",
                border_bottom="1px solid black",
                border_radius="0px",
                margin="2px",
            ),
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
                height="1.75rem",
                border="None",
                bg="lightseagreen",
                margin="2px",
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
                height="1.75rem",
                border="None",
                bg="lightseagreen",
                margin="2px",
            ),
            pc.spacer(),
            align="center",
            width="350px",
        ),
        pc.flex(
            pc.flex(
                pc.radio("Active", font_size="12px"),
                pc.radio("Inactive"),
                pc.radio("Advanced"),
                display="flex",
                direction="column",
                width="100px",
                margin="10px",
            ),
            pc.flex(
                pc.text(
                    "From",
                    font_size="0.75rem",
                ),
                pc.spacer(),
                pc.input(
                    height="1.75rem",
                    w="100px",
                    border="None",
                    border_bottom="1px solid black",
                    border_radius="0px",
                ),
                pc.spacer(),
                align="end",
                justify="end",
                width="200px",
                margin="10px",
            ),
            pc.flex(
                pc.text(
                    "To",
                    font_size="0.75rem",
                ),
                pc.spacer(),
                pc.input(
                    height="1.75rem",
                    border="None",
                    w="100px",
                    border_bottom="1px solid black",
                    border_radius="0px",
                ),
                pc.spacer(),
                align="end",
                justify="end",
                width="200px",
                margin="10px",
            ),
            pc.flex(
                pc.text(
                    "Remarks",
                    font_size="0.75rem",
                ),
                pc.spacer(),
                pc.input(
                    height="1.75rem",
                    w="100px",
                    border="None",
                    border_bottom="1px solid black",
                    border_radius="0px",
                ),
                pc.spacer(),
                align="end",
                justify="end",
                width="200px",
                margin="10px",
            ),
            align="center",
            justify="center",
            width="100%",
            padding_top="40px",
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
                    pc.input(
                        height="1.75rem",
                        border="None",
                        border_bottom="1px solid black",
                        border_radius="0px",
                    ),
                    pc.spacer(),
                    align="end",
                    justify="end",
                ),
                pc.flex(
                    pc.text(
                        "Standard Item Identification",
                        font_size="0.75rem",
                        width="300px",
                    ),
                    pc.spacer(),
                    pc.input(
                        height="1.75rem",
                        border="None",
                        border_bottom="1px solid black",
                        border_radius="0px",
                    ),
                    pc.spacer(),
                    align="end",
                    justify="end",
                ),
                pc.flex(
                    pc.text(
                        "Commodity Classification",
                        font_size="0.75rem",
                        width="300px",
                    ),
                    pc.spacer(),
                    pc.input(
                        height="1.75rem",
                        border="None",
                        border_bottom="1px solid black",
                        border_radius="0px",
                    ),
                    pc.spacer(),
                    align="end",
                    justify="end",
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
            pc.button("Add", margin="10px", bg="teal", color="white", w="200px"),
            pc.button("Cancel", margin="10px", bg="teal", color="white", w="200px"),
            justify="start",
            align="center",
            width="300px",
            padding_top="40px",
        ),
        direction="column",
        justify="center",
        align="left",
        padding="10px",
        width="100%",
        padding_top="50px",
    )


def purchase_table():
    return pc.flex(
        pc.vstack(
            pc.flex(
                pc.text("Request", w="150px", font_size="0.75rem", margin="10px"),
                pc.select(
                    placeholder="Kizito", border="None", h="1.75rem", bg="steelblue"
                ),
                pc.input(
                    h="1.75rem",
                    w="200px",
                    border="None",
                    border_radius="0px",
                    border_bottom="1px solid black",
                ),
                justify="end",
                align="end",
            ),
            pc.flex(
                pc.text(
                    "Requester Name", w="200px", font_size="0.75rem", margin="10px"
                ),
                pc.input(
                    h="1.75rem",
                    border="None",
                    border_radius="0px",
                    border_bottom="1px solid black",
                    w="200px",
                ),
                justify="end",
                align="end",
            ),
            pc.flex(
                pc.text("Branch", w="200px", font_size="0.75rem", margin="10px"),
                pc.select(
                    placeholder="Site",
                    h="1.75rem",
                    border="None",
                    bg="steelblue",
                    w="150px",
                ),
                justify="end",
                align="end",
            ),
            pc.flex(
                pc.text("Department", w="200px", font_size="0.75rem", margin="10px"),
                pc.input(
                    h="1.75rem",
                    w="150px",
                    border="None",
                    border_radius="0px",
                    border_bottom="1px solid black",
                ),
                justify="end",
                align="end",
            ),
            pc.flex(
                pc.checkbox("Send Email if PO or GRPO is added"),
                justify="end",
                align="end",
            ),
            pc.flex(
                pc.text("Email Address", font_size="0.75rem", w="200px", margin="10px"),
                pc.input(
                    h="1.75rem",
                    w="150px",
                    border="None",
                    border_radius="0px",
                    border_bottom="1px solid black",
                ),
                justify="end",
                align="end",
            ),
            flex="2",
        ),
        pc.vstack(
            pc.vstack(
                pc.flex(
                    pc.text("No."),
                    pc.select(placeholder="PR"),
                    pc.input(
                        h="1.75rem",
                        border="None",
                        border_radius="0px",
                        border_bottom="1px solid black",
                    ),
                ),
                pc.flex(
                    pc.text("Status"),
                    pc.input(
                        h="1.75rem",
                        border="None",
                        border_radius="0px",
                        border_bottom="1px solid black",
                    ),
                ),
                pc.flex(
                    pc.text("Posting Date"),
                    pc.input(
                        h="1.75rem",
                        border="None",
                        border_radius="0px",
                        border_bottom="1px solid black",
                    ),
                ),
                pc.flex(
                    pc.text("Valid Until"),
                    pc.input(
                        h="1.75rem",
                        border="None",
                        border_radius="0px",
                        border_bottom="1px solid black",
                    ),
                ),
                pc.flex(
                    pc.text("Document Date"),
                    pc.input(
                        h="1.75rem",
                        border="None",
                        border_radius="0px",
                        border_bottom="1px solid black",
                    ),
                ),
                pc.flex(
                    pc.text("Required Date"),
                    pc.input(
                        h="1.75rem",
                        border="None",
                        border_radius="0px",
                        border_bottom="1px solid black",
                    ),
                ),
                w="500px",
                h="500px",
            ),
        ),
        # flex settings
        justify="end",
        align="end",
        w="100%",
        h="100%",
    )


@pc.route(route="/", title="Index Home")  # Similar to app.add_page()
def index() -> pc.Component:
    # Render the main Index Page
    return pc.center(
        pc.vstack(
            add_new_item_header(),
            add_new_item_middle(),
            add_new_item_menu(),
            general_data(),
            box_shadow="0 16px 30px 0 rgba(110, 50, 70, 0.4)",
        ),
        bg="lightblue",
        width="100%",
        height="100%",
    )


@pc.route(route="purchase-request", title="Purchase Request Page")
def purchase_request():
    return pc.center(
        pc.vstack(
            purchase_request_header(),
            pr_middle(),
            # center settings
            box_shadow="0 16px 30px 0 rgba(110, 90, 170, 0.4)",
        ),
        bg="lightskyblue",
        width="100%",
        height="100%",
        padding_top="50px",
    )


# Add state and page to the app.
app = pc.App(state=Inventory)
app.compile()
