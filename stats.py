import time
import board
import busio
import digitalio

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import subprocess

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Display Parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(
    WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

font = ImageFont.truetype('PixelOperator.ttf', 16)
#font = ImageFont.load_default()


def drawAnimation():
    current_frame = 0

    while True:
        if(current_frame == 0):
            draw.text((40, 16), "Te iubesc", font=font, fill=255)
            draw.text((30, 32), "cel mai mult", font=font, fill=255)
            oled.show()
            time.sleep(1.5)
        if(current_frame == 1):
            heart1 = Image.open('heart1.jpg').convert('1')
            oled.image(heart1)
            oled.show()
            time.sleep(0.5)
        if(current_frame == 2):
            heart1 = Image.open('heart2.jpg').convert('1')
            oled.image(heart1)
            oled.show()
            time.sleep(0.5)
        if(current_frame == 3):
            heart1 = Image.open('heart3.jpg').convert('1')
            oled.image(heart1)
            oled.show()
            time.sleep(0.5)
        if(current_frame == 4):
            heart1 = Image.open('heart4.jpg').convert('1')
            oled.image(heart1)
            oled.show()
            time.sleep(0.5)
        if(current_frame == 5):
            heart1 = Image.open('heart5.jpg').convert('1')
            oled.image(heart1)
            oled.show()
            time.sleep(0.5)
        if(current_frame == 6):
            heart1 = Image.open('heart6.jpg').convert('1')
            oled.image(heart1)
            oled.show()
            time.sleep(0.5)
        if(current_frame == 7):
            heart1 = Image.open('heart7.jpg').convert('1')
            oled.image(heart1)
            oled.show()
            time.sleep(0.5)
        if(current_frame == 8):
            heart1 = Image.open('heart8.jpg').convert('1')
            oled.image(heart1)
            oled.show()
            time.sleep(0.5)
        if(current_frame == 9):
            heart1 = Image.open('heart7.jpg').convert('1')
            oled.image(heart1)
            oled.show()
            time.sleep(0.5)
        if(current_frame == 10):
            heart1 = Image.open('heart6.jpg').convert('1')
            oled.image(heart1)
            oled.show()
            time.sleep(0.5)
        if(current_frame == 11):
            heart1 = Image.open('heart5.jpg').convert('1')
            oled.image(heart1)
            oled.show()
            time.sleep(0.5)
        if(current_frame == 12):
            heart1 = Image.open('heart4.jpg').convert('1')
            oled.image(heart1)
            oled.show()
            time.sleep(0.5)
        if(current_frame == 13):
            heart1 = Image.open('heart3.jpg').convert('1')
            oled.image(heart1)
            oled.show()
            time.sleep(0.5)
        if(current_frame == 14):
            heart1 = Image.open('heart2.jpg').convert('1')
            oled.image(heart1)
            oled.show()
            time.sleep(0.5)
        if(current_frame == 15):
            heart1 = Image.open('heart1.jpg').convert('1')
            oled.image(heart1)
            oled.show()
            time.sleep(0.5)

        current_frame = current_frame + 1

        if(current_frame > 15):
            current_frame = 0


while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

    oled.image(image)
    oled.show()
    drawAnimation()
