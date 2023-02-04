from modular import Transaction

print("Selamat datang di Cashier Pacmann".center(40,'='))
user = input("Masukan nama Anda: ")
user = Transaction()

while True:
    print('-'*40)
    print(" Super Cashier ".center(40,'='))
    print('-'*40)
    print("1. Add Item")
    print("2. Update Item Name")
    print("3. Update Item Quantity")
    print("4. Update Item Price")
    print("5. Delete Item")
    print("6. Reset Trx")
    print("7. Check Order")
    print("8. Calculate Total Price")
    print("9. Exit")
    print('-'*40)

    pilihan = input("Masukan Pilihan Anda = ")
    if pilihan == "1":
        nama = input("Masukan nama barang: ")
        qty = int(input("Masukan qty barang: "))
        harga = int(input("Masukan harga barang: "))
        user.add_items(nama, qty, harga)
    elif pilihan == "2":
        nama_lama = input("Masukan nama barang yang ingin anda update: ")
        nama_baru = input("Masukan nama barang terbaru: ")
        user.update_item_name(nama_lama, nama_baru)
    elif pilihan == "3":
        nama = input("Masukan nama barang yang ingin anda update qty nya: ")
        qty_baru = int(input("Masukan qty terbaru: "))
        user.update_qty_item(nama, qty_baru)
    elif pilihan == "4":
        nama = input("Masukan nama barang yang ingin anda update qty nya: ")
        harga_baru = int(input("Masukan harga terbaru: "))
        user.update_price_item(nama, harga_baru)
    elif pilihan == "5":
        nama = input("Masukan nama barang yang ingin anda hapus: ")
        user.delete_item(nama)
    elif pilihan == "6":
        user.reset_trx()
    elif pilihan == "7":
        user.check_order()
    elif pilihan == "8":
        user.total_price()
    elif pilihan == "9":
        print("Terimakasih telah berbelanja di Pacmann Cashier")
        break
    else:
        print("Masukan hanya dengan angka menu yang tersedia!")