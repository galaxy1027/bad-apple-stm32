# bad-apple-stm32

There are two parts to this program: The bad-apple-uart directory contains the STM32 code. This recieves data over UART and sends it to an external OLED display (ssd1306).

The bad-apple-host directory contains python scripts to decode the original video and resize it to the resolution of the oled screen (128x64). It then processes individual PNG's and sends data to the microcontroller.

### Video demo
https://youtu.be/Om3NjUVqIXI
