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
        'd2': "Have you worked on Flatbed or Stepdeck trailer?",
        'd3': "Are you willing to learn?",
        'o1': "Do you have your own truck?",
        'od': "Do you want to be a driver?",
        'o2': "Do you have your own trailer?",
        'o3': "Do you have more than 2 years of experience?",
        'o4': "Have you worked on Flatbed or Stepdeck trailer?",
        'o5': "Are you willing to learn?",
        'Address': "What City and State you currently reside in?",
        'name' : "What is your name?",
        'phone' : "What is the best phone number to reach you?",
        'phone_error' : "Please enter number in correct format\nExample: +1(123)456-78-90",
        'sorry': "Sorry, we are looking for flatbed drivers",
        'write' : "Write message",
        'driver': "DRIVER",
        'owner_operator': "OWNER OPERATOR",
        'success_message': "Thank you for the form submission! We will contact you shortly."
    },
    'uk': {
        'welcome_message': "Привіт! Давайте розпочнемо розмову.",
        'field_question': "Ви шукаєте роботу водієм-власником або водієм?",
        'd1': "Чи маєте ви більше 2 років досвіду?",
        'd2': "Ви працювали на трейлері Flatbed або Stepdeck?",
        'd3': "Готові ви вчитися?",
        'o1': "Чи маєте ви свій власний вантажний автомобіль?",
        'od': "Ви хочете стати водієм?",
        'o2': "Чи маєте ви власний причіп?",
        'o3': "Чи маєте ви більше 2 років досвіду?",
        'o4': "Ви працювали на трейлері Flatbed або Stepdeck?",
        'o5': "Готові ви вчитися?",
        'Address': "В якому місті ви наразі проживаєте?",
        'name' : "Як вас звати?",
        'phone' : "За яким номером телефону з вами найкраще зв'язатись?",
        'phone_error' : "Будь ласка введіть номер в правильному форматі\nНаприклад: +1(123)456-78-90",
        'sorry': "Вибачте, ми шукаємо водіїв платформ.",
        'write' : "Написати повідомлення",
        'success_message': "Дякуємо за надіслану форму! Ми зв'яжемося з вами найближчим часом.",
        'driver': "ВОДІЙ",
        'owner_operator': "ВЛАСНИК АВТОМОБІЛЯ",
    },
    'ru': {
        'welcome_message': "Привет! Давайте начнем разговор.",
        'field_question': "Вы ищете работу водителем-собственником или водителем?",
        'd1': "У вас более 2 лет опыта?",
        'd2': "ВВы работали на трейлере Flatbed или Stepdeck?",
        'd3': "Готовы ли вы учиться?",
        'o1': "У вас есть собственный грузовик?",
        'od': "Вы хотите быть водителем?",
        'o2': "У вас есть собственный прицеп?",
        'o3': "У вас есть более 2 лет опыта?",
        'o4': "Вы работали на трейлере Flatbed или Stepdeck?",
        'o5': "Готовы ли вы учиться?",
        'Address': "В каком городе вы сейчас проживаете?",
        'name' : "Как вас зовут?",
        'phone' : "По какому номеру телефона с вами лучше всего связаться?",
        'phone_error' : "Пожалуйста введите номер в правильном формате\nНапример: +1(123)456-78-90",
        'sorry': "Извините, мы ищем водителей платформы.",
        'write' : "Написать сообщение",
        'success_message': "Спасибо за отправку формы! Мы свяжемся с Вами в скором времени.",
        'driver': "ВОДИТЕЛЬ",
        'owner_operator': "ВЛАДЕЛЕЦ ГРУЗОВИКА",
    }
}

# Default language
default_language = 'en'


ADMIN_USERID = '283188328'
