#
# Copyright (C) scenüs, 2023.
# All rights reserved.
# Ehsan Haghpanah; ehsan@scenus.com
#

import pika

class RabbitMQWrapper(object):
     
     instance_a: pika.ConnectionParameters
     instance_b: pika.ConnectionParameters
     instance_c: pika.ConnectionParameters
     connection: pika.BlockingConnection

     def __init__(self) -> None:
          self.instance_a = pika.ConnectionParameters(
               host= '172.16.51.131', 
               port= 5672, 
               credentials= pika.PlainCredentials('6b4b9ed1b14ac257', '5fe9cf41075021696428674612af6246'), 
               connection_attempts= 5, 
               retry_delay= 1
          )
          self.instance_b = pika.ConnectionParameters(
               host= '172.16.51.132', 
               port= 5672, 
               credentials= pika.PlainCredentials('48ce2dceed290914', 'b8ce6186c9ddc46e8d798a9e6b46b7af'), 
               connection_attempts= 5, 
               retry_delay= 1
          )
          self.instance_c = pika.ConnectionParameters(
               host= '172.16.51.133', 
               port= 5672, 
               credentials= pika.PlainCredentials('4041b7b90126ce4f', '7cf2b305f981993b7496190a26e1e1d3'), 
               connection_attempts= 5, 
               retry_delay= 1
          )
          self.connection = yield pika.BlockingConnection(parameters= (self.instance_a))
          self.channel = yield self.connection.channel()
          pass # init

     def close(self) -> None:
          self.connection.close()

     def prepare(self) -> None:
          self.channel.exchange_declare(callback= self.onExchangeDeclared, exchange= 'FIX')

     def onExchangeDeclared(self, args):
          print('onExchangeDeclared')
          print(args)

     pass # RabbitMQWrapper

w = RabbitMQWrapper()
w.prepare()
