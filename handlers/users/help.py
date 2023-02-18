from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from filters.private_chat import IsPrivate

from loader import dp


@dp.message_handler(IsPrivate(), CommandHelp(),chat_id=1737841515)
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/setshart - Tanlov shartini o'zgartirish",
            "/users - foydalanuvchilar haqida malumot",
            "/addchannel - Tanlovga kanal qo'shish",
            "/delitechannel - Mavjud kannallarni o;chirish",
            "/post - bot foydalanuvchilarga Post yuborish")
    await message.answer("\n".join(text))

@dp.message_handler(IsPrivate(), CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    await message.answer("\n".join(text))