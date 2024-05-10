import numpy as np

def least_squares_fit(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x_squared = np.sum(x**2)
    sum_xy = np.sum(x*y)

    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)

    intercept = (sum_y - slope * sum_x) / n

    return slope, intercept

def main():
    try:
        data = np.loadtxt('data.txt')
        x = data[0, :]
        y = data[1, :]

        slope, intercept = least_squares_fit(x, y)

        print("Oluşturulan Model:")
        print("y =", slope, "x +", intercept)

        x_value = float(input("Tahmin etmek istediğiniz x değeri: "))

        predicted_y = slope * x_value + intercept
        print("Tahmini y değeri:", predicted_y)
    except FileNotFoundError:
        print("Dosya bulunamadı.")

if __name__ == "__main__":
    main()
