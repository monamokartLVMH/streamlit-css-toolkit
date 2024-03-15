import streamlit as st
import stars_html
from st_click_detector import click_detector


def get_star_opacities():
    """
    Select star button opacities acording to the outfit grade

    If grade is 1/3 -> first star with full opacity, the next ones with low opacity
    If grade is 2/3 -> two first stars with full opacity, the next one with low opacity
    If grade is 3/3 -> Three stars with full opacity

    output : a dict (key=star opacity id, values=opacity)
    """
    clicked_stars = int(st.session_state.clicked_stars)
    partial_opacity = 0.15
    full_opacity = 1.0
    keys = ["opacity_1", "opacity_2", "opacity_3"]
    values = clicked_stars * [full_opacity] + (3 - clicked_stars) * [partial_opacity]
    return dict(zip(keys, values))


def app():
    tab1, tab2, tab3 = st.tabs(["APP", "stars.py", "stars_html.py"])

    with tab1:
        # Initialize
        if not "clicked_stars" in st.session_state:
            st.session_state.clicked_stars = 0
    
        # Display stars with oppacities depending on the choosen grade
        opactities = get_star_opacities()
        click_detector(
            stars_html.stars.format(**opactities), key="clicked_stars"
        )  # Stars 'listener'
    with tab2:
        with open("stars.py") as python_file:
            python_stars_content = python_file.read()
        st.code(python_stars_content, language="python")

    with tab3:
        with open("stars_html.py") as python_file:
            python_html_content = python_file.read()
        st.code(python_html_content, language="python")


if __name__ == "__main__":
    app()
