import random
from datetime import datetime
print("========================================")
print("  🧮 MATH RACE O‘YINIGA XUSH KELIBSIZ!")
print("========================================")
print()
print("Sizga 10 ta matematik misol beriladi.")
print("Maqsad: iloji boricha TEZ va TO'G'RI javob berish.")
print()
print("Matematik amallar:")
print("  ➕ Qo'shish")
print("  ➖ Ayirish")
print("  ✖️  Ko'paytirish")
print("  ➗ Bo'lish")
print()
print("Vaqtingiz: sekundlarda o'lchanadi ⏱️")
print("Ball berish:")
print("  ✔️ To'g'ri javob = 10 ball")
print("  ⚡️ Tez yechsangiz bonus ball olasiz!")
print()
input("Boshlash uchun [ENTER] tugmasini bosing...")

togri=0
maxsavol=10
vaqt=0.0

for i in range(1, maxsavol+1):
    print("----------------------------------------")
    print(f"                SAVOL {i}/{maxsavol}")
    print("----------------------------------------")

    a=random.randrange(1, 20)
    b=random.randrange(1, 20)
    amal=random.choice(['+', '-', '*', '/'])

    if amal=='/':
        b=random.randrange(1, 20)
        a=b*random.randrange(1, 5)
    
    print("Misol:")
    print(  f"{a} {amal} {b}")

    if amal=='+':
        togri_javob=a+b
    elif amal=='-':
        togri_javob=a-b
    elif amal=='*':
        togri_javob=a*b
    elif amal=='/':
        togri_javob=a/b

    start=datetime.now()
    javob=input("Javobingizni kiriting: ")

    sarflangan=round((datetime.now()-start).total_seconds(), 2)
    vaqt+=sarflangan

    try:
        if not javob:
            print("Javob kiritmadingiz")
        foydalanuvchi_javobi=float(javob.replace(',', '.'))
        if abs(foydalanuvchi_javobi-togri_javob)<0.0001:
            print(f"✅ To'g'ri javob! ⏱️ Vaqt: {sarflangan} sekund")
            togri+=1
        else:
            print(f"❌ Noto'g'ri javob. To'g'ri javob: {togri_javob} ⏱️ Vaqt: {sarflangan} sekund\n")
    except ValueError:
        print(f"⚠️ Xatolik: Son kiritilmadi. Bu savol o'tkazib yuborildi. ⏱️ Vaqt: {sarflangan} sekund")

vaqt=round(vaqt, 2)
ortacha_vaqt=round(vaqt/maxsavol, 2)
asosiy_ball=togri*10

bonus=20 if ortacha_vaqt<3 else (10 if ortacha_vaqt < 5 else 0)
jami_ball=asosiy_ball+bonus

print("============================================")
print("                🏁 NATIJALAR")
print("============================================")
print(f"Jami savollar      : {maxsavol} ta")
print(f"To'g'ri javoblar   : {togri} ta")
print(f"Umumiy vaqt        : {vaqt} sekund")
print(f"O'rtacha vaqt/savol: {ortacha_vaqt} sekund")
print("--------------------------------------------")
print("                🎯 YAKUNIY BALL")
print("--------------------------------------------")
print(f"Asosiy ball        : {asosiy_ball}")
if bonus>0:
    print(f"Tezlik bonusi      : +{bonus}")
print("--------------------------------------------")
print(f"Umumiy ball        : {jami_ball}")
print("============================================")

if jami_ball>=90:
    print("🔥 Ajoyib ishladingiz! Tezlik ham, aniqlik ham zo'r!")
elif jami_ball>=60:
    print("💪 Yaxshi natija! Biroz ko'proq mashq qilsangiz yanada kuchli bo'lasiz!")
else:
    print("🙂 Hali hammasi oldinda! Mashq qilsangiz juda yaxshilanadi.")
print("============================================")