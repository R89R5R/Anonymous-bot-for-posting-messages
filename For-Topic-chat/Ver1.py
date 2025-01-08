import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "Your_Token"
TOPIC_MESSAGE_ID = 132  # ID первого сообщения в топике
GROUP_CHAT_ID = -100123456789  # chat_id вашей группы (с приставкой -100 для супергруппы)

# Инициализация бота
bot = Bot(token=TOKEN)

# Инициализация диспетчера
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer("Привет! Отправь мне сообщение, чтобы я мог ответить в топик.")

# Обработчик всех текстовых сообщений
@dp.message()
async def forward_to_topic(msg: types.Message):
    # Получаем текст вашего сообщения
    user_message_text = msg.text
    
    # Отправляем ваше сообщение в топик
    await bot.send_message(
        chat_id=GROUP_CHAT_ID, 
        text=user_message_text,  # Пересылаем текст пользователя в топик
        reply_to_message_id=TOPIC_MESSAGE_ID,  # ID первого сообщения в топике
        parse_mode="Markdown"  # Опционально, указываем формат
    )

# Запуск бота через asyncio
async def main():
    # Используем polling для получения новых сообщений
    await dp.start_polling(bot)

if __name__ == '__main__':
    # Запуск основного цикла событий
    asyncio.run(main())
