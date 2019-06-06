'''
    Count-It-First - Server EASY
    CSC/CPE 4750
    Author: Tai Doan, Hung Nguyen, Huyen Nguyen
'''

from socket import *
import re
import sys
import random
from time import gmtime, strftime
from datetime import datetime

easySocket = socket(AF_INET, SOCK_STREAM) #TCP
easySocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #make port reusable


# takes the first argument from command prompt as IP address
IP_address = str(sys.argv[1])
# takes second argument from command prompt as port number
Port1 = 43500       #Port for Easy mode


TWO_CLIENTS = 2
'''
 binds the server to an entered IP address and at the specified port number.
 The client must be aware of these parameters
 '''
#Connection socket for EASY mode
easySocket.bind((IP_address, int(Port1)))
easySocket.listen(1)

print('Server EASY is ready to accept client')

clients = []

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
# The function removes the object from the list
def remove(connection):
    if connection in clients:
        clients.remove(connection)

while 1:
    for i in range(0, int(TWO_CLIENTS)):
        #accept the connection from client
        connectionSocket,addr = easySocket.accept()
        #add new clients to the list
        clients.append((connectionSocket,addr))
        #send welcome message to client
        connectionSocket.send(b'Welcome to the play room!\n')
        #Announce new connection
        welcomeMessage = "Player " + str(len(clients)-1) +" connected to server EASY"
        print(welcomeMessage)
    
    ran_num = random.randint(10, 30)
    print("Generated number: ", ran_num)
    sum = 0
    gen_num = str(ran_num).encode('utf-8')
    for c in clients:
        c[0].send(gen_num)
 
    while 1:
        for i in range(0, len(clients)):
            #receive message from client
            sentence = clients[i][0].recv(2048).decode('utf-8')
            print("Player ", i, " entered: ", sentence)
            sum += int(sentence)
            print("Current Number: ", sum)
            
            '''code for close/shutdown'''
            
            if sum == ran_num or sum == ran_num +1:
                print("THE WINNER IS PLAYER ", i)
                clients[i][0].send(b'YOU WIN')
                broadcast(b'YOU LOSE', clients[i][0], clients)
                for c in clients:
                    c[0].close()
                exit()
            else:
                curr_num = str(sum).encode('utf-8')
                for c in clients:
                    c[0].send(curr_num)
