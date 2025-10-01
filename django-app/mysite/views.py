from django.http import JsonResponse
import pika

def enqueue(request):
    msg = request.GET.get("msg", "default-task")
    conn = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
    channel = conn.channel()
    channel.queue_declare(queue="myqueue", durable=True)
    channel.basic_publish(exchange="", routing_key="myqueue", body=msg)
    conn.close()
    return JsonResponse({"status": "queued", "message": msg})