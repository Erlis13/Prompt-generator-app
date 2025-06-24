# --- LOGIKA UNTUK MENGHASILKAN PROMPT ---
if generate_button:
    if not subjek_input or not aksi_input:
        st.error("Harap isi setidaknya 'Subjek Utama' dan 'Aksi & Skenario'.")
    else:
        # ... (Bagian prompt_kreatif dan prompt_dialog tetap sama) ...
        prompt_kreatif = (
            f"Gaya: {gaya_pilihan}.\n"
            f"Subjek: {subjek_input}.\n"
            f"Karakter: {karakter_input}.\n"
            f"Lokasi: {lokasi_input}.\n"
            f"Aksi: {aksi_input}."
        )

        prompt_dialog = ""
        if dialog1_input or dialog2_input:
            dialog_lines = []
            if dialog1_input: dialog_lines.append(f"Dialog 1: \"{dialog1_input}\"")
            if dialog2_input: dialog_lines.append(f"Dialog 2: \"{dialog2_input}\"")
            prompt_dialog = "\n\n// -- DIALOG --\n" + "\n".join(dialog_lines)

        # TAMBAHAN BARU: Bangun referensi wajah jika ada
        prompt_referensi = ""
        if face_url_input:
            prompt_referensi = f"\n\n// -- REFERENSI WAJAH --\n--cref {face_url_input}"
        
        # ... (Bagian prompt_teknis tetap sama) ...
        kualitas_tag = f"--quality {resolusi.split(' ')[0]}"
        rasio_tag = f"--ar {rasio_aspek.split('(')[1].split(')')[0]}"
        durasi_tag = f"--duration {durasi}"
        kamera_tag = f"--camera \"{gerakan_kamera.split(' ')[0]}\""
        bahasa_tag = f"--lang {bahasa_dialog.split(' ')[0]}" if bahasa_dialog != "Tanpa Dialog" else ""
        prompt_teknis = f"\n\n// -- PARAMETER TEKNIS --\n{kualitas_tag} {rasio_tag} {durasi_tag} {kamera_tag} {bahasa_tag}"

        # Gabungkan semuanya (dengan bagian referensi baru)
        prompt_lengkap = f"// -- DESKRIPSI KREATIF --\n{prompt_kreatif}{prompt_dialog}{prompt_referensi}{prompt_teknis}"

        st.subheader("✅ Prompt Profesional Anda Siap Digunakan:")
        st.code(prompt_lengkap, language="bash")
