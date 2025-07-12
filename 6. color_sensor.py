import motor_pair, color_sensor
import time
import runloop
from hub import port
import motor_pair


async def main():
    # Initialize motor pair
    motor_pair.pair(motor_pair.PAIR_1, port.E, port.B)
    motor = motor_pair

    # Initialize color sensor on port A
    sensor = color_sensor

    # Run the main control loop
    await main_loop(motor, sensor)

async def move_the_motors() -> None:
    """Move motors using motor_pair."""

    # Create an object for motor pair control
    moterz = motor_pair

    # Create a motor pair using ports A and B
    moterz.pair(motor_pair.PAIR_1, port.E, port.B)

    # Move s
    traight for 2 seconds at a speed of 50
    moterz.move(motor_pair.PAIR_1, 100)
    # Wait for 2 seconds
    await runloop.sleep_ms(2000)

    # Stop the motor pair explicitly
    moterz.move(motor_pair.PAIR_1, 0)

    # Wait for another 2 seconds
    await runloop.sleep_ms(2000)

    # Move backward at speed -60 for 2 seconds
    moterz.move(motor_pair.PAIR_1, 60)
    await runloop.sleep_ms(2000)

    # Explicitly stop the motors
    motor_pair.stop(motor_pair.PAIR_1)# Stop the motor pair completely

    #return motors, sensor

def handle_color_behavior(color, motors):
    # Color constants from LEGO SPIKE Prime API:
    RED = 9
    BLUE = 3

    if color == RED:
        motors.stop(motor_pair.PAIR_1)
        time.sleep(3)
        motors.move(motor_pair.PAIR_1, 100)
        print("Red detected — stopping")
        return False

    elif color == BLUE:
        print("Blue detected — turning")
        motors.stop(motor_pair.PAIR_1)
        time.sleep(0.5)
        motors.move(motor_pair.PAIR_1, 100)

    else:
        motors.move(motor_pair.PAIR_1, 100)

    print("Detected Color:", color)
    return True

    
def main_loop(motors, sensor):
    try:
        while True:
            color = color_sensor.reflection(port.D)
            if not handle_color_behavior(color, motors):
                break
            time.sleep(0.1)
    except KeyboardInterrupt:
        motors.stop()
        print("Stopped by user")

# Run the program
runloop.run(main())


