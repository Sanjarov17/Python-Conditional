score = int(input("score: "))


if score >= 90 and score <= 100:
    print("A{A'lo}")
elif score >= 80 and score <= 89:
    print("B{Yaxshi}")
elif score >= 70 and score <= 79:
    print("C{Qoniqarli}")
elif score >= 60 and score <= 69:
    print("D{Qoniqarsiz}")
elif score >= 0 and score <= 59:
    print("F{Rad}")
else:
    print("siz nototo'g'ri ball kiritdingiz")