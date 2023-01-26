
from rabbitmq.rabbitmq_configure import RabbitMQConfigure
from rabbitmq.rabbitmq import RabbitMq
from measurement.measurements import Measurements 
import timeit

import time

if __name__ == "__main__":
    start = timeit.default_timer()

    configureMeasurement = RabbitMQConfigure(queue='measurement', host='localhost', routingKey='sensor-data', exchange='')
    
    rabbitmqMeasurement = RabbitMq(configureMeasurement)

    measurements = Measurements()

    while True:
        
        measurements.set_sensors_data()
        data_json = measurements.toJSON()
        rabbitmqMeasurement.publish(payload=data_json, pattern="sensor-data")
        print("sent")

        time.sleep(30)