import pika
import sys
import json

class RabbitMq():

    def __init__(self, server):

        self.server = server

        self._connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.server.host))
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self.server.queue)

    def publish(self, payload, pattern):
        
        bodyToStr = json.dumps({"pattern": pattern,
        "data":payload})
        
        self._channel.basic_publish(exchange=self.server.exchange,
                      routing_key=self.server.routingKey,
                      body=bodyToStr)

        print(bodyToStr)

