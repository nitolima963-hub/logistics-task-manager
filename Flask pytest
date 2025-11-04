# tests/test_app.py
import json
from app import app, tasks  # Importa o app e a lista de tasks do seu app.py

# Este teste verifica se a rota POST funciona e se adiciona a tarefa
def test_status_code_create_task():
    # Configura o app para modo de teste
    app.config['TESTING'] = True
    client = app.test_client()

    new_task_data = {'title': 'Completar testes', 'status': 'A Fazer'}

    # Garante que a lista está limpa antes do teste
    tasks.clear() 

    # Simula uma requisição POST com o JSON
    response = client.post('/tasks', 
                           data=json.dumps(new_task_data), 
                           content_type='application/json')

    # 1. Verifica se o status HTTP é 201 (Created)
    assert response.status_code == 201

    # 2. Verifica se a lista tasks contém a tarefa (CRUD básico)
    assert len(tasks) == 1
