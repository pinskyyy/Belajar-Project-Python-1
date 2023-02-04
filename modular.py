from dataclasses import dataclass
from IPython.display import display
import pandas as pd

@dataclass
class Transaction():
    pass
    keranjang = {}
    total_bayar = 0
                
    def add_items(self, nama, qty, harga):
            print(f'Item {nama} berhasil ditambahkan ke dalam keranjang!')
            self.keranjang[nama] = [qty,harga]
            sub_total = qty * harga
            self.total_bayar += sub_total
        
    def update_item_name(self, nama_lama, nama_baru):
        self.keranjang[nama_baru] = self.keranjang[nama_lama]
        print(f'{nama_lama} berhasil diupdate menjadi {nama_baru}')
        del self.keranjang[nama_lama]
        
    def update_qty_item(self, nama, qty_baru):
        self.keranjang[nama][0] = qty_baru
        print(f'Qty {nama} berhasil diupdate menjadi {qty_baru}')
        
    def update_price_item(self, nama, harga_baru):
        self.keranjang[nama][1] = harga_baru
        print(f'Harga {nama} berhasil diupdate menjadi {harga_baru}')
        
    def delete_item(self, nama):
        print(f'{nama} berhasil dihapus!')
        del self.keranjang[nama]
        
    def reset_trx(self):
        yakin = input("Apakah anda yakin ingin menghapus semua item?(y/n): ")
        if yakin == "y":
            self.keranjang.clear()
            print("Semua item berhasil direset")
        if yakin != "y":
            pass
    def check_order(self):
        df = pd.DataFrame(self.keranjang,["Qty","Harga/item"])
        data = df.T
        data["Total"] = data["Qty"] * data["Harga/item"]
        display(data)
        
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