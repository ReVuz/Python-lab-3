import pygame
import sys
import numpy
pygame.init()
box = (numpy.array([
    [0,0,0],
    [0,0,0],
    [0,0,0]
]))
XO = 'o'
draw=False
Winner=None
width,height=400,400
win=pygame.display.set_mode((width,height+200))
pygame.display.set_caption('Tic Tac Toe')
win.fill((0,0,0))

def start():
    font=pygame.font.Font(None,82)
    win.fill((200,200,200))
    text=font.render("Tic Tac Toe",True,(0,0,255),(200,200,200))
    show_text=text.get_rect()
    show_text.center=(width//2,height//2)
    win.blit(text,show_text)
    pygame.display.update()
    pygame.time.wait(1200)
    win.fill((250,250,250))
    # vertical lines
    pygame.draw.line(win,(0,0,0),(3,0),(3,600),5)
    pygame.draw.line(win,(0,0,0),(396,0),(396,600),5)
    pygame.draw.line(win,(0,0,0),(width/3,0),(width/3,height),5)
    pygame.draw.line(win,(0,0,0),((width/3)*2,0),((width/3)*2,height),5)
    #horizontal lines
    pygame.draw.line(win,(0,0,0),(0,(height/3)*0.01),(width,(height/3)*0.01),5)
    pygame.draw.line(win,(0,0,0),(0,height/3),(width,height/3),5)
    pygame.draw.line(win,(0,0,0),(0,(height/3)*2),(width,(height/3)*2),5)
    pygame.draw.line(win,(0,0,0),(0,(height/3)*3),(width,(height/3)*3),5)
    pygame.draw.line(win,(0,0,0),(0,(height/3)*3.72),(width,(height/3)*3.72),5)
    font=pygame.font.Font(None,50)
    text=font.render("Press Space To Restart", True,(0,0,0),((250,250,250)))
    textRect = text.get_rect()
    textRect.center = (200,550)
    win.blit(text, textRect)
start()

def mouse_point():
    global row,col
    x,y=pygame.mouse.get_pos()
   # print(x,y)
    if(x<width/3) and (y<height/3):

        row=0

        col=0

    elif(x>width/3 and x<width/3*2) and (y<height/3):

        row=0

        col=1

    elif(x>width/3*2) and (y<height/3):

        row=0

        col=2

    elif(x<width/3) and (y>height/3 and y<height/3*2):

        row=1

        col=0

    elif(x>width/3 and x<width/3*2) and (y>height/3 and y<height/3*2):

        row=1

        col=1

    elif(x>width/3*2) and (y>height/3 and y<height/3*2):

        row=1

        col=2

    elif(x<width/3) and (y>height/3*2):

        row=2

        col=0

    elif(x>width/3 and x<width/3*2) and (y>height/3*2):

        row=2

        col=1

    elif(x>width/3*2) and (y>height/3*2):

        row=2

        col=2

    else:

        row=None

        col=None
    draw_figure(row,col)

def draw_figure(row,col):
     global XO

     if(box[row,col] == 0):
        global draw
        if row==0:
            posx = 65
        if row==1:
            posx = width/3 + 65
        if row==2:
            posx = width/3*2 + 65
        if col==0:
            posy = 65
        if col==1:
            posy = height/3 + 65
        if col==2:
            posy = height/3*2 + 65
        #drawing X and O on mainscreen

        if(XO=='o'):

            pygame.draw.circle(win, (0,0,0), (posy, posx ), 40,8)

            box[row][col] = 1

            XO='x'

        else:

            pygame.draw.line (win,(0,0,0), (posy - 30, posx - 30),

                         (posy + 30, posx + 30), 8)

            pygame.draw.line (win,(0,0,0), (posy + 30, posx - 30),

                         (posy - 30, posx + 30), 8)

            box[row][col] = 2

            XO='o'

        pygame.display.update()
        check_Winner()
     else:
         pass

    #Show Player Message turns 

     message= XO.upper() + "'s Turn"

     font=pygame.font.Font(None,70)

     text = font.render(message, True,(250,0,0),((250,250,250)))

     textRect = text.get_rect()

     textRect.center = (200,450)

     win.blit(text, textRect)


     pygame.display.update()


#This Function check Winner and draw

def check_Winner():

    global Winner

    for row in range (0,3):

        if ((box [row][0] == box[row][1] == box[row][2]) and(box [row][0] != 0)):

            # this row won

            Winner = box[row][0]

            pygame.draw.line(win, (0,0,0), (0, (row + 1)*height/3 -height/6),\

                              (width, (row + 1)*height/3 - height/6 ), 4)

            show_winning_message(Winner)

            break


    # check for winning columns

    for col in range (0, 3):

        if (box[0][col] == box[1][col] == box[2][col]) and (box[0][col] != 0):

            # this column won

            Winner = box[0][col]

            #draw winning line

            pygame.draw.line (win, (0,0,0),((col + 1)* width/3 - width/6, 0),\

                          ((col + 1)* width/3 - width/6, height), 4)

            show_winning_message(Winner)

            break


    # check for diagonal Winners

    if (box[0][0] == box[1][1] == box[2][2]) and (box[0][0] != 0):

        # game won diagonally left to right

        Winner = box[0][0]

        pygame.draw.line (win, (0,0,0), (50, 50), (350, 350), 4)

        show_winning_message(Winner)

       


    if (box[0][2] == box[1][1] == box[2][0]) and (box[0][2] != 0):

        # game won diagonally right to left

        Winner = box[0][2]

        pygame.draw.line (win, (0,0,0), (350, 50), (50, 350), 4)

        show_winning_message(Winner)

    

    if(all([all(row) for row in box]) and Winner is None ):

        draw = True
        font=pygame.font.Font(None,70)
        text=font.render("Match Draw", True,(0,0,250),((250,250,250)))
        textRect = text.get_rect()
        textRect.center = (200,450)
        win.blit(text, textRect)
        pygame.display.update()
        pygame.time.wait(1700)
        reset_game()


def show_winning_message(Winner):

    font=pygame.font.Font(None,70)

    if Winner == 1:

        Winner = "O WINS "

    elif Winner == 2:

        Winner = "X WINS "

    else:

        pass

    text=font.render(Winner, True,(250,0,0),((250,250,250)))

    textRect = text.get_rect()

    textRect.center = (200,450)

    win.blit(text, textRect)    

    pygame.display.update()

    pygame.time.wait(1700)
    
    reset_game()

def reset_game():

    global box,draw,Winner

    box = (numpy.array([

        [0,0,0],

        [0,0,0],

        [0,0,0]

    ]))

    XO='x'

    draw=False

    Winner=None
    start()

start()
        
while(True):
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_point()
        elif keys[pygame.K_SPACE]:
            reset_game()
    pygame.display.update()
    pygame.display.flip()
    
