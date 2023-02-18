from aiogram.types import Message, ContentTypes
from loader import dp, bot
from states.poststate import PostsState
from aiogram.dispatcher import FSMContext
from utils.db_api.postgres import send_ex


@dp.message_handler(chat_id=1737841515, commands='post')
async def commanda(message: Message):
    await message.answer('Marxamat Post rasmini yuboring')
    await PostsState.photo.set()



@dp.message_handler(content_types=ContentTypes.PHOTO, state=PostsState.photo)
async def photos_com(message : Message, state=FSMContext):
    photo_id = message.photo[-1].file_id
    await state.update_data(
        {'photo_id': photo_id}
    )
    await message.answer("endi rasim matnini yuboring")
    await PostsState.next()
@dp.message_handler(state=PostsState.comment)
async def coma(message: Message, state = FSMContext):
    text = message.text
    data = await state.get_data()
    photo_i = data.get('photo_id')

    users_id = send_ex("""SELECT telegram_id FROM users""")
    # print(users_id)


    for id in users_id:
        try:
            await bot.send_photo(chat_id=id[0], photo=str(photo_i), caption=text)
        except:
            await bot.send_message(chat_id=5260472719, text=f"{id[0]}Bu foydalanuvchi botni tark etgan")
    await state.finish()


