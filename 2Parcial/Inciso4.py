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

poten = ard.get_pin('a:0:i')
it = pyfirmata.util.Iterator(ard)
it.start()

def enc():
        po = poten.read()

        if po == 1:
                Led1.write(1)
                Led2.write(1)
                Led3.write(1)
                Led4.write(1)
                Led5.write(1)
                Led6.write(1)
                print("Led1:HIGH; Led2:HIGH; Led3:HIGH; Led4:HIGH; Led5:HIGH; Led6:HIGH")
                
        else:
                print("Led1:LOW; Led2:LOW; Led3:LOW; Led4:LOW; Led5:LOW; Led6:LOW")
                Led1.write(0)
                Led2.write(0)
                Led3.write(0)
                Led4.write(0)
                Led5.write(0)
                Led6.write(0)
                

while True:
        enc()

        
