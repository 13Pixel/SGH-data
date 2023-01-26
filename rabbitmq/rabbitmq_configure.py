class RabbitMQConfigure: 
    def __init__(self, queue, routingKey, exchange, host='localhost', exchangeType='topic', ):
        """ Configure Rabbit Mq Server for light value """
        self.queue = queue
        self.host = host
        self.routingKey = routingKey
        self.exchange = exchange
        self.exchangeType = exchangeType