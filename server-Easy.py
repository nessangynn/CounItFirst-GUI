'''
    Count-It-First - Server EASY
    CSC/CPE 4750
    Author: Tai Doan, Hung Nguyen, Huyen Nguyen
'''

import socket
import sys
import random

EASY_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
EASY_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #make port reusable


IP_ADDRESS = str(sys.argv[1])
PORT_1 = 43500 # Port for Easy mode


TWO_CLIENTS = 2
'''
 binds the server to an entered IP address and at the specified port number.
 The client must be aware of these parameters
 '''
# Connection socket for EASY mode
EASY_SOCKET.bind((IP_ADDRESS, int(PORT_1)))
EASY_SOCKET.listen(1)

# back-end testing message
# purpose: make sure the server is ready
print('Server EASY is ready to accept client')

CLIENTS = []

#accept up to 2 connections from clients, which
#must connect before we can move on

# broadcast() takes 2 parameters: a message and the connection to a client
# The function broadcasts the message to all clients whose object is not
# the same as the one sending the message
def broadcast(message, connection, receiver):
    for c in receiver:
        if c[0] != connection:
            c[0].send(message)

# remove() takes 1 parameters: the connection
# purpose: The function removes the object from the list
def remove(connection):
    if connection in CLIENTS:
        CLIENTS.remove(connection)

#GAME LOOP
# purpose: to keep running the game until one of the two players wins
while 1:
    for i in range(0, int(TWO_CLIENTS)):
        # Accept the connection from client
        connectionSocket, addr = EASY_SOCKET.accept()
        # Add new clients to the list
        CLIENTS.append((connectionSocket, addr))
        # Send welcome message to client
        connectionSocket.send(b'Welcome to the play room!\n')
        # Announce new connection
        welcomeMessage = "Player " + str(len(CLIENTS)-1) +" connected to server EASY"
        print(welcomeMessage)
    RAN_NUMBER = random.randint(7, 10)
    print("Generated number: ", RAN_NUMBER)
    SUM = 0
    GEN_NUMBER = str(RAN_NUMBER).encode('utf-8')
    for c in CLIENTS:
        c[0].send(GEN_NUMBER)
    while 1:
        for i in range(0, len(CLIENTS)):
            # Receive message from client - confirmed on server side that
            # clients are connected.
            sentence = CLIENTS[i][0].recv(2048).decode('utf-8')
            print("Player ", i, " entered: ", sentence)
            SUM += int(sentence)
            print("Current Number: ", SUM)
            if SUM == RAN_NUMBER or SUM == RAN_NUMBER +1:
                print("THE WINNER IS PLAYER ", i)
                CLIENTS[i][0].send(b'YOU WIN')

                if i + 1 == len(CLIENTS):
                    CLIENTS[0][0].send(b'YOU LOSE')
                else:
                    CLIENTS[i - 1][0].send(b'YOU LOSE')
                for c in CLIENTS:
                    c[0].close()
                exit()
            else:
                curr_num = str(SUM).encode('utf-8')
                for c in CLIENTS:
                    c[0].send(curr_num)
