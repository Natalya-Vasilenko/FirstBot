from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code
from aiogram.types import ParseMode

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    mtext = text(emojize('Привет! :lips:\nИспользуй /help'),
                        'чтобы узнать список доступных команд!')
    await message.reply(mtext)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = text(bold('Я могу ответить на следующие команды:'),
               '/test', '/mem', '/text', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['text'])
async def process_text_command(message: types.Message):
    mtext1 = text(italic('Сидит лось на рельсах,\nк нему другой лось подходит и говорит: "Подвинься"'))
    await message.reply(mtext1, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['test'])
async def process_test_command(message: types.Message):
    mtext1 = text(code('Я должен отвечать на эту команду смешной картиночкой,'
                       '\nно разрабы пока не знают, как прикрутить оправку медиа для меня'),
                  emojize(':crying_cat_face:'))
    await message.reply(mtext1, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['mem'])
async def process_mem_command(message: types.Message):
    mtext2 = text(code('Тут должен быть разрывной мем,'
                         '\nно разрабы пока не знают, как прикрутить оправку медиа для меня'),
                       emojize(':crying_cat_face::crying_cat_face::crying_cat_face:'))
    await message.reply(mtext2, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler()
async def unknown_message(msg: types.Message):
    message_text = text(emojize('Я не знаю, что с этим делать :eyes:'),
                        bold('\nПРОСТО НАПОМНЮ'), emojize(':rage::rage::rage:'),
                        '\nесть команда', '/help')
    await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(content_types=ContentType.ANY)
async def echo_message(msg: types.Message):
    message_text1 = text(emojize('С этим ТЕМ БОЛЕЕ я не знаю, что делать :eyes::eyes:'),
                        bold('\nПРОСТО НАПОМНЮ'), emojize(':rage::rage::rage:'),
                         '\nесть команда', '/help')
    await msg.reply(message_text1, parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    executor.start_polling(dp)