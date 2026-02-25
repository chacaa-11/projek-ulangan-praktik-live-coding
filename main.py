"""Program sederhana untuk menampilkan daftar destinasi wisata.
Setiap destinasi memiliki nama, lokasi, tanggal kedatangan, dan budget.
"""

def main():
    destinasi = []

    def tampilkan_daftar():
        if not destinasi:
            print("Tidak ada destinasi yang tercatat.")
            return
        print("\nDaftar Destinasi Wisata:\n")
        for d in destinasi:
            print(f"Nama    : {d['nama']}")
            print(f"Lokasi  : {d['lokasi']}")
            print(f"Tanggal : {d['tanggal']}")
            status_str = "[✓] sudah" if d.get('visited') else "[ ] belum"
            print(f"Status  : {status_str} dikunjungi")
            print(f"Budget  : Rp {d['budget']:,}")
            print("-" * 30)

    def tambah_destinasi():
        print("Masukkan detail destinasi wisata. Tekan enter pada nama untuk kembali ke menu.")
        while True:
            nama = input("Nama destinasi: ").strip()
            if not nama:
                break
            lokasi = input("Lokasi: ").strip()
            tanggal = input("Tanggal kedatangan (YYYY-MM-DD): ").strip()
            status = input("Sudah dikunjungi? (y/n): ").strip().lower()
            visited = status == "y"
            budget_str = input("Budget (angka, rupiah): ").strip()
            try:
                budget = int(budget_str.replace(",", ""))
            except ValueError:
                print("Budget tidak valid, di-set ke 0.")
                budget = 0
            destinasi.append({
                "nama": nama,
                "lokasi": lokasi,
                "tanggal": tanggal,
                "budget": budget,
                "visited": visited,
            })
            print("Destinasi ditambahkan.\n")
            lanjut = input("Tambah lagi? (y/n): ").strip().lower()
            if lanjut != "y":
                break

    # daftar rekomendasi statis (sederhana)
    rekomendasi = [
        "Taman Nasional Komodo - Nusa Tenggara Timur",
        "Kawah Putih - Jawa Barat",
        "Danau Toba - Sumatera Utara",
        "Candi Borobudur - Jawa Tengah",
        "Pulau Weh - Aceh",
        "Gunung Bromo - Jawa Timur",
        "Derawan - Kalimantan Timur",
        "Taman Mini Indonesia Indah - DKI Jakarta",
        "Pantai Padang Padang - Bali",
        "Lembang Ice Cream Park - Jawa Barat",
        "Pantai Kuta - Bali",
        "Kepulauan Seribu - DKI Jakarta",
        "Air Terjun Tumpak Sewu - Jawa Timur",
        "Pulau Belitung - Bangka Belitung",
        "Bukit Tinggi dan Ngarai Sianok - Sumatera Barat",
        "Pulau Karimunjawa - Jawa Tengah",
        "Taman Laut Bunaken - Sulawesi Utara",
        "Bali Safari & Marine Park - Bali",
        "Jembatan Barelang - Kepulauan Riau",
    ]

    def lihat_rekomendasi():
        print("\nRekomendasi Destinasi Wisata:\n")
        for r in rekomendasi:
            print(f"- {r}")
        print()

    while True:
        print("\nMenu:")
        print("1. Tambah destinasi")
        print("2. Lihat semua destinasi")
        print("3. Lihat rekomendasi")
        print("4. Keluar")
        pilihan = input("Pilih opsi (1/2/3/4): ").strip()
        if pilihan == "1":
            tambah_destinasi()
        elif pilihan == "2":
            tampilkan_daftar()
        elif pilihan == "3":
            lihat_rekomendasi()
        elif pilihan == "4":
            print("Keluar. Sampai jumpa!")
            break
        else:
            print("Opsi tidak dikenal, coba lagi.")


if __name__ == "__main__":
    main()
