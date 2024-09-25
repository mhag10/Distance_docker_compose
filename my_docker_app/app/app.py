from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis-container', port=6379)

@app.route('/')
def hello():
    redis.incr('hits')
    return f" - - - This basic web page has been viewed {redis.get('hits').decode('utf-8')} time(s) - - -"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
