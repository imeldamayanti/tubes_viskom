import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import time
import os
import base64

st.set_page_config(page_title="He", page_icon="📱")

st.title("Kalkulator Aritmatika dengan Deteksi Gesture ✌")
st.write(
    """Arahkan tangan ke kamera sesuai simbol angka dan operator, lalu sistem akan otomatis mendeteksi gesture tersebut dan menampilkan hasil perhitungannya secara real-time."""
)

current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "best_18mei.pt")

model = YOLO(model_path)

# Label mapping
label_map = {
    "O": "0", "1": "1", "2": "2", "3": "3", "4": "4",
    "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
    "addition": "+", "minus": "-", "multiplication": "*",
    "division": "/", "equal": "="
}

# Setup UI


run = st.checkbox("📸 Mulai Kamera")

# Inisialisasi session_state
if 'expression' not in st.session_state:
    st.session_state.expression = ""
if 'result' not in st.session_state:
    st.session_state.result = ""
if 'history' not in st.session_state:
    st.session_state.history = []

# Placeholder Streamlit
frame_placeholder = st.empty()
expr_placeholder = st.empty()
result_placeholder = st.empty()
history_placeholder = st.empty()

# Konstanta
FRAME_INTERVAL = 1
last_capture_time = 0

if run:
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.error("Gagal membuka kamera.")
            break

        frame = cv2.resize(frame, (640, 480))
        current_time = time.time()
        annotated_frame = frame.copy()

        if current_time - last_capture_time > FRAME_INTERVAL:
            results = model.predict(frame, imgsz=640, conf=0.5)

            labels = []
            if results and results[0].boxes is not None:
                boxes = results[0].boxes
                for box in boxes:
                    cls_id = int(box.cls[0])
                    label = model.names[cls_id]
                    labels.append((label, box.xyxy[0][0].item()))

                labels.sort(key=lambda x: x[1])  # Urut kiri ke kanan
                for label, _ in labels:
                    mapped = label_map.get(label.lower(), "")
                    if mapped == "=" and st.session_state.expression:
                        try:
                            st.session_state.result = eval(st.session_state.expression)
                            st.session_state.history.insert(
                                0, f"{st.session_state.expression} = {st.session_state.result}"
                            )
                        except:
                            st.session_state.result = "Error"
                            st.session_state.history.insert(
                                0, f"{st.session_state.expression} = Error"
                            )
                        st.session_state.expression = ""

                        # Batasi history maksimal 10 entri
                        if len(st.session_state.history) > 10:
                            st.session_state.history = st.session_state.history[:10]

                    elif mapped:
                        st.session_state.expression += mapped

                annotated_frame = results[0].plot()

            last_capture_time = current_time

        # Update UI
        expr_placeholder.markdown(f"**Ekspresi:** `{st.session_state.expression}`")
        if st.session_state.result != "":
            result_placeholder.markdown(f"### ✅ Hasil: `{st.session_state.result}`")

        with history_placeholder:
            st.markdown("### 🧾 Riwayat Perhitungan")
            for h in st.session_state.history:
                st.markdown(f"- `{h}`")

        annotated_frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(annotated_frame_rgb, channels="RGB")

    cap.release()



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
