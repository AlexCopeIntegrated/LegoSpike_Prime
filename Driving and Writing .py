import runloop
from hub import light_matrix, port
import motor_pair
from app import display


async def main():
    """Main function to control motors and display text."""

    # Display a message on the light matrix
    light_matrix.write("Hello World")

    # Move the motors after a brief delay
    await move_the_motors()
    
async def move_the_motors(): 
    """Move motors using motor_pair."""
    
    #Create an object
    moterz = motor_pair

    # Create a motor pair using ports A and B
    moterz.pair(motor_pair.PAIR_1, port.A, port.B)

    # Move straight for 2 seconds at a speed of 50
    moterz.move(motor_pair.PAIR_1, 50)
    # Wait for 2 seconds
    await runloop.sleep_ms(2000)

    # Stop the motor pair explicitly
    moterz.move(motor_pair.PAIR_1, 0)
    # Wait for another 2 seconds
    await runloop.sleep_ms(2000)

    moterz.move(motor_pair.PAIR_1, -60)# Set speed to 0 (attempt to stop)
    # Wait for another 2 seconds
    await runloop.sleep_ms(2000)
    # Explicitly stop the motors
    motor_pair.stop(motor_pair.PAIR_1)# Stop the motor pair completely
    await runloop.sleep_ms(1000)


# Run the main function in the event loop
runloop.run(main())
