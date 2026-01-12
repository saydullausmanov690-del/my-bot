# ===============================
# 1️⃣ Keep alive kodi (24/7 uchun)
# ===============================
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot ishga tayyor ✅"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Keep alive’ni ishga tushirish
keep_alive()

# ===============================
# 2️⃣ Telegram bot kodi
# ===============================
import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# 🔹 TOKENingizni shu yerga qo‘ying
TOKEN = "8302735242:AAFJD8lYto6KsFxNAqykYJxweplKh99XtfQ"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

quiz_mode = {}  # foydalanuvchi quiz holatini saqlash

# ▶️ Mini quiz savollari
quiz = [
    {"savol": "Python nima uchun mashhur?", "javob": "Oson va qulay sintaksis, AI va Data Science sohalari uchun"},
    {"savol": "Java dasturlash tili qaysi platformalarda ishlaydi?", "javob": "Platformadan mustaqil, Android va server tizimlarida"},
    {"savol": "Frontend dasturlashda qaysi texnologiya ishlatiladi?", "javob": "HTML, CSS, JavaScript, React, Vue, Angular"},
    {"savol": "Telegram bot yaratishda qaysi til ishlatiladi?", "javob": "Python va aiogram kutubxonasi"},
    {"savol": "Dasturchilar uchun eng foydali til qaysi?", "javob": "Python"}
]

# ▶️ Fun factlar
fun_facts = [
    "🐍 Python nomi Monty Python’dan ilhomlangan!",
    "☕ Java nomi qahva ichimligi bilan bog‘liq!",
    "💻 Frontend – foydalanuvchi ko‘radigan qism",
    "🎲 Kod yozish ba’zan sehrgarlik kabi his qilinadi!",
    "👨‍💻 Dasturchilar uchun eng yaxshi motivatsiya: kod yozish va tajriba"
]

# ▶️ Asosiy menyu tugmalari
def main_menu_keyboard():
    builder = ReplyKeyboardBuilder()
    main_buttons = ["🐍 Python", "☕ Java", "💻 Frontend", "📝 Mini quiz", "🎲 Fun fact", "ℹ️ Bot haqida", "👑 Admin", "🎵 Musiqa"]
    for btn in main_buttons:
        builder.add(KeyboardButton(text=btn))
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

# ▶️ Xabarlarni qabul qilish
@dp.message()
async def main_menu(message: types.Message):
    user_id = message.from_user.id
    text = message.text

    # 🔹 Quiz javobini tekshirish
    if quiz_mode.get(user_id):
        correct_answer = quiz_mode[user_id]
        if text.strip().lower() == correct_answer.lower():
            await message.answer("✅ To‘g‘ri! Zo‘r ishladingiz!", reply_markup=main_menu_keyboard())
        else:
            await message.answer(f"❌ Noto‘g‘ri! To‘g‘ri javob: {correct_answer}", reply_markup=main_menu_keyboard())
        quiz_mode.pop(user_id)
        return

    # 🔹 Mini Quiz
    if text == "📝 Mini quiz":
        q = random.choice(quiz)
        quiz_mode[user_id] = q['javob']  # foydalanuvchining javobini saqlaymiz
        builder = ReplyKeyboardBuilder()
        builder.add(KeyboardButton(text="🔙 Orqaga"))
        await message.answer(
            f"📝 Savol:\n{q['savol']}\n\nJavobini yozing:",
            reply_markup=builder.as_markup(resize_keyboard=True)
        )
        return

    # 🔹 Orqaga tugma
    if text == "🔙 Orqaga":
        await message.answer("Asosiy menyuga qaytdingiz 👌", reply_markup=main_menu_keyboard())
        quiz_mode.pop(user_id, None)
        return

    # 🔹 Dasturlash tillari
    if text == "🐍 Python":
        await message.answer(
            "🐍 *Python dasturlash tili*\n\n"
            "1️⃣ Oson va tushunarli sintaksis.\n"
            "2️⃣ Yangi boshlovchilar uchun qulay.\n"
            "3️⃣ Web (Django, Flask) da ishlatiladi.\n"
            "4️⃣ Telegram botlar yaratish mumkin.\n"
            "5️⃣ AI va Machine Learning sohalari.\n"
            "6️⃣ Data Science va analiz uchun qulay.\n"
            "7️⃣ Avtomatlashtirish ishlarida keng qo‘llaniladi.\n"
            "8️⃣ Platformaga bog‘liq emas.\n"
            "9️⃣ Katta kutubxonalar bazasi mavjud.\n"
            "🔟 Dunyo bo‘yicha eng mashhur tillardan biri.",
            parse_mode="Markdown",
            reply_markup=main_menu_keyboard()
        )
    elif text == "☕ Java":
        await message.answer(
            "☕ *Java dasturlash tili*\n\n"
            "1️⃣ Ob’ektga yo‘naltirilgan til.\n"
            "2️⃣ Android ilovalar yaratishda ishlatiladi.\n"
            "3️⃣ Katta kompaniyalar ishlatadi.\n"
            "4️⃣ Server va backend tizimlarda qo‘llanadi.\n"
            "5️⃣ Xavfsiz va barqaror.\n"
            "6️⃣ Kuchli xotira boshqaruvi mavjud.\n"
            "7️⃣ Platformadan mustaqil.\n"
            "8️⃣ Java Spring framework mashhur.\n"
            "9️⃣ Katta loyihalar uchun mos.\n"
            "🔟 Bank va moliya tizimlarida ishlatiladi.",
            parse_mode="Markdown",
            reply_markup=main_menu_keyboard()
        )
    elif text == "💻 Frontend":
        await message.answer(
            "💻 *Frontend dasturlash*\n\n"
            "1️⃣ Foydalanuvchi ko‘radigan qism.\n"
            "2️⃣ HTML sahifa tuzilishi.\n"
            "3️⃣ CSS dizayn va bezak beradi.\n"
            "4️⃣ JavaScript interaktivlik qo‘shadi.\n"
            "5️⃣ Responsive dizayn.\n"
            "6️⃣ Mobil va kompyuterga moslashadi.\n"
            "7️⃣ React framework mashhur.\n"
            "8️⃣ Vue va Angular ishlatiladi.\n"
            "9️⃣ UX/UI dizayn bilan bog‘liq.\n"
            "🔟 Web saytni chiroyli qiladi.",
            parse_mode="Markdown",
            reply_markup=main_menu_keyboard()
        )

    # 🔹 Fun fact
    elif text == "🎲 Fun fact":
        fact = random.choice(fun_facts)
        await message.answer(f"🎲 Fun fact:\n{fact}", reply_markup=main_menu_keyboard())

    # 🔹 Bot haqida
    elif text == "ℹ️ Bot haqida":
        await message.answer(
            "ℹ️ *Programmer Hub Bot*\n\n"
            "1️⃣ Dasturchilar uchun yaratilgan.\n"
            "2️⃣ Python, Java, Frontend o‘rgatadi.\n"
            "3️⃣ Mini quiz va fun factlar bor.\n"
            "4️⃣ O‘rganish uchun qulay va qiziqarli.",
            parse_mode="Markdown",
            reply_markup=main_menu_keyboard()
        )

    # 🔹 Admin tugma
    elif text == "👑 Admin":
        await message.answer(
            "👑 Admin Profili:\n\n"
            "Username: @Error_oa\n"
            "Ruxsat: To‘liq\n"
            "Botni boshqarish huquqi: Ha\n"
            "Sozlamalarni ko‘rish mumkin",
            reply_markup=main_menu_keyboard()
        )

    # 🔹 Musiqa tugma
    elif text == "🎵 Musiqa":
        await message.answer(
            "🎵 Mening musiqa botim: @uz_musiqa_bot",
            reply_markup=main_menu_keyboard()
        )

    else:
        # Default javob: asosiy menyu
        await message.answer("Quyidagi tugmalardan birini tanlang ⬇️", reply_markup=main_menu_keyboard())

# ▶️ Botni ishga tushirish
async def main():
    print("✅ Bot ishga tushdi")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
