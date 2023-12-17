import pika

def connect():
    try:
        credentials = pika.PlainCredentials('rabbit_mq_user', 'rabbit_mq_password')
        parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)
        connection = pika.BlockingConnection(parameters)
        return connection.channel()
    except Exception as e:
        print(f"Exception during connection: {str(e)}")
        return None

def produce_message(message):
    channel = connect()
    if channel is None:
        return False

    try:
        channel.queue_declare(queue='to_crawl', durable=True)
        channel.basic_publish(exchange='', routing_key='to_crawl', body=message)
        print(f"Sent message to the queue")
        return True  # Indicate success
    except Exception as e:
        print(f"Exception while producing message: {str(e)}")
        return False
    finally:
        if channel:
            channel.close()

if __name__ == '__main__':
    print("testing rabbit mq")
    produce_message("Test1")
