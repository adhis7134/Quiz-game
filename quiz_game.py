import os
import sys
import time

# Mengaktifkan mode warna ANSI di Windows terminal
if os.name == 'nt':
    os.system('')

# Warna ANSI untuk visualisasi seperti game
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
MAGENTA = '\033[95m'
BLUE = '\033[94m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'

def bersihkan_layar():
    """Membersihkan tampilan terminal agar tampak seperti layar game baru."""
    os.system('cls' if os.name == 'nt' else 'clear')

def cetak_banner():
    bersihkan_layar()
    banner = rf"""
{CYAN}{BOLD}===================================================================
   ___   _   _  ___  ____    ____     _     __  __  _____ 
  / _ \ | | | ||_ _|/ ___|  / ___|   / \   |  \/  || ____|
 | | | || | | | | | \___ \ | |  _   / _ \  | |\/| ||  _|  
 | |_| || |_| | | |  ___) || |_| | / ___ \ | |  | || |___ 
  \__\_\\ \___/ |___||____/  \____|/_/   \_\|_|  |_||_____|
==================================================================={RESET}
    {YELLOW}🎮 Selamat Datang di Arena Kuis Interaktif Mahasiswa! 🎮{RESET}
"""
    print(banner)

def input_data_mahasiswa():
    """Mengambil input identitas mahasiswa (berdasarkan kode awal)."""
    cetak_banner()
    print(f"{MAGENTA}{BOLD}[ FORM REGISTRASI PESERTA ]{RESET}")
    print(f"{BLUE}Silakan masukkan identitas diri Anda sebelum memulai petualangan:{RESET}\n")

    while True:
        nim = input(f"{BOLD}Masukkan NIM     : {RESET}").strip()
        if nim:
            break
        print(f"{RED}NIM tidak boleh kosong!{RESET}")

    while True:
        nama = input(f"{BOLD}Masukkan Nama    : {RESET}").strip()
        if nama:
            break
        print(f"{RED}Nama tidak boleh kosong!{RESET}")

    jurusan = input(f"{BOLD}Masukkan Jurusan : {RESET}").strip() or "Umum"
    alamat = input(f"{BOLD}Masukkan Alamat  : {RESET}").strip() or "-"

    print(f"\n{GREEN}✔ Data berhasil disimpan! Menyiapkan arena kuis...{RESET}")
    time.sleep(1)

    return {
        "nim": nim,
        "nama": nama,
        "jurusan": jurusan,
        "alamat": alamat
    }

def get_daftar_soal():
    """Daftar soal kuis, opsi, jawaban benar, dan penjelasannya."""
    return [
        {
            "tanya": "Dalam bahasa Python, fungsi apa yang digunakan untuk menampilkan teks ke layar?",
            "opsi": {
                "A": "echo()",
                "B": "print()",
                "C": "console.log()",
                "D": "display()"
            },
            "kunci": "B",
            "poin": 20,
            "penjelasan": "print() adalah fungsi bawaan Python untuk mencetak teks atau variabel ke konsol."
        },
        {
            "tanya": "Manakah tipe data yang digunakan untuk menyimpan kumpulan karakter seperti 'Mahasiswa'?",
            "opsi": {
                "A": "Integer (int)",
                "B": "Boolean (bool)",
                "C": "String (str)",
                "D": "Float (float)"
            },
            "kunci": "C",
            "poin": 20,
            "penjelasan": "String (str) digunakan untuk teks yang diapit tanda petik."
        },
        {
            "tanya": "Berapakah hasil dari ekspresi matematika Python berikut: 10 + 2 * 5?",
            "opsi": {
                "A": "20",
                "B": "60",
                "C": "25",
                "D": "100"
            },
            "kunci": "A",
            "poin": 20,
            "penjelasan": "Operasi perkalian (*) memiliki prioritas lebih tinggi dibanding penjumlahan (+): 2 * 5 = 10, lalu 10 + 10 = 20."
        },
        {
            "tanya": "Simbol apakah yang digunakan untuk membuat komentar 1 baris di kode Python?",
            "opsi": {
                "A": "//",
                "B": "/* */",
                "C": "#",
                "D": "--"
            },
            "kunci": "C",
            "poin": 20,
            "penjelasan": "Tanda pagar (#) digunakan untuk menulis komentar satu baris di Python."
        },
        {
            "tanya": "Jika x = 5 dan y = '5', apakah hasil dari perintah: type(x) == type(y)?",
            "opsi": {
                "A": "True",
                "B": "False",
                "C": "Error",
                "D": "None"
            },
            "kunci": "B",
            "poin": 20,
            "penjelasan": "x bertipe 'int' sedangkan y bertipe 'str', sehingga tipenya berbeda (False)."
        }
    ]

def gunakan_bantuan_5050(soal):
    """Menghilangkan 2 jawaban salah untuk membantu pemain."""
    kunci = soal["kunci"]
    salah = [opt for opt in soal["opsi"].keys() if opt != kunci]
    import random
    hilangkan = random.sample(salah, 2)
    opsi_baru = {}
    for k, v in soal["opsi"].items():
        if k in hilangkan:
            opsi_baru[k] = f"{RED}[TERELEMINASI]{RESET}"
        else:
            opsi_baru[k] = v
    return opsi_baru

def jalankan_game(mahasiswa):
    daftar_soal = get_daftar_soal()
    skor = 0
    nyawa = 3
    combo = 0
    max_combo = 0
    bantuan_tersedia = True
    jawaban_benar_count = 0

    total_soal = len(daftar_soal)

    for nomor, soal in enumerate(daftar_soal, start=1):
        bersihkan_layar()
        # Baris status game (HUD)
        hati = "❤️ " * nyawa + "🖤 " * (3 - nyawa)
        print(f"{CYAN}{'='*65}{RESET}")
        print(f"👤 {BOLD}{mahasiswa['nama']}{RESET} | 🎯 Soal: {BOLD}{nomor}/{total_soal}{RESET} | 🏆 Skor: {YELLOW}{skor}{RESET}")
        print(f"Nyawa: {hati} | Combo: {MAGENTA}{combo}x 🔥{RESET}")
        if bantuan_tersedia:
            print(f"💡 Bantuan Khusus: {GREEN}[Ketik '50' untuk Bantuan 50:50 (1x pakai)]{RESET}")
        else:
            print(f"💡 Bantuan Khusus: {RED}[Bantuan 50:50 Sudah Digunakan]{RESET}")
        print(f"{CYAN}{'='*65}{RESET}\n")

        print(f"{BOLD}Pertanyaan {nomor}:{RESET}")
        print(f"{BLUE}{soal['tanya']}{RESET}\n")

        opsi_tampil = soal["opsi"]
        opsi_aktif = opsi_tampil.copy()

        while True:
            for huruf, teks in opsi_aktif.items():
                print(f"  {BOLD}[{huruf}]{RESET} {teks}")

            print()
            pilihan = input(f"{YELLOW}Jawab (A/B/C/D) >> {RESET}").strip().upper()

            if pilihan == "50":
                if bantuan_tersedia:
                    bantuan_tersedia = False
                    opsi_aktif = gunakan_bantuan_5050(soal)
                    print(f"\n{GREEN}✨ Bantuan 50:50 diaktifkan! 2 opsi salah telah dihapus.{RESET}\n")
                    continue
                else:
                    print(f"\n{RED}Bantuan 50:50 sudah pernah digunakan! Silakan jawab A/B/C/D.{RESET}\n")
                    continue

            if pilihan in ["A", "B", "C", "D"]:
                if "[TERELEMINASI]" in opsi_aktif.get(pilihan, ""):
                    print(f"\n{RED}Pilihan {pilihan} sudah tereliminasi! Pilih jawaban lain.{RESET}\n")
                    continue
                break
            else:
                print(f"{RED}Pilihan tidak valid! Masukkan A, B, C, atau D.{RESET}\n")

        # Cek Jawaban
        if pilihan == soal["kunci"]:
            combo += 1
            if combo > max_combo:
                max_combo = combo
            bonus_combo = (combo - 1) * 5
            poin_didapat = soal["poin"] + bonus_combo
            skor += poin_didapat
            jawaban_benar_count += 1

            print(f"\n{GREEN}{BOLD}🎉 TEPAT SEKALI! +{poin_didapat} Poin!{RESET}")
            if combo > 1:
                print(f"{MAGENTA}🔥 COMBO STREAK x{combo}! Bonus +{bonus_combo} poin!{RESET}")
        else:
            combo = 0
            nyawa -= 1
            print(f"\n{RED}{BOLD}💥 YAH SALAH! Jawaban yang benar adalah [{soal['kunci']}].{RESET}")
            print(f"{RED}Nyawa Anda berkurang 1!{RESET}")

        print(f"{BLUE}ℹ️  Info: {soal['penjelasan']}{RESET}")
        print(f"\n{CYAN}Tekan ENTER untuk lanjut...{RESET}")
        input()

        # Cek Game Over
        if nyawa <= 0:
            bersihkan_layar()
            print(f"""
{RED}{BOLD}
===================================================================
                       💀 GAME OVER! 💀
                   Nyawa Anda telah habis!
===================================================================
{RESET}""")
            print(f"Jangan berkecil hati, {mahasiswa['nama']}! Latihan lagi ya!\n")
            time.sleep(2)
            break

    # Rangkuman Hasil
    tampilkan_raport_akhir(mahasiswa, skor, jawaban_benar_count, total_soal, max_combo, nyawa > 0)

def tampilkan_raport_akhir(mhs, skor, benar, total, max_combo, tamat):
    bersihkan_layar()
    
    # Skala Nilai 0 - 100
    nilai_akhir = int((benar / total) * 100)
    
    if nilai_akhir >= 85:
        grade = "A (Cumlaude / Master)"
        pesan = "🌟 LUAR BIASA! Kemampuan Anda sangat impresif!"
        warna_grade = GREEN
    elif nilai_akhir >= 70:
        grade = "B (Hebat / Unggul)"
        pesan = "👏 Bagus sekali! Sedikit lagi menuju sempurna!"
        warna_grade = CYAN
    elif nilai_akhir >= 55:
        grade = "C (Cukup)"
        pesan = "👍 Lumayan, pelajari materi lagi agar makin mantap!"
        warna_grade = YELLOW
    else:
        grade = "D (Perlu Remedial)"
        pesan = "💪 Jangan menyerah, coba lagi untuk skor lebih tinggi!"
        warna_grade = RED

    status_tamat = "BERHASIL TAMAT 🏆" if tamat else "GUGUR DI TENGAH JALAN ❌"

    laporan = f"""
{CYAN}===================================================================
                 🎓 KARTU HASIL UJIAN GAME QUIZ 🎓
==================================================================={RESET}
  {BOLD}Data Mahasiswa:{RESET}
  • NIM          : {mhs['nim']}
  • Nama         : {mhs['nama']}
  • Jurusan      : {mhs['jurusan']}
  • Alamat       : {mhs['alamat']}

{CYAN}-------------------------------------------------------------------{RESET}
  {BOLD}Statistik Permainan:{RESET}
  • Status Game  : {BOLD}{status_tamat}{RESET}
  • Soal Benar   : {benar} dari {total} soal
  • Max Combo    : {max_combo}x 🔥
  • Skor Game    : {YELLOW}{BOLD}{skor} PTS{RESET}
  • Nilai Ujian  : {warna_grade}{BOLD}{nilai_akhir} / 100{RESET}
  • Peringkat    : {warna_grade}{BOLD}{grade}{RESET}

  {BOLD}Catatan:{RESET}
  {pesan}
{CYAN}==================================================================={RESET}
"""
    print(laporan)

    # Simpan ke file riwayat
    simpan_riwayat(mhs, skor, nilai_akhir, grade)

def simpan_riwayat(mhs, skor, nilai, grade):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        path_file = os.path.join(script_dir, "riwayat_quiz.txt")
        with open(path_file, "a", encoding="utf-8") as f:
            f.write(f"NIM: {mhs['nim']} | Nama: {mhs['nama']} | Jurusan: {mhs['jurusan']} | Nilai: {nilai} | Skor: {skor} | Grade: {grade}\n")
        print(f"{GREEN}📄 Hasil ujian berhasil dicatat ke file 'riwayat_quiz.txt'!{RESET}\n")
    except Exception as e:
        pass

def main():
    while True:
        data_mhs = input_data_mahasiswa()
        jalankan_game(data_mhs)

        pilihan = input(f"{YELLOW}Apakah ingin main lagi? (y/n): {RESET}").strip().lower()
        if pilihan != 'y':
            print(f"\n{CYAN}Terima kasih telah bermain, sukses selalu untuk studinya! 👋{RESET}\n")
            break

if __name__ == "__main__":
    main()
