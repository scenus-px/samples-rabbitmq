#
# Copyright (C) scenüs, 2023.
# All rights reserved.
# Ehsan Haghpanah; ehsan@scenus.com
#

# https://pypi.org/project/pika/

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
channel.basic_publish(exchange= 'FIX', routing_key= 'BBOC', body= b'FIX-Message')
connection.close()
