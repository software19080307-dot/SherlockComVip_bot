import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import asyncio
import os

TOKEN = "8558971167:AAE9GFlX26_HVWS36BdcMIsF6dVnXEyCLM4"

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

SITES = {
    "Telegram": "https://t.me/{}",
    "Instagram": "https://instagram.com/{}",
    "TikTok": "https://tiktok.com/@{}",
    "GitHub": "https://github.com/{}",
}

@dp.message()
async def handler(message: types.Message):
    username = message.text.strip()

    text = f"🔍 Проверяю: {username}\n\n"

    for name, url in SITES.items():
        text += f"➡️ {name}: {url.format(username)}\n"

    await message.answer(text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
