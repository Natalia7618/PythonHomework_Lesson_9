from pyrogram import Client, filters
import logging
import download
import os
import validation

logging.basicConfig(level = logging.INFO)

bot = Client(
    "ses1",
    api_id = 348759, 
    api_hash = "5dc6f4b54b1985199b42a069a5745306",
    workers = 100, 
    bot_token = '5318135141:AAF7nUV62qC4sA0POqirp9bVIglWIJ4L2U4')

@bot.on_message(filters.command("start", ["!", "/"]))
def connect(chat, m):
	try:
		userID = m.chat.id
		bot.send_message(userID, 'Привет! Я твой помощник для скачивания видео из YouTube. Отправь мне ссылку и я отправлю тебе скачанное видео в ответ :)')
	except Exception as e:
		print(e)

@bot.on_message(filters.text)
def get(chat, m):
	url = m.text	
	userID = m.chat.id
	try:
		VID_ID = ''
		VID_ID = validation.to_valid(url, VID_ID) 
		bot.send_message(m.chat.id, 'Начинаю загрузку видео... Нужно немного подождать :)')
		download.worker(VID_ID) 
		bot.send_video(m.chat.id, str(VID_ID) + '.mp4') 
		os.remove(VID_ID + '.mp4') 
	except Exception as e:
		bot.send_message(m.chat.id, f'Неправильная ссылка! Введите ссылку с сайта Youtube. `{e}`')	

bot.run()