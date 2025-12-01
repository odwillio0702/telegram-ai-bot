
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from openai import OpenAI
ipmort os

# Получаем токены из Environment Variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

# Создаём объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Создаём клиент OpenAI (без proxies!)
client = OpenAI(api_key=OPENAI_KEY)

# Команда /start
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Hey! I'm your AI bot. Just send me a message 😊")

# Обработка любых сообщений
@dp.message()
async def chat(message: types.Message):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": message.text}
            ]
        )
        answer = response.choices[0].message["content"]
        await message.answer(answer)
    except Exception as e:
        await message.answer(f"Error: {str(e)}")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())