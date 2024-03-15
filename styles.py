import streamlit as st
import styles_html
from st_click_detector import click_detector


def init_chosen_styles():
    """
    Initialization of 'style' button values -> False
    """
    st.session_state.chosen_styles = {
        "casual": False,
        "rock": False,
        "urban": False,
        "tailoring": False,
        "other": False,
    }


def set_chosen_styles():
    """
    Set chosen styles
    If a style has been clicked on, its choosen value becomes True
    """
    if st.session_state.get("clicked_style"):
        clicked_style = st.session_state.get("clicked_style")
        st.session_state.chosen_styles[clicked_style] = (
            not st.session_state.chosen_styles[clicked_style]
        )


def get_style_color_dict():
    """
    Select style button color acording to the selection

    If a style is not selected -> silver
    If a style is selected -> black

    output : a dict (key=style colo id, values=color)
    """
    style_color_dict = {
        f"{k}_color": "black" if v else "silver"
        for k, v in st.session_state.chosen_styles.items()
    }
    return style_color_dict


def app():
    tab1, tab2, tab3 = st.tabs(["APP", "styles.py", "styles_html.py"])
    
    with tab1:
        if not "chosen_styles" in st.session_state:
            init_chosen_styles()
        set_chosen_styles()

        # Display style choices with color depending on the clicked styles
        style_color_dict = get_style_color_dict()
        style_choice_html = styles_html.get_styles(
            style_color_dict
        )  # Style choice html text
        click_detector(style_choice_html, key="clicked_style")  # Style choice 'listener'
    
    with tab2:
        with open("styles.py") as python_file:
            python_styles_content = python_file.read()
        st.code(python_styles_content, language="python")

    with tab3:
        with open("styles_html.py") as python_file:
            python_html_content = python_file.read()
        st.code(python_html_content, language="python")


if __name__ == "__main__":
    app()
