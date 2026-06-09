from os import getenv # взаимодействие с файлом настроек
import asyncio # ассионхронные функции
from aiogram import Bot, Dispatcher # Bot - получает обновления от Telegram API, Dispatcher - получает обновления от Bot и перенаправляет их в соответствующие Router'ы
from aiogram.client.session.aiohttp import AiohttpSession # настраивать сессию для HTTP-запросов к Telegram API, включая прокси
from dotenv import load_dotenv # импорт настроек из файла
from handlers.routes import router

load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(router)

async def main():
    session = AiohttpSession(proxy="socks5://127.0.0.1:3067") # указали как идет подключение
    bot = Bot(token=TOKEN, session=session) # указали доступ к боту через токен, указали канал подключения

    print("Start..")
    await dp.start_polling(bot) # запуск бота и ожидание чего-либо

if __name__ == "__main__":
    asyncio.run(main())