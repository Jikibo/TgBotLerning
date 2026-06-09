from aiogram import Router # Контейнер для обработчиков 
from aiogram.filters import Command # Обработка конкретных команд через фильтр
from aiogram.types import Message # Тип данных для сообщений Telegram, подсказки

router = Router() # Создали обработчик

# Обработчики работают сверху вниз, если они пересекаются, то сработает первый
@router.message(Command("start")) # Обрабатывает именно start
async def start(message: Message): # Добавляет аннотации типа для аргумента функции
    await message.answer("Привет, я *простой* _бот_.\n\nНапиши /help для помощи",
                         parse_mode="Markdown")

@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer("Команды:\n<b>/start</b> - запустить бота\n<i>/help</i> - список <a href='https://google.com'> команд</a>\n/about",
                         parse_mode="HTML")

@router.message(Command("about"))
async def about(message: Message):
    await message.answer(f"Опсиание. Твое имя: {message.from_user.full_name}")

@router.message()
async def textUser(message: Message):
    await message.answer(f"{Message}")