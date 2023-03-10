from aiogram import types
from utils.db_api.postgres import send_ex
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from states.murojat import MurojatState
from filters.private_chat import IsPrivate
from loader import dp, bot
from aiogram.dispatcher import FSMContext

# '''Tugmalar uchun handlarlar'''
@dp.message_handler(IsPrivate(),text ='馃摙 Tanlovda ishtirok etish')
async def tanlovdaishtirok(ishtirok: types.Message):
    await ishtirok.answer(
        f"KATTA TANLOVDAda qatnashing va pul mukofotlarini birini yutib oling. Tanlovda ishtirok etish uchun 馃憞"
        f"\n\nhttps://t.me/konkurs_sam_bot/?start={ishtirok.from_user.id}\n\n"
        f"馃憜 Yuqoridagi sizning referal link/havolangiz. Uni ko始proq tanishlaringizga ulashing. Omad!")

@dp.message_handler(IsPrivate(),text ='馃搳 Reyting')
async def tanlovreyitng(reyting: types.Message):
    reyting_user = send_ex(f"""SELECT ball FROM users WHERE telegram_id='{reyting.from_user.id}'""")
    reyting10 =send_ex(f"""SELECT name,ball FROM users ORDER BY ball DESC LIMIT 10""")
    top = f"馃搳 Botimizga eng ko始p do始stini taklif qilib ball to始plaganlar ro始yhati:\n\n"
    n = 1
    for name, bal in reyting10:
        if n == 1:
            top +=f"馃 {n}-o'rin {name} -> {bal} ball\n"
        elif n == 2:
            top += f"馃 {n}-o'rin {name} -> {bal} ball\n"
        elif n == 3:
            top +=f"馃 {n}-o'rin {name} -> {bal} ball\n"
        else:
            top +=f"馃弲 {n}-o'rin {name} -> {bal} ball\n"
        n+=1
    await reyting.answer(top+f"\n\n鉁? Sizda {reyting_user[0][0]} ball. Ko'proq do'stlaringizni taklif etib ballaringizni ko'paytiring!\n\n"
    f"鈥硷笍 Nakrutka qilganlar, pullik spamlardan, 馃敒 axloqsiz kanallarda spam tarqatganlar"
    f" konkursdan chetlashtiriladi. 鈥硷笍")


@dp.message_handler(IsPrivate(),text ='馃棐 Tanlov shartlari')
async def tanlovshartlar(shart: types.Message):
    database_sharti = send_ex('''SELECT sharti FROM tanlov_sharti WHERE id=(SELECT MAX(ID) FROM tanlov_sharti)''')
    if database_sharti:
        await shart.answer(database_sharti[0][0])
    else:

        await shart.answer(f"馃帗 TANLOV SHARTLARI\n"
        f"KATTA KONKURSda g'oliblar to鈥榩lagan ballariga qarab aniqlanadi.\n\n"
        
        f"鉂? Ballar qanday to鈥榩lanadi?\n\n"
        
        f"鉃? BOTda keltirilgan kanallarga obuna bo鈥榣gach, 芦Obuna bo鈥榣dim禄 tugmasini bosasiz, so'ngra Ism familiyangiz va telefon raqamingizni yuborsiz. Shundan so'ng 芦馃摙 Tanlovda ishtirok etish禄 tugmasini bosganingizdan sizga maxsus referal link (havola) beriladi.\n\n"
        
        f"鉃? O鈥榮ha link orqali obuna bo鈥榣gan har bir inson uchun sizga +1 balldan berib boriladi. Qancha ko鈥榩 ball yig鈥榮angiz, g鈥榦lib bo鈥榣ish imkoniyatingiz shuncha ortib boradi.\n\n"
        
        f"馃挔 25-dekabr kuni 23:59 da ball yig'ish to'xtatiladi va eng ko'p ball yig'gan 10 ishtirokchi pul yutuqlari bilan taqdirlanadi:\n\n"
        
        f"馃 1-o'rin 鈥? Xiaomi RedMi 1A telefoni\n"
        f"馃 2-o'rin 鈥? Xiaomi RedMi 9A telefon\n"
        f"馃 3-o'rin 鈥? 500 ming so'm\n"
        f"馃帡 4-5-6 - o'rinlar 鈥? 200 ming so'm\n"
        f"馃帡 8-9-10 - o'rinlar 鈥? 100 ming so'm\n\n"
        
        f"鈥硷笍 Diqqat! <b>bu bot sinov jarayonida ko'rsatilgan sovrinlar mavjud emas</b>\nTanlov davomida sun鈥檌y (o鈥榣ik akkauntlar qo鈥榮hgan), boshqa davlatlar raqamlaridan qatnashgan, nakrutka va h.k.lardan foydalanganlar tanlovdan chetlashtiriladi!\n\n"
        
        f"馃檪 Faol bo鈥榣ing va pul yutuqlaridan birini yutib oling. Barchaga omad!")


@dp.message_handler(IsPrivate(),text ='Bot haqida')
async def haqida(haqid: types.Message):
    await haqid.answer(f"assalomu aleykum bu bot @AIisheyx tomonidan yaratilgan\n\n"
                       f"bot nimaga kerak? \n"
                       f"Bot egasi bir yoki birnechta kannallarga obunachi yig'ib berish maqsadida bot yordamida konkurs o'tkazadi.\nbotda har bir kishining takrorlanmas taklif qilish linki bo'ladi va shu link yordamida botga odamlarni taklif qiladi va har bir taklif qilingan user uchun 1 baldan oladi va botga eng ko'p odam taklif qilganlar. bot egasi ajratgan sovrinlar bilan taqdirlanadi.\nuserlar botdan foydalanish uchun admin belgilagan kanallarga obuna bo'lishlari shart!\n\n"
                        f"Bot python, aiogram va postgresql texnologilayari ishlatilgan"
                        f"va admin uchun alohida imkoniyatlar mavjud:\n\n"
                        f"  tanlov uchun kanallar qo'shish, o'chirish\n\n"
                        f"  tanlov shartini o'zgartirish imkoniyati\n\n"
                        f"  barcha foydalanuvchilarga xabar yuborish imkoniyati\n\n"
                        f"  bot foydalanuvchilar soni ko'rish"
                        f"  va foydalanuvchilarning qisqacha telegram malumotlari(ism, familya, username va tanlovda to'plagan ballari va hokazolarni) taqdim etadi\n\n"
                        f"siz ham shundey botingiz bo'lishini istasangiz\n"
                        f"yoki boshqa turdagi dasturlash xizmatiga extiyojingiz bo'lsa  @AIisheyx ga  murojat qiling\n\n",parse_mode='MarkDown')



@dp.message_handler(IsPrivate(),text ='鈽庯笍 Murojaat')
async def tanlovmurojat(murojat: types.Message):
    user = send_ex(f"""SELECT ball FROM users WHERE telegram_id='{murojat.from_user.id}'""")[0][0]
    if user > 10:
        await murojat.answer(f"Admin bilan bog'laish uchun kamida 10 ball to'plagan bo'lishingiz kerak!\nhozirda to'lpagan ballaringiz - {user} ball")
    else:
        await murojat.answer('Marxamat murojatingizni yozib qoldirishingiz mumkin:')
        await MurojatState.tingla.set()

@dp.message_handler(state=MurojatState.tingla)
async def tanlovmurojat2(murojat2: types.Message,state = FSMContext):
    inline_murojat = InlineKeyboardMarkup(
        inline_keyboard=[
            {InlineKeyboardButton(text='javob yozish',callback_data=f'murojat{murojat2.from_user.id}'),
             InlineKeyboardButton(text="o'chirish", callback_data="delite")}
        ]
    )
    await bot.send_message(chat_id=murojat2.from_user.id, text='Murojatingiz adminga yuborildi')
    await bot.send_message(chat_id=1737841515,text= f'sizga foydalanuvchi @{murojat2.from_user.username} dan murojat\n {murojat2.text}', reply_markup=inline_murojat)
    await state.finish()

