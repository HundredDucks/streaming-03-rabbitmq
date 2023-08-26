"""
    This program sends a message to a queue on the RabbitMQ server. It originally had typos associated with the local host.
    Fixing this makes things run smoothly. It is best to run this file and v1_listen_for_messages.py in 2 separate terminals simultaneously.

    Zach Fuller
    08/26/2023

"""

# add imports at the beginning of the file
import pika

message = 'Whats up?'

# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LOCALHOST"))
# use the connection to create a communication channel
ch = conn.channel()
# use the channel to declare a queue
ch.queue_declare(queue="hello")
# use the channel to publish a message to the queue
ch.basic_publish(exchange="", routing_key="hello", body=message)
# print a message to the console for the user
print(f" [x] Sent {message}")
# close the connection to the server
conn.close()
