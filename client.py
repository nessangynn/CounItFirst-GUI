'''
    Count-It-First - Client (BACK END)
    CSC/CPE 4750
    Author: Tai Doan, Hung Nguyen, Huyen Nguyen
    '''


import socket

class Client(object):

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP socket
        self.port = None
        self.connection = None

        self.ip_address = "127.0.0.1"
        self.mode = 0
        self.generated_number = 0
        self.updated_number = 1
        self.updated_message = None
    
    #def converting_function (self):
    

    def check_result(self, message):
        if message == "YOU WIN" or message == "YOU LOSE":
            return 0

    def handle_input(self, game_mode):
        if game_mode == "1":
            #Valid input is only 1 or 2
            while 1:
                input_number = input('Enter 1 or 2: ')
                if input_number == "1" or input_number == "2":
                    break
                else:
                    print("Invalid input")
        elif game_mode == "2":
            #Valid input is only 1 or 2
            while 1:
                input_number = input('Enter 1 or 3 or 5: ')
                if input_number == "1" or input_number == "3" or input_number == "5":
                    break
                else:
                    print("Invalid input")
        else:
            print("Invalid input")
        return input_number



#clientSocket = socket(AF_INET, SOCK_STREAM) #TCP socket

# # checks whether sufficient arguments have been provided
# if len(sys.argv) != 2:
#     print("Correct usage: script, IP address/host name")
#     exit()

    def prep_game(self, number= ""):
        #Mode selection
        while 1:
            #mode = input("Please choose mode (Enter 1 or 2):  1. Easy   2. Hard\n")
            self.mode = number
            if self.mode == "1":
                self.port = 43500
                print("You have chosen EASY mode!")
                #connect to the server
                print(self.port, self.ip_address)
                self.connection = self.client_socket.connect((self.ip_address, self.port))
                break
            elif self.mode == "2":
                self.port = 43505
                print("You have chosen HARD mode!")
                #connect to the server

                self.connection = self.client_socket.connect((self.ip_address, self.port))
                break
            else:
                print("Invalid input")


        #After connected, player is welcomed by the server
        welcome_message = self.client_socket.recv(2048).decode('utf-8')
        print(welcome_message)

    def gen_number(self):
        #Get the message of generated number
        
        number = self.client_socket.recv(2048).decode('utf-8')
        
        self.generated_number = int(number)
        return self.generated_number

    #Get the message to start the game
    # start = self.clientSocket.recv(2048).decode('utf-8')
    # print(start)

    def receive_current_number(self, number):
        self.updated_number = str(number)

        return self.updated_number
    def receive_message(self, string):
        self.updated_message = string
        return self.updated_message
#Game loop
    def game_logic(self, input_number):
        print("\nYOUR TURN")
        #inputNumber = self.handleInput(self.mode)
        #Send player's input
        self.client_socket.send(repr(input_number).encode('utf-8')) # repr = str
        #Receive current total number from server
        current_number = self.client_socket.recv(2048).decode('utf-8')

        self.receive_current_number(current_number)

        if self.check_result(current_number) == 0:
            self.client_socket.close()
            #exit()

        #if input is "close", close connection
        if input_number == "/close":
            close_message = self.client_socket.recv(2048).decode('utf-8')
            print(close_message)
            self.client_socket.close()
        else:
            #receive message from server, print it
            from_server = self.client_socket.recv(2048).decode('utf-8')
            self.receive_message(from_server)
            if self.check_result(from_server) == 0:
                self.client_socket.close()
                #exit()
        #If cannot connect to server, close the connection
        #close connection
