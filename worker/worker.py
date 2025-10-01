import pika, time

def callback(ch, method, props, body):
    print(f"[worker] Received: {body.decode()}")
    time.sleep(2)  # simulate work
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    conn = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    channel = conn.channel()
    channel.queue_declare(queue="myqueue", durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="myqueue", on_message_callback=callback)
    print("[worker] Waiting for messages...")
    channel.start_consuming()

if __name__ == "__main__":
    main()