#BEBEK LEPAS
#PROGRAM KASIR POSTEST3

pilihan = "YA"
while pilihan == "YA":
    print("""
    ------------------------------------------------
    ----------- MENU DI RM BEBEK LEPAS -------------
    ------------------------------------------------

        MAKANAN: 1. Ayam Bakar      Rp25.000
                 2. Ayam Geprek     Rp20.000
                 3. Ayam Goreng     Rp10.000
                 4. Ayam Guling     Rp30.000
  
    -----------------PROMO MINGGUAN------------------
             DISKON TIAP HARI SENIN DAN JUMAT  
    -------------------------------------------------""")

    pembeli = input("Masukkan Nama Pelanggan: ") 
    def total(harga,jumlah):
        return(harga*jumlah) 
    print ("1. ayam bakar")
    print ("2. ayam geprek")
    print ("3. ayam goreng")
    print ("4. ayam guling")
    menu  = int(input("pilih kode menu yang diinginkan: "))
    if    menu == 1 :
          print("ayam bakar 25000")
          menu = 25000
    elif  menu == 2 :
          print ("ayam geprek 20000")
          menu = 20000
    elif  menu == 3 : 
          print ("ayam goreng 10000")
          menu = 10000
    elif  menu == 4 :
          print ("ayam guling 30000")
          menu == 30000 
    else:
          while True :
             print("maaf menu tidak ada")
             menu  = int(input("pilih kode menu yang diinginkan: "))
             if   menu == 1 or menu == 2 or menu == 3 or menu == 4 :
                  if    menu == 1 :
                        print("ayam bakar 25000")
                        menu = 25000
                  elif  menu == 2 :
                        print ("ayam geprek 20000")
                        menu = 20000
                  elif  menu == 3 : 
                        print ("ayam goreng 10000")
                        menu = 10000
                  elif  menu == 4 :
                        print ("ayam guling 30000")
                        menu == 30000 
                  break

    
    Jumlah = int(input("masukan jumlah menu yang dibeli: "))
    Total = menu*Jumlah 
    Hari = input('masukan hari pembelian: ')
    
    if Hari == 'senin':
          diskon = 0.1*Total
          print('-Diskon 10 %-')

    elif Hari == 'jumat':
          diskon = 0.25*Total
          print('-Diskon 25 %-')

    else:
          diskon = 0
          print('maaf,tidak dapat diskon')

    totalbayar=int(Total-diskon)

    uang = int(input("Uang Tunai Pembeli: Rp"))
    kembalian = int(uang - totalbayar)
    print(f"Kembalian: Rp{kembalian}")

    print(f"""
    --------------------------------------------------
    ----------------- S T R U K   B E L I ------------
    --------------------------------------------------
    Nama          : {pembeli}
    Beli          :  {menu} porsi {Jumlah}
    Total         : Rp{Total}
    Diskon        : - Rp{diskon}
    Total Tagihan : Rp{totalbayar}
    Uang          : Rp{uang}
    Kembalian     : Rp{kembalian}
    --------------------------------------------------
        Terima Kasih Telah Makan DI RM BEBEK LEPAS
    --------------------------------------------------
    """)
    pilihan=input("Apakah anda ingin Membeli Tambahan YA/TIDAK= ")
pilihan="TIDAK"
print('Terima Kasih Telah Makan Di RM BEBEK LEPAS')