import serial, os, sys, time

os.system('cls' if os.name == 'nt' else 'clear')

# constants
PORT = 'COM3'
BAUD_RATE = 115200

ser = serial.Serial(PORT, BAUD_RATE, timeout = 1)

if ser:
    ser.flushInput()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        led_input = input('Turn LED on: H\nturn LED off: L\nQuit: q\n\n')

        if led_input == 'H':
            ser.write(b'H')
            time.sleep(0.5)
            bytes_to_read = ser.inWaiting()
            print("On -> ")
            print(ser.read(bytes_to_read).decode('UTF-8'))
            time.sleep(1)

        elif led_input == 'L':
            ser.write(b'L')
            time.sleep(0.5)
            bytes_to_read = ser.inWaiting()
            print("Off -> ")
            print(ser.read(bytes_to_read).decode('UTF-8'))
            time.sleep(1)

        elif led_input == 'q':
            ser.close()
            break

        else:
            print('Please retype your command')
            time.sleep(1)
sys.exit(0)
