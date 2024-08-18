import zmq
import random


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5552")


while True:
    message = socket.recv().decode()

    if message == 'Exit':
        break

    card_list = message.split(';')
    card_list = card_list[:-1]

    socket.send_string(card_list[random.randint(0, len(card_list)-1)])
