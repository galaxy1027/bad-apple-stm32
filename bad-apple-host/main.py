import serial
import sys
import os
import video_encode as videnc
import time

def main():

    videnc.generate_frames("bad_apple_ssd1306.mp4")
    num_frames = 6570

    for i in range(0, num_frames):
        image = videnc.img_to_matrix(f"video_frames/frame_{i}.png")
        videnc.print_matrix(image)
        time.sleep(1/30)
        os.system("clear")

    com_port = ""

'''
    if len(sys.argv) > 1:
        com_port = sys.argv[1]
    else:
        com_port = "/dev/ttyACM0"
    serial_port = serial.Serial(com_port, 115200, timeout=1)

    message = serial_port.readline().decode('utf-8').strip()
    print(f"<STM32>: {message}")

    serial_port.close()

'''

if __name__ == "__main__":
    main()
