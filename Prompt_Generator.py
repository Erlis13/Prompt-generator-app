import streamlit as st

# --- OPSI UNTUK DROPDOWN ---
gaya_visual_options = [
    "Fotorealistik, sinematik 35mm", "Video dokumenter alam liar", "Gaya anime Ghibli", 
    "Cyberpunk, penuh lampu neon", "Film noir, hitam putih", "Fantasi epik",
    "Lukisan cat air", "Stop-motion dengan tanah liat", "Video game 8-bit retro"
]
gerakan_kamera_options = [
    "Static Shot (Kamera diam)", "Pan Kiri/Kanan", "Tilt Atas/Bawah", 
    "Tracking Shot (Mengikuti subjek)", "Dolly Zoom (Efek Vertigo)", "Drone Shot dari atas"
]
bahasa_dialog_options = ["Indonesia", "English", "Japanese", "Tanpa Dialog"]

# --- DESAIN ANTARMUKA APLIKASI v3.0 ---
st.set_page_config(page_title="VidPrompt Architect v3.0", layout="wide")

st.title("🚀 VidPrompt Architect v3.0")
st.markdown("Konfigurator Adegan Profesional untuk AI Video")

# --- BAGIAN PENGATURAN TEKNIS (DI SIDEBAR) ---
st.sidebar.header("⚙️ Parameter Teknis")

resolusi = st.sidebar.selectbox(
    "Resolusi & Kualitas",
    ["HD (1080p)", "4K", "8K Ultra HD"], index=1
)
rasio_aspek = st.sidebar.selectbox(
    "Rasio Aspek (Platform)",
    ["16:9 (YouTube)", "9:16 (TikTok, Reels)", "1:1 (Instagram Post)"]
)
gerakan_kamera = st.sidebar.selectbox("Gerakan Kamera", gerakan_kamera_options)
bahasa_dialog = st.sidebar.selectbox("Bahasa Dialog", bahasa_dialog_options)
durasi = st.sidebar.slider("Perkiraan Durasi (detik)", 4, 30, 12)

# --- BAGIAN KREATIF (DI HALAMAN UTAMA) ---
st.header("🎬 Rancang Adegan Anda")

# Menggunakan kolom agar lebih rapi
col1, col2 = st.columns(2)

with col1:
    gaya_pilihan = st.selectbox("Gaya Visual Dasar", gaya_visual_options)
    subjek_input = st.text_input("Subjek Utama", placeholder="Contoh: Seorang penjelajah waktu")
    karakter_input = st.text_area("Deskripsi Karakter", placeholder="Contoh: Mengenakan jubah teknologi dengan mata bionik, wajahnya terlihat lelah.", height=100)

with col2:
    aksi_input = st.text_area("Aksi & Skenario", placeholder="Contoh: Tiba-tiba muncul di tengah pasar malam yang ramai, kebingungan melihat sekeliling.", height=155)
    lokasi_input = st.text_input("Deskripsi Lokasi", placeholder="Contoh: Pasar malam di Jakarta tahun 1990")

st.subheader("💬 Dialog")
dialog1_input = st.text_input("Baris Dialog 1", placeholder="Karakter A: Di tahun berapa ini?")
dialog2_input = st.text_input("Baris Dialog 2", placeholder="Karakter B: Anda siapa?")

# Tombol untuk menghasilkan prompt
st.write("---") # Garis pemisah
generate_button = st.button("Buat Prompt Lengkap & Profesional ✨", use_container_width=True)

# --- LOGIKA UNTUK MENGHASILKAN PROMPT ---
if generate_button:
    if not subjek_input or not aksi_input:
        st.error("Harap isi setidaknya 'Subjek Utama' dan 'Aksi & Skenario'.")
    else:
        # 1. Bangun Deskripsi Kreatif
        prompt_kreatif = (
            f"Gaya: {gaya_pilihan}.\n"
            f"Subjek: {subjek_input}.\n"
            f"Karakter: {karakter_input}.\n"
            f"Lokasi: {lokasi_input}.\n"
            f"Aksi: {aksi_input}."
        )

        # 2. Bangun Bagian Dialog (hanya jika ada isinya)
        prompt_dialog = ""
        if dialog1_input or dialog2_input:
            dialog_lines = []
            if dialog1_input: dialog_lines.append(f"Dialog 1: \"{dialog1_input}\"")
            if dialog2_input: dialog_lines.append(f"Dialog 2: \"{dialog2_input}\"")
            prompt_dialog = "\n\n// -- DIALOG --\n" + "\n".join(dialog_lines)

        # 3. Bangun Parameter Teknis
        kualitas_tag = f"--quality {resolusi.split(' ')[0]}"
        rasio_tag = f"--ar {rasio_aspek.split('(')[1].split(')')[0]}"
        durasi_tag = f"--duration {durasi}"
        kamera_tag = f"--camera \"{gerakan_kamera.split(' ')[0]}\""
        bahasa_tag = f"--lang {bahasa_dialog.split(' ')[0]}" if bahasa_dialog != "Tanpa Dialog" else ""

        prompt_teknis = f"\n\n// -- PARAMETER TEKNIS --\n{kualitas_tag} {rasio_tag} {durasi_tag} {kamera_tag} {bahasa_tag}"

        # 4. Gabungkan semuanya
        prompt_lengkap = f"// -- DESKRIPSI KREATIF --\n{prompt_kreatif}{prompt_dialog}{prompt_teknis}"

        st.subheader("✅ Prompt Profesional Anda Siap Digunakan:")
        st.code(prompt_lengkap, language="bash")
        st.info("Format ini dirancang agar mudah dibaca oleh manusia dan dipahami oleh AI canggih.")

