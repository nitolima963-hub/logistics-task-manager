from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    tasks.append(data)
    return jsonify(data), 201

@app.route("/tasks/<int:index>", methods=["PUT"])
def update_task(index):
    data = request.json
    tasks[index] = data
    return jsonify(data)

@app.route("/tasks/<int:index>", methods=["DELETE"])
def delete_task(index):
    task = tasks.pop(index)
    return jsonify(task)

if __name__ == "__main__":
    app.run(debug=True)
