#input
nama_produk = input("Masukkan nama produk: ")
harga_beli = float(input("Masukkan harga produk: "))
harga_jual = float(input("Masukkan harga jual produk: "))   
jumlah_terjual = int(input("Masukkan jumlah produk yang terjual: "))

#kalkulasi
total_omzet = harga_jual * jumlah_terjual
total_keuntungan = total_omzet - (harga_beli * jumlah_terjual)
persentase_keuntungan = (total_keuntungan / (harga_beli * jumlah_terjual)) * 100

#if else
if persentase_keuntungan < 0:
    status = "Rugi"
elif persentase_keuntungan < 10:
    status = "Untung Kecil"
elif persentase_keuntungan < 20:
    status = "Untung Sedang"
else:
    status = "Untung Besar"

#output
lebar = 50
print("=" * lebar)
print("Laporan Penjualan Produk".center(lebar))
print("Oleh: Muhammad Hasyim Noor Rizki".center(lebar))
print("=" * lebar)
print