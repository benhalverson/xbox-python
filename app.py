import pygame
pygame.init()
pygame.joystick.init()

# Check for joystick presence
if pygame.joystick.get_count() > 0:
    # Use the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Initialized Joystick : {joystick.get_name()}")
else:
    print("No joystick detected!")
    quit()

# Loop to keep the application running
try:
    while True:
        # Update the joystick events
        pygame.event.pump()

        # Iterate through buttons
        for i in range(joystick.get_numbuttons()):
            button = joystick.get_button(i)
            if button:
                print(f"Button {i} pressed")

        # Axis motion
        for i in range(joystick.get_numaxes()):
            axis = joystick.get_axis(i)
            print(f"Axis {i} value: {axis:.2f}")

        # Hat switch position
        for i in range(joystick.get_numhats()):
            hat = joystick.get_hat(i)
            print(f"Hat {i} position: {hat}")

        # Small delay to make the output readable
        pygame.time.wait(100)

except KeyboardInterrupt:
    print("Application exited.")
