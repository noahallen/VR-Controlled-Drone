import socket
import tello
import math
from ast import literal_eval

def droneController(coords):
    #Testing function calls

    x = intPos[0]
    z = intPos[2]
    min = z

    if x < z:
        min = x
    distanceFromCenter = math.sqrt(math.pow(x, 2) + math.pow(z, 2))
    trackerXToDrone = (x / min) * 20
    trackerYToDrone = intPos[1]
    trackerZToDrone = (z / min) * 20
    trackerToSpeed = (distanceFromCenter / 6.2) + 9

    go_xyz_speed(trackerXToDrone, trackerYToDrone, trackerZToDrone, trackerToSpeed)


import pygame, math, time


class GUI_Support:

    def initDisplay(self, dims):
        pygame.init()
        return pygame.display.set_mode(dims)

    def isQuit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            else:
                return False

    
    def drawGraphics(self, position, screen, dims):
        handX, handY, handZ = position
        #Centers the X and Z coordinates
        handY = handY * -1
        handX += 400
        handZ += 400
        handY += 800
        width, height = dims
        screen.fill((255, 255, 255))

        circleRadius = 20
        pygame.draw.circle(screen, (0, 0, 0), (handX, handZ), circleRadius)
        pygame.draw.circle(screen, (0, 0, 0), (1050, handY), circleRadius)

        #Draws the circle and lines across the screen
        pygame.draw.circle(screen, (0, 0, 0), (400, 400), 150, 5)

        #Vertical Line
        pygame.draw.line(screen, (0, 0, 0), (800, 0), (800, 800))

        #Y Axis Deadzone
        pygame.draw.line(screen, (0, 0, 0), (800, 225), (1300, 225))
        pygame.draw.line(screen, (0, 0, 0), (800, 675), (1300, 675))




    def getTextObjects(self, text, font):
        textSurface = font.render(text, True, (255,255,255))
        return textSurface, textSurface.get_rect()




def guiDisplay(coords):
    guiSupport.drawGraphics(coords, screen, (800, 800))
    pygame.display.update()
    print(coords)   


def main():
    prevVal = (0, 450, 0)
    try:
        while True:
            full_msg = ''
            msg = s.recv(1024)

            #Full message recieves a decoded string of the server data
            full_msg = msg.decode("utf-8")

            #Turns the string array into an actual array of integers
            coordinateArr = literal_eval(full_msg)
            if(coordinateArr != prevVal):
                guiDisplay(coordinateArr)
            prevVal = coordinateArr

    except:
        print("Connection closed")


if __name__ == "__main__":
    guiSupport = GUI_Support()
    #Square is 800x800 but 1300 for X for y portion to be displayed
    xWidth = 1300
    yHeight = 800
    screen = guiSupport.initDisplay((xWidth, yHeight))
    
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1243))
    main()
