import os
import asyncio
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text("Бот работает 24/7 🚀")


async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Обрабатываем /start
    app.add_handler(CommandHandler("start", start))

    # ТЕСТ: реагируем вообще на любые сообщения
    app.add_handler(MessageHandler(filters.ALL, start))

    print("Бот запущен...")

    # Убираем возможный старый webhook
    await app.bot.delete_webhook(drop_pending_updates=True)

    await app.run_polling()


if __name__ == "__main__":
    asyncio.run(main())
