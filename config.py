import logging
from email.message import EmailMessage

# Set up logging
logging.basicConfig(level=logging.INFO)

# Telegram Bot token
API_TOKEN = '7036077332:AAE_cM_pgBADFLjNaR6TCpYR1gwMlcaxJOc'

# SMTP Server Configuration
SMTP_SERVER = 'smtp.elasticemail.com'
SMTP_PORT = 2525
SMTP_USERNAME = 'rogis54003@ahieh.com'
SMTP_PASSWORD = 'E6BB2E4CA28BF36D634F8C1808D48269D6CD'
SENDER_EMAIL = 'rogis54003@ahieh.com'
RECIPIENT_EMAIL = 'rogis54003@ahieh.com'

# Translations
translations = {
    'en': {
        'welcome_message': "Hi! Let's start a conversation.",
        'field_question': "Are you looking for owner operator or driver's job?",
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
        'field_question': "Вы ищете работу водителем-собственником или водителем?",
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
