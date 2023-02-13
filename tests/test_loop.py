import pi_servo_hat
import time

test = pi_servo_hat.PiServoHat()
test.restart()

test.move_servo_position(0, 0)

time.sleep(1)

while True:
    test.move_servo_position(0,130)
    time.sleep(3)
    test.move_servo_position(0,0)
    time.sleep(3)
