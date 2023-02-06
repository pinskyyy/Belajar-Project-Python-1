# Import class berserta methodnya dari file modular
from modular import Transaction

print("Selamat datang di Cashier Pacmann".center(40,'='))
# Membuat object dari class dengan menggunakan nama user
user = input("Silakan masukan nama Anda: ")
user = Transaction()

while True:
    print('-'*40)
    print(" Super Cashier ".center(40,'='))
    print('-'*40)
    print(f' Menu '. center(40,'='))
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
    # Membuat pilihan menu
    pilihan = input("Masukan Pilihan Anda = ")

    # Function add items
    if pilihan == "1":
        nama = input("Masukan nama barang: ")
        qty = int(input("Masukan qty barang: "))
        harga = int(input("Masukan harga barang: "))
        # Recall method add items from modular.py with object already filled
        user.add_items(nama, qty, harga)
    # Function Update Item Name
    elif pilihan == "2":
        nama_lama = input("Masukan nama barang yang ingin anda update: ")
        nama_baru = input("Masukan nama barang terbaru: ")
        # Recall method update item name from modular.py with object already filled
        user.update_item_name(nama_lama, nama_baru)
    # Function Update Item Quantity
    elif pilihan == "3":
        nama = input("Masukan nama barang yang ingin anda update qty nya: ")
        qty_baru = int(input("Masukan qty terbaru: "))
        # Recall method update qty item from modular.py with object already filled
        user.update_qty_item(nama, qty_baru)
    # Function Update Item Price
    elif pilihan == "4":
        nama = input("Masukan nama barang yang ingin anda update qty nya: ")
        harga_baru = int(input("Masukan harga terbaru: "))
        # Recall method update price item from modular.py with object already filled
        user.update_price_item(nama, harga_baru)
    # Function Delete Item
    elif pilihan == "5":
        nama = input("Masukan nama barang yang ingin anda hapus: ")
        # Recall method delete item from modular.py with object already filled
        user.delete_item(nama)
    # Function Reset Trx
    elif pilihan == "6":
        # Recall method reset trx from modular.py with object already filled
        user.reset_trx()
    # Function Check Order
    elif pilihan == "7":
        # Recall method check order from modular.py with object already filled
        user.check_order()
    # Function Calculate Total Price
    elif pilihan == "8":
        # Recall method total price from modular.py with object already filled
        user.total_price()
    # Function Exit for end the menu
    elif pilihan == "9":
        print("Terimakasih telah berbelanja di Pacmann Cashier")
        break
    else:
        print("Masukan hanya dengan angka menu yang tersedia!")