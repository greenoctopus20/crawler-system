import pika

def connect():
    #try:
    credentials = pika.PlainCredentials('admin', '6ce1081613ffea9b262f3703475e222047c5c63392aa1a40')
    parameters = pika.ConnectionParameters('146.190.236.216', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    return connection.channel()
    #except Exception as e:
    #    print(f"Exception during connection: {str(e)}")
    #    return None

def produce_message(message):
    channel = connect()
    if channel is None:
        return False

    try:
        channel.queue_declare(queue='to_crawl', durable=True)
        channel.basic_publish(exchange='', routing_key='to_crawl', body=message)
        print(f"Sent message to the queue")
        return True
    except Exception as e:
        print(f"Exception while producing message: {str(e)}")
        return False
    finally:
        if channel:
            channel.close()
            
            
def consume_message(callBack):
    channel = connect()
    if channel is None:
        return False

    try:
        channel.queue_declare(queue='to_extract', durable=True)
        channel.basic_consume(queue='to_extract', on_message_callback=callBack, auto_ack=True)
        print(" *** EXTRACTOR STARTED *** \n  Waiting for messages. To exit press CTRL+C")
        channel.start_consuming()
        return True
    except Exception as e:
        print(f"Exception while consuming message: {str(e)}")
        return False
    finally:
        if channel:
            channel.close()

def callback(ch, method, properties, body):
    print(f"Received '{body}' from 'to_crawl' queue")
    
    
if __name__ == '__main__':
    
    #produce_message("test2")
    #produce_message("test3")
    consume_message(callBack=callback)
