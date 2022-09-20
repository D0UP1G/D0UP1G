import logging

import random
import cmds
import tokens
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, InlineKeyboardButton,  KeyboardButton

logging.basicConfig(level=logging.INFO)

bot = Bot(token = tokens.tkns)
dp = Dispatcher(bot)


@dp.message_handler(commands=['add'])
async def add(message: types.Message):
    cmds.mat.append(message.text[5:50])

    print(cmds.mat)

@dp.message_handler(commands=['start'])
async def NewMem(message: types.Message):
    fire = KeyboardButton(text='💥', callback_data= 'fire')
    kybr = InlineKeyboardMarkup()
    kybr.add(fire)
    
    
    await bot.send_message(message.from_user.id, 'Привет, я Еврей, скинь пж, на карту немного золотого',
                           Markup=kybr)

@dp.message_handler(commands=['delm'])
async def deadd(message: types.Message):
#    await cmds.mat.remove()
    print(1000-7)





@dp.message_handler()
async def sortMes(message: types.Message):
    if message.text.lower() in cmds.mat:
        await message.delete()
        await bot.send_message(message.from_user.id, "нельзя такое говорить")

@dp.message_handler()
async def fire():
    if

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
