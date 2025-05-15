![PXL_20250303_004522193](https://github.com/user-attachments/assets/7ad07a53-52b5-4d6c-a2c5-f976895f0b8e)

# Introduction
This is an incomplete project, but I nevertheless wanted to write down what I've done so far with it. Right now, the biggest issue for me is sealing the 3D-printed parts. There may be several ways of doing this, like using a specific sealant or printing in something other than PLA + sealant, for example, but I have yet to explore those avenues.

Another issue I am presently having with this design is that if the bottle has too much water, it will simply tip over. I need to most likely redesign the holder such that it can hold itself against the edge much better.

# Material(s)

* [6x6x5mm 4 Pins Push Button ($7.79)](https://www.amazon.com/dp/B07HCFM3H1?ref=ppx_yo2ov_dt_b_fed_asin_title)

* [Micro 9g Servo ($4.22)](https://www.amazon.com/SG92R-Carbon-Replace-Aeromo-Helicopter/dp/B0CJM8RC5F/ref=sr_1_3?dib=eyJ2IjoiMSJ9.aZ20P_8vZkmEWpX2naPLNiA2xtVb4wQNDHvFir1nNruuNLIri83DVrUm2bzLRAVIk5p6DKIhsT4mva0O0iNj7ixwQ9lmgQgnmOZXIisGRYYT9xCLysam_gsRbedvhea9NmrV3OOPZat6JUBBiRmwXlWMWD_FxV6fGCxrjwvvO-bh1KYXiVSAb9v3kNI45zoqQAF9vqItsv0Oz25hpcxyUzmX63rVsmct_lLWVGYeg9PlubFer20F7TPwz_7vnt7bVRYVCDpUBKGx9aGQeDxKbvbxM5Hn3UNj5iqINPLFuwYoUJbfJ_Nt1yh1b-npgXpQUo896yNz7fwy9DH7dAV1qip0ipeakdVNnUS-9O-ZPkSVpKMs4I3q5fOO_EvBteOENAqnUaueqFaio2ecawoJQuDT5Jjr3bdJSpVfRI4TPJW5MnRTRd6zb2m4wMzsEjQy.PFxqt18FjjhYzFHmeMXQVaj-zEK4Xywi1l6lnxdNoZo&dib_tag=se&keywords=sg92r&qid=1740963172&sr=8-3)

* [ESP32 Type-C Module ($9.99)](https://www.amazon.com/ESP32-NodeMCU-Development-ESP32-WROOM-32-CP-2102/dp/B0DF56JRDW/ref=sr_1_20?crid=2XBJN10JOSDZE&dib=eyJ2IjoiMSJ9.UdLxS8engRob9RiEzo8GfanhXZE8xzQ1ghundWrHQ1gC_J4XScYVl5afct6qHL93oQOi2t_nUBS4dDjhvTrv7z3qxeopA5KNSOkpF1u5PrAw8ywfW1nSNXSNN9sQYNQX-GWq34hOIKcuaPrFEG4j-L-zI1Z6x29t1sfz6ZAOP0PnIBKMqw6cLlWTuNnZV56GAG-ryMRkzHh8wyi93yCYJmN5a2CKRjN8jsjpJqquw5Y.xWXN9GrEB2gFIaUIC2c4Loq5Jh_fYOMPZ7ZQD7-wI3U&dib_tag=se&keywords=esp32%2Busb%2Bc&qid=1740963223&sprefix=esp32%2Busb%2B%2Caps%2C139&sr=8-20&th=1)

* [Steve Spangler's 1 Liter Soda Bottles ($16.47)](https://www.amazon.com/Steve-Spanglers-Liter-Soda-Bottles/dp/B071J7VSHB/ref=sr_1_2?crid=1M0GJCB1AMEGL&dib=eyJ2IjoiMSJ9.bgPMXOM1S6TgODbVCI2uF2EhwdKxl-bdgbiXJfU_KYHZzdglx5wWR_L-ffRJ02VlLgjwgqlP591r-S8e7OwDMPo7srF5DXLMu5QsktmuNH2eC-e1DZCWZCzUyZ8dyrRECOTDYsq216ZRfNkvQd69io0LBLj8Ie4zpnJAT_TtvfJoDh91XcVC1CnrCoUcnTa-R6neATgUDQum1bob-G8o_tuijRPBlh0bfPUUkkpajlCjmv-wvrFfeR7JcSnwTZGsBPKav7codd23B_Kh5DKSzbJNK39NNubZe-4eYWnbQnQ.Jh7oFhUoCetp8ugnM5qzoGfKTgcnNYN4xRtHVnaieDk&dib_tag=se&keywords=2%2Bliter%2Bplastic%2Bbottle%2Bempty&qid=1721746901&sprefix=2%2Bliter%2Bplastic%2Bbottle%2Bempty%2Caps%2C103&sr=8-2&th=1)

* [5V 2A 10W DC Power Supply Adapter ($8.49)](https://www.amazon.com/Arkare-100V-240V-Replacement-Monitor-Scanner-Raspberry/dp/B09W96X88K/ref=sr_1_3?crid=1KKL8XA5F4QDO&dib=eyJ2IjoiMSJ9.o06Dmtr-hTUcwX5PloGXIGnIUbodjnDDucVNdmgxN0qjcRDYA0S3qSGbzJ-9u-PE7m-3S8Z-wWIyMpSy0j9k7SBiU_qGZIk1xcblcYDuL8oXQ90Qqubei5UnPBmLXTd2m34Ut9eAwKBjvU7BZ5Pql8flcNF1QCtJK_EQtZwzaSnApN9w_jqd9wXjN2gZqnL511yMNnMO5gJGHJbtHLDiuDe3Q8S2DnYSulWAKdivCWA.r7o0heX_oBl7sgdeny7e2SxlP6klaAOmn5HD4pE1KZc&dib_tag=se&keywords=5v+2a+ac+adapter&qid=1740963486&sprefix=5v+2a+ac+adapte%2Caps%2C134&sr=8-3)

# Custom PCB

One important aspect of this project is the use of a custom PCB. This was created with EasyEDA. Here are the schematics:

![image](https://github.com/user-attachments/assets/44ecc89b-3cdd-4da3-99c9-52e4c7eabb46)

Here is the PCB outline:

![image](https://github.com/user-attachments/assets/b514f2c9-eef9-40e9-a129-f96b11c3f52a)

I have attached the Gerber file for this project so it is easy to order using EasyEDA's partner website: https://jlcpcb.com/

# 3D-Printed Parts

![image](https://github.com/user-attachments/assets/7efa9d2a-d2e1-4c45-a655-ee21e8b9ea24)

### Specifications & Material(s)
Below you can find the printer and material used.
#### 3D Printer
 Original Prusa Mini+
#### Material(s)

* [INLAND Gray PLA+ Filament ($26.99)](https://www.amazon.com/Micro-Center-Inland-Speed-Filament/dp/B0CTR6SXBD/ref=sr_1_6?crid=H4IWIMNXWFRT&dib=eyJ2IjoiMSJ9.jtzsQdU9hAW9WIzOWiyxAqICr91-2fQVZ9EQpZWIG4SBrGzYr7FREh8bUfA3acn1zP3vvVKpC8uLxSKBH9JE0HHudVS3HINPevgjVAZVgYIbEsgnJ9ZyC64X1p4K32tjXyAE4IHNDNj2sIY7LmhELL02-moDEuSCAbwnSzO5oJnNK9t48X6rlhvanYOWVFytZSnMcczt51IKkxxIr_6XduEr7_bX1-8svJma0PtqOIs.ggUIwKYRNYpFMNCBx8On8xgnb6B8GxjVEk3VEckEzrg&dib_tag=se&keywords=inland%2Bgray%2Bpla&qid=1740963816&sprefix=inland%2Bgray%2Bpl%2Caps%2C137&sr=8-6&th=1)

#### Software
 PrusaSlicer
 
![image](https://github.com/user-attachments/assets/16f9d201-4cf2-425c-83e7-7f85e8d8aec7)

#### Settings
  Layer Height: .2mm \
  Infill: 100% \
  Supports: Everywhere \
  Estimated Printing Time: 5 hours and 48 minutes.

## Software
I personally like to use Thonny for my editing/programming of microcontrollers, so that is what I have here.

![image](https://github.com/user-attachments/assets/bdf82154-0b6a-46a4-ad36-1136e40ee667)

## Code

If you do not want to download the .py file, you can just copy the following to your clipboard.

```bash
from machine import Pin, PWM
from time import sleep, time

# Define the servo control pin
servo_pin = 26
servo = PWM(Pin(servo_pin), freq=50)  # Initialize PWM

# Define the push button pin
button_pin = 25
button = Pin(button_pin, Pin.IN, Pin.PULL_UP)

# Function to set the servo angle
def set_servo_angle(angle):
    min_duty = 40  # Minimum duty cycle (0 degrees)
    max_duty = 105  # Adjusted maximum duty cycle (80 degrees)
    duty = min_duty + (angle / 80) * (max_duty - min_duty)
    servo.duty(int(duty))
    sleep(0.5)  # Allow time for servo to move

# Function to open and close once a day
last_open_time = 0
def daily_open():
    global last_open_time
    current_time = time()
    if current_time - last_open_time >= 86400:  # 86400 seconds in a day
        last_open_time = current_time
        set_servo_angle(30)  # Open position
        sleep(3)
        set_servo_angle(0)  # Closed position

# Main loop
while True:
    daily_open()
    if button.value() == 0:  # Button is pressed
        set_servo_angle(30)  # Open position
        while button.value() == 0:  # Wait while button is held
            sleep(0.1)
        set_servo_angle(0)  # Closed position
    sleep(1)
```
# Video

https://github.com/user-attachments/assets/65a6cb7d-3ea9-44d5-b50c-2d82d885eb4d

As you can see in the video above, I do it without water, which is kind of defeating the purpose, but this design does suffer from the previously mentioned issues in the introduction section.

# Tips

I hope that if anyone does something similar, they are able to troubleshoot the issues I've been having and maybe even help out a bit. For now, I'm shelving this project.
