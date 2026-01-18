# -*- coding: utf-8 -*-
"""
Grafik çizim fonksiyonları
"""
import matplotlib.pyplot as plt
def plot_time(t, x_raw, x_filt, save_path):
    """
    Ham ve filtrelenmiş sinyali zaman domeninde çizer

    Parametreler:
        t        : zaman vektörü
        x_raw   : ham sinyal
        x_filt  : filtrelenmiş sinyal
        save_path : kayıt edilecek dosya yolu
    """
    # TODO:
    # matplotlib kullanarak:
    # - iki sinyali aynı grafikte çiz
    # - eksen isimleri ve başlık ekle
    # - grafiği dosyaya kaydet
    plt.figure(figsize=(10, 5))

    plt.plot(t, x_raw, label="Ham Sinyal")

    plt.plot(t, x_filt, label="Filtrelenmiş Sinyal")

    plt.xlabel("Zaman (s)")
    plt.ylabel("Genlik")
    plt.title("Zaman Domeninde Sinyal")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()