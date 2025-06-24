import streamlit as st
import random

# --- DATA UNTUK PROMPT (DARI BAGIAN 2) ---
# Menggunakan dictionary agar lebih terstruktur
options = {
    "gaya_visual": [
        "Fotorealistik, kualitas tinggi", "Sinematik, film 35mm", "Video dokumenter alam liar",
        "Gaya anime Ghibli", "Film noir, hitam putih", "Rekaman VHS tahun 1980-an",
        "Cyberpunk, penuh lampu neon", "Fantasi epik, gaya Lord of the Rings"
    ],
    "subjek_utama": [
        "Seekor astronot yang kesepian", "Robot raksasa yang sedang berkarat",
        "Seekor rubah ajaib dengan bulu bercahaya", "Seorang detektif di era Victoria",
        "Mobil terbang futuristik", "Pasangan lansia yang sedang berdansa"
    ],
    "aksi_kegiatan": [
        "menjelajahi reruntuhan kuno", "berlari di tengah hujan lebat",
        "membaca buku di perpustakaan yang nyaman", "memasak di dapur yang ramai",
        "terbang melintasi awan", "menatap cakrawala kota dari atap gedung"
    ],
    "lokasi": [
        "di permukaan planet Mars yang tandus", "di jalanan Tokyo yang basah oleh hujan neon",
        "di dalam hutan lebat yang berkabut", "di sebuah kastil abad pertengahan",
        "di pasar malam yang ramai di Indonesia", "di stasiun luar angkasa yang sunyi"
    ],
    "pencahayaan": [
        "saat golden hour", "di tengah malam, diterangi bulan purnama",
        "di pagi yang cerah dan berkabut", "dengan pencahayaan dramatis dan bayangan tajam",
        "dengan lampu studio yang lembut"
    ],
    "sudut_kamera": [
        "extreme close-up", "wide shot", "drone shot dari atas",
        "tracking shot", "point-of-view (POV)"
    ],
    "detail_tambahan": [
        "dengan partikel debu yang melayang di udara", "jalanan yang berkilau basah",
        "dengan efek lens flare sinematik", "dengan angin lembut meniup dedaunan",
        "dengan asap atau uap yang mengepul"
    ]
}

# --- DESAIN ANTARMUKA APLIKASI ---

st.set_page_config(page_title="VidPrompt Architect", layout="wide")

st.title("🚀 VidPrompt Architect")
st.markdown("Generator Prompt Cerdas untuk AI Video")

st.sidebar.header("Pengaturan Adegan")

# Membuat pilihan di sidebar
pilihan = {}
for key, value in options.items():
    # Mengubah key menjadi judul yang lebih rapi (contoh: 'gaya_visual' -> 'Gaya Visual')
    display_name = key.replace('_', ' ').title()
    pilihan[key] = st.sidebar.selectbox(display_name, value)

# Tombol untuk generate
col1, col2 = st.columns([1, 4])

with col1:
    generate_button = st.button("Buat Prompt ✨", use_container_width=True)
    random_button = st.button("Beri Aku Kejutan! 🎲", use_container_width=True)

# Tempat untuk menampilkan hasil
with col2:
    if generate_button:
        # Menggabungkan pilihan pengguna menjadi sebuah prompt
        prompt = (
            f"{pilihan['gaya_visual']}. "
            f"{pilihan['subjek_utama']} {pilihan['aksi_kegiatan']} {pilihan['lokasi']}, {pilihan['pencahayaan']}. "
            f"Sudut kamera: {pilihan['sudut_kamera']}. "
            f"Detail: {pilihan['detail_tambahan']}."
        )
        st.subheader("Prompt Anda Siap Digunakan:")
        st.code(prompt, language=None)
        st.info("Salin prompt di atas dan tempelkan ke AI generator video favorit Anda (Sora, Runway, Pika, dll.)")

    if random_button:
        # Memilih opsi acak dari setiap kategori
        random_prompt_parts = {key: random.choice(value) for key, value in options.items()}
        prompt = (
            f"{random_prompt_parts['gaya_visual']}. "
            f"{random_prompt_parts['subjek_utama']} {random_prompt_parts['aksi_kegiatan']} {random_prompt_parts['lokasi']}, {random_prompt_parts['pencahayaan']}. "
            f"Sudut kamera: {random_prompt_parts['sudut_kamera']}. "
            f"Detail: {random_prompt_parts['detail_tambahan']}."
        )
        st.subheader("Prompt Kejutan Anda:")
        st.code(prompt, language=None)
        st.info("Tidak suka? Coba klik tombol kejutan lagi untuk ide baru!")
