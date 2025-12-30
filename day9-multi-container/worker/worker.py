import time
import redis

r = redis.Redis(host='redis', port=6379, decode_responses=True)

while True:
    msg = f"Worker reading hits: {r.get('hits')}"
    print(msg)
    time.sleep(5)
