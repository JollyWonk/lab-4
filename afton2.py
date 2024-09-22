import sys

def pyramid_volume(a, b, h):
    base_area = a * b
    volume = (1/3) * base_area * h
    return volume

try:
    a = float(input("Введіть довжину першої сторони прямокутної основи: "))
    b = float(input("Введіть довжину другої сторони прямокутної основи: "))
    h = float(input("Введіть висоту піраміди: "))

    if a <= 0 or b <= 0 or h <= 0:
        print("Сторони основи та висота повинні бути додатними числами.")
        sys.exit(1) 
except ValueError:
    print("Введіть правильні числові значення.")
    sys.exit(1)  

volume = pyramid_volume(a, b, h)
print(f"Об'єм піраміди: {volume:.2f}")
