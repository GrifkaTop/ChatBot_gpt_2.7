from ML_base import ML_request
from datetime import *
import os.path
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils import executor
from datetime import datetime, timedelta
from aiogram import Bot, executor, types
from aiogram.dispatcher import Dispatcher

from config import TOKEN
# функция базы
# где все хранится будет
path_main = os.path.realpath(__file__)[:-7]
# Логирование инфы
current_datetime = str(datetime.now()).replace(':', '-')
logging.basicConfig(level=logging.INFO, filename=os.path.join(f"{path_main}log", f"py_log_{current_datetime}.log"),
                    filemode="w",
                    format="%(asctime)s : %(name)s : %(levelname)s : %(message)s")

# Подключение бота там где Токен вставить токен
bot = Bot(token=TOKEN)
# не думай
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

#индикатор запуска бота
print("Бот запустился!")


# ВСЯкая КРАСОТА
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    logging.info(f"new_user: {message.from_user.id}")
    await message.answer(
        'Пожалуйста, напишите начало сообщения матвея\n\nВ будущих версиях вы сможете задавать Матвею вопросы.')


# Все отальное

@dp.message_handler(content_types=["text"])
async def handle_text(message: types.Message, state: FSMContext):
    text = message.text
    logging.info(f"{message.from_user.id} print {text}")
    msg = await message.answer("Обрабытваем ваш запрос")
    answer = await ML_request(text)
    logging.info(f"Answer:{msg.message_id}. Bot print: {text}")
    await bot.edit_message_text(chat_id=msg.chat.id,
                                text=answer,
                                message_id=msg.message_id)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
