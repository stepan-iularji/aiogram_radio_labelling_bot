import os

API_TOKEN = os.environ.get('API_TOKEN')


welc_t = 'Привет!' + chr(129311) + '\nЯ вам помогу с расшифровкой маркировки радиодеталей!'
base_welc_t = 'Выберите нужный вам калькулятор! Помощь: /help'
resDip_welc_t = 'Последовательно введите цвета полос резистора , \n начиная с ближайшей к выводу резистора ,\nили с самой широкой полосы!\n Затем отправьте ' + chr(9989) +  'ВЫЧИСЛИТЬ'
resSmd_welc_t = 'Введите код SMD резистора!'
error_t = chr(10060) * 3 + 'Ошибка!!!\n'
LowInputLength_s = error_t + 'Короткий код SMD резистора!'
HighInputLength_s = error_t + 'Длиный код SMD резистора!'
IncorrectSymb_s = error_t + 'Недопустимый символ : '
IncorrectColor_s = error_t + 'Неверный формат кода!!!'
LowInputLength_t = error_t + 'Вы ввели мало полос : '
HighInputLength_t = error_t + 'Вы ввели много полос : '
IncorrectColor_t_1 = ' цвет не может являться '
IncorrectColor_t_2 = ' полосой \n'
IncorrectColor_t_3 =  '-полосного резистора.'
info_help = '\nБолее подробно читайте на '
c_info_res_dip = '/info_res_dip'
c_info_res_smd = '/info_res_smd'

info_base = '''Данный <i>чат-бот</i> призван помочь вам с <strong>расшифровкой маркировок радиодеталей.</strong>\n
На данный момент бот не явлеятся коммерческим, и полностью <b>бесплатен</b>, принадлежит своему разработчику!\n
Если у вас есть какие-либо мысли или идеи относительно данного бота , или вы нуждаетесь в разработке чат-бота, вы можете связаться с разработчиком, отправив этому боту текст вашего сообщения, заключенного в ***
<i>Например</i>: <i>***Привет , я столкнулся с ошибкой вашего калькулятора, свяжись со мной!***</i> 
Ваше сообщение будет доставлено по нужному адресу, разработчик напишет вам лично!\n
/start - Перезапуск бота
/help - Общая информация о боте ; Поддержка
/info_res_dip - Информация о маркировке DIP резисторов
/info_res_smd - Информация о маркировке SMD резисторов
'''

info_rd_1 = '''
В соответствии с ГОСТ 28883-90 и международным стандартом, сопротивление резисторов маркируется в виде цветных колец. Каждому цветному кольцу соответствует определенный цифровой код. Маркировка с тремя полосками используется для резисторов с точностью 20%, с четырьмя полосками – с точностью 5% и 10%, с пятью – с точностью до 0.005%. Шестая полоска на резистора показывает температурный коэффициент сопротивления (ТКС). Цветная маркировка на резисторах сдвинута к одному из выводов и читается слева направо. Первая полоса при этом - ближайшая к выводу резистора. Если из-за малого размера резистора цветную маркировку нельзя сдвинуть к одному из выводов, то первый знак делается полосой с шириной приблизительно вдвое большей, чем остальные.
'''
info_rd_2 = '''<b>* 3 полосы:</b>
Цвет первых двух полос означает первые цифры сопротивления. Третья полоса означает множитель в виде степени десяти, на который надо умножить число, состоящее из первых двух цифр. Точность резисторов с 3-мя полосами - 20%.

<b>* 4 полосы:</b>
Цвет первых двух полос означает первые цифры сопротивления. Третья полоса означает множитель в виде степени десяти, на который надо умножить число, состоящее из первых двух цифр. Четвертая полоса означает точность резистора в процентах. Она может быть серебристого или золотистого цвета, что значит допуск в 10% или 5% соответственно.

<b>* 5 полос:</b>
Цвет первых трех полос означает цифры сопротивления. Четвертая полоса означает множитель в виде степени десяти, на который надо умножить число, состоящее из первых трех цифр. Пятая полоса означает точность резистора в процентах.

<b>* 6 полос:</b>
Цвет первых трех полос означает цифры сопротивления. Четвертая полоса означает множитель в виде степени десяти, на который надо умножить число, состоящее из первых трех цифр. Пятая полоса означает точность резистора в процентах. Шестая полоса означает температурный коэффициент сопротивления.

<b>Температурный коэффициент сопротивления резистора:</b>
ТКС - величина, характеризующая относительное изменение сопротивления резистора при изменении температуры на один градус.
ТКС = [(R2-R1) / R1 * (T2 - T1)] * 0.000001
Что такое ± ppm/°С ?  За рубежом принято использовать сокращение ppm (Parts per million – одна миллионная часть). Считается, что такая запись гораздо удобнее, чем 1×10-6.
'''

info_rs_1 = '''В связи с размером SMD резисторов были разработаны особые способы маркировки. Наиболее часто встречающаяся маркировка содержит три или четыре цифры, либо  две цифры и букву, имеющая название EIA-96.

'''

un_t = chr(10060)
r_t = chr(9989)

base_keyboard = (('Резистор DIP' , 'Резистор SMD') ,)

colors_r = (chr(9899) + chr(65039) + 'Черный' , chr(128996) + 'Коричневый',
	chr(128308) + 'Красный' ,chr(128992) + 'Оранжевый' , chr(128993) + 'Желтый' ,
	chr(128994) + 'Зеленый', chr(128309) + 'Синий' ,chr(128995) + 'Фиолетовый' ,
	chr(128280) + 'Серый' , chr(9898) + chr(65039) + 'Белый', chr(128192) + 'Золотой',
	chr(128191) + 'Серебряный' )

b_count = chr(9989) +  'ВЫЧИСЛИТЬ'
b_back = chr(128281) + 'НАЗАД'
b_clear = chr(127377) + 'ОЧИСТИТЬ'

