import pyfirmata
import time
ard = pyfirmata.Arduino('COM3')
print("Conectado")

Led1 = ard.digital[6]
Led2 = ard.digital[7]
Led3 = ard.digital[8]
Led4 = ard.digital[9]
Led5 = ard.digital[10]
Led6 = ard.digital[11]

while True:
    #MITAD DE LOS LEDS 5 AL 7
    Led6.write(1)
    Led5.write(1)
    Led4.write(1)
    time.sleep(1)
    Led6.write(0)
    Led5.write(0)
    Led4.write(0)
    
    #LA OTRA MITAD DE LOS LEDS 8 AL 10
    Led3.write(1)
    Led2.write(1)
    Led1.write(1)
    time.sleep(2)
    Led3.write(0)
    Led2.write(0)
    Led1.write(0)
   