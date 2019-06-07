'''
    Count-It-First - Client (BACK END)
    CSC/CPE 4750
    Author: Tai Doan, Hung Nguyen, Huyen Nguyen
    '''


import socket

#import easyWindow


class Client(object):

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP socket
        self.port = None
        self.connection = None
        self.ip_address = "127.0.0.1" #localhost
        self.mode = 0
        self.generated_number = 0 #random number
        self.updated_number = 0
        self.updated_message = 0

    def check_result(self, message):
        if message == "YOU WIN" or message == "YOU LOSE":
            return 0

    # back-end testing (Terminal)
    # GUI replaced this method with buttons +1, +2 (EASY) and +1, +3, +5 (HARD)
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


    # prep_game function is created to call in ___init___ in
    # easyWindow.py - easy mode
    # hardWindow.py - hard mode
    # purpose: for home.py (HOME PAGE of the game) to know which MODE
    #         the player choose to redirect player to go on that screen
    def prep_game(self, number=""):
        # Mode selection for the Game
        # EASY as "1"
        # HARD as "2"
        while 1:
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
                print(self.port, self.ip_address)
                self.connection = self.client_socket.connect((self.ip_address, self.port))
                break
            else:
                print("Invalid input")
        #back-end tester (Terminal)
        #After connected, player is welcomed by the server
        welcome_message = self.client_socket.recv(2048).decode('utf-8')
        print(welcome_message)


    # gen_number function is created to call in ___init___ in
    # easyWindow.py - easy mode
    # hardWindow.py - hard mode
    # purpose: to retrieve random number from the server and
    #         display on GUI through Win Number QLCD display.
    def gen_number(self):

        #Get the generated number from the server
        number = self.client_socket.recv(2048).decode('utf-8')

        #convert the number from str to int
        self.generated_number = int(number)

        #call RETURN to get the output in order to display on GUI
        return self.generated_number

    # Receive updated message from the server every time server sends to the client socket
    # receive_message() method get the output from game_logic2
    # print out on currNumber QLCD Display on GUI
    def receive_message(self, string):
        self.updated_message = string
        return self.updated_message

    def get_lastest_number(self):
        current_number = self.client_socket.recv(2048).decode('utf-8')
        if (current_number == "YOU WIN" or current_number == "YOU LOSE"):
            return None
        else:
            return int(current_number)

    #Game loop 1
    def game_logic(self, input_number):

        #testing on back-end (Terminal)
        print("\nYOUR TURN")

        #Send player's input then send to server
        #repr = str
        self.client_socket.send(repr(input_number).encode('utf-8'))
        #Receive current total number from server
        current_number = self.client_socket.recv(2048).decode('utf-8')

        if self.check_result(current_number) == 0:
            print("reach 1") #testing
            self.receive_message(current_number)
            self.client_socket.close()

        #change GUI current number
        self.receive_message(current_number)


    #Game loop 2
    def game_logic2(self, input_number):
        #testing for back-end (Terminal)
        #if input is "close", close connection
        if input_number == "/close":
            close_message = self.client_socket.recv(2048).decode('utf-8')
            print(close_message)
            self.client_socket.close()
        else:
            # receive message from server
            # contains calculated number after everytime:
            #   + players add 1 or 2 (EASY MODE)
            #   + players add 1, 3, or 5 (HARD MODE)
            # included "YOU WIN" or "YOU LOSE" string at the end when the game is done
            from_server = self.client_socket.recv(2048).decode('utf-8')


            self.receive_message(from_server)
            if self.check_result(from_server) == 0:
                print("reach 2") #testing
                self.client_socket.close() #close connection
