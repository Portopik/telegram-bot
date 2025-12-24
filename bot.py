import os
import time
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Получаем токен из секретов GitHub
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    print("❌ Ошибка: BOT_TOKEN не найден!")
    print("📝 Установи токен в Secrets репозитория")
    exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Привет! Я бот проекта «Автостопом По Краю»!\n\n"
        "📢 Новости здесь: https://t.me/autostopompoproecty\n"
        "🌐 Сайт проекта: /site\n"
        "❓ Помощь: /help\n\n"
        "✅ Бот работает на GitHub Actions 24/7!"
    )

async def site(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌐 Ты хочешь зайти на сайт?\n"
        "Вот ссылка:\n"
        "https://portopik.github.io/Minecraft-siteee/\n\n"
        "Приятного просмотра! 👀"
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Доступные команды:\n"
        "/start - Приветствие и информация\n"
        "/site - Ссылка на сайт проекта\n"
        "/help - Список команд\n\n"
        "⚡ Бот хостится на GitHub бесплатно!"
    )

def main():
    print("🚀 Запускаю Telegram бота...")
    
    # Создаем приложение
    app = Application.builder().token(TOKEN).build()
    
    # Добавляем обработчики команд
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("site", site))
    app.add_handler(CommandHandler("help", help_cmd))
    
    print("✅ Бот успешно запущен!")
    print("📡 Ожидаю сообщения...")
    
    # Запускаем бота
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
