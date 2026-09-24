daftar_transaksi = []#dictionary

#jumlah produk yang mau di itung
jumlah_produk = int(input("mau itung berapa produk: "))

grand_total_omzet = 0 
grand_total_keuntungan = 0


#Loop
for i in range(jumlah_produk + 1):
    print(f"\nProduk ke-{i}")

    #Input
    nama_produk = input("Nama Produk: ")
    harga_beli = float(input("Harga Beli / HPP: RP."))
    harga_jual = float(input("Harga Jual: RP."))
    jumlah_terjual = int(input("Jumlah Terjual: "))

    #Aritmatika
    total_omzet = harga_jual * jumlah_terjual
    total_keuntungan_kotor = (harga_jual - harga_beli) * jumlah_terjual
    persentase_margin = (total_keuntungan_kotor / total_omzet) * 100

    #Diskon
    if jumlah_terjual >= 100:
        persen_diskon = 15
    elif jumlah_terjual >= 50:
        persen_diskon = 10
    elif jumlah_terjual >= 20:
        persen_diskon = 5
    else:   
        persen_diskon = 0

    nilai_diskon = total_omzet  * (persen_diskon / 100)
    total_setelah_diskon = total_omzet - nilai_diskon

    grand_total_omzet += total_setelah_diskon
    grand_total_keuntungan += total_keuntungan_kotor

    daftar_transaksi.append({
        "nama": nama_produk,
        "omzet": total_omzet,
        "keuntungan": total_keuntungan_kotor,
        "diskon": nilai_diskon,
        "total_setelah_diskon": total_setelah_diskon
    })

    print(f"Omzet: Rp {total_omzet:,.2f} | Margin: {persentase_margin:.2f}% | "
          f"Diskon: {persen_diskon}% | Total Bersih: Rp {total_setelah_diskon:,.2f}")

#rekap dari list 
print("\n=== REKAP SEMUA PRODUK - Muhammad Hasyim Noor Rizki ===")
for t in daftar_transaksi:
    print(f"{t['nama']:<15} Rp {t['total_setelah_diskon']:,.2f}")
 
grand_total = sum(t["total_setelah_diskon"] for t in daftar_transaksi)
grand_untung = sum(t["keuntungan"] for t in daftar_transaksi)
print(f"\nGrand Total Omzet Bersih : Rp {grand_total:,.2f}")
print(f"Grand Total Keuntungan   : Rp {grand_untung:,.2f}")
