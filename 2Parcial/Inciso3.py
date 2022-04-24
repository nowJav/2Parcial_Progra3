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

it = pyfirmata.util.Iterator(ard)
it.start()

poten = ard.get_pin('a:0:i')

def descpot():
    po = poten.read()
    if po is not None:
        delay = po + 0.01
        time.sleep(delay)
        Led6.write(1)
        time.sleep(delay)
        Led5.write(1)
        time.sleep(delay)
        Led4.write(1)
        time.sleep(delay)
        Led3.write(1)
        time.sleep(delay)
        Led2.write(1)
        time.sleep(delay)
        Led1.write(1)
        time.sleep(delay)
        Led6.write(0)
        Led5.write(0)
        Led4.write(0)
        Led3.write(0)
        Led2.write(0)
        Led1.write(0)
    else:
        time.sleep(0.1)


while True:
    descpot()