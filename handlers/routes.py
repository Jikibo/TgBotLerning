from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from forms.user import Form
from aiogram.fsm.context import FSMContext

router = Router() # Создали обработчик

# Обработчики работают сверху вниз, если они пересекаются, то сработает первый
@router.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer("Анкета!\nСперва ввдите введите ваше имя:")
    await state.set_state(Form.name)

@router.message(Command("cancel"))
async def cancel_form(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("No")

@router.message(Form.name, F.text)
async def proccess_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)

    await message.answer("Отлично!\n Возраст:")
    await state.set_state(Form.age)

@router.message(Form.age, F.text)
async def proccess_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Не число")
        return
    if int(message.text) < 0 or int(message.text) > 120:
        await message.answer("Слишком большое число или малое")
        return
    
    await state.update_data(age=int(message.text))

    await message.answer("Отлично!\n Ваш email")
    await state.set_state(Form.email)

@router.message(Form.email, F.text)
async def proccess_email(message: Message, state: FSMContext):
    email_text = message.text
    if "@" not in email_text or "." not in email_text:
        await message.answer("Email некорректный")
        return
    
    await state.update_data(email=email_text)

    data = await state.get_data()
    name = data["name"]
    age = data["age"]
    email = data["email"]

    await message.answer(f"Отлично! Все готово!\nИмя: {name}\nВозраст: {age}\nEmail: {email}")
    await state.clear()