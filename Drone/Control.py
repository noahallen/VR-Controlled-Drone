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


def testFunc(coords):
    print(coords)


def main():
    try:
        while True:
            full_msg = ''
            msg = s.recv(1024)

            #Full message recieves a decoded string of the server data
            full_msg = msg.decode("utf-8")

            #Turns the string array into an actual array of integers
            coordinateArr = literal_eval(full_msg)
            testFunc(coordinateArr)

    except:
        print("Connection closed")


if __name__ == "__main__":
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1243))
    main()
