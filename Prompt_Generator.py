import streamlit as st

# --- OPSI DASAR (Hanya untuk hal-hal yang sering diulang) ---
# Subjek dan Aksi sekarang akan diketik bebas oleh pengguna
options = {
    "gaya_visual": [
        "Fotorealistik, sinematik 35mm", "Video dokumenter alam liar", "Gaya anime Ghibli", 
        "Cyberpunk, penuh lampu neon", "Film noir, hitam putih", "Fantasi epik",
        "Lukisan cat air", "Stop-motion dengan tanah liat", "Video game 8-bit retro"
    ]
}

# --- DESAIN ANTARMUKA APLIKASI v2.0 ---

st.set_page_config(page_title="VidPrompt Architect v2.0", layout="wide")

st.title("🚀 VidPrompt Architect v2.0")
st.markdown("Konfigurator Adegan untuk AI Video Generatif (VEO3, Sora, dll.)")

# --- BAGIAN PENGATURAN TEKNIS (DI SIDEBAR) ---
st.sidebar.header("⚙️ Parameter Teknis")

resolusi = st.sidebar.selectbox(
    "Resolusi & Kualitas",
    ["HD (1080p)", "4K", "8K Ultra HD"],
    index=1 # Nilai default adalah 4K
)

rasio_aspek = st.sidebar.selectbox(
    "Rasio Aspek (Untuk Platform)",
    ["16:9 (Widescreen - YouTube, Vimeo)", 
     "9:16 (Vertikal - TikTok, Reels, Shorts)", 
     "1:1 (Persegi - Instagram Feed)"]
)

durasi = st.sidebar.slider(
    "Perkiraan Durasi (detik)",
    min_value=4,
    max_value=30,
    value=10 # Nilai default adalah 10 detik
)

# --- BAGIAN KREATIF (DI HALAMAN UTAMA) ---
st.header("🎬 Deskripsi Adegan Kreatif")

# Gaya Visual tetap menggunakan dropdown untuk konsistensi
gaya_pilihan = st.selectbox("Pilih Gaya Visual Dasar:", options["gaya_visual"])

# Input bebas untuk Subjek dan Aksi (Ide dari "Isi Otak Kita")
subjek_input = st.text_input(
    "Subjek Utama:",
    placeholder="Contoh: Seekor naga kristal raksasa, seorang anak kecil dengan robot peliharaannya"
)

skenario_input = st.text_area(
    "Skenario Detail (Aksi, Lokasi, Mood):",
    placeholder="Contoh: terbang rendah melintasi lembah futuristik yang dipenuhi air terjun neon. Suasananya megah dan sedikit misterius. Awan badai berkumpul di kejauhan.",
    height=150
)

# Tombol untuk menghasilkan prompt
generate_button = st.button("Buat Prompt Lengkap ✨", use_container_width=True)

# --- LOGIKA UNTUK MENGHASILKAN PROMPT BARU ---
if generate_button:
    if not subjek_input or not skenario_input:
        st.error("Harap isi bagian 'Subjek Utama' dan 'Skenario Detail'.")
    else:
        # Memformat parameter teknis menjadi tag yang umum digunakan
        kualitas_tag = f"--quality {resolusi.split(' ')[0]}"
        rasio_tag = f"--ar {rasio_aspek.split(' ')[-1].replace(':', ' ')}" # menghasilkan --ar 9 16
        durasi_tag = f"--duration {durasi}"
        
        # Menggabungkan semua bagian menjadi prompt akhir
        deskripsi_kreatif = f"{gaya_pilihan}. {subjek_input} {skenario_input}"
        parameter_teknis = f"{kualitas_tag} {rasio_tag} {durasi_tag}"
        
        prompt_lengkap = f"{deskripsi_kreatif}\n{parameter_teknis}"
        
        st.subheader("✅ Prompt Profesional Anda Siap Digunakan:")
        st.code(prompt_lengkap, language=None)
        st.info("Salin teks di atas. Bagian pertama adalah deskripsi kreatif, dan baris kedua adalah parameter teknis yang bisa dipahami oleh banyak model AI canggih.")

