import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port=8000

server.bind(ip_address,port)
server.listen

list_of_clients=[]
print("Server has started ........ :}")

questions=[
    "What is the other name of civil code of 1804 \n a.Nepoleonic code \n b.Narendra Modi code \n c.Velamir Putin code",
    "Water boils at ___degree celcius \na.100 \nb.200 \nc.15",
    "Which state refer as most educated state of India \na.Maharastra \nb.Kerela \nc.Tamilnadu"
]
answers=["a","a","b"]


def clientthread(conn):
    score = 0
    conn.send("Welcome to this quiz game!".encode('utf-8'))
    conn.send("Try to ans the questions in a,b or c").encode('utf-8')
    conn.send("Good luck\n\n".encode('utf-8'))
    index,question,answer = get_random_question_answer()
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                if message.lower() == answer:
                    score += 1
                    conn.send(f"Bravo! Your score is {score}\n\n".encode('utf-8'))
                else:
                    conn.send("Incorrect answer_get_better_luck_next_time\n".encode('utf-8'))
                remove_question(index)
                index,question,answer = get_random_question_answer()
            else:
                remove(conn)
        except:
            continue

def get_random_question_answer(conn):
    random_index = random.randit(0,len(questions)-1)
    random_question = questions[random_index]
    random_answer = answers[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_index,random_question,random_answer

def remove_question(index):
    questions.pop(index)
    answers.pop(index)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    conn,addr = server.accept()
    list_of_clients.append(conn)
    print(addr[0] + "connected")
    new_thread = Thread(target = clientthread,args=(conn,addr))
    new_thread.start()