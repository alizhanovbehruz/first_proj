from aiogram import types
from utils.db_api.postgres import send_ex
from keyboards.inline.language import til, admin, menu, user, user_ru
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from keyboards.default.menu import menu
from filters.private_chat import IsPrivate
from loader import dp, bot
from utils.misc.subscription import check

admins = 1737841515
bot_url = 'https://t.me/testing8342132bot'




@dp.message_handler(commands='start')
async def starts(message: types.Message):
    """refeller uchun"""
    ref_id = message.text[7:]
    if message.from_user.id == admins:
        """admin botga start bossa"""
        til = send_ex("""select til from project_creator""")
        if til[0][0] == 'ru':
            pass
        else:
            await message.answer('Salom Admin siz Bosh Sahifadasiz',reply_markup=admin)

    elif ref_id:
        """Taklif qilingan odam"""

        users = send_ex('''select tg_id from project_author''')
        if str(message.from_user.id) not in [i[0] for i in users]:
            if int(ref_id) != int(admins):
                user = send_ex('''SELECT zanjir FROM project_author''')
            else:
                user = send_ex(f'''SELECT tg_id FROM project_creator''')
            path = f"{user[0][0]}/{message.from_user.id}"
            if len(path) > 110:
                path = path.split('/')
                path.pop(0)
                '/'.join(path)
            send_ex(f"""insert into project_author(name, zanjir, price, tg_id) values('{message.from_user.first_name}','{path}', 1,'{message.from_user.id}') returning * """)
            from keyboards.inline.language import til
            await message.answer('Tilni tanlang:\nВыберите язык:', reply_markup=til)
        else:
            '''Taklif qilib bo'lingan foydalanuvchi'''
            await message.answer(f'Salom {message.from_user.first_name}', reply_markup=menu)
    else:
        users = send_ex('''select tg_id from project_author''')
        if str(message.from_user.id) not in [i[0] for i in users]:
            """hechkim taklif qilmay botga start bosgan user admin tagidan hisobga kiradi"""

            user = send_ex(f'''SELECT tg_id FROM project_creator''')
            path = f"{user[0][0]}/{message.from_user.id}"
            send_ex(f"""insert into project_author(name, zanjir, price, tg_id) values('{message.from_user.first_name}','{path}', 1,'{message.from_user.id}') returning * """)
            from keyboards.inline.language import til
            await message.answer('Tilni tanlang:\nВыберите язык:', reply_markup=til)
        else:
            lan = send_ex("""select til from project_author""")
            if lan[0][0] == 'ru':
                from keyboards.inline.language import user_ru
                await message.answer(f'Привет {message.from_user.first_name}', reply_markup=user_ru)
            else:
                from keyboards.inline.language import user
                await message.answer(f'Salom {message.from_user.first_name}', reply_markup=user)


@dp.callback_query_handler(text='tekshir_uz')
async def checking(call: types.CallbackQuery):
    await call.answer()
    ans = ''
    CHANNELS = [i[0] for i in send_ex("""select channel_id from project_channel""")]
    for i in CHANNELS:
        status = await check(user_id=call.from_user.id,channel=i)
        i = await bot.get_chat(i)
        if status:
            ans += f'<b>{i.title}</b>✅\n'
        else:
            inv_link = await i.export_invite_link()
            ans += (f'<b>{i.title}</b> ❌'
                    f"<a href='{inv_link}'>obuna buling</a>\n")


    await call.message.answer(ans)

@dp.callback_query_handler(text='tekshir_ru')
async def callbacktekshir(call: types.CallbackQuery):
    await call.answer()
    ans = ''
    CHANNELS = [i[0] for i in send_ex("""select channel_id from project_channel""")]
    for i in CHANNELS:
        status = await check(user_id=call.from_user.id,channel=i)
        i = await bot.get_chat(i)
        if status:
            ans += f'<b>{i.title}</b>✅\n'
        else:
            inv_link = await i.export_invite_link()
            ans += (f'<b>{i.title}</b> ❌'
                    f"<a href='{inv_link}'>подписаться</a>\n")



@dp.callback_query_handler(text='lang_uz')
async def callbacklang(message: types.CallbackQuery):
    send_ex(f"""UPDATE project_author SET til = 'uz' WHERE tg_id ='{message.from_user.id}' returning * """)
    await message.message.answer(f"Salom {message.from_user.first_name} botdan foydalanish uchun quyidagi kanallarga a'zo bo'ling", reply_markup=kanal)


@dp.callback_query_handler(text='lang_ru')
async def callbacklang(message: types.CallbackQuery):
    send_ex(f"""UPDATE project_author SET til = 'ru' WHERE tg_id ='{message.from_user.id}' returning * """)
    await message.message.answer(f"Привет {message.from_user.first_name} Подпишитесь на следующие каналы, чтобы использовать бота", reply_markup=kanal_ru)




@dp.callback_query_handler(text ='refeller')
async def callbackprofile(message: types.CallbackQuery):
    await message.message.delete()
    await message.message.answer(f"Sizning refelleringiz:\n\n{bot_url}?start={message.from_user.id}\n\n", reply_markup=menu)


@dp.callback_query_handler(text='profile')
async def callbackprofile(message: types.CallbackQuery):
    if message.from_user.id == admins:
        info = send_ex('''select price from project_creator''')
    else:
        info = send_ex(f"""select price from project_author where tg_id='{str(message.from_user.id)}'""")
    await message.message.delete()
    await message.message.answer(f"Profile {message.from_user.first_name}\nBalance: {info[0][0]}", reply_markup=menu)



@dp.callback_query_handler(text ='menu')
async def callbackmenu(message: types.CallbackQuery):
    channel = send_ex("""select channel_id from project_channel""")
    obuna = 1
    for i in channel:
        s = await bot.get_chat_member(int(i[0]), message.from_user.id)
        if s.status == 'left':
            obuna=0
            break
    if obuna:
        await message.message.delete()
        if message.from_user.id != admins:
            await message.message.answer(f'Salom {message.from_user.first_name}', reply_markup=user)
        else:
            await message.message.answer(f'Salom Admin siz bosh sahifadasiz', reply_markup=admin)
    else:
        await message.message.delete()
        await message.message.answer("quyidagi kannallarga a'zo bo'ling", reply_markup=kanal)




