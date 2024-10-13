print ('------------------------- isi Biodata Anda -------------------------------\n')

nama_anda = input ("Masukan nama anda : ")
kelas_anda = int (input ('Masukan Umur Anda : '))
debbit = int (input ("Masukan Duit Nominal Anda : "))
merek_baju = input ("Masukan baju kalian xl/l/xxl : ")
merek_baju2 = (input ("Masukan sepatu adidas/puma/nike : "))
iniukuran_almameter =input("Masukan Ukuran Almameter Anda Dari 38-46 : ")
print ('------------------------- Inilah Data Dan Harga Yang Harus Anda Selesaikan -------------------------------\n')

if merek_baju == 'xl' : 
    print ("baju tersebut yang anda pilih XL 😎")
elif merek_baju == 'l' :
    print ("Baju Tersebut Yang Anda Pilih L 😎")
elif merek_baju == 'xxl' :
    print ("Baju Tersebut Yang Anda Pilih XXL 😎")
else :
    print ("pililah dengan baik dan benar perhatikanlah 😸😸")   
if merek_baju2 == 'adidas' :
    print ("Harganya Adalah 200rb 👾")
    masuk = debbit - 200000
    print ("Pembayaran", masuk , " Telah Terverivikasi Pembayaran Anda Telah Selesai ✔️")
elif merek_baju2 == 'puma' :
    print ("harganya adalah 300rb 👾")
    masuk = debbit - 300000
    print ("Pembayaran", masuk , " Telah Terverivikasi Pembayaran Anda Telah Selesai ✔️")
elif merek_baju2 == 'nike' :
    print ("harganya adalah 400rb 👾")
    masuk = debbit - 400000
    print ("Pembayaran", masuk , " Telah Terverivikasi Pembayaran Anda Telah Selesai ✔️")
else :
    print ("pililah sepatu yang sesuai dengan harga di atas tersebut 😁😁")

if iniukuran_almameter == '38' :
    print ("anda telah terbaca memilih ukuran 38 Harga Tersebut Adalah 50rb 🤖")
    masuk2 = masuk - 50000
    print ("Pembayaran ",masuk2,"Almameter Telah Berhasil ✔️")
elif iniukuran_almameter == '39' :
    print ("anda telah terbaca memilih ukuran 39 Harga Tersebut Adalah 50rb 🤖")
    masuk2 = masuk - 50000
    print ("Pembayaran ",masuk2,"Almameter Telah Berhasil ✔️")
elif iniukuran_almameter == '40' :
    print ("anda telah terbaca memilih ukuran 40 Harga Tersebut Adalah 50rb 🤖")
    masuk2 = masuk - 50000
    print ("Pembayaran ",masuk2,"Almameter Telah Berhasil ✔️")
elif iniukuran_almameter == '41' :
    print ("anda telah terbaca memilih ukuran 41 Harga Tersebut Adalah 50rb 🤖")
    masuk2 = masuk - 50000
    print ("Pembayaran ",masuk2,"Almameter Telah Berhasil ✔️")
elif iniukuran_almameter == '42' :
    print ("anda telah terbaca memilih ukuran 42 Harga Tersebut Adalah 50rb 🤖")
    masuk2 = masuk - 50000
    print ("Pembayaran ",masuk2,"Almameter Telah Berhasil ✔️")
elif iniukuran_almameter == '43' :
    print ("anda telah terbaca memilih ukuran 43 Harga Tersebut Adalah 50rb 🤖")
    masuk2 = masuk - 50000
    print ("Pembayaran ",masuk2,"Almameter Telah Berhasil ✔️")
elif iniukuran_almameter == '44' :
    print ("anda telah terbaca memilih ukuran 44 Harga Tersebut Adalah 50rb 🤖")
    masuk2 = masuk - 50000
    print ("Pembayaran ",masuk2,"Almameter Telah Berhasil ✔️")
elif iniukuran_almameter == '45' :
    print ("anda telah terbaca memilih ukuran 45 Harga Tersebut Adalah 50rb 🤖")
    masuk2 = masuk - 50000
    print ("Pembayaran ",masuk2,"Almameter Telah Berhasil ✔️")
elif iniukuran_almameter == '46' :
    print ("anda telah terbaca memilih ukuran 46 Harga Tersebut Adalah 50rb 🤖")
    masuk2 = masuk - 50000
    print ("Pembayaran ",masuk2,"Almameter Telah Berhasil ✔️")
else :
    print ("Pilih Yang Benar Almameter Anda 😭😭\n")
    
print ("----------------------------- Data Sudah Terverivikasi ----------------------------------------------\n")

print ("Nama Anda Adalah",nama_anda , 'selamat bergabung di university')
print ("Nama Anda : ",nama_anda)
print ("umur anda adalah : ",kelas_anda)
print ("Anda Memilih Baju : ",merek_baju)
print ("Sepatu Yang Anda Pilih Adalah : ",merek_baju2)
print ("Ukuran Almameter Anda Adalah : ",iniukuran_almameter)
print ("Sisa Saldo Anda Adalah : ",masuk2)

print("---------------------------------------------------------------------------------------------------------s")