'''
    Count-It-First - Client
    CSC/CPE 4750
    Author: Tai Doan, Hung Nguyen, Huyen Nguyen
    '''


import socket
import sys

class client(object):

    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP socket
        self.Port = None
        self.connection = None

        self.IP_address = "127.0.0.1"
        self.mode = 0
        
        self.generatedNumber = None


    def checkResult(self, message):
        if message == "YOU WIN" or message == "YOU LOSE":
            return 0

    def handleInput(self, gameMode):
        if gameMode == "1":
            #Valid input is only 1 or 2
            while 1:
                inputNumber = input('Enter 1 or 2: ')
                if inputNumber == "1" or inputNumber == "2":
                    break
                else:
                    print("Invalid input")
        else:
            #Valid input is only 1 or 2
            while 1:
                inputNumber = input('Enter 1 or 3 or 5: ')
                if inputNumber == "1" or inputNumber == "3" or inputNumber == "5":
                    break
                else:
                    print("Invalid input")
        return inputNumber



#clientSocket = socket(AF_INET, SOCK_STREAM) #TCP socket

# # checks whether sufficient arguments have been provided
# if len(sys.argv) != 2:
#     print("Correct usage: script, IP address/host name")
#     exit()

    def prep_game(self, number="1"):
        #Mode selection
        while 1:
            #mode = input("Please choose mode (Enter 1 or 2):  1. Easy        2. Hard\n")
            self.mode = number
            if self.mode == "1":
                self.Port = 43500
                print("You have chosen EASY mode!")
                #connect to the server
                print(self.Port, self.IP_address)
                self.connection = self.clientSocket.connect((self.IP_address,self.Port))
                break
            elif self.mode == "2":
                self.Port = 43505
                print("You have chosen HARD mode!")
                #connect to the server

                self.connection = self.clientSocket.connect((self.IP_address,self.Port))
                break
            else:
                print("Invalid input")


        #After connected, player is welcomed by the server
        welcomeMessage = self.clientSocket.recv(2048).decode('utf-8')
        print(welcomeMessage)

        #Get the message of generated number
        # print("check2")
        number = self.clientSocket.recv(2048).decode('utf-8')
        # print("check3")
        print(number)
        self.generatedNumber = number

        #Get the message to start the game
        start = self.clientSocket.recv(2048).decode('utf-8')
        print(start)

#Game loop
    def game_logic(self, inputNumber):
        while 1:
            print("\nYOUR TURN")
            #inputNumber = self.handleInput(self.mode)
            try:
                #Send player's input
                self.clientSocket.send(repr(inputNumber).encode('utf-8')) # repr = str
                #Receive current total number from server
                currentNumber = self.clientSocket.recv(2048).decode('utf-8')
                print(currentNumber)
                if self.checkResult(currentNumber) == 0:
                    self.clientSocket.close()
                    exit()

                #if input is "close", close connection
                if inputNumber == "/close":
                    closeMsg = self.clientSocket.recv(2048).decode('utf-8')
                    print(closeMsg)
                    self.clientSocket.close()
                else:
                    #receive message from server, print it
                    fromServer = self.clientSocket.recv(2048).decode('utf-8')
                    print(fromServer)
                    if self.checkResult(fromServer) == 0:
                        self.clientSocket.close()
                        exit()
            #If cannot connect to server, close the connection
            except IOError:
                print("Connection error")
                self.clientSocket.close()
                exit()
        self.clientSocket.close() #close connection
