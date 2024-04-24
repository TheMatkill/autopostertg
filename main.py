import asyncio
import time
import os
from pyrogram import Client
import schedule
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import datetime

api_id = 5764858
api_hash = "e9b58ae019c249f25ff8eca400a73ba2"
app = Client("Android", api_id, api_hash, app_version='9.3.2 (30239)', device_model='Samsung SM-G998B', system_version='Android 7.1')
chats = [
['GRINCH OTC | ЧАТ УСЛУГ ♻️', -1001820989484, "🛡 Гарант: +"],
['ZELENKA | УСЛУГИ', -1001344995571,"\n🛡 Гарант: @zelenka_guarantor_robot"],
['Gansta Group | УСЛУГИ', -1001409985813,"\n🛡 Гарант: +"],
['Услуги S&A', -1001304553138, "\n🛡 Гарант: @GarantBotSa_bot"],
['♦️BLESS 2♦️ ЧАТ УСЛУГ', -1001440808872,"\n🛡 Гарант: +"],
['NASA BAZAR', -1001444976345,"\n🛡 Гарант: +"],
['Chip & Dale | Чат Услуг🌰', -1001573290879,"\n🛡 Гарант: +"],
['𝐌𝐎𝐍𝐎𝐏𝐎𝐋𝐈𝐘𝐀 | 𝐂𝐇𝐀𝐓 𝐔𝐒𝐋𝐔𝐆 💰', -1001307354033,"\n🛡 Гарант: +"],
['Услуги Скруджа💰', -1001266598286,"\n🎩 Гарант: @GarantScroogeBot"]
]

text = f"""
👩‍💻Python Programmer👩‍💻

⚡️Различные скрипты
⚡️Telegram / Discord / VK боты
⚡️Поиск и исправление багов в вашем проекте
⚡️Установка на сервер и поддержка проекта
⚡️Знание и помощь по Python, SQL
⚡️Опыт разработки больше года.

☄️Постоянный онлайн. 
☄️Высокая отзывчивость. 
☄️Исправим, согласуем и сделаем все в кротчайшие сроки.

💸💸Любой удобный для вас способ оплаты.💸💲

📝 Связь: @CryptoFlatz"""


async def sending():
    # async with app:
    success = 0
    nothing = 0
    photo = 0
    # await app.send_photo("me", "poster.jpg", caption=f"{text}")
    for chat in chats:
        try:
            await app.send_photo(chat[1], "autopostertg/poster.jpg", caption=f"{text + chat[2]}")
            photo += 1
            success += 1
            await asyncio.sleep(10)
        except Exception as e:
            try:
                await app.send_message(chat[1], text + chat[2])
                success += 1
            except Exception as e:
                nothing += 1
            
            continue
    await app.send_message('me', 
f"""
Успешно отправлено: {success}
С фото: {photo}
Неудачно: {nothing}
Время: {datetime.datetime.now()}
""")

    
scheduler = AsyncIOScheduler()
scheduler.add_job(sending, "cron", hour='9,10,15,17', minute='30')
scheduler.start()
app.run()


