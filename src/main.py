"""
Ana çalışma dosyası
Öğrenciler bu dosyayı çalıştıracaktır.
"""
from io_utils import load_signal_csv
from analysis import sampling_rate, basic_stats
from signal_tools import moving_average
from plotting import plot_time

def main():
    # TODO:
    # 1. CSV dosyasını oku
    # 2. örnekleme frekansını hesapla
    # 3. temel istatistikleri yazdır
    # 4. hareketli ortalama filtresi uygula
    # 5. sonucu çizdir


    t, x = load_signal_csv("data/sample_signal.csv")
    fs = sampling_rate(t)
    print("Ornekleme frekansi:", fs)
    stats = basic_stats(x)
    print("Temel istatistikler:")
    for key in stats:
        print(key, ":", stats[key])

    x_filt = moving_average(x, 5)


    plot_time(t, x, x_filt, "report/figures/time_signal.png")


if __name__ == "__main__":
    main()
