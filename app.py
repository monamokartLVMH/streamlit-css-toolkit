import streamlit as st
import os
import html_utils

theme_config = '[theme]\nprimaryColor="#A3CB38"'

fonts = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Josefin+Sans:wght@200;400&display=swap" rel="stylesheet">
"""

logo_svg = """
<div class= 'logo'> 
    <svg width="60px" height="60px" viewBox="0 0 1024 1024" class="icon"  version="1.1" xmlns="http://www.w3.org/2000/svg">
        <path d="M512 960c-92.8 0-160-200-160-448S419.2 64 512 64s160 200 160 448-67.2 448-160 448z m0-32c65.6 0 128-185.6 128-416S577.6 96 512 96s-128 185.6-128 416 62.4 416 128 416z" fill="#050D42" />
        <path d="M124.8 736c-48-80 92.8-238.4 307.2-363.2S852.8 208 899.2 288 806.4 526.4 592 651.2 171.2 816 124.8 736z m27.2-16c33.6 57.6 225.6 17.6 424-97.6S905.6 361.6 872 304 646.4 286.4 448 401.6 118.4 662.4 152 720z" fill="#050D42" />
        <path d="M899.2 736c-46.4 80-254.4 38.4-467.2-84.8S76.8 368 124.8 288s254.4-38.4 467.2 84.8S947.2 656 899.2 736z m-27.2-16c33.6-57.6-97.6-203.2-296-318.4S184 246.4 152 304 249.6 507.2 448 622.4s392 155.2 424 97.6z" fill="#050D42" />
        <path d="M512 592c-44.8 0-80-35.2-80-80s35.2-80 80-80 80 35.2 80 80-35.2 80-80 80zM272 312c-27.2 0-48-20.8-48-48s20.8-48 48-48 48 20.8 48 48-20.8 48-48 48zM416 880c-27.2 0-48-20.8-48-48s20.8-48 48-48 48 20.8 48 48-20.8 48-48 48z m448-432c-27.2 0-48-20.8-48-48s20.8-48 48-48 48 20.8 48 48-20.8 48-48 48z" fill="#2F4BFF" />
    </svg>
</div>
"""

lena_im_link = "https://www.cosy.sbg.ac.at/~pmeerw/Watermarking/lena_gray.gif"


def check_events():
    if "disabled" not in st.session_state:
        st.session_state.disabled = False
    if "theme" not in st.session_state:
        st.session_state.theme = False
    if st.session_state.get("disable_clicked") :
        st.session_state.disabled = not st.session_state.disabled
    
    if st.session_state.get("theme_clicked") :
        st.session_state.theme = not st.session_state.theme
        if st.session_state.theme:
            with open(".streamlit/config.toml", "w") as w:
                w.write(theme_config)
        else:
            with open(".streamlit/config.toml", "w") as w:
                w.write("")
    

order_key = lambda x: int(x.split(".css")[0])

def app():
    # Select sytle
    st.selectbox("Choose your style", sorted(os.listdir("styles"), key=order_key), key="selected_style")
    selected_style = st.session_state.get("selected_style")

    # Load CSS sytle
    with open(f"styles/{selected_style}") as css:
        css_content = css.read()
        st.write(f"<style>{css_content}</style>", unsafe_allow_html=True)
    st.write(fonts, unsafe_allow_html=True)

    # Check state
    check_events()
    
    # App
    tab1, tab2 = st.tabs(["APP", "CSS"])

    with tab1:

        st.write(logo_svg, unsafe_allow_html=True)
        st.write("""<p class="title"><br />STREAMLIT DEMO<br /></p>""", unsafe_allow_html=True)
        
        st.write("""<p class="question">Do you like those images?</p>""", unsafe_allow_html=True)

        _, col1, col2, _ = st.columns([1, 2, 2, 1])

        col1.image(lena_im_link, use_column_width=True)
        col2.image(lena_im_link, use_column_width=True)

        col1.button("YES", use_container_width=True, key="yes_but", disabled=st.session_state.disabled)
        col2.button("NO", type="primary", use_container_width=True, key="no_but", disabled=st.session_state.disabled)

        _, col_center, _ = st.columns([1, 4, 1])
        col_center.text_input("Do you have something to add ?", placeholder="Nothing")

        col_center.button("DISABLE BUTTONS", use_container_width=True, key="disable_clicked")
        col_center.button("THEME", use_container_width=True, key="theme_clicked")
    with tab2:
        st.code(css_content, language="css")


if __name__ == "__main__":
    
    app()