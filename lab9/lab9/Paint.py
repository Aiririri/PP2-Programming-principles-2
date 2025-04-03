import pygame
import tkinter as tk
from tkinter import colorchooser
import math

# Function to open a color chooser dialog using Tkinter
def pick_color():
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window
    color_code = colorchooser.askcolor(title="Choose color")[0]
    # Returns the RGB color tuple if a color is chosen, otherwise None
    return (int(color_code[0]), int(color_code[1]), int(color_code[2])) if color_code else None

# Main function where the Pygame application runs
def main():
    pygame.init()  # Initialize Pygame modules
    screen = pygame.display.set_mode((640, 480))  # Create the game window with specified dimensions
    pygame.display.set_caption("Simple Paint")  # Set the title of the window
    clock = pygame.time.Clock()  # Create a clock object to control the frame rate

    # Initial drawing parameters
    radius = 15  # Initial radius for the line drawing tool
    mode = 'blue'  # Initial color mode (blue, red, green, custom)
    draw_mode = 'line'  # Initial drawing mode (line, eraser, rect, circle, square, triangle_right, triangle_equilateral, rhombus)
    points = []  # List to store points for line drawing
    rect_start, rect_end = None, None  # Start and end points for rectangle drawing
    circle_start, circle_end = None, None  # Start and end points for circle drawing
    square_start, square_end = None, None  # Start and end points for square drawing
    triangle_right_start, triangle_right_end = None, None  # Start and end points for right triangle drawing
    triangle_equilateral_start, triangle_equilateral_end = None, None  # Start and end points for equilateral triangle drawing
    rhombus_start, rhombus_end = None, None  # Start and end points for rhombus drawing
    custom_color = (0, 0, 255)  # Initial custom color (blue)

    # Load icons for tools
    try:
        eraser_icon = pygame.image.load("eraser.png").convert_alpha()
        rectangle_icon = pygame.image.load("rectangle.png").convert_alpha()
        circle_icon = pygame.image.load("circle.png").convert_alpha()
        square_icon = pygame.image.load("square.png").convert_alpha()  # Load square icon
        triangle_right_icon = pygame.image.load("triangle_right.png").convert_alpha()  # Load right triangle icon
        triangle_equilateral_icon = pygame.image.load("triangle_equilateral.png").convert_alpha()  # Load equilateral triangle icon
        rhombus_icon = pygame.image.load("rhombus.png").convert_alpha()  # Load rhombus icon
    except pygame.error as e:
        print(f"Error loading images: {e}")
        return

    # Scale the icons to a reasonable size
    icon_size = (50, 50)
    eraser_icon = pygame.transform.scale(eraser_icon, icon_size)
    rectangle_icon = pygame.transform.scale(rectangle_icon, icon_size)
    circle_icon = pygame.transform.scale(circle_icon, icon_size)
    square_icon = pygame.transform.scale(square_icon, icon_size)
    triangle_right_icon = pygame.transform.scale(triangle_right_icon, icon_size)
    triangle_equilateral_icon = pygame.transform.scale(triangle_equilateral_icon, icon_size)
    rhombus_icon = pygame.transform.scale(rhombus_icon, icon_size)

    # Main game loop
    while True:
        pressed = pygame.key.get_pressed()  # Get the state of all keyboard buttons

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        # Event handling loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user clicks the close button
                return

            # Keyboard event handling for color mode and line mode
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_c:
                    color = pick_color()  # Open the color chooser dialog
                    if color:
                        mode = 'custom'
                        custom_color = color
                elif event.key == pygame.K_l:
                    draw_mode = 'line'

            # Mouse button down event handling
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos  # Get the mouse coordinates

                # Check if the mouse click is within the bounds of the tool icons
                if 10 <= mouse_x <= 60:
                    if 10 <= mouse_y <= 60:
                        draw_mode = 'eraser'
                    elif 70 <= mouse_y <= 120:
                        draw_mode = 'rect'
                    elif 130 <= mouse_y <= 180:
                        draw_mode = 'circle'
                    elif 190 <= mouse_y <= 240:
                        draw_mode = 'square'  # Set draw mode to square
                    elif 250 <= mouse_y <= 300:
                        draw_mode = 'triangle_right'  # Set draw mode to right triangle
                    elif 310 <= mouse_y <= 360:
                        draw_mode = 'triangle_equilateral'  # Set draw mode to equilateral triangle
                    elif 370 <= mouse_y <= 420:
                        draw_mode = 'rhombus'  # Set draw mode to rhombus
                else:
                    # If click is not on a tool, record the starting point for the current draw mode
                    if draw_mode == 'rect':
                        rect_start = event.pos
                    elif draw_mode == 'circle':
                        circle_start = event.pos
                    elif draw_mode == 'square':
                        square_start = event.pos
                    elif draw_mode == 'triangle_right':
                        triangle_right_start = event.pos
                    elif draw_mode == 'triangle_equilateral':
                        triangle_equilateral_start = event.pos
                    elif draw_mode == 'rhombus':
                        rhombus_start = event.pos
                    # Handle radius increase/decrease for line drawing
                    elif event.button == 1:  # Left mouse button
                        radius = min(200, radius + 1)
                    elif event.button == 3:  # Right mouse button
                        radius = max(1, radius - 1)

            # Mouse button up event handling
            if event.type == pygame.MOUSEBUTTONUP:
                # Draw the shape based on the draw mode and recorded start/end points
                if draw_mode == 'rect' and rect_start:
                    rect_end = event.pos
                    pygame.draw.rect(screen, custom_color if mode == 'custom' else (255, 255, 255), (*rect_start, rect_end[0] - rect_start[0], rect_end[1] - rect_start[1]), 2)
                    rect_start = None
                elif draw_mode == 'circle' and circle_start:
                    circle_end = event.pos
                    radius = int(((circle_end[0] - circle_start[0]) ** 2 + (circle_end[1] - circle_start[1]) ** 2) ** 0.5)
                    pygame.draw.circle(screen, custom_color if mode == 'custom' else (255, 255, 255), circle_start, radius, 2)
                    circle_start = None
                elif draw_mode == 'square' and square_start:
                    square_end = event.pos
                    side = min(abs(square_end[0] - square_start[0]), abs(square_end[1] - square_start[1]))
                    top_left = square_start
                    if square_end[0] < square_start[0]:
                        top_left = (top_left[0] - side, top_left[1])
                    if square_end[1] < square_start[1]:
                        top_left = (top_left[0], top_left[1] - side)
                    pygame.draw.rect(screen, custom_color if mode == 'custom' else (255, 255, 255), (*top_left, side, side), 2)
                    square_start = None
                elif draw_mode == 'triangle_right' and triangle_right_start:
                    triangle_right_end = event.pos
                    points_triangle = [triangle_right_start, (triangle_right_end[0], triangle_right_start[1]), triangle_right_end]
                    pygame.draw.polygon(screen, custom_color if mode == 'custom' else (255, 255, 255), points_triangle, 2)
                    triangle_right_start = None
                elif draw_mode == 'triangle_equilateral' and triangle_equilateral_start:
                    triangle_equilateral_end = event.pos
                    base_width = triangle_equilateral_end[0] - triangle_equilateral_start[0]
                    height = abs(base_width) * math.sqrt(3) / 2
                    if triangle_equilateral_end[1] < triangle_equilateral_start[1]:
                        height *= -1
                    top_point = (triangle_equilateral_start[0] + base_width / 2, triangle_equilateral_start[1] - height)
                    points_triangle = [triangle_equilateral_start, triangle_equilateral_end, top_point]
                    pygame.draw.polygon(screen, custom_color if mode == 'custom' else (255, 255, 255), points_triangle, 2)
                    triangle_equilateral_start = None
                elif draw_mode == 'rhombus' and rhombus_start:
                    rhombus_end = event.pos
                    center_x = (rhombus_start[0] + rhombus_end[0]) // 2
                    center_y = (rhombus_start[1] + rhombus_end[1]) // 2
                    half_width = abs(rhombus_end[0] - rhombus_start[0]) // 2
                    half_height = abs(rhombus_end[1] - rhombus_start[1]) // 2
                    points_rhombus = [(center_x, center_y - half_height), (center_x + half_width, center_y), (center_x, center_y + half_height), (center_x - half_width, center_y)]
                    pygame.draw.polygon(screen, custom_color if mode == 'custom' else (255, 255, 255), points_rhombus, 2)
                    rhombus_start = None

            # Mouse motion event handling for line and eraser
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is pressed
                    if draw_mode == 'line' or draw_mode == 'eraser':
                        points.append((position, draw_mode == 'eraser'))
                        points = points[-256:]  # Keep only the last 256 points for performance

        # Drawing section
        screen.fill((0, 0, 200))  # Fill the screen with black

        # Draw the lines based on the recorded points
        for i in range(len(points) - 1):
            p1, erase = points[i]
            p2, _ = points[i + 1]
            drawLineBetween(screen, i, p1, p2, radius, mode, erase, custom_color)

        # Draw the tool icons on the screen
        screen.blit(eraser_icon, (10, 10))
        screen.blit(rectangle_icon, (10, 70))
        screen.blit(circle_icon, (10, 130))
        screen.blit(square_icon, (10, 190))  # Blit square icon
        screen.blit(triangle_right_icon, (10, 250))  # Blit right triangle icon
        screen.blit(triangle_equilateral_icon, (10, 310))  # Blit equilateral triangle icon
        screen.blit(rhombus_icon, (10, 370))  # Blit rhombus icon

        # Indicate the active drawing mode with a white border around the icon
        if draw_mode == 'eraser':
            pygame.draw.rect(screen, (255, 255, 255), (10, 10, 50, 50), 2)
        elif draw_mode == 'rect':
            pygame.draw.rect(screen, (255, 255, 255), (10, 70, 50, 50), 2)
        elif draw_mode == 'circle':
            pygame.draw.rect(screen, (255, 255, 255), (10, 130, 50, 50), 2)
        elif draw_mode == 'square':
            pygame.draw.rect(screen, (255, 255, 255), (10, 190, 50, 50), 2)
        elif draw_mode == 'triangle_right':
            pygame.draw.rect(screen, (255, 255, 255), (10, 250, 50, 50), 2)
        elif draw_mode == 'triangle_equilateral':
            pygame.draw.rect(screen, (255, 255, 255), (10, 310, 50, 50), 2)
        elif draw_mode == 'rhombus':
            pygame.draw.rect(screen, (255, 255, 255), (10, 370, 50, 50), 2)
        elif draw_mode == 'line':
            pygame.draw.rect(screen, (255, 255, 255), (10, 430, 50, 50), 2) # Assuming you might want to add a line icon later

        # Draw a preview of the shape while the mouse button is held down
        if draw_mode == 'rect' and rect_start:
            mouse_pos = pygame.mouse.get_pos()
            pygame.draw.rect(screen, (255, 255, 255), (*rect_start, mouse_pos[0] - rect_start[0], mouse_pos[1] - rect_start[1]), 1)
        elif draw_mode == 'circle' and circle_start:
            mouse_pos = pygame.mouse.get_pos()
            radius = int(((mouse_pos[0] - circle_start[0]) ** 2 + (mouse_pos[1] - circle_start[1]) ** 2) ** 0.5)
            pygame.draw.circle(screen, (255, 255, 255), circle_start, radius, 1)
        elif draw_mode == 'square' and square_start:
            mouse_pos = pygame.mouse.get_pos()
            side = min(abs(mouse_pos[0] - square_start[0]), abs(mouse_pos[1] - square_start[1]))
            top_left = square_start
            if mouse_pos[0] < square_start[0]:
                top_left = (top_left[0] - side, top_left[1])
            if mouse_pos[1] < square_start[1]:
                top_left = (top_left[0], top_left[1] - side)
            pygame.draw.rect(screen, (255, 255, 255), (*top_left, side, side), 1)
        elif draw_mode == 'triangle_right' and triangle_right_start:
            mouse_pos = pygame.mouse.get_pos()
            points_triangle = [triangle_right_start, (mouse_pos[0], triangle_right_start[1]), mouse_pos]
            pygame.draw.polygon(screen, (255, 255, 255), points_triangle, 1)
        elif draw_mode == 'triangle_equilateral' and triangle_equilateral_start:
            mouse_pos = pygame.mouse.get_pos()
            base_width = mouse_pos[0] - triangle_equilateral_start[0]
            height = abs(base_width) * math.sqrt(3) / 2
            if mouse_pos[1] < triangle_equilateral_start[1]:
                height *= -1
            top_point = (triangle_equilateral_start[0] + base_width / 2, triangle_equilateral_start[1] - height)
            points_triangle = [triangle_equilateral_start, mouse_pos, top_point]
            pygame.draw.polygon(screen, (255, 255, 255), points_triangle, 1)
        elif draw_mode == 'rhombus' and rhombus_start:
            mouse_pos = pygame.mouse.get_pos()
            center_x = (rhombus_start[0] + mouse_pos[0]) // 2
            center_y = (rhombus_start[1] + mouse_pos[1]) // 2
            half_width = abs(mouse_pos[0] - rhombus_start[0]) // 2
            half_height = abs(mouse_pos[1] - rhombus_start[1]) // 2
            points_rhombus = [(center_x, center_y - half_height), (center_x + half_width, center_y), (center_x, center_y + half_height), (center_x - half_width, center_y)]
            pygame.draw.polygon(screen, (255, 255, 255), points_rhombus, 1)

        pygame.display.flip()  # Update the full display Surface to the screen
        clock.tick(60)  # Limit the frame rate to 60 frames per second

# Function to draw a line between two points with a specific color and width
def drawLineBetween(screen, index, start, end, width, color_mode, erase, custom_color):
    # Calculate color components based on the index for a rainbow effect
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    # Determine the color based on the color mode
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'custom':
        color = custom_color

    # If in eraser mode, set the color to black (assuming black background)
    if erase:
        color = (0, 0, 200)

    # Draw a series of circles to create the line effect
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

# Entry point of the script
if __name__ == '__main__':
    main()