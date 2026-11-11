def hitung_biaya_berat(berat):
    if berat <= 2:
        return 10000
    else:
        return 10000 + (berat - 2) * 4000

def hitung_biaya_jarak(jarak):
    if jarak <= 20:
        return 0
    else:
        return 5000

def hitung_potongan(total_biaya, status_anggota):
    if status_anggota.lower() == "ya":
        return int(total_biaya * 0.10)
    return 0

def cetak_struk_dan_hitung_total(daftar_pesanan):
    total_pendapatan_hari_ini = 0
    
    print("=" * 60)
    print(f"{'STRUK PENGIRIMAN TOKO DARING':^60}")
    print("=" * 60)
    
    for pesanan in daftar_pesanan:
        nama = pesanan["nama"]
        berat = pesanan["berat"]
        jarak = pesanan["jarak"]
        anggota = pesanan["anggota"]
        
        
        b_berat = hitung_biaya_berat(berat)
        b_jarak = hitung_biaya_jarak(jarak)
        subtotal = b_berat + b_jarak
        potongan = hitung_potongan(subtotal, anggota)
        ongkir_akhir = subtotal - potongan
        
        total_pendapatan_hari_ini += ongkir_akhir
        
        
        print(f"Nama Pelanggan : {nama}")
        print(f"Detail Paket   : {berat} kg | {jarak} km | Anggota: {anggota}")
        print(f"Biaya Berat    : Rp{b_berat:,}")
        print(f"Biaya Jarak    : Rp{b_jarak:,}")
        if potongan > 0:
            print(f"Potongan (10%) : -Rp{potongan:,}")
        print(f"Ongkos Kirim   : Rp{ongkir_akhir:,}")
        print("-" * 60)
        
    print(f"TOTAL PENDAPATAN ONGKOS KIRIM HARI INI : Rp{total_pendapatan_hari_ini:,}")
    print("=" * 60)

data_pesanan = [
    {"nama": "Rina",  "berat": 1, "jarak": 10, "anggota": "Bukan"},
    {"nama": "Sari",  "berat": 5, "jarak": 25, "anggota": "Bukan"},
    {"nama": "Tono",  "berat": 5, "jarak": 25, "anggota": "Ya"},
    {"nama": "Umar",  "berat": 2, "jarak": 30, "anggota": "Ya"},
    {"nama": "Vina",  "berat": 8, "jarak": 15, "anggota": "Bukan"}
]

if __name__ == "__main__":
    cetak_struk_dan_hitung_total(data_pesanan)