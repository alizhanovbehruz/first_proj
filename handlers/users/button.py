from aiogram import types
from utils.db_api.postgres import send_ex
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from states.murojat import MurojatState
from filters.private_chat import IsPrivate
from loader import dp, bot
from aiogram.dispatcher import FSMContext

# '''Tugmalar uchun handlarlar'''
@dp.message_handler(IsPrivate(),text ='📢 Tanlovda ishtirok etish')
async def tanlovdaishtirok(ishtirok: types.Message):
    await ishtirok.answer(
        f"KATTA TANLOVDAda qatnashing va pul mukofotlarini birini yutib oling. Tanlovda ishtirok etish uchun 👇"
        f"\n\nhttps://t.me/konkurs_sam_bot/?start={ishtirok.from_user.id}\n\n"
        f"👆 Yuqoridagi sizning referal link/havolangiz. Uni koʼproq tanishlaringizga ulashing. Omad!")

@dp.message_handler(IsPrivate(),text ='📊 Reyting')
async def tanlovreyitng(reyting: types.Message):
    reyting_user = send_ex(f"""SELECT ball FROM users WHERE telegram_id='{reyting.from_user.id}'""")
    reyting10 =send_ex(f"""SELECT name,ball FROM users ORDER BY ball DESC LIMIT 10""")
    top = f"📊 Botimizga eng koʼp doʼstini taklif qilib ball toʼplaganlar roʼyhati:\n\n"
    n = 1
    for name, bal in reyting10:
        if n == 1:
            top +=f"🥇 {n}-o'rin {name} -> {bal} ball\n"
        elif n == 2:
            top += f"🥈 {n}-o'rin {name} -> {bal} ball\n"
        elif n == 3:
            top +=f"🥉 {n}-o'rin {name} -> {bal} ball\n"
        else:
            top +=f"🏅 {n}-o'rin {name} -> {bal} ball\n"
        n+=1
    await reyting.answer(top+f"\n\n✅ Sizda {reyting_user[0][0]} ball. Ko'proq do'stlaringizni taklif etib ballaringizni ko'paytiring!\n\n"
    f"‼️ Nakrutka qilganlar, pullik spamlardan, 🔞 axloqsiz kanallarda spam tarqatganlar"
    f" konkursdan chetlashtiriladi. ‼️")


@dp.message_handler(IsPrivate(),text ='🗒 Tanlov shartlari')
async def tanlovshartlar(shart: types.Message):
    database_sharti = send_ex('''SELECT sharti FROM tanlov_sharti WHERE id=(SELECT MAX(ID) FROM tanlov_sharti)''')
    if database_sharti:
        await shart.answer(database_sharti[0][0])
    else:

        await shart.answer(f"🎓 TANLOV SHARTLARI\n"
        f"KATTA KONKURSda g'oliblar to‘plagan ballariga qarab aniqlanadi.\n\n"
        
        f"❓ Ballar qanday to‘planadi?\n\n"
        
        f"➖ BOTda keltirilgan kanallarga obuna bo‘lgach, «Obuna bo‘ldim» tugmasini bosasiz, so'ngra Ism familiyangiz va telefon raqamingizni yuborsiz. Shundan so'ng «📢 Tanlovda ishtirok etish» tugmasini bosganingizdan sizga maxsus referal link (havola) beriladi.\n\n"
        
        f"➖ O‘sha link orqali obuna bo‘lgan har bir inson uchun sizga +1 balldan berib boriladi. Qancha ko‘p ball yig‘sangiz, g‘olib bo‘lish imkoniyatingiz shuncha ortib boradi.\n\n"
        
        f"💠 25-dekabr kuni 23:59 da ball yig'ish to'xtatiladi va eng ko'p ball yig'gan 10 ishtirokchi pul yutuqlari bilan taqdirlanadi:\n\n"
        
        f"🥇 1-o'rin — Xiaomi RedMi 1A telefoni\n"
        f"🥈 2-o'rin — Xiaomi RedMi 9A telefon\n"
        f"🥉 3-o'rin — 500 ming so'm\n"
        f"🎗 4-5-6 - o'rinlar — 200 ming so'm\n"
        f"🎗 8-9-10 - o'rinlar — 100 ming so'm\n\n"
        
        f"‼️ Diqqat! <b>bu bot sinov jarayonida ko'rsatilgan sovrinlar mavjud emas</b>\nTanlov davomida sun’iy (o‘lik akkauntlar qo‘shgan), boshqa davlatlar raqamlaridan qatnashgan, nakrutka va h.k.lardan foydalanganlar tanlovdan chetlashtiriladi!\n\n"
        
        f"🙂 Faol bo‘ling va pul yutuqlaridan birini yutib oling. Barchaga omad!")


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



@dp.message_handler(IsPrivate(),text ='☎️ Murojaat')
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

