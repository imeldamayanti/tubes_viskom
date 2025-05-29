import streamlit as st
import base64

st.set_page_config(page_title="About Us", page_icon="❓")

st.title("Development Team")
st.markdown("""
 Aplikasi ini dikembangkan menggunakan Streamlit dengan bahasa Python untuk membangun
 antarmuka web, serta YOLOv11 sebagai model deteksi gesture tangan secara real-time.  
""")
st.markdown("---")
# Kolom untuk 3 orang
col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/altap.png", caption="Althaf Rizqullah - 1301223107", width=200)
    # st.markdown("Fokus pada pengembangan model YOLOv11 dan integrasi kamera dengan sistem deteksi gesture.")

with col2:
    st.image("images/imeld.png", caption="Imelda Damayanti - 1301223287", width=200)
    # st.markdown("Bertanggung jawab atas pengolahan data gesture dan perhitungan aritmatika secara otomatis.")

with col3:
    st.image("images/sari.png", caption="Brian Anashari - 1301223227", width=200)
    # st.markdown("Riset literatur gesture recognition dan menyusun dokumentasi proyek secara menyeluruh.")

st.markdown("---")
st.write("Terima kasih telah mengunjungi aplikasi kami. Semoga bermanfaat!")



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
