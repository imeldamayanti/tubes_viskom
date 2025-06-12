import streamlit as st
import base64

st.set_page_config(page_title="About Us", page_icon="❓")

st.title("Development Team")
st.markdown("""
 This application was developed using Streamlit with Python to build the web interface, and YOLOv11 as the model for real-time hand gesture detection.
""")
st.markdown("---")
# Kolom untuk 3 orang
col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/altap.png", caption="Althaf Rizqullah", width=200)
    # st.markdown("Fokus pada pengembangan model YOLOv11 dan integrasi kamera dengan sistem deteksi gesture.")

with col2:
    st.image("images/imeld.png", caption="Imelda Damayanti", width=200)
    # st.markdown("Bertanggung jawab atas pengolahan data gesture dan perhitungan aritmatika secara otomatis.")

with col3:
    st.image("images/sari.png", caption="Brian Anashari", width=200)
    # st.markdown("Riset literatur gesture recognition dan menyusun dokumentasi proyek secara menyeluruh.")

st.markdown("---")
st.markdown("""
 Hands4Math was developed as a solution to make arithmetic operations more accessible through hand gestures and sign language. Our journey started with a simple idea: using computer vision to recognize gestures and translate them into calculations in real time.

1. Ideation : We began by identifying a real-world challenge—making math operations more inclusive using American Sign Language (ASL) and AI technology.

2. Data Collection : We recorded custom gesture data to build a relevant and high-quality dataset tailored to arithmetic hand signs.

3. Annotation : All collected data was manually annotated to train our detection model accurately.

4. Model Development : We developed the core AI model to detect and classify hand gestures.

5. Model Comparison : We experimented with various architectures, including DETR, MobileNet, and YOLOv11. After evaluation, YOLOv11 was chosen as the most efficient and accurate for real-time detection.

6. Web Implementation : We built an interactive website using Streamlit, integrating the YOLOv11 model to allow users to perform arithmetic operations through live gesture detection.
""")
st.markdown("---")
st.write("Thank you for visiting our application. We hope you find it useful!")



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
