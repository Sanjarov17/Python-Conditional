soat = int(input("Soatni kiriting (0-23): "))

if 5 <= soat <= 11:
    print("Ertalab")
elif 12 <= soat <= 17:
    print("Kunduzi")
elif 18 <= soat <= 21:
    print("Kechqurun")
elif (22 <= soat <= 23) or (0 <= soat <= 4):
    print("Tun")
else:
    print("Noto'g'ri soat! (0-23 oralig'ida kiriting)")

