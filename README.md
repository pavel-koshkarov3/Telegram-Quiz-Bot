# Telegram Quiz Bot

## Команды
- `/start` - Начало работы с ботом.
- `/quiz` - Начать квиз.

## Описание
Этот бот проводит квиз по различным вопросам. Каждый пользователь может проходить квиз и получать результаты.

## Как найти бота
[Ссылка на бота](https://t.me/Brain_Teaser_Bot)

## Установка и запуск
1. Клонирование репозитория
   git clone https://github.com/your-repo/telegram-quiz-bot.git
   cd telegram-quiz-bot
2. Установка зависимостей
   Рекомендуется использовать виртуальное окружение:
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate  # Для Windows
   pip install -r requirements.txt
3. Настройка переменных окружения
   Создайте файл .env и добавьте в него:
   BOT_TOKEN=your_telegram_bot_token
   DATABASE_URL=your_database_url
4. Запуск бота
   python bot.py
