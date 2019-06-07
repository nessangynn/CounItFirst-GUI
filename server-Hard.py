'''
    Count-It-First - Server HARD
    CSC/CPE 4750
    Author: Tai Doan, Hung Nguyen, Huyen Nguyen
    '''

import socket
import sys
import random

HARD_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
HARD_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #make port reusable


IP_ADDRESS = str(sys.argv[1])
PORT_2 = 43505 # Port for Hard mode
TWO_CLIENTS = 2

#Connection socket for HARD mode
HARD_SOCKET.bind((IP_ADDRESS, int(PORT_2)))
HARD_SOCKET.listen(1)

print('Server HARD is ready to accept client')

CLIENTS_HARD = []

# broadcast() takes 2 parameters: a message and the connection to a client
# The function broadcasts the message to all clients whose object is not
# the same as the one sending the message
def broadcast(message, connection, receiver):
    for c in receiver:
        if c[0] != connection:
            c[0].send(message)

# remove() takes 1 parameters: the connection
# The function removes the object from the list
def remove(connection):
    if connection in CLIENTS_HARD:
        CLIENTS_HARD.remove(connection)

while 1:
    for i in range(0, int(TWO_CLIENTS)):
        #accept the connection from client
        connectionSocket_Hard, addr_H = HARD_SOCKET.accept()
        #add new clients to the list
        CLIENTS_HARD.append((connectionSocket_Hard, addr_H))
        #send welcome message to client
        connectionSocket_Hard.send(b'Welcome to the play room!\n')
        #Announce new connection
        welcomeMessage = "Player " + str(len(CLIENTS_HARD)-1) +" connected to server HARD"
        print(welcomeMessage)
    RAN_NUMBER = random.randint(30, 50)
    print("Generated number: ", RAN_NUMBER)
    SUM = 0
    GEN_NUMBER = str(RAN_NUMBER).encode('utf-8')
    for c in CLIENTS_HARD:
        c[0].send(GEN_NUMBER)

    #the loop makes the game last infinitely
    while 1:
        for i in range(0, len(CLIENTS_HARD)):
            #receive message from client
            sentence = CLIENTS_HARD[i][0].recv(2048).decode('utf-8')
            print("Player ", i, " entered: ", sentence)
            SUM += int(sentence)
            print("Current Number: ", str(SUM))
            if SUM == RAN_NUMBER or SUM > RAN_NUMBER:
                print("THE WINNER IS PLAYER ", i)
                CLIENTS_HARD[i][0].send(b'YOU WIN')
                broadcast(b'YOU LOSE', CLIENTS_HARD[i][0], CLIENTS_HARD)
                for c in CLIENTS_HARD:
                    c[0].close()
                    exit()
            else:
                cur_num = str(SUM).encode('utf-8')
                for c in CLIENTS_HARD:
                    c[0].send(cur_num)
