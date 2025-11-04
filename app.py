from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    
    # --- IMPLEMENTAÇÃO DA MUDANÇA (PRIORIDADE) ---
    # 1. Garante que a tarefa tenha uma prioridade, com 'Média' como padrão
    if 'priority' not in data:
        data['priority'] = 'Média' 
    
    # 2. Adiciona um ID sequencial (Melhoria de Robustez)
    if not data.get('id'):
        new_id = len(tasks) + 1
        data['id'] = new_id
    # ---------------------------------------------
        
    tasks.append(data)
    return jsonify(data), 201
