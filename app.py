from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello, this is my first class."

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)

# Created/Modified files during execution:
print("app.py")