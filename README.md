# 🎮 Game Kuis Mahasiswa (Python Quiz Game)

Aplikasi kuis interaktif bertema game dengan sistem nyawa, kombo poin, bantuan 50:50, serta integrasi identitas mahasiswa (NIM, Nama, Jurusan, Alamat).

---

## ✨ Fitur Game
1. **Form Registrasi Mahasiswa**: Meminta input NIM, Nama, Jurusan, dan Alamat sesuai format awal Anda.
2. **Sistem Nyawa (Lives)**: Pemain memiliki 3 nyawa (`❤️ ❤️ ❤️`). Jika salah menjawab, nyawa berkurang 1.
3. **Sistem Combo & Skor**: Menjawab benar berturut-turut akan melipatgandakan poin bonus (`🔥 COMBO STREAK`).
4. **Bantuan 50:50**: Pemain bisa mengetik `50` untuk mengeliminasi 2 pilihan jawaban yang salah (dapat digunakan 1x).
5. **Penjelasan Edukatif**: Setiap soal selesai dijawab, sistem menampilkan pembahasan singkat.
6. **Kartu Hasil Ujian (Raport Akhir)**: Menampilkan konversi nilai (0-100), perolehan Grade (A/B/C/D), dan status kelulusan.
7. **Simpan Riwayat**: Hasil ujian otomatis dicatat ke file `riwayat_quiz.txt`.

---

## 🚀 Cara Menjalankan di VS Code

1. Buka folder proyek ini di VS Code:
   - Pilih menu **File > Open Folder...**
   - Arahkan ke folder:
     `C:\Users\MyBook Hype AMD\.gemini\antigravity\scratch\quiz_game`

2. Buka Terminal di VS Code:
   - Tekan tombol `Ctrl + ` ` (tanda petik miring di bawah tombol Esc) atau pilih menu **Terminal > New Terminal**.

3. Jalankan aplikasi dengan mengetikkan:
   ```bash
   python quiz_game.py
   ```
