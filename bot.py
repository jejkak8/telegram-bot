import os
import asyncio
from telegram import Bot

TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

async def send_message():
    await bot.send_message(chat_id=CHAT_ID, text="Бот работает 24/7 🚀")

async def main():
    while True:
        try:
            await send_message()
            await asyncio.sleep(3600)  # отправка каждый час
        except Exception as e:
            print(f"Ошибка: {e}")
            await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
