vazn = float(input("Vazningizni kiriting (kg): "))
boy = float(input("Bo'yingizni kiriting (m): "))

bmi = vazn / (boy ** 2)

print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Kam vazn")
elif 18.5 <= bmi < 25:
    print("Normal vazn")
elif 25 <= bmi < 30:
    print("Ortiqcha vazn")
else:
    print("Semizlik")

