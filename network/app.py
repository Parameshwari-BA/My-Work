import redis

client = redis.Redis(host='redis_server', port=6379, decode_responses=True)

client.set("message", "Hello from Python container!")

print("Reading message from Redis:")
print(client.get("message"))
