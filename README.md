![PXL_20250303_004522193](https://github.com/user-attachments/assets/7ad07a53-52b5-4d6c-a2c5-f976895f0b8e)

# Introduction
This is an incomplete project, but I nevertheless wanted to write down what I've done so far with it. Right now, the biggest issue for me is sealing the 3D-printed parts. There may be several ways of doing this, like using a specific sealant or printing in something other than PLA + sealant, for example, but I have yet to explore those avenues.

Another issue I am presently having with this design is that if the bottle has too much water, it will simply tip over. I need to most likely redesign the holder such that it can hold itself against the edge much better.

# Material(s)

uxcell 6x6x5mm Momentary Panel PCB Surface Mounted Devices SMT Mount 4 Pins Push Button SPST Tactile Tact Switch 50PCS  - this can be purchased for $7.79 at the following link: https://www.amazon.com/dp/B07HCFM3H1?ref=ppx_yo2ov_dt_b_fed_asin_title

SG92R 2.5KG Micro 9g Servo Nylon Carbon Fiber Gears Replace SG90 for RC Model Aeromo ing Helicopter Parts - this can be purchased for $4.22 at the following link: https://www.amazon.com/SG92R-Carbon-Replace-Aeromo-Helicopter/dp/B0CJM8RC5F/ref=sr_1_3?dib=eyJ2IjoiMSJ9.aZ20P_8vZkmEWpX2naPLNiA2xtVb4wQNDHvFir1nNruuNLIri83DVrUm2bzLRAVIk5p6DKIhsT4mva0O0iNj7ixwQ9lmgQgnmOZXIisGRYYT9xCLysam_gsRbedvhea9NmrV3OOPZat6JUBBiRmwXlWMWD_FxV6fGCxrjwvvO-bh1KYXiVSAb9v3kNI45zoqQAF9vqItsv0Oz25hpcxyUzmX63rVsmct_lLWVGYeg9PlubFer20F7TPwz_7vnt7bVRYVCDpUBKGx9aGQeDxKbvbxM5Hn3UNj5iqINPLFuwYoUJbfJ_Nt1yh1b-npgXpQUo896yNz7fwy9DH7dAV1qip0ipeakdVNnUS-9O-ZPkSVpKMs4I3q5fOO_EvBteOENAqnUaueqFaio2ecawoJQuDT5Jjr3bdJSpVfRI4TPJW5MnRTRd6zb2m4wMzsEjQy.PFxqt18FjjhYzFHmeMXQVaj-zEK4Xywi1l6lnxdNoZo&dib_tag=se&keywords=sg92r&qid=1740963172&sr=8-3

ESP32 Type-C Module ESP32 30PIN NodeMCU Development Board ESP32-WROOM-32 2.4 GHz WLAN CP-2102 - this can be purchased for $9.99 at the following link: https://www.amazon.com/ESP32-NodeMCU-Development-ESP32-WROOM-32-CP-2102/dp/B0DF56JRDW/ref=sr_1_20?crid=2XBJN10JOSDZE&dib=eyJ2IjoiMSJ9.UdLxS8engRob9RiEzo8GfanhXZE8xzQ1ghundWrHQ1gC_J4XScYVl5afct6qHL93oQOi2t_nUBS4dDjhvTrv7z3qxeopA5KNSOkpF1u5PrAw8ywfW1nSNXSNN9sQYNQX-GWq34hOIKcuaPrFEG4j-L-zI1Z6x29t1sfz6ZAOP0PnIBKMqw6cLlWTuNnZV56GAG-ryMRkzHh8wyi93yCYJmN5a2CKRjN8jsjpJqquw5Y.xWXN9GrEB2gFIaUIC2c4Loq5Jh_fYOMPZ7ZQD7-wI3U&dib_tag=se&keywords=esp32%2Busb%2Bc&qid=1740963223&sprefix=esp32%2Busb%2B%2Caps%2C139&sr=8-20&th=1

Steve Spangler's 1 Liter Soda Bottles - 6 Pack - for Science Experiment Use - this can be purchased for $16.47 at the following link: https://www.amazon.com/Steve-Spanglers-Liter-Soda-Bottles/dp/B071J7VSHB/ref=sr_1_2?crid=1M0GJCB1AMEGL&dib=eyJ2IjoiMSJ9.bgPMXOM1S6TgODbVCI2uF2EhwdKxl-bdgbiXJfU_KYHZzdglx5wWR_L-ffRJ02VlLgjwgqlP591r-S8e7OwDMPo7srF5DXLMu5QsktmuNH2eC-e1DZCWZCzUyZ8dyrRECOTDYsq216ZRfNkvQd69io0LBLj8Ie4zpnJAT_TtvfJoDh91XcVC1CnrCoUcnTa-R6neATgUDQum1bob-G8o_tuijRPBlh0bfPUUkkpajlCjmv-wvrFfeR7JcSnwTZGsBPKav7codd23B_Kh5DKSzbJNK39NNubZe-4eYWnbQnQ.Jh7oFhUoCetp8ugnM5qzoGfKTgcnNYN4xRtHVnaieDk&dib_tag=se&keywords=2%2Bliter%2Bplastic%2Bbottle%2Bempty&qid=1721746901&sprefix=2%2Bliter%2Bplastic%2Bbottle%2Bempty%2Caps%2C103&sr=8-2&th=1

5V 2A 10W DC Power Supply Adapter AC/DC Wall Plug Charger AC 100V-240V to DC 5 Volt 2Amp 1A 1.5A Replacement Power Cord USB Type C for Security Camera Baby Monitor Scanner TV Box Raspberry - this can be purchased for $8.49 at the following link: https://www.amazon.com/Arkare-100V-240V-Replacement-Monitor-Scanner-Raspberry/dp/B09W96X88K/ref=sr_1_3?crid=1KKL8XA5F4QDO&dib=eyJ2IjoiMSJ9.o06Dmtr-hTUcwX5PloGXIGnIUbodjnDDucVNdmgxN0qjcRDYA0S3qSGbzJ-9u-PE7m-3S8Z-wWIyMpSy0j9k7SBiU_qGZIk1xcblcYDuL8oXQ90Qqubei5UnPBmLXTd2m34Ut9eAwKBjvU7BZ5Pql8flcNF1QCtJK_EQtZwzaSnApN9w_jqd9wXjN2gZqnL511yMNnMO5gJGHJbtHLDiuDe3Q8S2DnYSulWAKdivCWA.r7o0heX_oBl7sgdeny7e2SxlP6klaAOmn5HD4pE1KZc&dib_tag=se&keywords=5v+2a+ac+adapter&qid=1740963486&sprefix=5v+2a+ac+adapte%2Caps%2C134&sr=8-3

# Custom PCB

One important aspect of this project is the use of a custom PCB. This was created with EasyEDA. Here are the schematics:

![image](https://github.com/user-attachments/assets/44ecc89b-3cdd-4da3-99c9-52e4c7eabb46)

Here is the PCB outline:

![image](https://github.com/user-attachments/assets/b514f2c9-eef9-40e9-a129-f96b11c3f52a)

I have attached the Gerber file for this project so it is easy to order using EasyEDA's partner website: https://jlcpcb.com/

# 3D-Printed Shell

![Image_4](https://github.com/user-attachments/assets/394a6f5a-1db3-4be6-94b7-dc6c6ed665c6)

I created a 3D-printed shell for the robot, which I have broken up into several different parts, all illustrated below.

## Rotating Base

![Image_5](https://github.com/user-attachments/assets/0f2ae642-4bfd-4bc3-a46a-0f05c361c0cf)

This is where one of the servos will be placed. 

## Components Holder
![Image_6](https://github.com/user-attachments/assets/6857d242-256e-455f-bebe-d681828e4b75)

This is where most of the components will be placed.

## Outer Shell
![Image_7](https://github.com/user-attachments/assets/80e815b9-db93-4135-a4e0-198317a5eb68)

This is just to make the robot look pretty and more humanoid.

## Helmet
![Image_8](https://github.com/user-attachments/assets/edb6a8e5-cd30-46c8-9844-760885c1d8fd)

This is the "helmet" for the little bot. It will be attached to one of the servos and the LDR, PIR sensor, as well as the LED ring will be coming out from the top.

### Specifications & Material(s)
Below you can find the printer and material used.
#### 3D Printer
 Original Prusa Mini+
#### Material(s)

For the outer shell and helmet:
INLAND Micro Center PLA+ 3D Printing Filament 1.75mm - PLA Plus 3D Printer Filament - PLA Pro Dimensional Accuracy +/- 0.03 mm - 1kg Cardboard Spool (2.2 lbs) (1 Pack White, 1.75mm)
 – this can be purchased for $26.99 at the following link: https://www.amazon.com/Inland-1-75mm-PLA-Printer-Filament/dp/B081S5YNYY/ref=sr_1_1?crid=24PIPNTON7TBE&dib=eyJ2IjoiMSJ9.AUad6kwB7LpIUJ4-g7QAvVzUPA7Mw7C5hMYzXztCGix1xIT8j9GJaTn9t8fB2HOZc8DY_LwUu7dBLXDk1mpWweMCpmQD6RZudxgEVnr2BzcuBTJDILwl6eXqR_6wClOx5G1m97ulpcIp_Nzuy17rtAJOzhUKI3q4QJbM0cHjoMbSz7KVTiPL-EQWBplJfC5Jw_Pk7zzePwdNTgOK0jCgWuCJT9s4g2b8pnAHPgttRHsf0mqGlG83rwujIfDD9PibeKCvzkjsYvWT-FGXWyD4xuWQV1qDAjslZCbNlKAAD4F84xQ09fYi2GovVpI8YhIYwHeKvmE-j3P-XE1vBN1k7A8OwT_u2JuJwKlIf5qhZmdOL-4oREFn34fGUxCYgsIK22FsfgGzKdxErfv_ghV8pl78YQbF1i1uXpAO3Z8UNz5-UKRKS4N9yM1EbtDqEUo3.QkasFqdRXPRNS1FBsB2mOheh0O_zriR0lbAna6-sskg&dib_tag=se&keywords=white%2Bpla%2Binland&qid=1737417506&sprefix=white%2Bpla%2Binlan%2Caps%2C129&sr=8-1&th=1

For the rotating base and components holder:
INLAND PLA 3D Printer Filament - 3D Printing PLA Filament 1.75mm, Dimensional Accuracy +/- 0.03mm - 1kg Cardboard Spool (2.2 lbs), Black PLA - this can be purchased for $23.99 at the following link: https://www.amazon.com/Inland-1-75mm-Black-Printer-Filament/dp/B00YQB85PG/ref=sr_1_1?crid=MPICCT5BIG20&dib=eyJ2IjoiMSJ9.2vLkzpUXu0xOQM7qzzzuCEEn1RZ2Lp717IWwW5pJTeO3qGtDcS0eJnAnOFm0h24YtaNmPcLjbYwXerAwUZ7hQ_EJZiJUaxn3YZ12AuVGup72wyWMlrNU2_r0gTY-y9pbjeDx3kOPssdfjf4uGJJ7-a6n2gmbjlkt6uxrVlgxbqOb4HZkSw1h3tGrd20jUjD044CDn4PdrAU2BGnrHTGgau6JbPMUvcsoajbAQP_pgbRPwhuxoPpSGuU3s-gw-P-lCvMi6bPJifW9qqk6KkXH0lbYnE41XwSGrmNfjkcwpm5y2SaUwtquYUlgJBysjewOTBqsH8a72hQP2OvzBUvfY2ZAjnVZOx_xIO9PeN4eWq8ZYaROmG70PHkf1RZWQ830HLKmKswCdGbyRKS3bcnWMV0V3Jo0hdVY4oLSdGV1Uwz0dW45TBYpSwIKBMXj1cuz.MVdZPD9KIXfB1CppCg3gye6mxfG1ImPQGc7jQbFBbcM&dib_tag=se&keywords=black%2Bpla%2Binland&qid=1737417541&sprefix=black%2Bpla%2Binland%2Caps%2C120&sr=8-1&th=1

For magnets:
DIYMAG 120Pcs Refrigerator Magnets 10x2mm Premium Brushed Nickel Small Round Cylinder Fridge Magnet, Perfect to use as Office Magnets, Dry Erase Board Magnetic pins, Whiteboard, Map Pins - this can be purchased for $12.99 at the following link: https://www.amazon.com/DIYMAG-Refrigerator-Magnets-100-piece/dp/B0753ZPBLQ/ref=sr_1_19?crid=4S38QACW5AEP&dib=eyJ2IjoiMSJ9.EYtZ7hOWoiRCrhWwwsVJrzaAfrfRynJzx0wpiY7EsDZ_R-bKmqQ46Kr_FJ605BzEmuvGgxXUmGzYITG6lXI-Y-QS1oPBC3tEEx4AuWbXIllhps4bsrN73sPxXvwDwjxnnNoBRcNRsZD0FSY8oCu01ctJIgLgNL79HUSnNnuCjsskJ3paOzRH5ifOJrdhgmuFKdXm3msnuZGOTHAOwH48ZJCPbHj7LhqKhDLUPQbLvsc.g_VQ_G2BEWRtxm6rLwTTMmpZn3GpH8QrYflAKJWOVWI&dib_tag=se&keywords=10%2Bmm%2Bmagnets&qid=1736535291&sprefix=10%2Bmm%2Bmagnet%2Caps%2C88&sr=8-19&th=1

#### Software
 PrusaSlicer
 
![Image_9](https://github.com/user-attachments/assets/0fad7cbf-1074-4ec7-ba74-3657b0ace70d)

![Image_10](https://github.com/user-attachments/assets/2a9adcd2-1671-4205-a598-3c8581338094)

#### Settings
  Layer Height: .2mm \
  Infill: 50% \
  Supports: Everywhere \
  Estimated Printing Time: 1 day, 14 hours, & 25 minutes + 12 hours and 41 minutes

# Code
The code for this LEDBot can be found below, as well as in the main.py file attached herein.
## Software
I personally like to use Thonny for my editing/programming of microcontrollers, so that is what I have here.

![Image_11](https://github.com/user-attachments/assets/3bb344c6-c447-4589-9c79-f7717bc9d967)


## Code

If you do not want to download the .py file, you can just copy the following to your clipboard.

```bash
from machine import Pin, ADC, PWM
from utime import sleep
import neopixel
import time
# Initialization
bottomservo = PWM(Pin(5, mode=Pin.OUT)) # Servo PIN reference
bottomservo.freq(50) # Servo frequency
topservo = PWM(Pin(6, mode=Pin.OUT)) # Servo PIN reference
topservo.freq(50) # Servo frequency

# Neopixel
n = 7
p = 10
np = neopixel.NeoPixel(machine.Pin(p), n)

# LDR
ldr = ADC(26)

# PIR
PIR_sensor = Pin(13, Pin.IN, Pin.PULL_UP)

# TOUCH
pin_sensor = Pin(18, mode=Pin.IN, pull=Pin.PULL_UP)

def bottomservomove(degree):
    servomin = 1800
    servomax = 8500
    servostep = (servomax-servomin)/180
    position = servomin + (degree * servostep)
    bottomservo.duty_u16(int(position))
def topservomove(degree):
    servomin = 1800
    servomax = 8500
    servostep = (servomax-servomin)/180
    position = servomin + (degree * servostep)
    topservo.duty_u16(int(position))
def center():
    topservomove(90)
    bottomservomove(90)
def shake():
    for i in range(45, 135, 5):
        bottomservomove(i)
        sleep(.1)
        print(i)
    sleep(1)
    for i in range(135, 45, -5):
        bottomservomove(i)
        sleep(.1)
        print(i)
    sleep(1)
    for i in range(45, 135, 5):
        topservomove(i)
        sleep(.1)
        print(i)
    sleep(1)
    for i in range(135, 45, -5):
        topservomove(i)
        sleep(.1)
        print(i)
    sleep(1)
def clear():
  for i in range(n):
    np[i] = (0, 0, 0)
    np.write()
def set_color(r, g, b):
  for i in range(n):
    np[i] = (r, g, b)
  np.write()
def cycle(r, g, b, wait):
  for i in range(1 * n):
    for j in range(n):
      np[j] = (0, 0, 0)
    np[i % n] = (r, g, b)
    np.write()
    time.sleep_ms(wait)
    
# Code
sleep(29+--)
while True:
    if pin_sensor.value() == 1:
        print("Enter Assist Mode")
        while True:
            clear()
            digital_value = ldr.read_u16()   # Lowest value 1440, Average 13500, Max 45300
            rgb_value = int((digital_value)/120)
            rgb = 155-rgb_value
            set_color(rgb,int(rgb/2),rgb)
            sleep(.5)
            if pin_sensor.value() == 1:
                clear()
                print("Exit LED Mode")
                break
    if PIR_sensor.value() == 1:
        if pin_sensor.value() == 1:
            print("Enter Assist Mode")
            while True:
                clear()
                digital_value = ldr.read_u16()   # Lowest value 1440, Average 13500, Max 45300
                rgb_value = int((digital_value)/120)
                rgb = 155-rgb_value
                set_color(rgb,int(rgb/2),rgb)
                sleep(.5)
                if pin_sensor.value() == 1:
                    clear()
                    print("Exit LED Mode")
                    break
        print("Motion Detected!")
        sleep(1)
        topservomove(90)
        bottomservomove(20)
        sleep(3)
        bottomservomove(0)
        sleep(.2)
        bottomservomove(40)
        sleep(.2)
        bottomservomove(0)
        sleep(.2)
        topservomove(45)
        sleep(.2)
        topservomove(135)
        sleep(.2)
        topservomove(90)
        sleep(1)
        cycle(0,200,0,100)
        sleep(1)
        clear()
        set_color(15,15,0)
        sleep(5)
        topservomove(135)
        sleep(1)
        while True:
            set_color(15,15,0)
            if PIR_sensor.value() == 0:
                break
            if pin_sensor.value() == 1:
                break
    elif PIR_sensor.value() == 0:
        if pin_sensor.value() == 1:
            print("Enter Assist Mode")
            while True:
                clear()
                digital_value = ldr.read_u16()   # Lowest value 1440, Average 13500, Max 45300
                rgb_value = int((digital_value)/120)
                rgb = 155-rgb_value
                set_color(rgb,int(rgb/2),rgb)
                sleep(.5)
                if pin_sensor.value() == 1:
                    clear()
                    print("Exit LED Mode")
                    break
        print("No Motion Detected!")
        topservomove(90)
        bottomservomove(20)
        sleep(3)
        clear()
        sleep(1)
```
# Video

Unfortunately, I don't have a video of this working, but when it did - it was super adorable. LEDBot would move side to side then nod head up and down, followed by light pattern.
# Tips
I really wish I spent more time or had more experience. I didn't get to program the touch sensor. I think I would have used the touch sensor to change light colors with subsequent touches.
