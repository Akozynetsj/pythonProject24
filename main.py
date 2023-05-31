import math


def calculate_hexagonal_pyramid_volume():
    a = float(input("Введіть довжину сторони основи (a): "))
    h = float(input("Введіть висоту піраміди (h): "))
    volume = (3 * math.sqrt(3) / 2) * a ** 2 * h
    return volume
pyramid_volume = calculate_hexagonal_pyramid_volume()
print(f"Об'єм шестикутної піраміди: {pyramid_volume}")

