from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api.postgres import send_ex


til = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='UZ 🇺🇿' ,callback_data='lang_uz')],
    [InlineKeyboardButton(text='RU 🇷🇺', callback_data='lang_ru')],
])


admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Profile',callback_data='profile')],
    [InlineKeyboardButton(text='Refeller', callback_data='refeller'),
     InlineKeyboardButton(text='Product', callback_data='product')],
    [InlineKeyboardButton(text='foydalanuvchilar soni' ,callback_data='users')],
    [InlineKeyboardButton(text='pulni olish', callback_data='get_money')],
    [InlineKeyboardButton(text='sozlamalar', callback_data='sozlama')],

])

channel = send_ex("""select * from project_channel""")
kanal = InlineKeyboardMarkup()
kanal_ru = InlineKeyboardMarkup()

for i in channel:
    a = InlineKeyboardButton(text=f'{i[1]}', url=f"{i[2]}")
    kanal.add(a)
    kanal_ru.add(a)
tekshir_uz = InlineKeyboardButton(text='tekshirish', callback_data='tekshir_uz')
tekshir_ru = InlineKeyboardButton(text='Проверять', callback_data='tekshir_ru')
kanal.add(tekshir_uz)
kanal_ru.add(tekshir_ru)

admin_ru = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Профиль',callback_data='profile_ru')],
    [InlineKeyboardButton(text='Рефеллер', callback_data='refeller_ru'),
     InlineKeyboardButton(text='Продукт', callback_data='product_ru')],
    [InlineKeyboardButton(text='Количество пользователей' ,callback_data='users_ru')],
    [InlineKeyboardButton(text='получать деньги', callback_data='get_money_ru')],
    [InlineKeyboardButton(text='настройки', callback_data='sozlama_ru')],
])



menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Menu',callback_data='menu')],
])


user = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Profile',callback_data='profile')],
    [InlineKeyboardButton(text='Refeller', callback_data='refeller'),
     InlineKeyboardButton(text='Product', callback_data='product')],
    [InlineKeyboardButton(text='Pulni olish', callback_data='get_money')],
    [InlineKeyboardButton(text='sozlamalar', callback_data='sozlama')],

])

user_ru = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Профиль',callback_data='profile')],
    [InlineKeyboardButton(text='Рефеллер', callback_data='refeller'),
     InlineKeyboardButton(text='Продукт', callback_data='product')],
    [InlineKeyboardButton(text='получать деньги', callback_data='get_money')],
    [InlineKeyboardButton(text='настройки', callback_data='sozlama')],

])
