BOBOT_TUGAS = 0.30
BOBOT_UTS = 0.30
BOBOT_UAS = 0.40


def hitung_nilai_akhir(tugas, uts, uas):
    return tugas * BOBOT_TUGAS + uts * BOBOT_UTS + uas * BOBOT_UAS


def tentukan_nilai_huruf(nilai_akhir):
    if nilai_akhir >= 85:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 55:
        return "C"
    elif nilai_akhir >= 40:
        return "D"
    return "E"


def apakah_lulus(nilai_huruf):
    return nilai_huruf in ("A", "B", "C")


def tampilkan_header():
    print(f"{'Nama':<10}{'Nilai Akhir':>12}{'Huruf':>8}  Keterangan")
    print("-" * 45)


def proses_mahasiswa(nama, tugas, uts, uas):
    akhir = hitung_nilai_akhir(tugas, uts, uas)
    huruf = tentukan_nilai_huruf(akhir)
    keterangan = "Lulus" if apakah_lulus(huruf) else "Tidak Lulus"
    print(f"{nama:<10}{akhir:>12.2f}{huruf:>8}  {keterangan}")
    return akhir


def tampilkan_ringkasan(total_nilai, jumlah_lulus, jumlah_mahasiswa):
    print("-" * 45)
    print(f"Rata-rata nilai akhir kelas : {total_nilai / jumlah_mahasiswa:.2f}")
    print(f"Jumlah mahasiswa yang lulus : {jumlah_lulus}")


def main():
    total_nilai = 0
    jumlah_lulus = 0

    tampilkan_header()

    akhir = proses_mahasiswa("satria", 80, 70, 90)
    total_nilai += akhir
    if apakah_lulus(tentukan_nilai_huruf(akhir)):
        jumlah_lulus += 1

    akhir = proses_mahasiswa("suarnata", 90, 85, 88)
    total_nilai += akhir
    if apakah_lulus(tentukan_nilai_huruf(akhir)):
        jumlah_lulus += 1

    akhir = proses_mahasiswa("alit", 60, 45, 50)
    total_nilai += akhir
    if apakah_lulus(tentukan_nilai_huruf(akhir)):
        jumlah_lulus += 1

    akhir = proses_mahasiswa("dewi", 75, 80, 65)
    total_nilai += akhir
    if apakah_lulus(tentukan_nilai_huruf(akhir)):
        jumlah_lulus += 1

    akhir = proses_mahasiswa("adi", 30, 40, 35)
    total_nilai += akhir
    if apakah_lulus(tentukan_nilai_huruf(akhir)):
        jumlah_lulus += 1

    tampilkan_ringkasan(total_nilai, jumlah_lulus, 5)


if __name__ == "__main__":
    main()
