import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from openai import OpenAI

# ====== ВСТАВЬ СЮДА СВОИ ТОКЕНЫ ======
TOKEN = ":AAHIdjrrXBOaIPD6-wN17cXtxleHYOWxJiw"
OPENAI_KEY = "k-proj-aG-g0jOcnTf5U7G8IJSzTd6-OBqaZKQYy9cZTFhpvivaJkWE406r_aADSN61TGCV4kjBtHC5GUT3BlbkFJTPLcvYuqfD7gH8BIHNuDxBSSP8S-82X59omiSFymFTHFAs_xn4jt28Ux3l-Rv1JbhRokjYFkQA"
# =====================================

bot = Bot(TOKEN)
dp = Dispatcher()
client = OpenAI(api_key=OPENAI_KEY)

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("👋 Yo! I'm your AI bot. Just text me anything.")

@dp.message()
async def chat(message: types.Message):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": message.text}]
    )
    answer = response.choices[0].message["content"]
    await message.answer(answer)

async def main():
    print("Bot is starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())