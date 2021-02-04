import serial
from playsound import playsound
arduino = serial.Serial('COM3',9600)
while True:
	data = arduino.readline().decode('ascii')

	print(data[0:8])
	if (data[0:8]=="audio_on"):
	   print('playing')
	   playsound('audio_filename.mp3')
