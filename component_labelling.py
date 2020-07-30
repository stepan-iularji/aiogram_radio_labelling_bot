import math


admission_r = ('0.005' , '1' , '2' , '0.01' , '0.02' , '0.5' , '0.25' , '0.1' , '0.05' , '_' , '5' , '10')

tks_r = ('' , '100' , '50' , '15' , '25' , '' , '10' , '5' , '' , '1' , '500' , '1000')

pr_d = { 18 : 'Э' , 15 : 'П' , 12 : 'Т' , 9 : 'Г' , 6 : 'М' , 3 : 'к' , 2 : 'г' , 1 : 'да', 
0 : '' , -1 : 'д' , -2 : 'с' , -3 : 'м' , -6 : 'мк' , -9 : 'Н' , -12 : 'п' , -15 : 'ф' , -18 : 'а'}

all_pr = (18 , 15 , 12 , 9 , 6 , 3 , 2 , 1 , 0, -1 , -2 , -3, -6 , -9 , -12 , -15 , -18)

power_r_s = {
	'Z' : -3 ,
	'Y' : -2 ,
	'R' : -2 ,
	'X' : -1 ,
	'S' : -1 ,
	'A' : 0 ,
	'B' : 1 ,
	'H' : 1 ,
	'C' : 2 ,
	'D' : 3 ,
	'E' : 4 ,
	'F' : 5 
}

codes_r_s = {
	'01' : 100 ,
	'02' : 102 ,
	'03' : 105 ,
	'04' : 107 ,
	'05' : 110 ,
	'06' : 113 ,
	'07' : 115 ,
	'08' : 118 ,
	'09' : 121 ,
	'10' : 124 ,
	'11' : 127 ,
	'12' : 130 ,
	'13' : 133 ,
	'14' : 137 ,
	'15' : 140 ,
	'16' : 143 ,
	'17' : 147 ,
	'18' : 150 ,
	'19' : 154 ,
	'20' : 158 ,
	'21' : 162 ,
	'22' : 165 ,
	'23' : 169 ,
	'24' : 174 ,
	'25' : 178 ,
	'26' : 182 ,
	'27' : 187 ,
	'28' : 191 ,
	'29' : 196 ,
	'30' : 200 ,
	'31' : 205 ,
	'32' : 210 ,
	'33' : 215 ,
	'34' : 221 ,
	'35' : 226 ,
	'36' : 232 ,
	'37' : 237 ,
	'38' : 243 ,
	'39' : 249 ,
	'40' : 255 ,
	'41' : 261 ,
	'42' : 267 ,
	'43' : 274 ,
	'44' : 280 ,
	'45' : 287 ,
	'46' : 294 ,
	'47' : 301 ,
	'48' : 309 ,
	'49' : 316 ,
	'50' : 324 ,
	'51' : 332 ,
	'52' : 340 ,
	'53' : 348 ,
	'54' : 357 ,
	'55' : 365 ,
	'56' : 374 ,
	'57' : 383 ,
	'58' : 392 ,
	'59' : 402 ,
	'60' : 412 ,
	'61' : 422 ,
	'62' : 432 ,
	'63' : 442 ,
	'64' : 453 ,
	'65' : 464 ,
	'66' : 475 ,
	'67' : 487 ,
	'68' : 499 ,
	'69' : 511 ,
	'70' : 523 ,
	'71' : 536 ,
	'72' : 549 ,
	'73' : 562 ,
	'74' : 576 ,
	'75' : 590 ,
	'76' : 604 ,
	'77' : 619 ,
	'78' : 634 ,
	'79' : 649 ,
	'80' : 665 ,
	'81' : 681 ,
	'82' : 698 ,
	'83' : 715 ,
	'84' : 732 ,
	'85' : 750 ,
	'86' : 768 ,
	'87' : 787 ,
	'88' : 806 ,
	'89' : 825 ,
	'90' : 845 ,
	'91' : 866 ,
	'92' : 887 ,
	'93' : 909 ,
	'94' : 931 ,
	'95' : 953 ,
	'96' : 976 



}

class LowInputLength(Exception):
	def __init__(self , l):
		Exception.__init__(self)
		self.l = l

class HighInputLength(Exception):
	def __init__(self , l):
		Exception.__init__(self)
		self.l = l

class IncorrectColor(Exception):
	def __init__(self , ind=0 , color_i=0 , lent=0):
		Exception.__init__(self)
		self.ind = ind 
		self.color_i = color_i
		self.lent = lent

class IncorrectSymb(Exception):
	def __init__(self , ind , symb):
		Exception.__init__(self)
		self.ind = ind 
		self.symb = symb


def d_res(a):

	nom = 0
	l=len(a);
	#print(a[len(a)-1])
	if l < 3 :
		raise  LowInputLength(l) #errror
	elif l < 5:
		l = 2
	elif l <= 6:
		l = 3
	else:
		raise  HighInputLength(l) #errror

	#print(a)

	if a[0] in (0 , 10 , 11):
		raise IncorrectColor(0 , a[0] , len(a))

	if a[1] in(10 , 11):
		raise IncorrectColor(1 , a[1] , len(a))

	if l==3:
		if a[2] in(10 , 11):
			raise IncorrectColor(2 , a[2] , len(a))

	if a[l] in(9,):
		raise IncorrectColor(l , a[l] , len(a))

	if len(a) > 3 :
		if a[l+1] in(9,):
			raise IncorrectColor(l+1 , a[l+1] , len(a))

	if len(a) > 5 :
		if a[l+2] in(0 , 5 , 8):
			raise IncorrectColor(l+2 , a[l+2] , len(a))

	#print('l=' , l)

	for i in range(0, l):
		z = a[i]
		if z in range(1 , 10):
			nom+=z * (10**(l-1-i))
			#print(i)
			#print(nom)

	#print ('nom' , nom)

	z = a[l]
	#print(z)
	if z < 9 :
		nom = nom*(10**(z))
	elif z==10 :
		nom = nom/10
	elif z==11 :
		nom = nom/100
	else:
		pass

	#print ('nom = ' , nom)

	nom = pr(nom ,  6 , 3 ,  0 , -3)
	nom += 'Ом'
	
	#print (nom)
	
	if len(a)>3 :
		nom+= ' ± '
		nom += admission_r[a[l+1]]
		nom+='%'

	if len(a)>5 :
		nom+= ' , '
		nom+= tks_r[a[5]]
		nom+= ' ppm/°С'

	return nom

#d_res(['Красный' , 'Черный' , 'Красный' ,'Золотой'])


def s_res(e):
	#print(tuple(str(x) for x in range(0 , 10)) + tuple(power_r_s.keys()))
	#print(a)
	e = e.strip()
	a = e.upper()
	
	#print(a)
	nom = 0
	delt = ''

	if (len(a)<3) and (a != '0'):
		raise  LowInputLength(len(a))

	elif len(a)>4:
		raise  HighInputLength(len(a))

	for i in range(0 , len(a)):
		
		if a[i] not in (tuple(str(u) for u in range(0 , 10)) + tuple(power_r_s.keys())):
			raise IncorrectSymb(i , e[i])

	if a.isdigit():
		#print('a=' , a)
		nom = int(a[:-1]) * 10**int(a[-1])
		if len(a) == 3:
			delt = ' ± 5%'
		else:
			delt = ' ± 1%'
		

	elif a[:-1].isdigit() and (len(a) == 3):
		nom = codes_r_s[a[:-1]] * 10 ** power_r_s[a[-1]]
		delt = ' ± 1%'

	else:
		a = a.rpartition('R')

		if (a[0].isdigit() or a[0]=='') and a[1]=='R' and a[2].isdigit() :
			nom = float(a[0] + '.' + a[2])

		else:
			raise IncorrectColor()

	#print('nom = ' , nom)

	nom = pr(nom ,  6 , 3 ,  0 , -3) + 'Ом' + delt
	return nom



def pr(val , *p_s):
	z = 0
	o = list(p_s)
	o.sort(reverse = True)
	for i in o:
		if val >= 10**i:
			val = val/(10**i)
			if (val - math.floor(val)) == 0 :
				val = math.floor(val)
			return '{0} {1}'.format( val , pr_d[i])
			 
#while True :
	
#	print(s_res(input()))
