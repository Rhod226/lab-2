import pyfirmata2

retardo=1
puerto= pyfirmata2.Arduino.AUTODETECT

placa= pyfirmata2.Arduino(puerto)

while True:
    placa.digital [2] .write (1)
    placa.digital [3] .write (1)
    placa.digital [4] .write (1)
    placa.digital [5] .write (1)
    placa.digital [6] .write (1)
    placa.pass_time (retardo)
    placa.digital [2] .write (0)
    placa.digital [3] .write (0)
    placa.digital [4] .write (0)
    placa.digital [5] .write (0)
    placa.digital [6] .write (0)
    placa.pass_time (retardo)
