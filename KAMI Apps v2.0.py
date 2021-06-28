"""
{ CORETAN AJA YA :)
   "Key0": ["Value00",
   "Value01",
   "Value02",
   "Value03",
   Value04,
   "Value05",
   ["Value060","Value061"],
   ["Value070","Value071",Value072,Value073,Value074,[Value0750,Value0751]],
   "Value08"]
}

"""
dikte = {
   "andhika12": ["Andhika12@",
   "andhika@gmail.com",
   "Mas Andhika",
   "Pria",
   30,
   "Petani",
   ["Nyeduh Kopi","Minum Kopi"],
   ["Jl. Jakarta No. 69","Pamanukan",12,13,66666,[69,96]],
   "086666666666"]
}   

cupang = {
   'Blue Rim': 12,
   'Black Galaxy': 13,
   'Halfmoon': 29
   }

while True:
   try:
      print("="*60)
      print("\t          WELCOME TO KAMI APPS\n")
      print("\t         -Kevin Aldo Ming Ibun-\n")
      print("PILIHAN :")
      print("1. Register")
      print("2. Login")
      print("3. Exit")
      print("\t\t\t\t\t      Mini Apps v2.0")
      print("="*60)
      login = int(input("Silahkan Masukkan Pilihan Menu (1-3) : "))
# NOMOR 1
      if login == 1:
         print("1. Register Menu")
   # ID
         while True:
            daftarID = input("Silahkan Masukkan ID : ")
            kotakid = []
            if daftarID.isalnum() != True:
               print("Format ID Salah !")
               continue

            for i in daftarID:
               kotakid.append(i)

            # print(kotakid)
            hurufid = 0
            angkaid = 0

            for x1 in kotakid:
               apakah1id = x1.isalpha()
               if apakah1id == True:
                  hurufid += 1
            # print(hurufid)

            for x2 in kotakid:
               apakah2id = x2.isdigit()
               if apakah2id == True:
                  angkaid += 1
            # print(angkaid)

            if hurufid < 1:
               print("Harus ada huruf ya bos :)")
               continue
            elif angkaid < 1:
               print("Harus ada angka ya bos :)")
               continue
            # else:
            #     print("User ID bisa digunakan")

            panjangid = len(daftarID)
            if 6 <= panjangid <= 20:
               if daftarID in dikte:
                  print("ID sudah terdaftar !")
                  continue
               else:
                  break
            else:
               print("Jumlah Karakter ID min 6 char, max 20 char")
               continue
   # Password
         while True:
            daftarPass = input("Silahkan Masukkan Password : ")
            kotakpass = []
            for i in daftarPass:
               kotakpass.append(i)

            # print(kotakpass)
            gede = 0
            kecil = 0
            digit = 0
            spesial = 0

            for x1 in kotakpass:
               apakah1pass = x1.isupper()
               if apakah1pass == True:
                  gede += 1
            # print(gede)

            for x2 in kotakpass:
               apakah2pass = x2.islower()
               if apakah2pass == True:
                  kecil += 1
            # print(kecil)

            for x3 in kotakpass:
               apakah3pass = x3.isdigit()
               if apakah3pass == True:
                  digit += 1
            # print(digit)

            for x4 in kotakpass:
               apakah3pass = x4.isalnum()
               if apakah3pass != True:
                  spesial += 1
            # print(spesial) # spasi diitung ya bos

            if gede < 1:
               print("Harus ada huruf kapital ya bos :)")
               continue
            elif kecil < 1:
               print("Harus ada huruf kecil ya bos :)")
               continue
            elif digit < 1: 
               print("Harus ada angka ya bos :)")
               continue
            elif spesial < 1:
               print("Harus ada karakter spesial ya bos :)")
               continue
            else:
               break
   # Email
         kesempatan = 1
         bataskesempatan = 3
         while kesempatan <= bataskesempatan:
            daftarEmail = input("Silahkan Masukkan Email : ")
            kotak = []
            balik = []
            depan = []
            hosting = []
            ekstensi = []
            bantuan1 = []
            diktekosong = []

            if kesempatan < bataskesempatan:
               for i in dikte.values():
                  diktekosong += i

               if daftarEmail in diktekosong:
                  print("Email Sudah Terdaftar !")
                  print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                  kesempatan += 1
                  continue

               # print(daftarEmail)

               if "@" not in daftarEmail:
                  print("Email tidak valid, Format Email yang masukan salah!")
                  print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                  kesempatan += 1
                  continue
               elif daftarEmail.count("@") >1:
                  print("Email tidak valid, Jumlah @ lebih dari 1")
                  print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                  kesempatan += 1
                  continue
               elif "." not in daftarEmail:
                  print("Email tidak valid, Format Email yang masukan salah!")
                  print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                  kesempatan += 1
                  continue
               else:
                  kotak.extend(daftarEmail)
                  # print(kotak) # di pencarin masing masing huruf
                  balik.extend(daftarEmail)
                  balik.reverse()
                  # print(balik) # di reverse huruf2nya

                  for a in kotak:
                     depan.append(a)
                     if a == "@": # diambil nama usernya
                        break

                  for b1 in balik:
                     bantuan1.append(b1)
                     if b1 == "@": # diambil sisa dari nama user (nama hosting, ekstensi)
                        break

                  bantuan1.reverse()
                  # print(bantuan1) # ini sisanya (nama hosting, ekstensi)

                  bantuan2 = bantuan1.copy() # perlu bantuan2 biar dapetin ekstensi
                  bantuan2.reverse() # dibalik bantuan2 nya buat hapus format ekstensinya

                  for d in bantuan1: # ambil hosting dari bantuan1
                     hosting.append(d)
                     bantuan2.pop() # format hosting belakang dari bantuan2 dihapus
                     if d == ".":
                        break

                  # print(bantuan2) # sisanya ekstensinya
                  bantuan2.append(".") # ditambahin (.) ekstensinya
                  bantuan2.reverse() # direverse biar jadi .co.id

                  depan.pop() # dihapus si "@" nya dari nama user
                  gabungdepan = "".join(depan) # gabungin biar dapet format nama usernya
                  jumlahgabungdepan = len(gabungdepan) # buat handling depannya
                  # print(gabungdepan)

                  hosting.remove("@") # hostingnya dihapus "@" nya
                  hosting.remove(".") # hostingnya dihapus "." nya
                  gabunghosting = "".join(hosting) # biar dapet hostingnya
                  # print(gabunghosting)
               
                  gabungekstensi = "".join(bantuan2) # ekstensinya yang udah ditambahin (.) digabungin

                  jumlahhosting = len(gabunghosting) # hitung jumlah hostingnya
                  jumlahekstensi = gabungekstensi.count(".") # ini dihitung jumlah (.)nya dari ekstensi
                  # print(jumlahekstensi) # ngecek jumlah ekstensinya
                  # print(gabungekstensi) # cek ekstensinya gimana
                  # print(bantuan2)
                  bantuan3 = gabungekstensi.split(".") # butuh bantuan ketiga buat ekstensi yang pertama kalo ada 2
                  # print(bantuan3) # habis displit (".")nya, di cek ada apa aja
                  bantuan3.remove("") # dibuang tanda ""nya
                  # print(bantuan3) # sisa co id dalam bentuk list

                  bantuan3.reverse() # bantuan 3 nya di reverse [id, co]

                  if jumlahekstensi == 2: # kalo jumlah (.) ekstensinya 2
                     dot1 = bantuan3.pop() # buat dapet ekstensi 1
                     dot2 = bantuan3.pop() # buat dapet ekstensi 2
                  elif jumlahekstensi == 1: # kalo jumlah (.) ekstensinya 1
                     dot1 = bantuan3.pop() # buat dapet ekstensi 1
                     dot2 = "" # dianggap gaada
                  else:
                     dot1 = bantuan3.pop() # buat dapet ekstensi 1
                     dot2 = bantuan3.pop() # buat dapet ekstensi 2
                     dot3 = "" # dianggap gaada

                  # print(dot1)
                  # print(dot2)
                  kotakdot1 = []
                  kotakdot2 = []
                  dot1angka = 0
                  dot2angka = 0

                  for x in dot1:
                     kotakdot1.append(x)
                  for y in dot2:
                     kotakdot2.append(y)
                  
                  for x1 in dot1:
                     dot1angka = x1.isdigit()
                     if dot1angka == True:
                        dot1angka += 1

                  for x2 in dot2:
                     dot2angka = x2.isdigit()
                     if dot2angka == True:
                        dot2angka += 1

                  if gabungdepan.startswith("_"):
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "!" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "#" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "$" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "%" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "^" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "&" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "*" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "(" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif ")" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif ":" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif ";" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "," in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "<" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif ">" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "?" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "/" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "[" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "]" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "{" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "}" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "|" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "\\" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "=" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "+" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "~" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "`" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "\"" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "\'" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif " " in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif jumlahgabungdepan < 1:
                     print("Email tidak valid, Format nama user yang anda masukkan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif gabunghosting.isalnum() != True:
                     print("Email tidak valid, Format hosting yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif gabungekstensi.isdigit() == True:
                     print("Email tidak valid, Format ekstensi yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif jumlahekstensi > 2:
                     print("Email tidak valid, Jumlah ekstensi yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif dot1angka > 0:
                     print("Email tidak valid, Format Ekstensi yang anda masukkan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif dot2angka > 0:
                     print("Email tidak valid, Format Ekstensi yang anda masukkan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif len(dot1) > 5:
                     print("Email tidak valid, Jumlah Ekstensi maksimal 5 karakter")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif len(dot2) > 5:
                     print("Email tidak valid, Jumlah Ekstensi maksimal 5 karakter")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue
                  elif "_" in gabungdepan:
                     break
                  elif "." in gabungdepan:
                     break
                  elif gabungdepan.isalnum() == True:
                     break
                  elif gabunghosting.isalnum() == True:
                     break
                  elif gabungekstensi.startswith("."):
                     break
                  else:
                     print("Email tidak valid, Format ekstensi yang anda masukan salah!")
                     print("Kesempatan Hanya 3x, Percobaan ke : ", kesempatan)
                     kesempatan += 1
                     continue

            if kesempatan == bataskesempatan:
               for i in dikte.values():
                  diktekosong += i

               if daftarEmail in diktekosong:
                  print("Email Sudah Terdaftar !")
                  print("Kesempatan Input Anda Habis!")
                  kesempatan += 1
                  quit()

               # print(daftarEmail)

               if "@" not in daftarEmail:
                  print("Email tidak valid, Format Email yang masukan salah!")
                  print("Kesempatan Input Anda Habis!")
                  kesempatan += 1
                  quit()
               elif daftarEmail.count("@") >1:
                  print("Email tidak valid, Jumlah @ lebih dari 1")
                  print("Kesempatan Input Anda Habis!")
                  kesempatan += 1
                  quit()
               elif "." not in daftarEmail:
                  print("Email tidak valid, Format Email yang masukan salah!")
                  print("Kesempatan Input Anda Habis!")
                  kesempatan += 1
                  quit()
               else:
                  kotak.extend(daftarEmail)
                  # print(kotak) # di pencarin masing masing huruf
                  balik.extend(daftarEmail)
                  balik.reverse()
                  # print(balik) # di reverse huruf2nya

                  for a in kotak:
                     depan.append(a)
                     if a == "@": # diambil nama usernya
                        break

                  for b1 in balik:
                     bantuan1.append(b1)
                     if b1 == "@": # diambil sisa dari nama user (nama hosting, ekstensi)
                        break

                  bantuan1.reverse()
                  # print(bantuan1) # ini sisanya (nama hosting, ekstensi)

                  bantuan2 = bantuan1.copy() # perlu bantuan2 biar dapetin ekstensi
                  bantuan2.reverse() # dibalik bantuan2 nya buat hapus format ekstensinya

                  for d in bantuan1: # ambil hosting dari bantuan1
                     hosting.append(d)
                     bantuan2.pop() # format hosting belakang dari bantuan2 dihapus
                     if d == ".":
                        break

                  # print(bantuan2) # sisanya ekstensinya
                  bantuan2.append(".") # ditambahin (.) ekstensinya
                  bantuan2.reverse() # direverse biar jadi .co.id

                  depan.pop() # dihapus si "@" nya dari nama user
                  gabungdepan = "".join(depan) # gabungin biar dapet format nama usernya
                  jumlahgabungdepan = len(gabungdepan) # buat handling depannya
                  # print(gabungdepan)

                  hosting.remove("@") # hostingnya dihapus "@" nya
                  hosting.remove(".") # hostingnya dihapus "." nya
                  gabunghosting = "".join(hosting) # biar dapet hostingnya
                  # print(gabunghosting)
               
                  gabungekstensi = "".join(bantuan2) # ekstensinya yang udah ditambahin (.) digabungin

                  jumlahhosting = len(gabunghosting) # hitung jumlah hostingnya
                  jumlahekstensi = gabungekstensi.count(".") # ini dihitung jumlah (.)nya dari ekstensi
                  # print(jumlahekstensi) # ngecek jumlah ekstensinya
                  # print(gabungekstensi) # cek ekstensinya gimana
                  # print(bantuan2)
                  bantuan3 = gabungekstensi.split(".") # butuh bantuan ketiga buat ekstensi yang pertama kalo ada 2
                  # print(bantuan3) # habis displit (".")nya, di cek ada apa aja
                  bantuan3.remove("") # dibuang tanda ""nya
                  # print(bantuan3) # sisa co id dalam bentuk list

                  bantuan3.reverse() # bantuan 3 nya di reverse [id, co]

                  if jumlahekstensi == 2: # kalo jumlah (.) ekstensinya 2
                     dot1 = bantuan3.pop() # buat dapet ekstensi 1
                     dot2 = bantuan3.pop() # buat dapet ekstensi 2
                  elif jumlahekstensi == 1: # kalo jumlah (.) ekstensinya 1
                     dot1 = bantuan3.pop() # buat dapet ekstensi 1
                     dot2 = "" # dianggap gaada
                  else:
                     dot1 = bantuan3.pop() # buat dapet ekstensi 1
                     dot2 = bantuan3.pop() # buat dapet ekstensi 2
                     dot3 = "" # dianggap gaada

                  # print(dot1)
                  # print(dot2)
                  kotakdot1 = []
                  kotakdot2 = []
                  dot1angka = 0
                  dot2angka = 0

                  for x in dot1:
                     kotakdot1.append(x)
                  for y in dot2:
                     kotakdot2.append(y)
                  
                  for x1 in dot1:
                     dot1angka = x1.isdigit()
                     if dot1angka == True:
                        dot1angka += 1

                  for x2 in dot2:
                     dot2angka = x2.isdigit()
                     if dot2angka == True:
                        dot2angka += 1

                  if gabungdepan.startswith("_"):
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "!" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "#" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "$" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "%" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "^" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "&" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "*" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "(" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif ")" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif ":" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif ";" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "," in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "<" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif ">" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "?" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "/" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "[" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "]" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "{" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "}" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "|" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "\\" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "=" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "+" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "~" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "`" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "\"" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "\'" in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif " " in gabungdepan:
                     print("Email tidak valid, Format nama user yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif jumlahgabungdepan < 1:
                     print("Email tidak valid, Format nama user yang anda masukkan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif gabunghosting.isalnum() != True:
                     print("Email tidak valid, Format hosting yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif gabungekstensi.isdigit() == True:
                     print("Email tidak valid, Format ekstensi yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif jumlahekstensi > 2:
                     print("Email tidak valid, Jumlah ekstensi yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif dot1angka > 0:
                     print("Email tidak valid, Format Ekstensi yang anda masukkan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif dot2angka > 0:
                     print("Email tidak valid, Format Ekstensi yang anda masukkan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif len(dot1) > 5:
                     print("Email tidak valid, Jumlah Ekstensi maksimal 5 karakter")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif len(dot2) > 5:
                     print("Email tidak valid, Jumlah Ekstensi maksimal 5 karakter")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
                  elif "_" in gabungdepan:
                     break
                  elif "." in gabungdepan:
                     break
                  elif gabungdepan.isalnum() == True:
                     break
                  elif gabunghosting.isalnum() == True:
                     break
                  elif gabungekstensi.startswith("."):
                     break
                  else:
                     print("Email tidak valid, Format ekstensi yang anda masukan salah!")
                     print("Kesempatan Input Anda Habis!")
                     kesempatan += 1
                     quit()
   # Nama
         while True:
            daftarNama = input("Silahkan Masukkan Nama Anda : ")
            masuknama = daftarNama.lower()
            masuknama1 = masuknama.replace(" ","")
            bukanhuruf = 0

            for f2 in masuknama1:
               apakah1bukan = f2.isalpha()
               if apakah1bukan == False:
                     bukanhuruf += 1

            if bukanhuruf > 0:
               print("Format Nama yang anda Masukkan Salah !!")
               continue
            else:
               break
   # Gender
         while True:
            daftarGender = input("Silahkan Masukkan Gender Anda (Pria / Wanita) : ")
            masukgender = daftarGender.lower()
            if masukgender == "pria":
               break
            elif masukgender == "wanita":
               break
            else:
               print("Gender yang anda masukkan tidak dikenal !")
               continue
   # Usia
         while True:
            try:
               daftarUsia = input("Silahkan Masukkan Usia Anda : ")
               usia = int(daftarUsia)
               if usia < 17:
                  print("Masih bocah gaboleh jadi member lu !")
                  continue
               elif usia > 80:
                  print("Udah ketuaan lu gaboleh jadi member !")
                  continue
               else:
                  break
            except:
               print("Input usia hanya menerima angka bilangan bulat !")
               continue
   # Pekerjaan
         while True:
            daftarPekerjaan = input("Silahkan Masukkan Pekerjaan Anda : ")
            masukpekerjaan = daftarPekerjaan.lower()
            masukpekerjaan1 = masukpekerjaan.replace(" ","")
            bukanhuruf1 = 0

            for f3 in masukpekerjaan1:
               apakah2bukan = f3.isalpha()
               if apakah2bukan == False:
                  bukanhuruf1 += 1

            if bukanhuruf1 > 0:
               print("Format Pekerjaan yang anda Masukkan Salah !!")
               continue
            else:
               break
   # Hobi
         while True:
            hobi = input("Silahkan Masukkan Hobi Anda (Hobi 1, Hobi 2, ..., Hobi 5) Minimal 2, Maksimal 5 : ")
            daftarHobi = hobi.split(",")
            bukanhuruf2 = 0
            huruf2 = 0
            panjang = len(daftarHobi)

            for x1 in daftarHobi:
               x2 = x1.replace(" ","")
               for i in x2:
                  apakah3bukan = i.isalpha()
                  if apakah3bukan == False:
                     bukanhuruf2 += 1

            if bukanhuruf2 > 0:
               print("Hobi Salah")
               continue
            elif "" in daftarHobi:
               print("Setelah \",\" tidak boleh kosong")
               continue
            elif panjang < 2:
               print("Hobi kurang")
               continue
            elif panjang > 5:
               print("Hobi kelebihan")
               continue
            else:
               break
   # Alamat
         while True:
            daftarAlamat = input("Silahkan Masukkan Alamat Anda : ")
            a = daftarAlamat.replace(" ","")
            b = a.replace(".","")
            c = b.replace(",","")
            d = c.replace("-","")
            if d.isalnum() == True:
               break
            else:
               print("Input Alamat Anda salah !!")
               continue
   # Kota
         while True:
            daftarKota = input("Silahkan Masukkan Kota Anda : ")
            a1 = daftarKota.replace(" ","")
            b1 = a1.replace(".","")
            if b1.isalpha() == True:
               break
            else:
               print("Input Kota Anda salah !!")
               continue
   # RT
         while True:
            try:
               rt = input("Silahkan Masukkan RT : ")
               a = int(rt)
               daftarRT = "%02d" % a
               if a > 99:
                  print("Input RT tidak boleh lebih dari 2 digit !")
                  continue
               elif a < 0:
                  print("Tidak ada RT yang negatif ya bang :)")
                  continue
               elif a < 1:
                  print("Input RT tidak boleh kurang dari 1 digit !")
                  continue
               else:
                  break
            except:
               print("Tidak menerima string dan float")
   # RW
         while True:
            try:
               rw = input("Silahkan Masukkan RW : ")
               b = int(rw)
               daftarRW = "%02d" % b
               if b > 99:
                  print("Input RW tidak boleh lebih dari 2 digit !")
                  continue
               elif b < 0:
                  print("Tidak ada RW yang negatif ya bang :)")
                  continue
               elif b < 1:
                  print("Input RW tidak boleh kurang dari 1 digit !")
                  continue
               else:
                  break
            except:
               print("Tidak menerima string dan float")
   # Zipcode
         while True:
            try:
               zipcode = input("Silahkan Masukkan Zipcode : ")
               daftarZipcode = int(zipcode)
               if daftarZipcode > 99999:
                  print("Input Zipcode Hanya Menerima 5 digit Positif !")
                  continue
               elif daftarZipcode < 10000:
                  print("Input Zipcode Hanya Menerima 5 digit Positif !")
                  continue
               else:
                  break
            except:
               print("Tidak menerima string dan float")
   # Lat
         while True:
            try:
               lat = input("Silahkan Masukkan Lat : ")
               daftarLat = float(lat)
               if daftarLat > 90:
                  print("Maksimal Lat +90")
                  continue
               elif daftarLat < -90:
                  print("Minimal Lat -90")
                  continue
               else:
                  break
            except:
               print("Inputan anda salah !")
   # Lng
         while True:
            try:
               lng = input("Silahkan Masukkan Lng : ")
               daftarLng = float(lng)
               if daftarLng > 180:
                  print("Maksimal Lng +180")
                  continue
               elif daftarLng < -180:
                  print("Minimal Lat -180")
                  continue
               else:
                  break
            except:
               print("Inputan anda salah !")
   # No HP
         while True:
            daftarHP = str(input("Silahkan Masukkan No HP Anda : "))
            no1 = daftarHP.replace("+62","0")

            if daftarHP.startswith("+62") or daftarHP.startswith("0"):
               bukanno = 0
               hayoloh = 0
               for i in no1:
                  apabukanno = i.isdigit()
                  if apabukanno == True:
                     bukanno += 1
                  elif apabukanno != True:
                     hayoloh += 1

               if hayoloh > 0:
                  print("No HP anda salah")
                  continue
               elif bukanno > 13:
                  print("Lebih dari 13 digit")
                  continue
               elif bukanno < 11:
                  print("Kurang dari 11 digit")
                  continue
               else:
                  break
            else:
               print("Hanya menerima nomor Indonesia saja :)")
   # Yes or No
         while True:
            h = input("Apakah anda yakin ingin Register Akun \""+ daftarID + "\"? (Y/N) : ")
            asking = h.lower()
            if asking == "y":
               dikte[daftarID] = [daftarPass,
               daftarEmail,
               daftarNama,
               daftarGender,
               daftarUsia,
               daftarPekerjaan,
               daftarHobi,
               [daftarAlamat,daftarKota,daftarRT,daftarRW,daftarZipcode,[daftarLat,daftarLng]],
               daftarHP]
               # print(dikte)
               print("Akun \"" + daftarID + "\" Berhasil Disimpan !")
               print("Kembali ke Menu Utama !")
               break
            elif asking == "n":
               print("Akun \"" + daftarID + "\" Tidak Jadi Disimpan !")
               print("Kembali ke Menu Utama !")
               break
            else:
               print("Silahkan pilih (Y/N)")
               continue
# NOMOR 2 (LOGIN)
      elif login == 2:
         print("2. Login - Silahkan Input ID dan Password Anda")
         kesempatanlogin = 1
         batascoba = 5
         while kesempatanlogin <= batascoba:
            print("Kesempatan Login Anda 5x, Percobaan ke : ", kesempatanlogin,"x")
            masukid = input("Masukkan ID Anda : ")
            masukpass = input("Masukkan Password Anda : ")

            if kesempatanlogin <= batascoba:
               if masukid not in dikte.keys():
                  print("ID Anda tidak terdaftar !")
                  kesempatanlogin += 1
                  if kesempatanlogin == batascoba:
                     print("Kesempatan terakhir anda untuk Login")
                  elif kesempatanlogin > batascoba:
                     print("Kesempatan Anda Habis !")
                  continue
               elif masukpass != dikte[masukid][0]:
                  print("Password yang Anda Masukkan Salah !")
                  kesempatanlogin += 1
                  if kesempatanlogin == batascoba:
                     print("Kesempatan terakhir anda untuk Login")
                  elif kesempatanlogin > batascoba:
                     print("Kesempatan Anda Habis !")
                  continue
               else:
                  print("Berhasil login\n")
                  while True:
                     try:
                        print("="*60)
                        print("\t               MENU UTAMA\n")
                        print("PILIHAN :")
                        print("1. User Profile")
                        print("2. Kalkulator")
                        print("3. Konversi Romawi")
                        print("4. Konversi Kode Morse")
                        print("5. Hitung Hari")
                        print("6. Kamus Hari")
                        print("7. Konversi Jumlah Hari")
                        print("8. Nilai Faktorial")
                        print("9. Jumlah Deret Fibonnaci")
                        print("10. Caesar Cipher")
                        print("11. Setting User")
                        print("12. Menu CRUD - Mini App v1.0")
                        print("13. Exit")
                        print("\t\t\t\t\t      Mini Apps v2.0")
                        print("="*60)
                        loginutama = int(input("Silahkan Masukkan Pilihan Menu (1-13) : "))
      # No 1 - User Profile
                        if loginutama == 1:
                           gabunghobi = ", ".join(dikte[masukid][6])
                           print("1. User Profile")
                           print("Data Anda")
                           print("Nama      :", dikte[masukid][2])
                           print("Email     :", dikte[masukid][1])
                           print("Gender    :", dikte[masukid][3])
                           print("Usia      :", dikte[masukid][4], "Tahun")
                           print("Pekerjaan :", dikte[masukid][5])
                           print("Hobi      :", gabunghobi)
                           print("Alamat    :", dikte[masukid][7][0])
                           print("    Nama Kota :", dikte[masukid][7][1])
                           print("    RT        :", dikte[masukid][7][2])
                           print("    RW        :", dikte[masukid][7][3])
                           print("    Zipcode   :", dikte[masukid][7][4])
                           print("    Geo       :")
                           print("               Lat :", dikte[masukid][7][5][0])
                           print("               Lng :", dikte[masukid][7][5][1])
                           print("No HP     :", dikte[masukid][8])

                           print("\nSUB MENU")
                           print("1. Kembali ke menu yang sedang diakses")
                           print("2. Kembali ke menu utama")
                           while True:
                              a = input("Apakah yang anda ingin lakukan? ")
                              do1 = str(a)
                              if do1 == "1":
                                 print("Kembali ke menu yang sedang diakses\n")
                                 print("1. User Profile")
                                 print("Data Anda")
                                 print("Nama      :", dikte[masukid][2])
                                 print("Email     :", dikte[masukid][1])
                                 print("Gender    :", dikte[masukid][3])
                                 print("Usia      :", dikte[masukid][4], "Tahun")
                                 print("Pekerjaan :", dikte[masukid][5])
                                 print("Hobi      :", gabunghobi)
                                 print("Alamat    :", dikte[masukid][7][0])
                                 print("    Nama Kota :", dikte[masukid][7][1])
                                 print("    RT        :", dikte[masukid][7][2])
                                 print("    RW        :", dikte[masukid][7][3])
                                 print("    Zipcode   :", dikte[masukid][7][4])
                                 print("    Geo       :")
                                 print("               Lat :", dikte[masukid][7][5][0])
                                 print("               Lng :", dikte[masukid][7][5][1])
                                 print("No HP     :", dikte[masukid][8])
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
                                 continue
                              elif do1 == "2":
                                 print("Kembali ke Menu Utama\n")
                                 break
                              else:
                                 print("\nSilahkan Pilih 1 atau 2")
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
      # No 2 - Kalkulator
                        elif loginutama == 2:
                           print("2. Kalkulator")
                           def kalkulator(angka1, angka2, operator):
                              if operator == "+":
                                 hasil = angka1 + angka2
                                 return print("Hasil Perhitungan ", masuk1 , operator , masuk2 , "=" , hasil)
                              elif operator == "-":
                                 hasil = angka1 - angka2
                                 return print("Hasil Perhitungan ", masuk1 , operator , masuk2 , "=" , hasil)
                              elif operator == "*":
                                 hasil = angka1 * angka2
                                 return print("Hasil Perhitungan ", masuk1 , operator , masuk2 , "=" , hasil)
                              elif operator == "/":
                                 hasil = angka1 / angka2
                                 return print("Hasil Perhitungan :", masuk1 , operator , masuk2 , "=" , hasil)
                              else:
                                 return print("Operator yang anda masukkan tidak dikenal")
                              
                           try:
                              masuk1 = input("Silahkan Masukkan Angka 1 : ")
                              masuk2 = input("Silahkan Masukkan Angka 2 : ")
                              masuk3 = input("Masukkan Operator : ")
                              angka1 = float(masuk1)
                              angka2 = float(masuk2)
                              operator = str(masuk3)
                              kalkulator(angka1, angka2, operator)
                           except ZeroDivisionError:
                              print("Angka Pembagi yang anda masukkan adalah nol")
                           except ValueError:
                              print("Angka tidak dapat menerima string")

                           print("\nSUB MENU")
                           print("1. Kembali ke menu yang sedang diakses")
                           print("2. Kembali ke menu utama")
                           while True:
                              a = input("Apakah yang anda ingin lakukan? ")
                              do1 = str(a)
                              if do1 == "1":
                                 print("Kembali ke menu yang sedang diakses\n")
                                 print("2. Kalkulator")
                                 try:
                                    masuk1 = input("Silahkan Masukkan Angka 1 : ")
                                    masuk2 = input("Silahkan Masukkan Angka 2 : ")
                                    masuk3 = input("Masukkan Operator : ")
                                    angka1 = float(masuk1)
                                    angka2 = float(masuk2)
                                    operator = str(masuk3)
                                    kalkulator(angka1, angka2, operator)
                                 except ZeroDivisionError:
                                    print("Angka Pembagi yang anda masukkan adalah nol")
                                 except ValueError:
                                    print("Angka tidak dapat menerima string")
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
                                 continue
                              elif do1 == "2":
                                 print("Kembali ke Menu Utama\n")
                                 break
                              else:
                                 print("\nSilahkan Pilih 1 atau 2")
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
      # No 3 - Konversi Angka Romawi
                        elif loginutama == 3:
                           print("3. Konversi Angka Romawi")
                           def angkakeromawi(angka):
                              angkapenting = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] # angka-angka penting
                              romawipenting = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"] # romawi penting
                              bantuan = '' # bantuan buat nampung dari angka ke romawi
                              for i in range(len(angkapenting)): # ngeloop dari panjang angka penting
                                 while angka >= angkapenting[i]: # ketika si angka lebih besar sama dengan angka penting
                                       angka -= angkapenting[i] # angka dikurangin angka penting yang ditarget
                                       bantuan += romawipenting[i] # bantuannya ditambahin dari romawi penting yang ditarget
                                                                  # begitu terus ngeloop sampe si angka habis jadi 0, dapet romawinya
                              return bantuan

                           def romawikeangka(angka):
                              romawipenting = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
                              bantuan2 = 0
                              for i in range(0, len(angka)): # ngeloop dari range 0 sampai panjangnya inputan angka romawi
                                 if i == 0 or romawipenting[angka[i]] <= romawipenting[angka[i - 1]]: # ketika i == 0 atau isi i=0 dari 
                                                                                                      # inputan angka romawi dijadiin 
                                                                                                      # angka biasa <= isi i-1 dari 
                                                                                                      # inputan angka romawi dijadiin 
                                                                                                      # angka biasa
                                       # print("isi = ", angka[i])                       # index dari angka inputan buat dapet romawi
                                       # print("kiri = ", romawipenting[angka[i]])       # ambil angka dari dictionary romawi penting
                                       # print("kanan = ", romawipenting[angka[i - 1]])  # buat pembanding angka dari dictionary i-1
                                       bantuan2 += romawipenting[angka[i]]              # kalau sesuai kondisi if nya, angkanya dimasukan
                                                                                       # dan dijumlahin terus sampai loopingnya beres
                                       if bantuan2 > 4000:
                                          return print("Angka tidak boleh lebih dari 4000 !!")
                                 else:           # ketika kondisi isi i=0 dari inputan angka romawi dijadiin angka biasa > isi i-1
                                                   # dari inputan angka romawi dijadiin angka biasa
                                       bantuan2 += romawipenting[angka[i]] - 2 * romawipenting[angka[i - 1]]
                                                   # angka di dalam dictionarynya si i dikurangin 2*angka di dalam dictionarynya si i-1
                                                   # misalkan CD => C = 100, ketemu D nih, kan lebih besar dari 100 jadi masuk begini
                                                   # 500 - 2*100 = 300, CD = 100 + 300 = 400
                                       # print("bawah = ", romawipenting[angka[i]] - 2 * romawipenting[angka[i - 1]])
                              if angkakeromawi(bantuan2) != b:
                                 return print("Angka Romawi yang anda Input tidak dikenal !")
                              else:
                                 return print("Angka Romawi yang anda Input :", b , "dan Angkanya :", bantuan2)

                           try:
                              a = input("Silahkan Masukkan Angka / Angka Romawi : ")
                              b = a.upper()
                              angka = str(b)
                              if angka.isdigit() == True:
                                 angka = int(angka)
                                 if angka > 4000:
                                    print("Maksimal menginput angka 4000 !!")
                                 elif angka < 1:
                                    print("Minimal menginput angka 1 !!")
                                 else:
                                    print("Angka yang anda Input :", b ,"dan Angka Romawinya :", angkakeromawi(angka))
                              elif angka.isalpha() == True:
                                 romawikeangka(angka)
                              elif angka.isalpha() != True:
                                 print("Angka yang anda masukkan salah (Tidak menerima desimal / kalimat)")
                           except:
                              print("Angka Romawi yang anda masukkan salah")

                           print("\nSUB MENU")
                           print("1. Kembali ke menu yang sedang diakses")
                           print("2. Kembali ke menu utama")
                           while True:
                              a = input("Apakah yang anda ingin lakukan? ")
                              do1 = str(a)
                              if do1 == "1":
                                 print("Kembali ke menu yang sedang diakses\n")
                                 print("3. Konversi Romawi")
                                 try:
                                    a = input("Silahkan Masukkan Angka / Angka Romawi : ")
                                    b = a.upper()
                                    angka = str(b)
                                    if angka.isdigit() == True:
                                       angka = int(angka)
                                       if angka > 4000:
                                          print("Maksimal menginput angka 4000 !!")
                                       elif angka < 1:
                                          print("Minimal menginput angka 1 !!")
                                       else:
                                          print("Angka yang anda Input :", b ,"dan Angka Romawinya :", angkakeromawi(angka))
                                    elif angka.isalpha() == True:
                                       romawikeangka(angka)
                                    elif angka.isalpha() != True:
                                       print("Angka yang anda masukkan salah (Tidak menerima desimal / kalimat)")
                                 except:
                                    print("Angka Romawi yang anda masukkan salah")
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
                                 continue
                              elif do1 == "2":
                                 print("Kembali ke Menu Utama\n")
                                 break
                              else:
                                 print("\nSilahkan Pilih 1 atau 2")
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")   
      # No 4 - Konversi Kode Morse
                        elif loginutama == 4:
                           print("4. Konversi Kode Morse")
                           kue = {
                           "0": "-----",
                           "1": ".----",
                           "2": "..---",
                           "3": "...--",
                           "4": "....-",
                           "5": ".....",
                           "6": "-....",
                           "7": "--...",
                           "8": "---..",
                           "9": "----.",
                           "a": ".-",
                           "b": "-...",
                           "c": "-.-.",
                           "d": "-..",
                           "e": ".",
                           "f": "..-.",
                           "g": "--.",
                           "h": "....",
                           "i": "..",
                           "j": ".---",
                           "k": "-.-",
                           "l": ".-..",
                           "m": "--",
                           "n": "-.",
                           "o": "---",
                           "p": ".--.",
                           "q": "--.-",
                           "r": ".-.",
                           "s": "...",
                           "t": "-",
                           "u": "..-",
                           "v": "...-",
                           "w": ".--",
                           "x": "-..-",
                           "y": "-.--",
                           "z": "--..",
                           ".": ".-.-.-",
                           ",": "--..--",
                           "?": "..--..",
                           "!": "-.-.--",
                           "-": "-....-",
                           "/": "-..-.",
                           "@": ".--.-.",
                           "(": "-.--.",
                           ")": "-.--.-",
                           " ": "|"
                           }

                           letsgo = input("Masukan Kata / Kode Morse: ")
                           letsgo1 = letsgo.lower()
                           letsgo2 = letsgo1.split() # buat dijadiin tuple untuk kode morse
                           letsgobersatu = letsgo1.split(" ") # buat pecah jadi ngisi
                           letstuple = tuple(letsgo2)

                           a = ""
                           ngisi = ""

                           # fl = float(letsgo)

                           # if letsgo1 == type(fl):
                           #     print("Tidak menerima Angka Desimal")
                           #     quit()

                           for y in letsgobersatu:
                              ngisi += y # untuk dijadiin baca biar spasinya bisa

                           # if letsgo1.replace(" ","").isalnum() != True:
                           #     print("Hanya menerima Alfabet, Angka dan Spasi")
                           if "!" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")
                           elif "@" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")
                           elif "#" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")
                           elif "$" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")
                           elif "%" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")
                           elif "^" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")
                           elif "&" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")
                           elif "*" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")
                           elif "(" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")
                           elif ")" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")
                           elif "," in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")
                           elif "/" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")
                           elif "?" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")    
                           elif "=" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")
                           elif "+" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")    
                           elif "_" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")  
                           elif ":" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")     
                           elif ";" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")   
                           elif "[" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")       
                           elif "]" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")    
                           elif "{" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")       
                           elif "}" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")    
                           elif "<" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")       
                           elif ">" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi") 
                           elif "~" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")       
                           elif "`" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")
                           elif "\'" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")       
                           elif "\"" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")      
                           elif "\\" in letsgo1:
                              print("Hanya menerima Alfabet, Angka, dan Spasi")  
                           # elif "|" in ngisi:
                           #     print("Hanya menerima Alfabet, Angka, dan Spasi")    
                           # elif "." in ngisi:
                           #     print("Hanya menerima Alfabet, Angka, dan Spasi")
                           elif ngisi.isalnum() == True:
                              for i in letsgo1:
                                 for p,q in kue.items():
                                    if i == p:
                                       a += q + " "
                                       continue
                              print("Kata yang anda masukkan adalah","\"", letsgo ,"\"", "jika diubah menjadi kode morse menjadi","\"", a ,"\"",end=" ")
                           elif ngisi.isalnum() != True:
                              if ngisi.startswith("-") or ngisi.startswith("."):
                                 for i in letstuple:
                                    for p,q in kue.items():
                                       if i == q:
                                          a += p
                                          continue
                                 print("Kode morse yang anda masukkan adalah","\"", letsgo ,"\"", "Jika diubah menjadi kata-kata menjadi","\"", a ,"\"",end=" ")
                              else:
                                 print("Hanya menerima Alfabet, Angka, Spasi, dan Kode Morse")
                           else:
                              print("Kata yang anda masukkan salah")

                           print("\nSUB MENU")
                           print("1. Kembali ke menu yang sedang diakses")
                           print("2. Kembali ke menu utama")
                           while True:
                              a = input("Apakah yang anda ingin lakukan? ")
                              do1 = str(a)
                              if do1 == "1":
                                 print("Kembali ke menu yang sedang diakses\n")
                                 print("4. Konversi Kode Morse")
                                 letsgo = input("Masukan Kata / Kode Morse: ")
                                 letsgo1 = letsgo.lower()
                                 letsgo2 = letsgo1.split() # buat dijadiin tuple untuk kode morse
                                 letsgobersatu = letsgo1.split(" ") # buat pecah jadi ngisi
                                 letstuple = tuple(letsgo2)

                                 a = ""
                                 ngisi = ""

                                 # fl = float(letsgo)

                                 # if letsgo1 == type(fl):
                                 #     print("Tidak menerima Angka Desimal")
                                 #     quit()

                                 for y in letsgobersatu:
                                    ngisi += y # untuk dijadiin baca biar spasinya bisa

                                 # if letsgo1.replace(" ","").isalnum() != True:
                                 #     print("Hanya menerima Alfabet, Angka dan Spasi")
                                 if "!" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")
                                 elif "@" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")
                                 elif "#" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")
                                 elif "$" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")
                                 elif "%" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")
                                 elif "^" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")
                                 elif "&" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")
                                 elif "*" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")
                                 elif "(" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")
                                 elif ")" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")
                                 elif "," in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")
                                 elif "/" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")
                                 elif "?" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")    
                                 elif "=" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")
                                 elif "+" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")    
                                 elif "_" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")  
                                 elif ":" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")     
                                 elif ";" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")   
                                 elif "[" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")       
                                 elif "]" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")    
                                 elif "{" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")       
                                 elif "}" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")    
                                 elif "<" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")       
                                 elif ">" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi") 
                                 elif "~" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")       
                                 elif "`" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")
                                 elif "\'" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")       
                                 elif "\"" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")      
                                 elif "\\" in letsgo1:
                                    print("Hanya menerima Alfabet, Angka, dan Spasi")  
                                 # elif "|" in ngisi:
                                 #     print("Hanya menerima Alfabet, Angka, dan Spasi")    
                                 # elif "." in ngisi:
                                 #     print("Hanya menerima Alfabet, Angka, dan Spasi")
                                 elif ngisi.isalnum() == True:
                                    for i in letsgo1:
                                       for p,q in kue.items():
                                          if i == p:
                                             a += q + " "
                                             continue
                                    print("Kata yang anda masukkan adalah","\"", letsgo ,"\"", "jika diubah menjadi kode morse menjadi","\"", a ,"\"",end=" ")
                                 elif ngisi.isalnum() != True:
                                    if ngisi.startswith("-") or ngisi.startswith("."):
                                       for i in letstuple:
                                          for p,q in kue.items():
                                             if i == q:
                                                a += p
                                                continue
                                       print("Kode morse yang anda masukkan adalah","\"", letsgo ,"\"", "Jika diubah menjadi kata-kata menjadi","\"", a ,"\"",end=" ")
                                    else:
                                       print("Hanya menerima Alfabet, Angka, Spasi, dan Kode Morse")
                                 else:
                                    print("Kata yang anda masukkan salah")                             
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
                                 continue
                              elif do1 == "2":
                                 print("Kembali ke Menu Utama\n")
                                 break
                              else:
                                 print("\nSilahkan Pilih 1 atau 2")
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
      # No 5 - Hitung Hari
                        elif loginutama == 5:
                           print("5. Hitung Hari")
                           try:
                              hari = ["senin","selasa","rabu","kamis","jumat","sabtu","minggu"]
                              a1 = input("Masukkan Nama Hari : ")
                              a2 = input("Masukkan Jumlah : ")
                              target1 = str(a1.lower())
                              target2 = int(a2)
                              if target1 not in hari:
                                 print("Tidak Ada Nama Hari / Nama Hari yang Anda Masukkan Salah !!")
                              else:
                                 x = hari.index(target1)
                                 hasil = (x + target2) % 7
                                 z = hari[hasil]
                                 print("Hari ini adalah hari " + str(target1.title()) + ", " + str(target2) + " hari lagi adalah hari " + z.title())
                           except:
                              print("Input Jumlah Tidak Bisa Desimal atau String !")

                           print("\nSUB MENU")
                           print("1. Kembali ke menu yang sedang diakses")
                           print("2. Kembali ke menu utama")
                           while True:
                              a = input("Apakah yang anda ingin lakukan? ")
                              do1 = str(a)
                              if do1 == "1":
                                 print("Kembali ke menu yang sedang diakses\n")
                                 print("5. Hitung Hari")
                                 try:
                                    hari = ["senin","selasa","rabu","kamis","jumat","sabtu","minggu"]
                                    a1 = input("Masukkan Nama Hari : ")
                                    a2 = input("Masukkan Jumlah : ")
                                    target1 = str(a1.lower())
                                    target2 = int(a2)
                                    if target1 not in hari:
                                       print("Tidak Ada Nama Hari / Nama Hari yang Anda Masukkan Salah !!")
                                    else:
                                       x = hari.index(target1)
                                       hasil = (x + target2) % 7
                                       z = hari[hasil]
                                       print("Hari ini adalah hari " + str(target1.title()) + ", " + str(target2) + " hari lagi adalah hari " + z.title())
                                 except:
                                    print("Input Jumlah Tidak Bisa Desimal atau String !")
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
                                 continue
                              elif do1 == "2":
                                 print("Kembali ke Menu Utama\n")
                                 break
                              else:
                                 print("\nSilahkan Pilih 1 atau 2")
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
      # No 6 - Kamus Hari
                        elif loginutama == 6:
                           print("6. Day Translator")
                           hari = {
                              "senin" : "monday",
                              "selasa" : "tuesday",
                              "rabu" : "wednesday",
                              "kamis" : "thursday",
                              "jumat" : "friday",
                              "sabtu" : "saturday",
                              "minggu" : "sunday"
                           }
                           masuk = input("Masukan Nama Hari / Please Input Name of Day : ")
                           masuk1 = masuk.lower()

                           a = list(hari.keys())
                           b = list(hari.values())

                           if masuk1 in a:
                              for m,n in hari.items():
                                 if masuk1 == m:
                                    print("Hari yang anda pilih","\"", masuk ,"\"", "dalam bahasa Inggris adalah","\"", n.title() ,"\"")
                                 else:
                                    continue
                           elif masuk1 in b:
                              for m,n in hari.items():
                                 if masuk1 == n:
                                    print("The day that you choose is","\"", masuk,"\"", "in Bahasa is","\"", m.title() ,"\"")
                                 else:
                                    continue      
                           elif masuk1.isalpha() != True:
                              print("Hari yang anda masukkan salah !")
                           else:
                              print("Hari Tidak Ditemukan")

                           print("\nSUB MENU")
                           print("1. Kembali ke menu yang sedang diakses")
                           print("2. Kembali ke menu utama")  
                           while True:
                              a = input("Apakah yang anda ingin lakukan? ")
                              do1 = str(a)
                              if do1 == "1":
                                 print("Kembali ke menu yang sedang diakses\n")
                                 print("6. Day Translator")
                                 masuk = input("Masukan Nama Hari / Please Input Name of Day : ")
                                 masuk1 = masuk.lower()

                                 a = list(hari.keys())
                                 b = list(hari.values())

                                 if masuk1 in a:
                                    for m,n in hari.items():
                                       if masuk1 == m:
                                          print("Hari yang anda pilih","\"", masuk ,"\"", "dalam bahasa Inggris adalah","\"", n.title() ,"\"")
                                       else:
                                          continue
                                 elif masuk1 in b:
                                    for m,n in hari.items():
                                       if masuk1 == n:
                                          print("The day that you choose is","\"", masuk,"\"", "in Bahasa is","\"", m.title() ,"\"")
                                       else:
                                          continue      
                                 elif masuk1.isalpha() != True:
                                    print("Hari yang anda masukkan salah !")
                                 else:
                                    print("Hari Tidak Ditemukan")
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
                                 continue
                              elif do1 == "2":
                                 print("Kembali ke Menu Utama\n")
                                 break
                              else:
                                 print("\nSilahkan Pilih 1 atau 2")
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
      # No 7 - Konversi Hari
                        elif loginutama == 7:
                           print("7. Konversi Jumlah Hari")
                           try:
                              masuk = int(input("Masukkan Jumlah Hari : "))
                              if masuk >= 4000:
                                 print("Jumlah hari diatas batas")
                              elif masuk < 0:
                                 print("Jumlah hari dibawah batas")
                              else:
                                 tahun = masuk // 365 # jadi berapa tahun
                                 # print("Tahun = ", tahun)
                                 ubah1 = masuk % 365 # dari total hari dijadiin sisa hari
                                 # print("Ubah 1 =", ubah1)
                                 bulan = ubah1 // 30 # sisa hari dijadiin ke bulan
                                 # print("Bulan =", bulan)
                                 ubah2 = ubah1 % 30 # sisa hari dijadiin sisa hari dari bulan
                                 # print("Ubah 2 =", ubah2)
                                 minggu = ubah2 // 7 # sisa hari dari bulan dijadiin ke minggu
                                 # print("Minggu =", minggu)
                                 ubah3 = ubah2 % 7 # sisa hari dari minggu dijadiin ke hari
                                 # print("Ubah 3 =", ubah3)
                                 hari = ubah3 # hari
                                 print("%02d" % tahun, "Tahun" ,"%02d" % bulan, "Bulan" ,"%02d" % minggu, "Minggu" ,"%02d" % hari, "Hari")
                           except:
                              print("Jumlah Hari yang Anda Masukkan Salah !")          

                           print("\nSUB MENU")
                           print("1. Kembali ke menu yang sedang diakses")
                           print("2. Kembali ke menu utama")   
                           while True:
                              a = input("Apakah yang anda ingin lakukan? ")
                              do1 = str(a)
                              if do1 == "1":
                                 print("Kembali ke menu yang sedang diakses\n")
                                 print("7. Konversi Jumlah Hari")      
                                 try:
                                    masuk = int(input("Masukkan Jumlah Hari : "))
                                    if masuk >= 4000:
                                       print("Jumlah hari diatas batas")
                                    elif masuk < 0:
                                       print("Jumlah hari dibawah batas")
                                    else:
                                       tahun = masuk // 365 # jadi berapa tahun
                                       # print("Tahun = ", tahun)
                                       ubah1 = masuk % 365 # dari total hari dijadiin sisa hari
                                       # print("Ubah 1 =", ubah1)
                                       bulan = ubah1 // 30 # sisa hari dijadiin ke bulan
                                       # print("Bulan =", bulan)
                                       ubah2 = ubah1 % 30 # sisa hari dijadiin sisa hari dari bulan
                                       # print("Ubah 2 =", ubah2)
                                       minggu = ubah2 // 7 # sisa hari dari bulan dijadiin ke minggu
                                       # print("Minggu =", minggu)
                                       ubah3 = ubah2 % 7 # sisa hari dari minggu dijadiin ke hari
                                       # print("Ubah 3 =", ubah3)
                                       hari = ubah3 # hari
                                       print("%02d" % tahun, "Tahun" ,"%02d" % bulan, "Bulan" ,"%02d" % minggu, "Minggu" ,"%02d" % hari, "Hari")
                                 except:
                                    print("Jumlah Hari yang Anda Masukkan Salah !")        
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
                                 continue
                              elif do1 == "2":
                                 print("Kembali ke Menu Utama\n")
                                 break
                              else:
                                 print("\nSilahkan Pilih 1 atau 2")
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
      # No 8 - Nilai Faktorial
                        elif loginutama == 8:
                           print("8. Nilai Faktorial")
                           def factorial():
                              try:
                                 x = int(input("Masukkan Angka : "))   
                                 if x < 0:
                                    return print("Tidak menerima angka negatif !")   
                                 f = 1
                                 for n in range(2, x + 1):
                                       f = f * n
                                 return print("Hasil Faktorial",x,"! adalah",f)
                              except: 
                                 return print("Hanya Menerima Integer")    
                           factorial()

                           print("\nSUB MENU")
                           print("1. Kembali ke menu yang sedang diakses")
                           print("2. Kembali ke menu utama")   
                           while True:
                              a = input("Apakah yang anda ingin lakukan? ")
                              do1 = str(a)
                              if do1 == "1":
                                 print("Kembali ke menu yang sedang diakses\n")
                                 print("8. Nilai Faktorial")
                                 factorial()

                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
                                 continue
                              elif do1 == "2":
                                 print("Kembali ke Menu Utama\n")
                                 break
                              else:
                                 print("\nSilahkan Pilih 1 atau 2")
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
      # No 9 - Fibonacci
                        elif loginutama == 9:
                           print("9. Fibonacci")
                           import math
                           from functools import reduce
                           try:
                              n = input("Masukkan Angka yang diinginkan : ")
                              n1 = int(n)
                              i = list(range(1,n1+1))
                              # a = (1/math.sqrt(5))
                              # b = ((1+math.sqrt(5))/2) ** i
                              # c = ((1-math.sqrt(5))/2) ** i

                              dapetfibo = list(map(lambda i: (((1/math.sqrt(5)) * ((1+math.sqrt(5))/2) ** i) - ((1/math.sqrt(5)) * ((1-math.sqrt(5))/2) ** i)), i))
                              hasiltotalfibo = reduce(lambda a,b: a + b, dapetfibo)
                              print(n1, "deret angka pertama baris fibonacci", dapetfibo, "dan jumlahnya : ", hasiltotalfibo)
                           except:
                              print("Angka tidak menerima string / desimal")

                           print("\nSUB MENU")
                           print("1. Kembali ke menu yang sedang diakses")
                           print("2. Kembali ke menu utama")  
                           while True:
                              a = input("Apakah yang anda ingin lakukan? ")
                              do1 = str(a)
                              if do1 == "1":
                                 print("Kembali ke menu yang sedang diakses\n")
                                 print("9. Fibonacci")
                                 import math
                                 from functools import reduce
                                 try:
                                    n = input("Masukkan Angka yang diinginkan : ")
                                    n1 = int(n)
                                    i = list(range(1,n1+1))
                                    # a = (1/math.sqrt(5))
                                    # b = ((1+math.sqrt(5))/2) ** i
                                    # c = ((1-math.sqrt(5))/2) ** i

                                    dapetfibo = list(map(lambda i: (((1/math.sqrt(5)) * ((1+math.sqrt(5))/2) ** i) - ((1/math.sqrt(5)) * ((1-math.sqrt(5))/2) ** i)), i))
                                    hasiltotalfibo = reduce(lambda a,b: a + b, dapetfibo)
                                    print(n1, "deret angka pertama baris fibonacci", dapetfibo, "dan jumlahnya : ", hasiltotalfibo)
                                 except:
                                    print("Angka tidak menerima string / desimal")
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
                                 continue
                              elif do1 == "2":
                                 print("Kembali ke Menu Utama\n")
                                 break
                              else:
                                 print("\nSilahkan Pilih 1 atau 2")
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
      # No 10 - Caesar Cipher
                        elif loginutama == 10:
                           print("10. Caesar Cipher")
                           data = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u",
                           "v","w","x","y","z"]
                           kotak = []
                           isi = []
                           hasil = []
                           hasilkata = []

                           def iterasi(data, kotak, bilangan):
                              # print(kotak)
                              for i in kotak:
                                 x = data.index(i)
                                 isi.append(x)
                                 continue

                              # print(isi)

                              for j in isi:
                                 y = (j + bilangan) % 26
                                 hasil.append(y)

                              # print(hasil)

                              for h in hasil:
                                 z = data[h]
                                 hasilkata.append(z)

                              # print(hasilkata)
                              return print("Hasil Caesar Cipher adalah : " + "".join(hasilkata))
                              # print(merger)

                           try:
                              go = input("Silahkan Masukkan Kata : ")
                              masukbang = go.lower()
                              kotak.extend(masukbang)
                              masukbang2 = input("Silahkan Masukkan Angka : ")
                              bilangan = int(masukbang2)
                              if masukbang.isalpha():
                                 iterasi(data, kotak, bilangan)
                              else:
                                 print("Masukkan kata ya bang, jangan kalimat / angka / simbol yaa :)")
                           except:
                              print("Angka tidak dapat menerima string")

                           print("\nSUB MENU")
                           print("1. Kembali ke menu yang sedang diakses")
                           print("2. Kembali ke menu utama")  
                           while True:
                              a = input("Apakah yang anda ingin lakukan? ")
                              do1 = str(a)
                              if do1 == "1":
                                 print("Kembali ke menu yang sedang diakses\n")
                                 print("10. Caesar Cipher")
                                 data = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u",
                                 "v","w","x","y","z"]
                                 kotak = []
                                 isi = []
                                 hasil = []
                                 hasilkata = []

                                 try:
                                    go = input("Silahkan Masukkan Kata : ")
                                    masukbang = go.lower()
                                    kotak.extend(masukbang)
                                    masukbang2 = input("Silahkan Masukkan Angka : ")
                                    bilangan = int(masukbang2)
                                    if masukbang.isalpha():
                                       iterasi(data, kotak, bilangan)
                                    else:
                                       print("Masukkan kata ya bang, jangan kalimat / angka / simbol yaa :)")
                                 except:
                                    print("Angka tidak dapat menerima string")
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
                                 continue
                              elif do1 == "2":
                                 print("Kembali ke Menu Utama\n")
                                 break
                              else:
                                 print("\nSilahkan Pilih 1 atau 2")
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
      # No 11 - Setting User
                        elif loginutama == 11:
                           print("11. Setting User")
                           print("User ID Anda adalah :", masukid)
                           print("Password Anda adalah :", dikte[masukid][0])
                           print("Email Anda adalah :", dikte[masukid][1])

                           print("\nSUB MENU")
                           print("1. Kembali ke menu yang sedang diakses")
                           print("2. Kembali ke menu utama")  
                           while True:
                              a = input("Apakah yang anda ingin lakukan? ")
                              do1 = str(a)
                              if do1 == "1":
                                 print("Kembali ke menu yang sedang diakses\n")
                                 print("11. Setting User")
                                 print("User ID Anda adalah :", masukid)
                                 print("Password Anda adalah :", dikte[masukid][0])
                                 print("Email Anda adalah :", dikte[masukid][1])
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
                                 continue
                              elif do1 == "2":
                                 print("Kembali ke Menu Utama\n")
                                 break
                              else:
                                 print("\nSilahkan Pilih 1 atau 2")
                                 print("\nSUB MENU")
                                 print("1. Kembali ke menu yang sedang diakses")
                                 print("2. Kembali ke menu utama")
      # No 12 - Menu CRUD
                        elif loginutama == 12:
                           udah = True
                           while udah:
                              print('''
------------------------------------------
Selamat Datang Mase di Menu Cupang Lovers
------------------------------------------
1. List Daftar Cupang
2. Tambah Data Cupang
3. Ubah Data Cupang
4. Hapus Data Cupang
5. Exit
                              ''')
                              choice = input("Pilih Menu Mase: ")
                              if choice == 1 or choice == '1':
                                 udah1 = True
                                 while udah1:
                                    print("Daftar Data Cupang")
                                    print("---------------------------")
                                    if cupang == {}: #=> nama dictionary bisa diganti
                                       print("Stock nya masi Kosong Mase")
                                    else:    
                                       NamCup = 'Nama Cupang'
                                       print(f'{NamCup:<20}: Stock')
                                       print('---------------------------')
                                       for i,j in cupang.items():
                                          print(f'{i:<20}: {j:<10}')
                                       print("---------------------------")
                                    while True :
                                       print("\nSUB MENU")
                                       print("1. Kembali ke menu yang sedang diakses")
                                       print("2. Kembali ke menu CRUD")
                                       pilih = input("Masukan Pilihan Anda: ")
                                       if pilih == "1":
                                          break
                                       elif pilih == "2":
                                          udah1 = False
                                          break
                                       else:
                                          print('Pilihan hanya 1 dan 2')
                                          continue
                              elif choice == 2 or choice == '2':
                                 udah2 = True
                                 while udah2 :
                                    print("Tambah Data Cupang")
                                    print("-------------")
                                    print("Masukan Data Cupang: ")
                                    baru = str(input())
                                    baru1 = baru.title()
                                    print("Masukan Jumlah Cupang: ")
                                    jumlah = input()
                                    baru2 = baru.split(" ")
                                    numpang = ""

                                    for y2 in baru2:
                                       numpang += y2

                                    # baru1=x2
                                    if numpang.isdigit() == True or numpang.isalpha() == False:
                                       print("Jenis Cupang yang Anda Masukkan Salah !")
                                    elif jumlah.isdigit() != True:
                                       print("Jumlah hanya bisa bilangan bulat")
                                    elif baru1.startswith(" "):
                                       print("Jenis Cupang yang Anda Masukkan Salah !")
                                    else:
                                       if baru1 in cupang.keys():
                                          while True:
                                             print("Cupang sudah ada mau di masukan lagi? (y/n)")
                                             ok = input("Y/N: ")
                                             ok1 = ok.lower()
                                             if ok1 == "y":
                                                cupang[baru1] += int(jumlah)
                                                print("Ada duplikasi. Data disimpan Mase")
                                                NamCup = 'Nama Cupang'
                                                print(f'{NamCup:<20}: Stock')
                                                print('--------------------------')
                                                for i,j in cupang.items():
                                                   print(f'{i:<20}: {j:<10}')
                                                print("--------------------------")
                                                break
                                             elif ok1 == "n":
                                                print("Tidak tersimpan")
                                                break
                                             else:
                                                print("Cuma y/n Mase")
                                                continue
                                       else:
                                          cupang[baru1] = int(jumlah)
                                          print("Data telah disimpan Mase")
                                          NamCup = 'Nama Cupang'
                                          print(f'{NamCup:<20}: Stock')
                                          print('--------------------------')
                                          for i,j in cupang.items():
                                             print(f'{i:<20}: {j:<10}')
                                          print("--------------------------")
                                    while True :
                                       print("\nSUB MENU")
                                       print("1. Kembali ke menu yang sedang diakses")
                                       print("2. Kembali ke menu CRUD")
                                       pilih = input("Masukan Pilihan Anda: ")
                                       if pilih == "1":
                                          break
                                       elif pilih == "2":
                                          udah2 = False
                                          break
                                       else:
                                          print('Pilihan hanya 1 dan 2')
                                          continue
                              elif choice == 3 or choice == '3':
                                 udah3 = True
                                 while udah3:
                                    print("Ubah Data Cupang")
                                    print("--------------------------")
                                    NamCup = 'Nama Cupang'
                                    print(f'{NamCup:<20}: Stock')
                                    print('--------------------------')
                                    for i,j in cupang.items():
                                       print(f'{i:<20}: {j:<10}')
                                    print("--------------------------")
                                    update = input("Pilih Data Cupang yg ingin diubah : ")
                                    update1 = update.title()
                                    if update1 not in cupang.keys():
                                       print("Nama Cupang Tidak Ada")
                                    elif update1 in cupang.keys():
                                       while True:
                                          print(f"Pilih yg mau diubah dari {update1} : ")
                                          print('1.Ganti Nama Cupang')
                                          print('2.Stock')
                                          print('3.Batal')
                                          choice = input('Masukkan Pilihan : ')
                                          if choice == '1':
                                             kosong=''
                                             upbarang = input('Masukkan Nama Baru: ').title()
                                             pisah = upbarang.split(' ')
                                             for i in pisah:
                                                kosong += i
                                             if kosong.isdigit() == True or kosong.isalpha() == False:
                                                print('Nama Baru yg anda Masukkan Tidak Bisa Diterima')
                                             elif upbarang.startswith(" "):
                                                print('Nama Baru yg anda Masukkan Tidak Bisa Diterima')
                                             elif kosong.isalpha() == True:
                                                cupang[upbarang] = cupang.pop(update1)
                                                print(f"{update1} Berhasil Diperbarui Menjadi {upbarang}")
                                             break
                                          elif choice == '2':
                                             try:
                                                upstock = int(input('Tambah/Kurang Stock : '))
                                                ups= cupang[update1]
                                                ups += upstock
                                                if ups < 0:
                                                   print('Tidak Diterima. Stock Akhir Minimal 0')
                                                   break
                                                else:   
                                                   cupang[update1] = ups
                                                   print(f"Jumlah Stock {update1} Berhasil Diperbarui")
                                                   break
                                             except ValueError:
                                                print('Hanya Menerima Angka Bilangan Bulat')
                                                break
                                          elif choice == '3':
                                             break
                                          else:
                                             print('Pilihan hanya 1, 2 dan 3')
                                             continue
                                    else:
                                       print("Nama Cupang yg Anda Masukkan Salah")
                                    while True:
                                       print("\nSUB MENU")
                                       print("1. Kembali ke menu yang sedang diakses")
                                       print("2. Kembali ke menu CRUD")
                                       pilih = input("Masukan Pilihan Anda: ")
                                       if pilih == "1":
                                          break
                                       elif pilih == "2":
                                          udah3 = False
                                          break
                                       else:
                                          print('Pilihan hanya 1 dan 2')
                                          continue
                              elif choice == 4 or choice == '4':
                                 udah4 = True
                                 while udah4:
                                    print("Hapus Data Cupang")
                                    print("--------------------------")
                                    NamCup = 'Nama Cupang'
                                    print(f'{NamCup:<20}: Stock')
                                    print('--------------------------')
                                    for i,j in cupang.items():
                                       print(f'{i:<20}: {j:<10}')
                                    print("--------------------------")
                                    hapus = input("Pilih Data Cupang yg ingin dihapus : ")
                                    hapus1 = hapus.title()
                                    for x1 in hapus1:
                                       x2 = x1.replace(" ","")
                                    if x2.isalpha():
                                       barangBaru = hapus1
                                       if barangBaru in cupang:
                                          keluarbang = True 
                                          while keluarbang:
                                             try:
                                                print('1. Hapus Total')
                                                print('2. Hapus Stock')
                                                print('3. Batal')
                                                pilihan = input('Apa yang ingin anda lakukan: ')
                                                pilihanBaru = int(pilihan)  
                                                   # Pilihan 1
                                                if pilihanBaru == 1:
                                                   total = str(cupang[barangBaru])
                                                   keluardong = True
                                                   while keluardong:
                                                      yakin1 = input('Ditemukan' + ' ' + hapus1 + ' ' + 'sebanyak' + ' ' +  total + ' ' + 'buah, yakin hapus total (y/n): ')
                                                      yakin = yakin1.lower() 
                                                      if yakin == 'y':
                                                         cupang.pop(barangBaru)
                                                         print('Data Cupang Berhasil Dihapus')
                                                         keluardong = False
                                                         keluarbang = False
                                                      elif yakin == 'n':
                                                         print('Data Cupang Tidak Jadi Dihapus')
                                                         keluardong = False
                                                         keluarbang = False
                                                      else: 
                                                         print('Hanya y/n')
                                                         continue
                                                # Pilihan 2
                                                elif pilihanBaru == 2:
                                                   if cupang[barangBaru] > 0:
                                                      total = str(cupang[barangBaru])
                                                      keluarpls = True
                                                      while keluarpls:
                                                         yakin1 = input('Ditemukan' + ' ' + hapus1 + ' ' + 'sebanyak' + ' ' +  total + ' ' + 'buah, yakin hapus stock cupang (y/n): ')
                                                         yakin = yakin1.lower()      
                                                         if yakin == 'y':
                                                            cupang.update({barangBaru : 0})
                                                            print('Stock Cupang berhasil dihapus !')
                                                            keluarpls = False
                                                            keluarbang = False
                                                         elif yakin == 'n':
                                                            print('Stock Cupang tidak jadi dihapus !')
                                                            keluarpls = False
                                                            keluarbang = False
                                                         else:
                                                            print('Hanya y/n')
                                                            continue
                                                   elif cupang[barangBaru] == 0:
                                                      print("Stock Cupang sudah kosong !")
                                                elif pilihanBaru == 3:
                                                   keluarbang = False
                                                   pass
                                                else:
                                                   print('Hanya 1, 2 & 3')
                                             except:
                                                print("Yang Anda Masukkan Bukan Angka !")
                                       else:
                                          print('Data Cupang tidak ditemukan')    
                                    else:
                                       print('Data Cupang tidak ditemukan')
                                    while True :
                                       print("\nSUB MENU")
                                       print("1. Kembali ke menu yang sedang diakses")
                                       print("2. Kembali ke menu CRUD")
                                       pilih = input("Masukan Pilihan Anda: ")
                                       if pilih == "1":
                                          break
                                       elif pilih == "2":
                                          udah4 = False
                                          break
                                       else:
                                          print('Pilihan hanya 1 dan 2')
                                          continue
                              elif choice == 5 or choice == '5':
                                 print("Yakin udahan Mase?")
                                 while True:
                                    pilih4 = str(input("Hayoo gimana Mase ? (Y/N): "))
                                    pilih5 = pilih4.lower()
                                    if pilih5 == "y":
                                       print("Bye Bye Mase ~")
                                       udah = False
                                       break
                                    elif pilih5 == "n":
                                       print("Lha kok ga jadi Mase?")
                                       break
                                    else:
                                       print("Y / N aja Mase")
                                       continue
                              else:
                                 print('Pilih Sesuai yg Ada Aja Mase')
                                 continue
      # No 13 - Exit
                        elif loginutama == 13:
                           print("13. Keluar Aplikasi (Exit)")
                           while True:
                              k = input("Apakah anda yakin ingin keluar dari Program? Pilih Yes (Y) atau No (N) : ")
                              keluar = k.lower()
                              if keluar == "y":
                                 print("\nKeluar dari Program - Terima Kasih sudah menggunakan KAMI Apps :)\n")
                                 exit()
                              elif keluar == "n":
                                 print("Kembali ke Menu Utama")
                                 break
                              else:
                                 print("Silahkan Pilih (Y) atau (N)") 
                        else:
                           print("Menu Tidak Ditemukan / Angka yang anda masukkan salah !!")
                     except ValueError:
                        print("Yang anda masukkan Bukan Angka !!")      
# NOMOR 3 (EXIT)
      elif login == 3:
         print("3. Keluar Aplikasi (Exit)")
         while True:
               k = input("Apakah anda yakin ingin keluar dari Program? Pilih Yes (Y) atau No (N) : ")
               keluar = k.lower()
               if keluar == "y":
                  print("\nKeluar dari Program - Terima Kasih sudah menggunakan KAMI Apps :)\n")
                  exit()
               elif keluar == "n":
                  print("Kembali ke Menu Utama")
                  break
               else:
                  print("Silahkan Pilih (Y) atau (N)") 
      else:
         print("Menu Tidak Ditemukan / Angka yang anda masukkan salah !!")
   except ValueError:
      print("Yang anda masukkan Bukan Angka !!")