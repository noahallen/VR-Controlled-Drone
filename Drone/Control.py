import socket
import tello
import pygame, math, time
from ast import literal_eval

def droneController(coords):
    #Testing function calls

    x = coords[0]
    y = coords[1] - 450
    z = coords[2]
    min = z

    if x < min:
        min = x
    if y < min:
        min = y

    distanceFromCenter = int(math.sqrt(math.pow(x, 2) + math.pow(z, 2) + math.pow(y, 2)))
    trackerXToDrone = int((x / min) * 20)
    trackerYToDrone = int((y / min) * 20)
    trackerZToDrone = int((z / min) * 20)
    trackerToSpeed = int((distanceFromCenter / 7.6) + 9)

    #The speed is calculated this way because the max distance from the center
    #is approximately 566 units away, and to divide it evenly to fit in
    #the tello's range of 10 - 100, every 7.6 units is converted to 1 unit of speed

    tello.go_xyz_speed(trackerXToDrone, trackerYToDrone, trackerZToDrone, trackerToSpeed)

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
