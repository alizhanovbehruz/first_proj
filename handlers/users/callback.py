from loader import dp, bot
from aiogram import types
from utils.db_api.postgres import send_ex
from states.murojat import SendState
from keyboards.default.menu import menu
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext



 # """adminga kegan murojatni o'chirish >>>"""
@dp.callback_query_handler(text ='delite')
async def murojatdelite(delite: types.CallbackQuery):
    await delite.message.delete()

 # """<<< adminga kegan murojatni o'chirish """




# """admin foydalanuvchilarga javob xati yuborish >>>"""
@dp.callback_query_handler()
async def javob1(javob: types.CallbackQuery):
    print(javob.data)
    if javob.data[0:7] == 'murojat':
        await SendState.send_sms.set()
        global user
        user = javob.data[7:]
        await javob.message.answer('marxamat murojatga javob yozing:')


    elif javob.data[:10] == 'tekshirish':
        obuna = True
        channels = send_ex(f"""SELECT channel FROM admins""")
        for kanal in channels:
            link = kanal[0][13:]
            channel_members = await bot.get_chat_member(f"@{link}", javob.from_user.id)
            if channel_members.status not in ['member', 'creator', 'adminstrator']:
                obuna = False
                break
        if obuna:
            member = send_ex(f"""SELECT telegram_id from users""")
            ref_id = javob.data[10:]
            print(ref_id)
            if str(javob.from_user.id) not in [m[0] for m in member]:
                send_ex(f'''INSERT INTO users (name, username, telegram_id, refeller_id) 
                        VALUES('{javob.from_user.first_name}',
                        '{javob.from_user.username}','{javob.from_user.id}','{ref_id}') returning *''')
                if ref_id:
                    ball = send_ex(f"""SELECT ball FROM users WHERE telegram_id='{ref_id}' """)[0][0]
                    send_ex(f"""UPDATE users SET ball ={ball + 1} WHERE telegram_id='{ref_id}' returning *""")
                    await javob.message.answer(f"siz konkursimiz a'zosiga aylandingiz!\n\n")
            else:
                await javob.message.answer('Sizni allaqachon botga taklif qilishgan!')
            await javob.message.answer(
                f"KATTA TANLOVDAda qatnashing va pul mukofotlarini birini yutib oling. Tanlovda ishtirok etish uchun 👇"
                f"\n\nhttps://t.me/konkurs_sam_bot/?start={javob.from_user.id}\n\n"
                f"👆 Yuqoridagi sizning referal link/havolangiz. Uni koʼproq tanishlaringizga ulashing. Omad!",
                reply_markup=menu)

            # """<<<  userlar uchun refeller yaratish"""

        else:
            inline_kanal = InlineKeyboardMarkup(row_width=1,
                                                inline_keyboard=[
                                                    [InlineKeyboardButton(text=ch[0][13:], url=ch[0])] for ch in
                                                    channels
                                                ]
                                                )
            inline_kanal.add(InlineKeyboardButton('Tekshirish', callback_data='tekshirish'))
            await javob.message.answer("Tanlovda qatnashish uchun quyidagi kanallarga azo bo'ling",
                                            reply_markup=inline_kanal)

    # '''<<< admin belgilagan kanallarga foydalanuvchi obuna bo'lganini tekshrish'''


@dp.message_handler(state=SendState.send_sms)
async def commands(sendsms: types.Message, state=FSMContext):
    await bot.send_message(chat_id=sendsms.from_user.id, text='javob xati yuborildi')
    await bot.send_message(chat_id=user, text=f"sizga admindan javob xati \n{sendsms.text}")
    await state.finish()
# """<<<< admin foydalanuvchilarga javob xati yuborish"""



