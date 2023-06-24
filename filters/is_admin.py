from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class AdminFilter(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        member = await message.chat.get_member(user_id=message.from_user.id)
        return member.is_chat_admin()
