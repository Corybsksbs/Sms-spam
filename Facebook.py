# PYTHON ....
# Telegram : @ndmmo - @zizfif
# instagram : ****
# Codeder : B7E | ابن بابل 

#ركز 👇 

# هذه الاداة مجانية وليست للبيع الرجاء عدم بيعها ..
# عدم ازالة الحقوق تقديرا لتعبنا وجعلنا نستمر في تقديم مثل هكذا (ادوات او بوتات)..
#ثق بربك ومن خلقك اذه اشوفك تبيع بل اده اخليك تحير شلون تحذف حسابك اخمط ونشر لاكن تبيع بي انيج عرضك صفح
#==========================#

import requests
import os

B7E = "http://128.199.36.57:5000/search"

class B7E2:
    B7E3 = '\033[95m'
    B7E4 = '\033[94m'
    B7E5 = '\033[92m'
    B7E6 = '\033[93m'
    B7E7 = '\033[91m'
    B7E8 = '\033[0m'
    B7E9 = '\033[1m'
    B7E10 = '\033[4m'

def B7E11():
    os.system('cls' if os.name == 'nt' else 'clear')

def B7E12():
    print(B7E2.B7E5 + "=" * 50)
    print(B7E2.B7E9 + "🔍 أداة البحث الـ VIP 💰".center(50) + B7E2.B7E8)
    print(B7E2.B7E5 + "=" * 50 + B7E2.B7E8)
    print("📌 يمكنك البحث عن طريق ( الاسم ~ الايدي ~ الايميل ~ الرقم )")
    print(f"{B7E2.B7E6}🔄 لرجوع للقائمة الرئيسية: 0{B7E2.B7E8}")
    print(f"{B7E2.B7E7}❌ لإيقاف الأداة: 1{B7E2.B7E8}")
    print("=" * 50)

def B7E13(B7E14):
    try:
        B7E15 = requests.get(B7E, params={"query": B7E14}, timeout=10)
        B7E16 = B7E15.json()

        if "error" in B7E16:
            print(f"{B7E2.B7E7}❌ خطأ: {B7E16['error']}{B7E2.B7E8}")
            return None

        return B7E16["results"] if "results" in B7E16 else []
    except requests.exceptions.RequestException as B7E17:
        print(f"{B7E2.B7E7}❌ خطأ في الاتصال بالسيرفر: {B7E17}{B7E2.B7E8}")
        return None

def B7E18():
    while True:
        B7E11()
        B7E12()
        B7E19 = input(f"{B7E2.B7E4}🔍 أدخل رقم أو اسم أو ايميل أو ID للبحث: {B7E2.B7E8}").strip()
        
        if B7E19 == "1":
            print(f"{B7E2.B7E7}👋  تم إنهاء الأداة ادعبل.{B7E2.B7E8}")
            break
        elif B7E19 == "0":
            continue

        B7E11()
        B7E12()
        print(f"🔎 البحث عن: {B7E2.B7E9}{B7E19}{B7E2.B7E8}\n")
        
        B7E20 = B7E13(B7E19)

        if B7E20:
            print(f"\n{B7E2.B7E5}✅ تم العثور على {len(B7E20)} نتائج:\n{B7E2.B7E8}")
            for B7E21, B7E22 in enumerate(B7E20, 1):
                print(f"{B7E2.B7E10}{B7E2.B7E9}🔹 النتيجة رقم {B7E21}{B7E2.B7E8}")
                print(f"{B7E2.B7E4}اسم:{B7E2.B7E8} {B7E22['اسم']}")
                print(f"{B7E2.B7E4}رقم:{B7E2.B7E8} {B7E22['رقم']}")
                print(f"{B7E2.B7E4}عنوان:{B7E2.B7E8} {B7E22['عنوان']}")
                print(f"{B7E2.B7E4}ايدي:{B7E2.B7E8} {B7E22['ايدي']}")
                print(f"{B7E2.B7E4}بايو:{B7E2.B7E8} {B7E22['بايو']}")
                print(f"{B7E2.B7E4}ذكر او انثه:{B7E2.B7E8} {B7E22['ذكر او انثه']}")
                print(f"{B7E2.B7E4}مرتبط او سنجل:{B7E2.B7E8} {B7E22['مرتبط او سنجل']}")
                print(f"{B7E2.B7E4}سيره ذاتيه:{B7E2.B7E8} {B7E22['سيره ذاتيه']}")
                print(f"{B7E2.B7E4}رابط حساب:{B7E2.B7E8} {B7E22['رابط حساب']}")
                print("=" * 50)
        else:
            print(f"{B7E2.B7E7}❌ لم يتم العثور على أي بيانات.{B7E2.B7E8}")

        input(f"\n{B7E2.B7E6}🔄 اضغط Enter للعودة إلى القائمة الرئيسية...{B7E2.B7E8}")

if __name__ == "__main__":
    B7E18()
