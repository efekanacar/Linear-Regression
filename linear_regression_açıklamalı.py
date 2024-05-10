import numpy as np

def least_squares_fit(x, y):
    # Veri setinin boyutunu al
    n = len(x)
    # x değerlerinin toplamını hesapla
    sum_x = np.sum(x)
    # y değerlerinin toplamını hesapla
    sum_y = np.sum(y)
    # x değerlerinin karelerinin toplamını hesapla
    sum_x_squared = np.sum(x**2)
    # x ve y değerlerinin çarpımlarının toplamını hesapla
    sum_xy = np.sum(x*y)

    # Eğimi hesapla
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)

    # Y-eksenini kestiği noktayı hesapla
    intercept = (sum_y - slope * sum_x) / n

    return slope, intercept

def main():
    try:
        # Dosyadan x ve y değerlerini okutma
        data = np.loadtxt('data.txt')
        x = data[0, :]  # İlk satır x değerlerini içerir
        y = data[1, :]  # İkinci satır y değerlerini içerir

        # En küçük kareler yöntemiyle eğimi ve kesim noktasını hesapla
        slope, intercept = least_squares_fit(x, y)

        # Elde edilen modeli ekrana yazdır
        print("Oluşturulan Model:")
        print("y =", slope, "x +", intercept)

        # Kullanıcıdan tahmin etmek istediği x değerini al
        x_value = float(input("Tahmin etmek istediğiniz x değeri: "))

        # Tahmini y değerini hesapla
        predicted_y = slope * x_value + intercept
        print("Tahmini y değeri:", predicted_y)
    except FileNotFoundError:
        print("Dosya bulunamadı.")

if __name__ == "__main__":
    main()