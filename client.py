import socket
import threading

# Choosing Nickname
nickname = input("Напишите ваше имя: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('cp1251')
            if message == 'NICK':
                client.send(nickname.encode('cp1251'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("Выход из чата...")
            client.close()
            break

def write():
    while True:
        text = input('')
        if text == "exit": 
            client.close()
            exit()
        message = '{}: {}'.format(nickname, text)
        client.send(message.encode('cp1251'))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()