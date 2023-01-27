from dataclasses import dataclass
from IPython.display import display
import pandas as pd

@dataclass
class Transaction():
    pass
    keranjang = {}
    total_bayar = 0
                
    def add_items(self, a, b, c):
        self.keranjang[a] = [b,c]
        sub_total = b * c
        self.total_bayar += sub_total
        print(f'Item {self.keranjang} berhasil ditambahkan ke dalam keranjang!')
        
    def update_item_name(self, a, x):
        self.keranjang[x] = self.keranjang[a]
        print(f'{a} berhasil diupdate menjadi {x}')
        del self.keranjang[a]
        
    def update_qty_item(self, a, qty_baru):
        self.keranjang[a][0] = qty_baru
        print(f'Qty {a} berhasil diupdate menjadi {qty_baru}')
        
    def update_price_item(self, a, new_price):
        self.keranjang[a][1] = new_price
        print(f'Harga {a} berhasil diupdate menjadi {new_price}')
        
    def delete_item(self, a):
        print(f'{a} berhasil dihapus!')
        del self.keranjang[a]
        
    def reset_trx(self):
        yakin = input("Apakah anda yakin ingin menghapus semua item?(y/n): ")
        if yakin == "y":
            self.keranjang.clear()
            print("Semua item berhasil direset")
        if yakin != "y":
            return
    def check_order(self):
        df = pd.DataFrame(self.keranjang,["Qty","Harga/item"])
        data = df.T
        data["Total"] = data["Qty"] * data["Harga/item"]
        display(data)
        
    def total_price(self):
        print(f'Item yang dibeli {self.keranjang}\nTotal yang harus dibayarkan adalah Rp {self.total_bayar}')        