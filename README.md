# TUGAS DAY 2 Forward Kinematics

## PROFIL

Nama: Salma Karimah Kamal

NIM: 25/556423/TK/62761

## DESKRIPSI
Program berbasis Python ini dirancang untuk menghitung *Forward Kinematics* pada 2 derajat kebebasan (2-DoF). Program ini menghitung posisi koordinat kartesian akhir (*end-effector*) pada sumbu x dan y.

## FITUR YANG DIIMPLEMENTASIKAN

### Fitur Wajib
- Forward Kinematics 2-DoF
- Input Parameter 
- Output Koordinat endeffector

### Fitur Bonus

- Spatial Kinematics (Perhitungan posisi dalam koordinat 3D)
- Visualisasi matplotlib
- Mathematical Proof 
- Homogeneous Transformation

## FILES

### FK2DoF.py
- Forward Kinemtics 2-DoF (program base)
- sudah ada implementasi matplotlib

### FK3D4DoF.py
- Forward Kinemtics 3D 4-DoF (4-DoF karena ada rotasi pada base femur dan base tibia)
- sudah ada implementasi matplotlib

### FK3D4DoF.py
- Forward Kinemtics Homogenous Transformation (sama dengan FK3D4DoF.py tetapi menggunakan matriks)
- sudah ada implementasi matplotlib


## CARA MENJALANKAN PROGRAM

### 1. Prasyarat

Pastikan Python 3 telah terpasang pada sistem.

### 2. Kloning Repositori atau Akses Direktori

Buka terminal dan arahkan ke direktori repositori:

```bash
cd /path/to/your/repository/directory
```

### 3. Instalasi Dependensi

Program menggunakan library Matplotlib dan numpy.

Instal dependensi menggunakan perintah:

```bash
pip install -r requirements.txt
```

### 4. Menjalankan Program

Jalankan program melalui terminal, contoh:

```bash
python3 FK3D4DoF.py
```