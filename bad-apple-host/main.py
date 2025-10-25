import serial
import sys

def main():
    com_port = ""
    if len(sys.argv) > 1:
        com_port = sys.argv[1]
    else:
        com_port = "/dev/ttyACM0"
    serial_port = serial.Serial(com_port, 115200, timeout=1)

    while (1):
        message = serial_port.readline().decode('utf-8').strip()
        print(f"<STM32>: {message}")

    serial_port.close()

if __name__ == "__main__":
    main()
