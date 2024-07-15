import logging
import re
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import executor
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.message import EmailMessage
from config import API_TOKEN, SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD, SENDER_EMAIL, RECIPIENT_EMAIL, translations, default_language, ADMIN_USERID

from aiogram.types.reply_keyboard import ReplyKeyboardRemove

# Initialize bot, dispatcher, and FSM storage
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Set up logging
logging.basicConfig(level=logging.INFO)

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
    name = State()
    phone = State()
    sorry = State()


def create_button(text):
    return types.KeyboardButton(text)


def translate(text, lang):
    user_language = lang if lang in ['uk', 'ru'] else 'en'
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
        data['id'] = message.from_user.id

        await message.answer(
            translate('welcome_message', message.from_user.language_code))
        #await message.answer(f"<a href='tg://openmessage?user_id={message.from_user.id}'>{message.from_user.full_name}</a>", "HTML")
        await ask_field(message, state)


async def ask_field(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            create_button(translate('owner_operator', message.from_user.language_code)),
            create_button(translate('driver', message.from_user.language_code)))
        await message.answer(translate('field_question', message.from_user.language_code),
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
        data['d2'] = translate('d2', message.from_user.language_code)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(create_button("✅"), create_button("❌"))
        await message.answer(data['d2'], reply_markup=markup)
        await ConversationStates.d2.set()


async def d3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['d3'] = translate('d3', message.from_user.language_code)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(create_button("✅"), create_button("❌"))
        await message.answer(data['d3'], reply_markup=markup)
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
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(create_button("✅"), create_button("❌"))
        await message.answer(translate('o2', message.from_user.language_code),
                             reply_markup=markup)
        await ConversationStates.o2.set()


async def od(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['od'] = True
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(create_button("✅"), create_button("❌"))
        await message.answer(translate('od', message.from_user.language_code),
                             reply_markup=markup)
        await ConversationStates.od.set()


async def o3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
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
        await message.answer(translate('Address',
                                        message.from_user.language_code),
                                        reply_markup=ReplyKeyboardRemove())
        await ConversationStates.address.set()


async def sorry(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        await message.answer(translate('sorry', 
                                       message.from_user.language_code),
                                       reply_markup=ReplyKeyboardRemove())
        await ConversationStates.sorry.set()
        await state.finish()

async def send_email(state: FSMContext, number: str = None):
    async with state.proxy() as data:
        # Initialize HTML message body
        html_message_body = "<html><body>"
        mes_body = "\n"

        # Iterate over the saved data in the state and append to HTML message body
        if number is not None:
            mes_body += f"Phone number: {number}\n"
            html_message_body += f"<p><strong>Phone number:</strong> {number}</p>"
        for key, value in data.items():
            translated_key = translate(key, 'en')
            if key == 'id':
                continue
            if translated_key:
                mes_body += f"{translated_key}: {value} \n"
                html_message_body += f"<p><strong>{translated_key}:</strong> {value}</p>"
            else:
                mes_body += f"{key}: {value}"
                html_message_body += f"<p><strong>{key}:</strong> {value}</p>\n"


        
        await bot.send_message(ADMIN_USERID, mes_body + f"<a href='tg://user?id={data['id']}'>{data['name']}</a>", parse_mode="HTML")
        html_message_body += "</body></html>"

        # Connect to SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USERNAME, SMTP_PASSWORD)

            # Create HTML email message
            msg = MIMEMultipart()
            msg.attach(MIMEText(html_message_body, 'html'))
            msg['Subject'] = 'User Information'
            msg['From'] = SENDER_EMAIL
            msg['To'] = RECIPIENT_EMAIL
            
            # Send email
            server.send_message(msg)
            await state.finish()

@dp.message_handler(content_types=["text"], state=ConversationStates.address)
async def handle_address(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # Send success message
        #await message.answer(translate('success_message', message.from_user.language_code))
        data['Address'] = message.text
        
        await message.answer(translate('name', message.from_user.language_code))
        await ConversationStates.name.set()
        #await send_email(state, message.text)

@dp.message_handler(content_types=["text"], state=ConversationStates.name)
async def handle_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # Send success message
        data['name'] = message.text
        await message.answer(translate('phone', message.from_user.language_code))
        await ConversationStates.phone.set()
        #await send_email(state, message.text)

pattern = r'^(\+?1)?[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{2}[\s.-]?\d{2}$'

@dp.message_handler(content_types=["text"], state=ConversationStates.phone)
async def handle_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        # Send success message
        if re.match(pattern, message.text):
            data['phone'] = message.text
            state.finish()
            await message.answer(translate('success_message', message.from_user.language_code))
            await send_email(state, message.text)
        else:
            await message.answer(translate('phone_error', message.from_user.language_code))


@dp.message_handler(lambda message: message.text in [
    translate('driver', message.from_user.language_code),
    translate('owner_operator', message.from_user.language_code), "✅", "❌"
], state="*")
async def process_response(message: types.Message, state: FSMContext):
    if (await state.get_state()) == ConversationStates.field.state:
        await state.update_data(field=message.text)
        if message.text == translate('driver', message.from_user.language_code):
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

# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
