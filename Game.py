import simplegui, random
from math import sqrt

center_point = [50, 50] # ponto central
window_width = 600 # largura da janela
window_height = 400 # altura da janela
radius = 20 # raio do círculo
score = 0 # pontuação

# desenha o canvas
def draw(canvas):
    canvas.draw_circle(center_point, radius, 1, 'Red', 'Red')
    

# temporizador
def timer_handler():
    center_point[0] = random.randint(0, window_height)
    center_point[1] = random.randint(0, window_height)
    
    
def mouse_handler(pos):
    
    global score
    
    # Distance calc
    dist = sqrt(((pos[0] - center_point[0]) ** 2) + 
                ((pos[1] - center_point[1]) ** 2))
    
    # Check if the user click inside the circle
    if dist < radius:
        score += 1 # Increase score
    else:
        if score > 0:
            score -= 1 # Decrease score
            
    # Att text from the label
    label.set_text('Score: ' + str(score))
    

# Create a window passing the title, Width e Height
frame = simplegui.create_frame('Clique na bolinha', window_width, window_height)

# Create a temporizer passing the interval and manipulator
timer = simplegui.create_timer(1000, timer_handler)

# Set the manipulators of the events
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_handler)

# Adds a label
label = frame.add_label('Score: ' + str(score))

timer.start() # Start temporizer
frame.start() # Main application loop
