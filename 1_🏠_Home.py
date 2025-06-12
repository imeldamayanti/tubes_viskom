import streamlit as st
from streamlit_lottie import st_lottie
import requests
from streamlit_extras.switch_page_button import switch_page
import base64

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
)

# Load assets
def load_lottieurl(url):
    r = requests.get(url)  
    if r.status_code != 200:    
        return None
    return r.json()

# ini orang
# lottie_code = load_lottieurl("https://lottie.host/24ca0439-215b-44e8-a2d6-150c93865357/60RRYtSfhQ.json")

# ini tangan
# lottie_code = load_lottieurl("https://lottie.host/b1e65c34-cde9-4469-a2cf-1ab78ead1b01/AnfKKl5kgL.json")

# ini tangan 3
lottie_code = load_lottieurl("https://lottie.host/9015186a-4f21-4adc-b18d-cf8d579f00ef/2st5NP7UeB.json")


st.markdown("<div style='margin-top: 100px;'></div>", unsafe_allow_html=True)

with st.container():
    st.write("-----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.title("Welcome!")
        st.write("""
            This is an Arithmetic Calculator Website with Gesture Detection, developed as a technological innovation combining artificial intelligence and sign language.
           
            Here, you can perform arithmetic operations automatically just by using American Sign Language (ASL) hand gestures.
            > On the left side, click Calculator.
                """)

    with right_column:
        st_lottie(lottie_code, height=300, key="coding")
    
    st.write("-----")

# Ini buat BG
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data).decode()

    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


# Pakai fungsi di atas
add_bg_from_local("images/bg1.png")
