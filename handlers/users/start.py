from aiogram import types
from utils.db_api.postgres import send_ex
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.default.menu import menu
from filters.private_chat import IsPrivate
from loader import dp, bot

admins = 1737841515

@dp.message_handler(commands='start')
async def starts(message: types.Message):
    ref_id = message.text[7:]
    if message.from_user.id == admins:
        await message.answer('salom admin \nodamlarni taklig qilish uchun sizning refeller linkingiz')
        await message.answer(f"\n\nhttps://t.me/testing8342132bot/?start={message.from_user.id}\n\n")
    elif ref_id:
        users = send_ex('''select tg_id from testing_author''')
        if str(message.from_user.id) not in users:
            if int(ref_id) != int(admins):
                user = send_ex('''SELECT zanjir FROM testing_author''')
            else:
                user = send_ex(f'''SELECT username FROM testing_creator''')
            path = f"{user[0][0]}/{message.from_user.id}"
            if len(path) > 110:
                path = path[11:]
            send_ex(f"""insert into testing_author(name, zanjir, price, tg_id) values('{message.from_user.first_name}','{path}', 1,'{message.from_user.id}') returning * """)
            await message.answer(f"salom foydalanuvchi boshqalarni taklif qilish uchun siznig linkingiz")
            await message.answer(f"\n\nhttps://t.me/testing8342132bot/?start={message.from_user.id}\n\n")
        else:
            zanjir = send_ex(f'''select zanjir from testing_author where tg_id={message.from_user.id}''')
            await message.answer('siz botga taklif qilingansiz\nsizning foydalanuvchi taklif qiladigan linkingiz\n',zanjir)
    else:
        await message.answer(f"foydalavunchi biron kimning refeller linki yordamida botga kiring")













