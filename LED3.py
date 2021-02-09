import RPi.GPIO as GPIO
import time

colors = [0,1]  # green and then red
pins = {'pin_R':11, 'pin_G':12}  # pins is a dict

GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
for i in pins:
    GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
    GPIO.output(pins[i], GPIO.LOW) # Set pins to high(+3.3V) to off led

p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
p_G = GPIO.PWM(pins['pin_G'], 2000)

p_R.start(0)      # Initial duty Cycle = 0(leds off)
p_G.start(0)


def setColor(col):   # For example : col = 0x112233

    if col:
        p_R.ChangeDutyCycle(10)# Change duty cycle
        time.sleep(1)
        p_R.ChangeDutyCycle(0)
    else:
        p_G.ChangeDutyCycle(10)
        time.sleep(1)
        p_G.ChangeDutyCycle(0)


def loop():
    while True:
        for col in colors:
            setColor(col)
            

def destroy():
    p_R.stop()
    p_G.stop()
    for i in pins:
        GPIO.output(pins[i], GPIO.LOW)    # Turn off all leds
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        loop()
    except KeyboardInterrupt:
        destroy()