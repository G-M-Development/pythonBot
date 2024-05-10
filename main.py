import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import executor
import smtplib
from email.message import EmailMessage

# Set up logging
logging.basicConfig(level=logging.INFO)

# Telegram Bot token
API_TOKEN = '7036077332:AAE_cM_pgBADFLjNaR6TCpYR1gwMlcaxJOc'

# Initialize bot, dispatcher, and FSM storage
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

translations = {
    'en': {
        'welcome_message': "Hi! Let's start a conversation.",
        'field_question':
        "Are you looking for owner operator or driver's job?",
        'd1': "Do you have more than 2 years of experience?",
        'd2': "Have you driven flatbed trucks?",
        'd3': "Are you willing to learn?",
        'o1': "Do you have your own truck?",
        'od': "Do you want to be a driver?",
        'o2': "Do you have your own trailer?",
        'o3': "Do you have more than 2 years of experience?",
        'o4': "Have you driven flatbed or stepdeck trucks?",
        'o5': "Are you willing to learn?",
        'address': "Please enter your living address",
        'sorry': "Sorry, we are looking for flatbed drivers",
        'driver': "driver",
        'owner_operator': "owner operator"
    },
    'ua': {
        'welcome_message': "Привіт! Давайте розпочнемо розмову.",
        'field_question': "Ви шукаєте роботу водієм-власником або водієм?",
        'd1': "Чи маєте ви більше 2 років досвіду?",
        'd2': "Чи їздили ви на платформах?",
        'd3': "Готові ви вчитися?",
        'o1': "Чи маєте ви свій власний вантажний автомобіль?",
        'od': "Ви хочете стати водієм?",
        'o2': "Чи маєте ви власний причіп?",
        'o3': "Чи маєте ви більше 2 років досвіду?",
        'o4': "Чи їздили ви на платформах чи на двоярусних автомобілях?",
        'o5': "Готові ви вчитися?",
        'address': "Будь ласка, введіть свою домашню адресу",
        'sorry': "Вибачте, ми шукаємо водіїв платформ.",
        'driver': "водій",
        'owner_operator': "власник автомобіля"
    },
    'ru': {
        'welcome_message': "Привет! Давайте начнем разговор.",
        'field_question':
        "Вы ищете работу водителем-собственником или водителем?",
        'd1': "У вас более 2 лет опыта?",
        'd2': "Вы ездили на платформах?",
        'd3': "Готовы ли вы учиться?",
        'o1': "У вас есть собственный грузовик?",
        'od': "Вы хотите быть водителем?",
        'o2': "У вас есть собственный прицеп?",
        'o3': "У вас есть более 2 лет опыта?",
        'o4': "Вы ездили на платформах или на двухъярусных автомобилях?",
        'o5': "Готовы ли вы учиться?",
        'address': "Пожалуйста, введите свой домашний адрес",
        'sorry': "Извините, мы ищем водителей платформы.",
        'driver': "водитель",
        'owner_operator': "владелец грузовика"
    }
}

# Default language
default_language = 'en'

# SMTP Server Configuration
SMTP_SERVER = 'smtp.elasticemail.com'
SMTP_PORT = 2525
SMTP_USERNAME = 'rogis54003@ahieh.com'
SMTP_PASSWORD = 'E6BB2E4CA28BF36D634F8C1808D48269D6CD'
SENDER_EMAIL = 'rogis54003@ahieh.com'
RECIPIENT_EMAIL = 'rogis54003@ahieh.com'


class ConversationStates(StatesGroup):
    field = State()
    o1 = State()
    o2 = State()
    o3 = State()
    o4 = State()
    o5 = State()
    od = State()
    d1 = State()
    d2 = State()
    d3 = State()
    address = State()
    sorry = State()


def create_button(text):
    return types.KeyboardButton(text)


def translate(text, lang):
    user_language = lang if lang in ['ua', 'ru'] else 'en'
    if user_language in translations and text in translations[user_language]:
        return translations[user_language][text]
    elif default_language in translations and text in translations[
            default_language]:
        return translations[default_language][text]
    else:
        return text


# Handler for /start command
@dp.message_handler(commands=['start'])
async def start_conversation(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["username"] = message.from_user.username
        data["firstname"] = message.from_user.first_name
        data['language'] = message.from_user.language_code
        await message.answer(
            translate('welcome_message', message.from_user.language_code))
        await ask_field(message, state)


async def ask_field(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            create_button(
                translate('owner_operator', message.from_user.language_code)),
            create_button(translate('driver',
                                    message.from_user.language_code)))
        await message.answer(translate('field_question',
                                       message.from_user.language_code),
                             reply_markup=markup)
        await ConversationStates.field.set()


async def d1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['field'] = "driver"
        data['d1'] = translate('d1', message.from_user.language_code)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(create_button("✅"), create_button("❌"))
        await message.answer(data['d1'], reply_markup=markup)
        await ConversationStates.d1.set()


async def d2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_d2'] = translate('d2', message.from_user.language_code)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(create_button("✅"), create_button("❌"))
        await message.answer(data['question_d2'], reply_markup=markup)
        await ConversationStates.d2.set()


async def d3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['question_d3'] = translate('d3', message.from_user.language_code)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(create_button("✅"), create_button("❌"))
        await message.answer(data['question_d3'], reply_markup=markup)
        await ConversationStates.d3.set()


async def o1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['field'] = "owner_operator"
        # Save the question and user response
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(create_button("✅"), create_button("❌"))
        await message.answer(translate('o1', message.from_user.language_code),
                             reply_markup=markup)
        await ConversationStates.o1.set()


async def o2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # Save the question and user response
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(create_button("✅"), create_button("❌"))
        await message.answer(translate('o2', message.from_user.language_code),
                             reply_markup=markup)
        await ConversationStates.o2.set()


async def od(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['od'] = True
        # Save the question and user response
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(create_button("✅"), create_button("❌"))
        await message.answer(translate('od', message.from_user.language_code),
                             reply_markup=markup)
        await ConversationStates.od.set()


async def o3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # Save the question and user response
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(create_button("✅"), create_button("❌"))
        await message.answer(translate('o3', message.from_user.language_code),
                             reply_markup=markup)
        await ConversationStates.o3.set()


async def o4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # Save the question and user response
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(create_button("✅"), create_button("❌"))
        await message.answer(translate('o4', message.from_user.language_code),
                             reply_markup=markup)
        await ConversationStates.o4.set()


async def o5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # Save the question and user response
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(create_button("✅"), create_button("❌"))
        await message.answer(translate('o5', message.from_user.language_code),
                             reply_markup=markup)
        await ConversationStates.o5.set()


async def address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer(translate('address',
                                       message.from_user.language_code),
                             reply_markup=types.ReplyKeyboardRemove())
        await ConversationStates.address.set()


async def sorry(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        await message.answer(translate('sorry',
                                       message.from_user.language_code),
                             reply_markup=markup)
        await ConversationStates.sorry.set()
        await send_email(state, None)


async def send_email(state: FSMContext, address: str = None):
    async with state.proxy() as data:
        # Initialize message body
        message_body = ""

        # Iterate over the saved data in the state and append to message body
        if address is not None:
            message_body += f"Address: {address}\n"
        for key, value in data.items():
            message_body += f"{key}: {value}\n"


        # Connect to SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)

            # Create email message
            msg = EmailMessage()
            msg.set_content(message_body)
            msg['Subject'] = 'User Information'
            msg['From'] = 'rogis54003@ahieh.com'
            msg['To'] = 'rogis54003@ahieh.com'

            # Send email
            server.send_message(msg)
            await state.finish()


@dp.message_handler(content_types=["text"], state=ConversationStates.address)
async def handle_text(message: types.Message, state: FSMContext):
    await send_email(state, message.text)


# Handler for processing the user's responses
@dp.message_handler(lambda message: message.text.lower() in [
    translate('driver', message.from_user.language_code),
    translate('owner_operator', message.from_user.language_code), "✅", "❌"
],
                    state="*")
async def process_response(message: types.Message, state: FSMContext):
    if (await state.get_state()) == ConversationStates.field.state:
        await state.update_data(field=message.text.lower())
        if message.text.lower() == translate('driver',
                                             message.from_user.language_code):
            await d1(message, state)
        else:
            await o1(message, state)
    elif (await state.get_state()) == ConversationStates.o1.state:
        await state.update_data(od=message.text.lower())
        if message.text.lower() == "✅":
            await o2(message, state)
        else:
            await od(message, state)
    elif (await state.get_state()) == ConversationStates.o2.state:
        await state.update_data(o2=message.text.lower())
        await o3(message, state)
    elif (await state.get_state()) == ConversationStates.o3.state:
        await state.update_data(o3=message.text.lower())
        await o4(message, state)
    elif (await state.get_state()) == ConversationStates.o4.state:
        await state.update_data(o4=message.text.lower())
        if message.text.lower() == "✅":
            await address(message, state)
        else:
            await o5(message, state)
    elif (await state.get_state()) == ConversationStates.o5.state:
        await state.update_data(o5=message.text.lower())
        if message.text.lower() == "✅":
            await address(message, state)
        else:
            await sorry(message, state)
    elif (await state.get_state()) == ConversationStates.od.state:
        await state.update_data(od=message.text.lower())
        if message.text.lower() == "✅":
            await d1(message, state)
        else:
            await sorry(message, state)
    elif (await state.get_state()) == ConversationStates.d1.state:
        await state.update_data(d1=message.text.lower())
        await d2(message, state)
    elif (await state.get_state()) == ConversationStates.d2.state:
        await state.update_data(d2=message.text.lower())
        if message.text.lower() == "✅":
            await address(message, state)
        else:
            await d3(message, state)
    elif (await state.get_state()) == ConversationStates.d3.state:
        await state.update_data(d3=message.text.lower())
        if message.text.lower() == "✅":
            await address(message, state)
        else:
            await sorry(message, state)


async def display_diagram(message: types.Message):
    user_data = await FSMContext.get_data()
    field_answer = user_data.get("field", "Unknown")
    o1_answer = user_data.get("o1", "Unknown")
    o2_answer = user_data.get("o2", "Unknown")
    o3_answer = user_data.get("o3", "Unknown")
    o4_answer = user_data.get("o4", "Unknown")
    o5_answer = user_data.get("o5", "Unknown")
    od_answer = user_data.get("od", "Unknown")
    d1_answer = user_data.get("d1", "Unknown")
    d2_answer = user_data.get("d2", "Unknown")
    d3_answer = user_data.get("d3", "Unknown")
    address_answer = user_data.get("address", "Unknown")

    diagram = f"Field: {field_answer}\n"
    diagram += f"Own Truck (o1): {o1_answer}\n"
    diagram += f"Own Trailer (o2): {o2_answer}\n"
    diagram += f"Experience (o3): {o3_answer}\n"
    diagram += f"Flatbed Trucks (o4): {o4_answer}\n"
    diagram += f"Willing to Learn (o5): {o5_answer}\n"
    diagram += f"Driver Decision (od): {od_answer}\n"
    diagram += f"Experience (d1): {d1_answer}\n"
    diagram += f"Flatbed Trucks (d2): {d2_answer}\n"
    diagram += f"Willing to Learn (d3): {d3_answer}\n"
    diagram += f"Address: {address_answer}"

    await message.answer(diagram)


# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
