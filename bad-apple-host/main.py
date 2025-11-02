import serial
import sys
import os
import video_encode as videnc
import time

def main():

    videnc.generate_frames("bad_apple_ssd1306.mp4")
    num_frames = 6570
    com_port = ""

    if len(sys.argv) > 1:
        com_port = sys.argv[1]
    else:
        com_port = "/dev/ttyACM0"
    serial_port = serial.Serial(port=com_port, baudrate=921600, timeout=1)

    print("connected to {com_port}")


    # Loop to send video frames
    for i in range(0, num_frames):
        serial_port.reset_input_buffer()
        while (serial_port.read(1) != b'\xFF'):
            pass
        image = videnc.img_to_matrix(f"video_frames/frame_{i}.png")
        print(f"frame {i}")
        videnc.print_matrix(image)
        transmit_matrix(image, serial_port)

        # os.system("clear")


    '''
    message = serial_port.readline().decode('utf-8').strip()
    print(f"<STM32>: {message}")
    '''
    serial_port.close()


def transmit_matrix(matrix, serial_port):
    data = bytearray()
    height = len(matrix)
    width = len(matrix[0])

    # Each byte send to oled contains 1 bit per pixel, storing 8 pixels total. Pack these into a single byte.
    for page in range(0, height, 8):
        for x in range(width):
            byte = 0
            for bit in range(8):
                y = page + bit
                if y < height:
                    pixel = matrix[y][x]
                    if pixel > 200:
                        byte |= (1 << bit)
            data.append(byte)

    '''
    for row in matrix:
        for pixel in row:
            data.append(255 if pixel > 200 else 0)
    '''

    serial_port.write(b'\xAA\x55' + data)



if __name__ == "__main__":
    main()
