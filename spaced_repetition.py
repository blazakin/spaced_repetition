import zmq
import random


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5552")


while True:
    message = socket.recv().decode()

    print(f"Received: {message}")
    if message == 'Exit':
        break

    card_list = message.split(';')[:-1]

    chosen_card = card_list[random.randint(0, len(card_list)-1)]
    socket.send_string(chosen_card)

    print(f"Sent: {chosen_card}")
