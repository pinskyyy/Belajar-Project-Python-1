# Import dataclasses for dataclass structure
from dataclasses import dataclass
# Import display for display pandas dataframe
from IPython.display import display
# Import pandas with inisial pd
import pandas as pd

@dataclass
class Transaction():
    pass
    # Membuat dictionary kosong untuk menampung item
    keranjang = {}
    # Assign some object for sub total basket
    total_bayar = 0
    # Method add items, untuk menambahkan item, qty, dan harga            
    def add_items(self, nama, qty, harga):
            print(f'Item {nama} berhasil ditambahkan ke dalam keranjang!')
            self.keranjang[nama] = [qty,harga]
            sub_total = qty * harga
            self.total_bayar += sub_total
    # Method update item name, untuk mengganti nama pada dictionary basket
    def update_item_name(self, nama_lama, nama_baru):
        self.keranjang[nama_baru] = self.keranjang[nama_lama]
        print(f'{nama_lama} berhasil diupdate menjadi {nama_baru}')
        del self.keranjang[nama_lama]
    # Method update qty item, untuk mengganti qty pada dictonary value
    def update_qty_item(self, nama, qty_baru):
        self.keranjang[nama][0] = qty_baru
        print(f'Qty {nama} berhasil diupdate menjadi {qty_baru}')
    # Method update price item, untuk mengganti harga pada dictonary value   
    def update_price_item(self, nama, harga_baru):
        self.keranjang[nama][1] = harga_baru
        print(f'Harga {nama} berhasil diupdate menjadi {harga_baru}')
    # Method delete item, untuk menghapus sebuah key pada dictionary serta valuesnya
    def delete_item(self, nama):
        print(f'{nama} berhasil dihapus!')
        del self.keranjang[nama]
    # Method reset trx, untuk menghapus seluruh key dan value pada dictionary
    def reset_trx(self):
        yakin = input("Apakah anda yakin ingin menghapus semua item?(y/n): ")
        if yakin == "y":
            self.keranjang.clear()
            self.total_bayar = 0
            print("Semua item berhasil direset")
        if yakin != "y":
            pass
    # Method check order, untuk menampilkan dictionary dengan bentuk dataframe
    def check_order(self):
        df = pd.DataFrame(self.keranjang,["Qty","Harga/item"])
        data = df.T
        data["Total"] = data["Qty"] * data["Harga/item"]
        display(data)
    # Method untuk menghitung total price berserta ketentuan diskonnya
    def total_price(self):
        discount = 0
        if self.total_bayar > 200_000 and self.total_bayar <= 300_000:
            discount = self.total_bayar * 0.05
        elif self.total_bayar > 300_000 and self.total_bayar < 500000:
            discount = self.total_bayar * 0.08
        elif self.total_bayar > 500000:
            discount = self.total_bayar * 0.10
        final_price = self.total_bayar - discount
        print(f'Item yang dibeli {self.keranjang}\nTotal yang harus dibayarkan adalah Rp {final_price}')