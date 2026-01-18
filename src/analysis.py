# -*- coding: utf-8 -*-
"""
Temel sinyal analiz fonksiyonları
"""
import numpy as np

def sampling_rate(t):
    """
    Zaman vektöründen örnekleme frekansını hesaplar

    Parametre:
        t : zaman vektörü

    Dönen:
        fs : örnekleme frekansı (Hz)
    """
    # TODO:
    # 1. ardışık iki zaman örneği arasındaki farkı hesapla
    # 2. fs = 1 / dt
    passt = np.asarray(t)

    dt = t[1] - t[0]
    fs = 1.0 / dt

    return fs


def basic_stats(x):
    """
    Sinyal için temel istatistikleri hesaplar

    Parametre:
        x : sinyal vektörü

    Dönen:
        stats (dict):
            mean
            std
            rms
            min
            max
    """
    # TODO:
    # numpy kullanarak gerekli istatistikleri hesapla
    return {
        "mean": np.mean(x),
        "std": np.std(x),
        "rms": np.sqrt(np.mean(x ** 2)),
        "min": np.min(x),
        "max": np.max(x)
    }
