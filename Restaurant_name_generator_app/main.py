import streamlit as st
from langchain_helper import open_ai_connector

st.title("Generate Name for Your New Restaurant :coffee:")


def cuisine_selector():

    cuisine_names = [
        "",
        "Italian",
        "French",
        "Chinese",
        "Japanese",
        "Indian",
        "Mexican",
        "Thai",
        "Spanish",
        "Greek",
        "Mediterranean",
    ]

    cuisine = st.sidebar.selectbox(
        "Which cuisine do you prefer?",
        cuisine_names,
    )

    return cuisine


cuisine = cuisine_selector()


if not cuisine:
    st.warning("Select An Cuisine !")
else:
    restaurant_name_menu = open_ai_connector(cuisine)

    if restaurant_name_menu:

        restaurant_name = restaurant_name_menu.get("restaurant_name", "")
        menu_items = [
            str_.strip()
            for str_ in restaurant_name_menu.get("menu_items", "").split("\n")
            if str_.strip()
        ]
        st.header(f"{restaurant_name} :fork_and_knife:")

        st.write("**Suggested Menu**")

        for item in menu_items:
            item = item.strip().replace(",", "")
            st.write(item)
