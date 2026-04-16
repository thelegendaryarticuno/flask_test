from flask import Flask, jsoify


app = Flask(__name__)

#final deploy check
@app.get("/health")
def health():
    return jsonify({"status": "ok"})

#deploy test -2 

@app.get("/user")
def user():
    return jsonify({"id": 1, "name": "demo-user"})
#deployment 

@app.get("/order")
def order():
    return jsonify({"order_id": 1001, "status": "created"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
