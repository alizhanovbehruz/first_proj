from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(resize_keyboard=True,keyboard=[
    [KeyboardButton(text='📢 Tanlovda ishtirok etish')],
    [KeyboardButton(text='📊 Reyting'), KeyboardButton(text='🗒 Tanlov shartlari')],
    [KeyboardButton(text='☎️ Murojaat')],
    [KeyboardButton(text='Bot haqida')]
])


