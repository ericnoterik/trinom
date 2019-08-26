import os
import pickle
import math
import shelve

#Clears the display and shows a persistent title bar
def display_title_bar():
	os.system('cls')
	print("\t************************************")
	print("\t  Trinomial Distribution Calculator  ")
	print("\t************************************\n")

#Display menu choices and get user response
def get_user_choice():
	print("\n[1] See current values.")
	print("[2] Enter new values.")
	print("[3] Calculate probability.")
	print("[4] Calculate cumulative probability.")
	print("[q] Quit.\n")
	return input("Please make a choice: ")

#Display the current trinomial values
#Flatten this code
def show_values():
	print("\nThe last entered values are: ")
	print("Number of trials: %s" % n)
	print("Number of successes of x: %d" % x)
	print("Number of successes of y: %d" % y)
	print("Number of successes of z: %d" % z)
	print("Probability of success of x: %s" % p_x)
	print("Probability of success of y: %s" % p_y)
	print("Probability of success of z: %s" % p_z)
		
def get_new_values():
	global n 
	global x 
	global y 
	global z
	global p_x 
	global p_y 
	global p_z
	n = int(input("\nEnter the number of trials, n: "))
	x = int(input("\nEnter the number of successes of x, x: "))
	y = int(input("\nEnter the number of successes of y, y: "))
	z = (n-x-y)
	p_x = float(input("\nEnter the probability of x, p_x: "))
	p_y = float(input("\nEnter the probability of y, p_y: "))
	p_z = round((1 - p_x - p_y),4)
	ntest = (x + y + z)
	if ntest < 0 or ntest > n:
		print("Number of trials does not match")
	else: 
		display_title_bar()
		show_values()
		
def load_values():
	filename="shelve.out"
	my_shelf = shelve.open(filename)
	for key in my_shelf:
		globals()[key]=my_shelf[key]
	my_shelf.close()
	print('Your previous values have been loaded')
	
def caltri():
	answer = round(((math.factorial(n))/(math.factorial(x)*math.factorial(y)*math.factorial(n-x-y)))*(pow(p_x,x)*pow(p_y,y)*pow(p_z,z)),4)
	if answer == 0.0:
		 print("The probability is less than 0.0001")
	else: 
		print("The probability is %s" %(answer))	

def cumcaltri():
	ans = 0
	for i in range(0,(x+1)):
		intans = ((math.factorial(n))/(math.factorial(i)*math.factorial(y)*math.factorial(n-i-y)))*(pow(p_x,i)*pow(p_y,y)*pow(p_z,(n-i-y)))
		ans += intans
	if ans == 0.0:
		 print("The probability is less than 0.0001")
	else: 
		print("The cumulative probability, P(X \u2264 x, Y = " +str(y)+"), is %s" %round(ans,4))	
		print("\nThis calculation holds y constant for the value entered")
	
#def quit(globals_=None):
#	if globals_ is None:
#		globals_ = globals()
#	filename = 'shelve.out'
#	my_shelf = shelve.open(filename, 'n')
#	for key, value in globals_.items():
#		if not key.startswith('__'):
#			try:
#				my_shelf[key] = value
#			except Exception:	
#				print('Error shelving: "%s"' % key)
#			else:
#				print('shelved: "%s"' % key)
#	my_shelf.close()
	
def quit():
	custvars = {'n' : n, 'x' : x, 'y' : y, 'z' : z, 'p_x' : p_x, 'p_y' : p_y, 'p_z' : p_z}
	filename = 'shelve.out'
	my_shelf = shelve.open(filename, 'n')
	for key, value in custvars.items():
		try:
			my_shelf[key] = value
		except Exception:	
				print('Error shelving: "%s"' % key)
		else:
				print('Saved: "%s"' % key)
	my_shelf.close()

#def quit(globals_=None):
#	if globals_ is None:
#		globals_ = globals()
#	filename = 'shelve.out'
#	my_shelf = shelve.open(filename, 'n')
#	for key, value in globals_.items():
#		if not key.startswith('__'):
#	try:
#				my_shelf[n] = n
#				my_shelf[x] = x
#				my_shelf[y] = y
#				my_shelf[key] = value
#	except Exception:	
#				print('Error shelving: "%s"' % key)
#	else:
#				print('shelved: "%s"' % key)
#	my_shelf.close()

	
#		global filename
#		filename='shelve.out'
#		my_shelf = shelve.open(filename,'n')
#		
##			try:
	#			my_shelf[key] = globals()[key]
	#		except TypeError:
	##	my_shelf.close()
		
		#try:
		#file_object = open('values.pydata', 'wb')
		#pickle.dump([n, x, y, p_x, p_y, p_z], file_object)
		#file_object.close()
		#print("\nThank you - your values have been saved")
	#except Exception as e:
	#	print("\nThere has been an error")
	#	print(e)

choice = ''
display_title_bar()
load_values()
while choice != 'q':
	choice = get_user_choice()
	display_title_bar()
	if choice == '1':
		show_values()
	elif choice == '2':
		get_new_values()
	elif choice == '3':
		caltri()
	elif choice == '4':
		cumcaltri()
	elif choice == 'q':
		quit()
		print("\nThanks for using this program! ")
	else:
		print("\nThere has been an error.  Please enter another choice. ")

