import config
import component_labelling
import logging
import aiogram
import sqlighter
from aiogram import Bot, Dispatcher, executor, types

sql = sqlighter.SQLighter('db.db') #init dataBase

logging.basicConfig(level=logging.INFO)

#init BOT annd Dispatcher
bot = Bot(token=config.API_TOKEN) 
dp = Dispatcher(bot)



base_keyboard = types.ReplyKeyboardMarkup(
	keyboard = [
			[types.KeyboardButton(text = config.base_keyboard[0][0]) , types.KeyboardButton(text = config.base_keyboard[0][1])]
	 	] ,
	 	resize_keyboard = True
	 )

resDip_keyboard = types.ReplyKeyboardMarkup(
	keyboard = [
			[types.KeyboardButton(text = config.colors_r[0]) , types.KeyboardButton(text = config.colors_r[1]) , types.KeyboardButton(text = config.colors_r[2]) ],
			[types.KeyboardButton(text = config.colors_r[3]) , types.KeyboardButton(text = config.colors_r[4]) , types.KeyboardButton(text = config.colors_r[5]) ],
			[types.KeyboardButton(text = config.colors_r[6]) , types.KeyboardButton(text = config.colors_r[7]) , types.KeyboardButton(text = config.colors_r[8]) ],
			[types.KeyboardButton(text = config.colors_r[9]) , types.KeyboardButton(text = config.colors_r[10]) , types.KeyboardButton(text = config.colors_r[11]) ],
			[types.KeyboardButton(text = config.b_count) , types.KeyboardButton(text = config.b_clear)],
			[types.KeyboardButton(text = config.b_back)]
		],
		resize_keyboard = True
	)

resSmd_keyboard = types.ReplyKeyboardMarkup(
	keyboard = [
			[types.KeyboardButton(text = config.b_back)]
		],
		resize_keyboard = True
	)



def unkn(t):
	#print(message.chat.id)

	print('new')
	print(t)
	for c in t :
		print(ord(c) , end = ' ')
	print('--')

	return config.un_t






@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start`  command
    """
    
    

    if not(sql.chat_exists(message.chat.id)):
    	sql.add_chat(message.chat.id)

    sql.clr_input(message.chat.id)
    sql.up_stage(message.chat.id , '0')

    await message.answer(config.welc_t , reply_markup = base_keyboard)
    await message.answer(config.base_welc_t)


@dp.message_handler(commands=['help'])
async def com_help(message: types.Message):
	await message.answer(config.info_base , parse_mode = 'HTML')

@dp.message_handler(commands=['info_res_dip'])
async def com_info_res_dip(message: types.Message):
	await message.answer(config.info_rd_1 , parse_mode = 'HTML')
	#f = open('info_res_smd_ph.jpg')
	await message.answer_photo(photo = sql.get_file_id(1))
	await message.answer(config.info_rd_2 , parse_mode = 'HTML')

@dp.message_handler(commands=['info_res_smd'])
async def com_info_res_smd(message: types.Message):
	await message.answer(config.info_rs_1 , parse_mode = 'HTML')
	await message.answer_photo(photo = sql.get_file_id(2))
	await message.answer_photo(photo = sql.get_file_id(3))
	await message.answer_photo(photo = sql.get_file_id(4))
	await message.answer_photo(photo = sql.get_file_id(5))


@dp.message_handler()
async def echo(message: types.Message):

	stage = sql.get_stage(message.chat.id)

	if (message.text.strip()[:3] == '***') and (message.text.strip()[-3:] == '***'):
		await message.answer(config.r_t)
		await bot.send_message(chat_id = 667148258 , text = message.text + ' --- ' + str(message.from_user.mention))

	elif message.text == config.b_back :
		sql.up_stage(message.chat.id , 0)
		sql.clr_input(message.chat.id)
		await message.answer(config.b_back ,  reply_markup = base_keyboard)
		await message.answer(config.base_welc_t)

	elif message.text == config.b_clear :
		sql.clr_input(message.chat.id)
		await message.answer(config.b_clear)

	else:

		if stage == '0':

			if message.text == config.base_keyboard[0][0] :
				await message.answer(config.resDip_welc_t , reply_markup = resDip_keyboard)
				sql.up_stage(message.chat.id , '1')

			elif message.text == config.base_keyboard[0][1] :
				await message.answer(config.resSmd_welc_t , reply_markup = resSmd_keyboard)
				sql.up_stage(message.chat.id , '2')

			else:
				await message.answer(unkn(message.text))

		elif stage == '1':

			if message.text in config.colors_r :

				sql.add_input(message.chat.id , chr(config.colors_r.index(message.text)+49))
			
			elif message.text == config.b_count :
			
				r = str(sql.get_input(message.chat.id))
			

				r = [ord(i)-49 for i in r]
				#print('r=' , r)

				#s = sql.get_stage(message.chat.id)

				#print('s=' , s)
				res = ''
				#if s == '1' :
				try:
					res = component_labelling.d_res(r)
				except component_labelling.LowInputLength as exx:
					res = config.LowInputLength_t + str(exx.l) + config.info_help + config.c_info_res_dip

				except component_labelling.HighInputLength as exx:
					res = config.HighInputLength_t + str(exx.l) + config.info_help + config.c_info_res_dip

				except component_labelling.IncorrectColor as exx:
					res = config.error_t + config.colors_r[exx.color_i] + config.IncorrectColor_t_1 + str(exx.ind +1 ) + config.IncorrectColor_t_2 + str(exx.lent) + config.IncorrectColor_t_3 + config.info_help + config.c_info_res_dip

				await message.answer(res)
				sql.clr_input(message.chat.id)

			else:
				await message.answer(unkn(message.text))

		elif stage == '2':

			res = ''

			try :
				res = component_labelling.s_res(message.text)

			except component_labelling.LowInputLength as exx:
				res = config.LowInputLength_s + config.info_help + config.c_info_res_smd

			except component_labelling.HighInputLength as exx:
				res = config.HighInputLength_s + config.info_help + config.c_info_res_smd

			except component_labelling.IncorrectSymb as exx:
				res = config.IncorrectSymb_s + exx.symb + config.info_help + config.c_info_res_smd

			except component_labelling.IncorrectColor as exx:
				res = config.IncorrectColor_s + config.info_help + config.c_info_res_smd

			await message.answer(res)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
