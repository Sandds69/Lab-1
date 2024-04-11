import pygame

pygame.init()
screen = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()

radius = 15

mode = (0, 0, 0)  # Initial drawing color is black
drawing_mode = 'line'  # Added: Track the drawing mode ('line', 'rect', 'circle')

strokes = []  # List of strokes, each stroke is a list of points for lines
current_stroke = []  # Current stroke being drawn

#shapes
rects = [] 
circles = [] 

squares = []
rights = []
triangles = []
rhombuses = []

start_pos = None  # Added: Starting position for drawing shapes


colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255), (255, 125, 47)]
font = pygame.font.Font(None, 20)

done = False

def draw_rounded_line(screen, start, end, color, radius):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0] + float(i) / distance * dx)
        y = int(start[1] + float(i) / distance * dy)
        pygame.draw.circle(screen, color, (x, y), radius)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_r:
                drawing_mode = 'rect'  # Switch to rectangle drawing mode

            elif event.key == pygame.K_c:
                drawing_mode = 'circle'  # Switch to circle drawing mode

            elif event.key == pygame.K_s:
                drawing_mode = 'square'  
            
            elif event.key == pygame.K_p:
                drawing_mode = 'right_triangle'  
            
            elif event.key == pygame.K_t:
                drawing_mode = 'equilateral_triangle'  
            
            elif event.key == pygame.K_h:
                drawing_mode = 'rhombus'  
            
            
            
            
            #erasing
            elif event.key == pygame.K_e: 
                strokes = []
                rects = [] 
                circles = []
                squares = []
                rights = []
                triangles = []
                rhombuses = []

            else:
                drawing_mode = 'line'  # Default to line drawing mode
                # Determine which color is picked
                for i, color in enumerate(colors, start=1):
                    if event.key == getattr(pygame, f'K_{i}'):
                        mode = color


        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                start_pos = event.pos  # Store start position for drawing shapes

                if drawing_mode == 'line':
                    if event.pos[1] < 600:  # Restrict y-coordinate for lines
                        current_stroke.append((event.pos, mode, radius))


        #draw when pressed
        if event.type == pygame.MOUSEMOTION and drawing_mode == 'line':
            if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is pressed
                if event.pos[1] < 600:  # Restrict y-coordinate for lines
                    current_stroke.append((event.pos, mode, radius))

        #when upping mouse
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left button released

                #add strokes to line
                if drawing_mode == 'line' and current_stroke:
                    strokes.append(current_stroke)
                    current_stroke = [] #clear current drawing when released

                #add strokes to rect
                elif drawing_mode == 'rect':
                    if event.pos[1] < 600:
                        rects.append((start_pos, event.pos, mode))

                #add strokes to circle
                elif drawing_mode == 'circle':
                    #limiting circles from being way too big
                    if abs(start_pos[0] - event.pos[0]) < 500 and abs(start_pos[1] - event.pos[1]) < 500 and event.pos[1] < 600 and start_pos[1] < 600:
                        circles.append((start_pos, event.pos, mode))
                
                elif drawing_mode == 'square':
                    if event.pos[1] < 600:
                        squares.append((start_pos, event.pos, mode))

                elif drawing_mode == 'right_triangle':
                    if event.pos[1] < 600:
                        rights.append((start_pos, event.pos, mode))

                elif drawing_mode == 'equilateral_triangle':
                    if event.pos[1] < 600:
                        triangles.append((start_pos, event.pos, mode))

                elif drawing_mode == 'rhombus':
                    if event.pos[1] < 600:
                        rhombuses.append((start_pos, event.pos, mode))

                

                start_pos = None  # Reset start position
    screen.fill((255, 255, 255))

    # Color menu
    for i, color in enumerate(colors, start=1):
        pygame.draw.rect(screen, color, ((i - 1) * 100, 630, 100, 70))
        text = font.render(f"Press {i} to pick", True, color)
        screen.blit(text, ((i - 1) * 100, 700 - 90))


    # Guide to keybinds 
    text = font.render(f"Key E to erase", True, (0, 0, 0))
    screen.blit(text, (605, 630))
    text = font.render(f"Key R to rect", True, (0, 0, 0))
    screen.blit(text, (605, 650))
    text = font.render(f"Key C to circle", True, (0, 0, 0))
    screen.blit(text, (605, 670))
    text = font.render(f"Key S, P, T, H", True, (0, 0, 0))
    screen.blit(text, (605, 690))


    #drawing
    for stroke in strokes + [current_stroke]:
        for i in range(len(stroke) - 1):
            start_point, start_color, start_radius = stroke[i]
            end_point, end_color, end_radius = stroke[i + 1]
            draw_rounded_line(screen, start_point, end_point, start_color, start_radius)

    # Draw rectangles
    for rect in rects:
        start, end, color = rect
        pygame.draw.rect(screen, color, pygame.Rect(start, (end[0] - start[0], end[1] - start[1])))

    for square in squares:
        start, end, color = square
        side = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
        pygame.draw.rect(screen, color, pygame.Rect(start, (side, side)))
    for right in rights:
        start, end, color = right
        pygame.draw.polygon(screen, color, [start, (end[0], start[1]), end])
    for triangle in triangles:
        start, end, color = triangle
        height = abs(end[1] - start[1])
        pygame.draw.polygon(screen, color, [start, (start[0] + height // 2, end[1]), (start[0] - height // 2, end[1])])
    for rhombus in rhombuses:
        start, end, color = rhombus
        mid_x = (start[0] + end[0]) // 2
        mid_y = (start[1] + end[1]) // 2
        pygame.draw.polygon(screen, color, [(mid_x, start[1]), (end[0], mid_y), (mid_x, end[1]), (start[0], mid_y)])
        

    # Draw circles
    for circle in circles:
        start, end, color = circle
        radius = max(abs(end[0] - start[0]), abs(end[1] - start[1])) // 2
        center = start[0] + (end[0] - start[0]) // 2, start[1] + (end[1] - start[1]) // 2
        pygame.draw.circle(screen, color, center, radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()