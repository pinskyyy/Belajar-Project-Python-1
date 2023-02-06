# *CASHIER - Project*

## *Latar Belakang*
Cashier adalah program kasir sederhana yang berfungsi untuk menyimpan atribut data dan menghitung sub total maupun grand total dari atribut tersebut.

## *Flow Chart*
![Flowchart](/img/Chasier%20Flowchart.png)

## *Tujuan Pengerjaan*
1. Membuat Aplikasi Cashier sederhana yang dapat melakukan tugas:
    * Membuat list keranjang belanja
    * Update nama barang
    * Update quantity barang
    * Update harga barang
    * Menghapus barang dari keranjanga belanja
    * Reset keranjang belanja
    * Melihat keranjang belanja
    * Menghitung total belanja dengan diskon
2. Mengaplikasikan pembuatan program yang berbasis fungsi dan objek
3. Mengaplikasikan penulisan kode yang bersih dan menggunakan modular code

## *Deskripsi Function*

* Function 'Item Name' berfungsi untuk menambahkan barang dengan parameter sebagai berikut :
    - nama = 'string' | nama barang yang akan dibeli
    - qty = 'int' | jumlah quantity barang yang akan dibeli
    - harga = 'int' | harga barang yang akan dibeli

* Function 'Update Item Name' berfungsi untuk mengganti nama barang yang sudah terinput di dalam keranjang, dengan parameter sebagai berikut :
    - nama_lama = 'string' | nama barang yang akan diganti
    - nama_baru = 'string' | nama baru yang diinginkan dari sebuah barang

* Function 'Update Item Qty' berfunsi untuk mengganti quantity barang yang sudah terinput di dalam keranjang, dengan parameter sebagai berikut :
    - nama = 'string' | nama barang yang akan diganti quantitynya
    - qty_baru = 'int' | quantity baru yang diinginkan dari barang

* Function 'Update Item Price' berfungsi untuk mengganti harga barang yang sudah terinput di dalam keranjang, dengan parameter sebagai berikut :
    - nama = 'string' | nama barang yang akan diganti harganya
    - harga_baru = 'int' | harga baru yang diinginkan dari barang

* Function 'Delete Item' berfungsi untuk menghapus barang beserta quantity dan harganya, dengan parameter sebagai berikut :
    - nama = 'string' | nama barang yang akan dihapus

* Function 'Reset Trx' berfungsi untuk menghapus semua barang yang sudah terinput di dalam keranjang

* Function 'Check Order' berfungsi untuk menampilkan semua atribut yang berada di keranjang dengan tampilan dataframe

* Function 'Total Price' berfungsi untuk menampilkan semua atribut yang berada di keranjang dan menghitung dari total harga (berserta dengan keadaan diskon)
    - Diskon 5% untuk total belanja Rp 200.000 - Rp 300.000
    - Diskon 8% untuk total belanja Rp 300.001 - Rp 499.999
    - Diskon 10% untuk total belanja >= Rp 500,000

* Function 'Exit' berfungsi untuk keluar dari menu utama
## *Cara Menggunakan Program*

1. Download semua file dan simpan dalam satu direktori yang sama.
2. Jalankan module 'Modular.py' di terminal.
3. Jalankan module 'Main.py' di terminal.
4. Untuk pertama kali, masukan nama user.
5. Pilih menu yang tersedia.

## *Hasil Test Case*

1. Menambahkan barang keranjang
    * Menambahkan item Ayam Goreng dengan quantity 2 harga 20000
    ![Case 1](/img/Case%201.1.png)

    * Menambahkan item Pasta Gigi dengan quantity 3 harga 15000
    ![Case 1](/img/Case%201.2.png)

2. Menghapus barang di keranjang
    * Menghapus barang (beserta dengan quantity dan harganya)
    ![Case 2](/img/Case%202.1.png)

    * Bukti bahwa barang sudah terhapus
    ![Case 2](/img/Case%202.2.png)

3. Reset semua barang di keranjang
    * Menghapus semua nama barang (beserta dengan quantity dan harganya)
    ![Case 3](/img/Case%203.png)

4. Menampilkan total yang harus dibayarkan
    * Barang yang ada di keranjang
    ![Case 4](/img/Case%204.1.png)

    * Total yang harus dibayarkan berserta nama barang
    ![Case 4](/img/Case%204.2.png)
