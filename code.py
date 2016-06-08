from PIL import ImageGrab
import time
import os
import win32api , win32con
# change padding
x_pad = 187
y_pad = 196
# x2 was 827 and y2 was 676

"""
	plate Cords
	1--76 240
	2--181 238
	3--280 237
	4--383 236
	5--485 235
	6--589 235
"""
class Cord:

	shrimp = (42,345)
	rice  = (96,351)
	nori = (38,400)
	roe = (89,400)
	salmon = (34,457)
	unagi = (90,457)
#-------------
	phone = (597,251)
	t_shrimp = (552,165)
	t_nori = (495,120)
	t_roe = (568,123)
	t_salmon = (495,174)
	t_unagi = (576,180)
	t_exit = (494,231)

	menu_rice = (576,221)
	buy_rice = (540,188)

	delivery_norm = (495,180)
def screen_shot():
	box = (x_pad+1,y_pad+1,x_pad+640,y_pad+480)
	im = ImageGrab.grab(box)
	im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png' , 'PNG')

def leftclick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	print'left clicked once'

def leftdown():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.1)
	print 'left_down'

def leftup():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	time.sleep(.1)
	print 'left_up'

def mousepos(cord):
	win32api.SetCursorPos((x_pad + cord[0] , y_pad + cord[1]))

def get_cords():
	x,y = win32api.GetCursorPos()
	x = x - x_pad
	y  =y - y_pad
	print x,y

def startgame():
	#start button
	mousepos((263,160))
	leftclick()
	time.sleep(.1)

	#continue button
	mousepos((309,345))
	leftclick()
	time.sleep(.1)

	#skip button
	mousepos((587,409))
	leftclick()
	time.sleep(.1)

	#final continue button
	mousepos((332,329))
	leftclick()
	time.sleep(.1)

def cleartable():
	mousepos(76,240)
	leftclick()
	time.sleep(.1)

	mousepos(181,238)
	leftclick()
	time.sleep(.1)
	
	mousepos(280,237)
	leftclick()
	time.sleep(.1)
	
	mousepos(383,236)
	leftclick()
	time.sleep(.1)
	
	mousepos(485,235)
	leftclick()
	time.sleep(.1)
	
	mousepos(589,235)
	leftclick()
	time.sleep(.1)
	
def main():
	#screen_shot()
	#pass
	startgame()
if __name__ == '__main__':
	main()