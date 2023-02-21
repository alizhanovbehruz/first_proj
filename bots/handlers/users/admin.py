from aiogram import types
from utils.db_api.postgres import send_ex
from filters.private_chat import IsPrivate
from loader import dp, bot


# '''admin uchun kanal qo'shish kamandasi >>>'''
@dp.message_handler(IsPrivate(),commands='addchannel', chat_id=1737841515)
async def addchannel(star: types.Message):
    try:
        if star.reply_to_message.text:
            send_ex(f'''INSERT INTO admins (channel) VALUES('{star.reply_to_message.text}') returning *''')
            await star.answer("Kanal qo'shildi")
    except:
        await star.answer('xatolik')

# '''<<< admin uchun kanal qo'shish kamandasi'''




# '''admin uchun foydalanuvchilar haqida kamanda>>>'''
@dp.message_handler(IsPrivate(),commands='users', chat_id=1737841515)
async def addchannel(star: types.Message):
    try:
        users_son = len(send_ex(f'''SELECT id FROM users'''))
        reyting30 = ''
        n = 1
        for name, bal in send_ex(f"""SELECT username,ball FROM users ORDER BY ball DESC LIMIT 50"""):
            reyting30+=f'{n} : @{name} -> {bal} ball\n'
            n+=1
        await star.answer(f"Foydalanuvchilar soni- {users_son}\n\ntop 30 foydalanuvchilar:\n\n{reyting30}")

    except:
        await star.answer('xatolik')

# '''<<< admin uchun foydalanuvchilar haqida kamanda'''



# """admin uchun tanlov shartini o'zgartirish kamandasi >>>"""
@dp.message_handler(IsPrivate(),commands='setshart', chat_id=1737841515)
async def shartniozgartirish(ozgarshart: types.Message):
    try:
        if ozgarshart.reply_to_message.text:
            send_ex(f'''INSERT INTO tanlov_sharti(sharti) VALUES('{ozgarshart.reply_to_message.text}')''')
            await ozgarshart.answer("shartlar muvafaqqiyatli o'zgartirildi")
    except:
        await ozgarshart.answer('xatolik')

# """<<< admin uchun tanlov shartini o'zgartirish kamandasi"""




# '''admin uchun kanal o'chirish kamandasi >>>'''
@dp.message_handler(IsPrivate(),commands='delitechannel', chat_id=1737841515)
async def delitechannel(delite: types.Message):
    try:
        if delite.reply_to_message.text:
            send_ex(f"""DELITE FROM admins WHERE channel='{delite.reply_to_message.text}'""")
            await delite.answer("Kanal qo'shildi")
    except:
        await delite.answer('xatolik')

# '''<<< admin uchun kanal o'chirish kamandasi'''

