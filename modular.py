from dataclasses import dataclass
from IPython.display import display
import pandas as pd

@dataclass
class Transaction():
    pass
    keranjang = {}
    total_bayar = 0
                
    def add_items(self):
        while True:
            a = input("Masukan nama barang: ")
            b = int(input("Masukan qty barang: "))
            c = int(input("Masukan harga barang: "))
            print(f'Item {a} berhasil ditambahkan ke dalam keranjang!')
            self.keranjang[a] = [b,c]
            sub_total = b * c
            self.total_bayar += sub_total
            lagi = input("Ingin menambah item lagi? (y/n): ")
            if lagi != "y":
                user.menu()
        
    def update_item_name(self):
        nama_lama = input("Masukan nama barang yang ingin anda update: ")
        nama_baru = input("Masukan nama barang terbaru: ")
        self.keranjang[nama_baru] = self.keranjang[nama_lama]
        print(f'{nama_lama} berhasil diupdate menjadi {nama_baru}')
        del self.keranjang[nama_lama]
        user.menu()
        
    def update_qty_item(self):
        a = input("Masukan nama barang yang ingin anda update qty nya: ")
        qty_baru = int(input("Masukan qty terbaru: "))
        self.keranjang[a][0] = qty_baru
        print(f'Qty {a} berhasil diupdate menjadi {qty_baru}')
        user.menu()
        
    def update_price_item(self):
        a = input("Masukan nama barang yang ingin anda update qty nya: ")
        price_baru = int(input("Masukan harga terbaru: "))
        self.keranjang[a][1] = price_baru
        print(f'Harga {a} berhasil diupdate menjadi {price_baru}')
        user.menu()
        
    def delete_item(self):
        a = input("Masukan nama barang yang ingin anda hapus: ")
        print(f'{a} berhasil dihapus!')
        del self.keranjang[a]
        user.menu()
        
    def reset_trx(self):
        yakin = input("Apakah anda yakin ingin menghapus semua item?(y/n): ")
        if yakin == "y":
            self.keranjang.clear()
            print("Semua item berhasil direset")
        if yakin != "y":
            user.menu()
    def check_order(self):
        df = pd.DataFrame(self.keranjang,["Qty","Harga/item"])
        data = df.T
        data["Total"] = data["Qty"] * data["Harga/item"]
        display(data)

        user.menu()
        
    def total_price(self):
        discount = 0
        if self.total_bayar > 200000 and self.total_bayar < 300000:
            discount = self.total_bayar * 0.05
        elif self.total_bayar > 300000 and self.total_bayar < 500000:
            discount = self.total_bayar * 0.08
        elif self.total_bayar > 500000:
            discount = self.total_bayar * 0.10
        final_price = self.total_bayar - discount
        print(f'Item yang dibeli {self.keranjang}\nTotal yang harus dibayarkan adalah Rp {final_price}')
        
        user.menu()

    def exit(self):
        print("Terimakasih telah berbelanja!")
        return

    def test(self):
        subtotal = self.keranjang.keys[0]
        print(subtotal)

    def menu(self):
        print('-'*40)
        print(" Super Cashier".center(40,'='))
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
            user.add_items()
        elif pilihan == "2":
            user.update_item_name()
        elif pilihan == "3":
            user.update_qty_item()
        elif pilihan == "4":
            user.update_price_item()
        elif pilihan == "5":
            user.delete_item()
        elif pilihan == "6":
            user.reset_trx()
        elif pilihan == "7":
            user.check_order()
        elif pilihan == "8":
            user.total_price()
        elif pilihan == "9":
            user.exit()
        elif pilihan == "10":
            user.test()
        else:
            print("Masukan hanya dengan angka menu yang tersedia!")

user = Transaction()