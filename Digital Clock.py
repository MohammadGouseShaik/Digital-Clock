import pygame
import time

# Initialize Pygame
pygame.init()

# Set the window size
size = (400, 300)
screen = pygame.display.set_mode(size)

# Set the title of the window
pygame.display.set_caption("Digital Clock")

# Run the clock
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Get the current time
    current_time = time.strftime("%H:%M:%S")

    # Render the text
    font = pygame.font.Font(None, 72)
    text = font.render(current_time, True, (0, 0, 0))

    # Draw the text on the screen
    screen.blit(text, (100, 100))

    # Update the display
    pygame.display.flip()

    # Wait for one second
    pygame.time.wait(1000)

# Quit Pygame
pygame.quit()
