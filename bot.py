import asyncio
import logging
from aiogram import Bot, Dispatcher
# Импортируем функции из других файлов
from handlers import setup_handlers
from db import create_table

# Включаем логирование
logging.basicConfig(level=logging.INFO)

API_TOKEN = '7747406396:AAEbx4fMCs0JHFT1XXHhHeR65r4MkCzLruY'

# Объект бота и диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

async def main():
    await create_table()  # Создаем таблицы базы данных
    setup_handlers(dp)     # Устанавливаем обработчики
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
