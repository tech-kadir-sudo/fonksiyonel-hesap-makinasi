import tkinter as tk
from tkinter import messagebox
import math


def toggle_entry():
    secim = var_secim.get()
    if secim in [6, 7]:  # Karekök ve faktöriyel için ikinci giriş kutusunu gizle
        entry2.pack_forget()
    else:
        entry2.pack()


def hesapla():
    try:
        secim = var_secim.get()
        # Girişlerin kontrol edilmesi
        if secim in [6, 7]:  # Karekök ve Faktöriyel için sadece bir giriş gerekir
            x = entry1.get().strip()
            if not x or not x.replace('.', '', 1).isdigit():
                messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")
                return

            if secim == 6:  # Karekök
                k = float(x)
                sonuc = karekok(k)

            elif secim == 7:  # Faktoriyel
                z = int(float(x))
                sonuc = faktoriyel(z)

        else:
            x = entry1.get().strip()
            y = entry2.get().strip()

            if not x or not x.replace('.', '', 1).isdigit():
                messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")
                return

            if not y or not y.replace('.', '', 1).isdigit():
                messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")
                return

            x = float(x)
            y = float(y)

            if secim == 1:  # Toplama
                sonuc = toplama(x, y)

            elif secim == 2:  # Çıkarma
                sonuc = cikarma(x, y)

            elif secim == 3:  # Çarpma
                sonuc = carpma(x, y)

            elif secim == 4:  # Bölme
                sonuc = bolme(x, y)

            elif secim == 5:  # Üs alma
                taban = x
                us = int(y)
                sonuc = us_alma(taban, us)

            elif secim == 8:  # Logaritma
                sonuc = logaritma(x)

            elif secim == 9:  # Kombinasyon
                n = int(x)
                p = int(y)
                sonuc = kombinasyon(n, p)

            elif secim == 10:  # Permütasyon
                n = int(x)
                r = int(y)
                sonuc = permutasyon(n, r)

            elif secim == 11:  # EBOB
                e = int(x)
                f = int(y)
                sonuc = ebob(e, f)

            elif secim == 12:  # EKOK
                o = int(x)
                ö = int(y)
                sonuc = ekok(o, ö)

            elif secim == 13:  # Sinüs
                aci = float(x)
                sonuc = sin_fonksiyonu(aci)

            elif secim == 14:  # Kosinüs
                aci = float(x)
                sonuc = cos_fonksiyonu(aci)

            elif secim == 15:  # Tanjant
                aci = float(x)
                sonuc = tan_fonksiyonu(aci)

            elif secim == 16:  # Cotanjant
                aci = float(x)
                sonuc = cot_fonksiyonu(aci)

        messagebox.showinfo("Sonuç", f"Sonuç: {sonuc}")

    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")


# Fonksiyonlar
def toplama(x, y):
    return x + y


def cikarma(x, y):
    return x - y


def carpma(x, y):
    return x * y


def bolme(x, y):
    if y == 0:
        messagebox.showerror("Hata", "Bu ifade tanımsızdır")
        return None
    return x / y


def us_alma(taban, us):
    if taban == 0 and us == 0:
        messagebox.showerror("Hata", "Bu ifade belirsizdir")
        return None
    return taban ** us


def faktoriyel(z):
    if z < 0:
        messagebox.showerror("Hata", "Lütfen pozitif bir değer giriniz.")
        return None
    return math.factorial(z)


def karekok(k):
    if k < 0:
        messagebox.showerror("Hata", "Negatif sayının karekökü alınamaz.")
        return None
    return math.sqrt(k)


def logaritma(l):
    if l <= 0:
        messagebox.showerror("Hata", "0 ve negatif sayının logaritması alınamaz.")
        return None
    return math.log(l)


def kombinasyon(n, p):
    if p > n:
        messagebox.showerror("Hata", "p değeri n'den büyük olamaz.")
        return None
    return math.comb(n, p)


def permutasyon(n, r):
    if r > n:
        messagebox.showerror("Hata", "r değeri n'den büyük olamaz.")
        return None
    return math.perm(n, r)


def ebob(e, f):
    return math.gcd(e, f)


def ekok(o, ö):
    return math.lcm(o, ö)


def sin_fonksiyonu(aci):
    return math.sin(math.radians(aci))


def cos_fonksiyonu(aci):
    return math.cos(math.radians(aci))


def tan_fonksiyonu(aci):
    return math.tan(math.radians(aci))


def cot_fonksiyonu(aci):
    tan_deger = math.tan(math.radians(aci))
    if tan_deger == 0:  # Tanjantın sıfır olduğu durum
        messagebox.showerror("Hata", "Cotanjant tanjantın sıfır olduğu bir noktada tanımsızdır.")
        return None
    return 1 / tan_deger


# Tkinter GUI oluşturma
root = tk.Tk()
root.title("Hesap Makinesi")

var_secim = tk.IntVar()
tk.Label(root, text="Yapmak istediğiniz işlemi seçin:").pack()

operations = [
    "Toplama", "Çıkarma", "Çarpma", "Bölme",
    "Üs alma", "Karekök", "Faktöriyel", "Logaritma",
    "Kombinasyon", "Permütasyon", "EBOB", "EKOK",
    "Sinüs", "Kosinüs", "Tanjant", "Cotanjant"
]

for index, operation in enumerate(operations):
    tk.Radiobutton(root, text=operation, variable=var_secim, value=index + 1, command=toggle_entry).pack(anchor=tk.W)

# Giriş kutularını büyütmek
entry1 = tk.Entry(root, width=30, font=("Arial", 14))  # Genişlik ve yazı tipi
entry1.pack(pady=10)  # Üstte biraz boşluk bırakmak için

entry2 = tk.Entry(root, width=30, font=("Arial", 14))  # Genişlik ve yazı tipi
entry2.pack(pady=10)  # Üstte biraz boşluk bırakmak için

entry1.insert(0, "Birinci Değer")
entry2.insert(0, "İkinci Değer (varsa)")

tk.Button(root, text="Hesapla", command=hesapla).pack(pady=10)  # Üstte biraz boşluk bırakmak için
tk.Button(root, text="Çıkış", command=root.quit).pack(pady=10)  # Üstte biraz boşluk bırakmak için

root.mainloop()
