# -*- coding: utf-8 -*-
"""
CSV dosyasından sinyal verisi okuma yardımcı fonksiyonları
"""
import csv
import numpy as np
def load_signal_csv(path):
    """
    CSV formatı:
    t,x
    0.0, 1.23
    0.01, 1.10
    ...

    Parametre:
        path (str): CSV dosya yolu

    Dönen:
        t : zaman vektörü
        x : sinyal vektörü
    """
    # TODO:
    # 1. csv modülünü kullan
    # 2. dosyayı satır satır oku
    # 3. t ve x listelerini doldur
    # 4. numpy array olarak döndür
    t = []
    x = []

    file = open(path, "r")
    reader = csv.reader(file)

    next(reader)  

    for row in reader:
        t.append(float(row[0]))
        x.append(float(row[1]))

    file.close()

    return np.array(t), np.array(x)
