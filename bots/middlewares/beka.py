import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware


from loader import dp, bot
from utils.misc import subscription

from utils.db_api.postgres import send_ex


class BigBro(BaseMiddleware):
    async def on_pre_procc_update(self, update:types.Update, data:dict):
        CHANNELS = send_ex("""select channel_id from project_channel""")
        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return
        logging.info(user)
        ans = ' Botdan foydalanish uchun quyidagi kanallarga a\'zo bo\'ling'
        final_status = True
        for i in CHANNELS:
            status = await  subscription.check(user_id=user, channel=i)
            final_status *= status
            i = await bot.get_chat(i)
            if not status:
                inv_link = await i.export_invite_link()
                ans += (f"👉 <a href='{inv_link}'>{i.title}</a>\n")

        if not final_status:
            await update.message.answer(ans, disable_web_page_preview=True)
            raise CancelHandler()