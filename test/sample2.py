#
# Copyright (C) scenüs, 2023.
# All rights reserved.
# Ehsan Haghpanah; ehsan@scenus.com
#

import pika

p1 = pika.ConnectionParameters(
     host= '172.16.51.131', 
     port= 5672, 
     credentials= pika.PlainCredentials('6b4b9ed1b14ac257', '5fe9cf41075021696428674612af6246'), 
     connection_attempts= 5, 
     retry_delay= 1
)

connection = pika.BlockingConnection(parameters= (p1))
channel = connection.channel()

for method_frame, properties, body in channel.consume('APP1SLE0105'):

    # displays the message parts and acknowledge the message
    print(method_frame, properties, body)
    channel.basic_ack(method_frame.delivery_tag)

    # escapes out of the loop after 10 messages
    if (method_frame.delivery_tag == 10):
        break

# cancels the consumer and return any pending messages
requeued_messages = channel.cancel()
print('Requeued %i messages' % requeued_messages)

connection.close()