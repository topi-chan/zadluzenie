inflation_value = [1.59282448436825, -0.453509101198007, 2.32467171712441, 1.26125440724877, 1.78252628571251, 2.32938454145522, 1.50222984223283, 1.78252628571251, 2.32884899407637, 0.616921348207244, 2.35229588637833, 0.337779545187098, 1.57703524727525, -0.292781442607648, 2.48619659017508, 0.267110317834564, 1.41795267229799, 1.05424326726375, 1.4805201044812, 1.57703524727525, -0.077420690314702, 1.16573339872354, -0.404186717638335, 1.49970852083123]

credit = input('Podaj początkową wysokość kredytu: ')
percent = input('Podaj wysokość oprocentowania: ')
installment = input('Podaj wartość raty: ')

try:
	a = float(credit)
	b = float(percent)
	c = float(installment)

except:
	a, b, c = ('' ,'' , '')
	

if (isinstance(a, float) and isinstance(b, float) and isinstance(c, float)) == True and (a and b and c) != 0:
	for i in range(24):
		calc = (1+((inflation_value[i]+b)/1200))*a-c
		calc_less = a-calc
		a = calc
		print('Twoja pozostała kwota kredytu to '+str(calc)+', to '+str(calc_less)+' mniej niz w poprzednim miesiącu\n')
else:
	print('Jedna z wartości jest ujemna, zerowa lub jest tesktem!')
