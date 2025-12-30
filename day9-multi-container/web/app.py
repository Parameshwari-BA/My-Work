from flask import Flask
import redis
app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)
@app.route('/')
def home():
       redis_client.incr('hits')
       count = redis_client.get('hits')
       return f"Page viewed {count} times!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

