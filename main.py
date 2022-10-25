import asyncio
import os
import logging

from aiogram import Bot, Dispatcher, executor, types
import aiohttp

import logic
from apitoken import API_TOKEN
import datetime
from logic import *

logging.basicConfig(level=logging.INFO)

API_TOKEN = API_TOKEN
my_id = '1118806718'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


#async def check_time():
#    while True:
#        await logic.check_notifications()
#        await asyncio.sleep(0.5)


@dp.message_handler(commands=['start'])
async def process_greetings(message: types.Message):
    if str(message['from']['id']) != my_id:
        return await message.reply('Ты не мой хозяин', reply=False)
    await bot.send_message(message.from_user.id, f'Привет, user {message.from_user.id}, работа запущена')


@dp.message_handler(commands=['help'])
async def process_greetings(message: types.Message):
    if str(message['from']['id']) != my_id:
        return await message.reply('Ты не мой хозяин', reply=False)
    await bot.send_message(message.from_user.id, f'Данный бот создан для отправления напоминаний')


@dp.message_handler(commands=['notifications'])
async def process_greetings(message: types.Message):
    await bot.send_message(message.from_user.id, 'Пытаюсь показать напоминалки')
    await bot.send_message(message.from_user.id, 'Введите текст напоминания')


@dp.message_handler()
async def create_notification(message: types.Message):
    inp = message.text
    time = datetime.datetime.now() + datetime.timedelta(0, 5)
    logic.create_notification(inp, time, message.from_user.id)
    await bot.send_message(message.from_user.id, 'Напоминание записано')


if __name__ == '__main__':
    #loop = asyncio.get_event_loop()
    #loop.create_task(check_time())
    executor.start_polling(dp, skip_updates=True)





