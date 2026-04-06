# 🧩 Maze Solver BFS (Animasi Pencarian Jalur)

## 📌 Deskripsi

Program ini merupakan implementasi algoritma **Breadth-First Search (BFS)** untuk mencari jalur terpendek pada sebuah labirin dari titik awal (`.`) menuju titik tujuan (`E`).

Program dilengkapi dengan **animasi visual menggunakan Matplotlib**, sehingga proses pencarian jalur dapat terlihat secara bertahap, mulai dari eksplorasi hingga menemukan solusi.

---

## 🎯 Tujuan

* Memahami konsep algoritma BFS
* Mengimplementasikan pencarian jalur (pathfinding)
* Memvisualisasikan proses algoritma dalam bentuk animasi
* Menyelesaikan tugas praktikum pencarian jalur pada labirin

---

## ⚙️ Teknologi yang Digunakan

* **Python 3**
* **Matplotlib** → visualisasi animasi
* **NumPy** → pengolahan array/grid
* **Collections (deque)** → struktur data BFS

---

## 🧠 Konsep Algoritma

Algoritma yang digunakan adalah **Breadth-First Search (BFS)**, yang bekerja dengan cara:

1. Menelusuri node secara melebar (level per level)
2. Menjamin menemukan **jalur terpendek**
3. Menggunakan struktur data **queue**

---

## 🗺️ Representasi Labirin

Labirin direpresentasikan dalam bentuk grid dengan simbol:

| Simbol  | Arti                     |
| ------- | ------------------------ |
| `#`     | Dinding                  |
| `.`     | Titik awal               |
| `E`     | Titik tujuan             |
| (spasi) | Jalur yang bisa dilewati |

---

## 🎨 Keterangan Warna Animasi

| Warna         | Keterangan                   |
| ------------- | ---------------------------- |
| 🔵 Biru Tua   | Dinding                      |
| ⚪ Putih       | Jalur                        |
| 🟩 Hijau Muda | Node yang sudah dieksplorasi |
| 🟦 Cyan       | Posisi saat ini              |
| 🟨 Kuning     | Jalur solusi                 |
| 🟢 Hijau      | Start                        |
| 🟧 Oranye     | End                          |

---

## ▶️ Cara Menjalankan

### 1. Install dependency

```bash
pip install matplotlib numpy
```

### 2. Jalankan program

```bash
python nama_file.py
```

---

## 📊 Alur Program

1. Membaca dan mengubah maze menjadi grid
2. Menentukan titik awal dan tujuan
3. Menjalankan algoritma BFS
4. Menyimpan jalur dan node yang dikunjungi
5. Menampilkan animasi:

   * 🔍 Eksplorasi BFS
   * ✅ Jalur solusi

---

## 📈 Output

Program akan menampilkan:

* Animasi proses pencarian
* Jalur terpendek dari `.` ke `E`
* Informasi jumlah langkah dan eksplorasi

---

## ✨ Keunggulan Program

* Visualisasi interaktif dan mudah dipahami
* Menggunakan algoritma BFS (optimal untuk shortest path)
* Struktur kode modular dan mudah dikembangkan
* Dapat dimodifikasi untuk berbagai bentuk labirin

---

## 🚀 Pengembangan Selanjutnya

* Menggunakan algoritma **A*** untuk efisiensi lebih tinggi
* Menambahkan GUI (Pygame / Tkinter)
* Export animasi menjadi GIF atau video
* Input maze dari file eksternal

---

## 👨‍💻 Author

**Muhammad Dava D.**

---

## 📌 Catatan

Program ini dibuat untuk memenuhi **Tugas Praktikum Pencarian Jalur (Maze Solver)** dengan animasi BFS dari titik awal ke tujuan.
