from flask import Flask, request, jsonify
from flask_cors import CORS
from models.task import Task

app = Flask(__name__)
CORS(app)

tasks = []
task_id_control = 1

@app.route('/api/health', methods=['GET'])
def health():
    return 'Server is healthy!', 200

@app.route('/api/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, name=data['name'], description=data['description'])
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({'message':'Task sucessfully created'}), 201

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks_dict = [task.to_dict() for task in tasks]
    output = {'tasks': tasks_dict, 'total_tasks': len(tasks_dict)}
    return jsonify(output), 200

@app.route('/api/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = next((task for task in tasks if task.id == id), None)
    if task:
        return jsonify(task.to_dict()), 200
    return jsonify({'message':'Task not found'}), 404

@app.route('/api/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    task = next((task for task in tasks if task.id == id), None)
    if task:
        task.name = data['name']
        task.description = data['description']
        task.status = data['status']
        return jsonify({'message':'Task sucessfully updated'}), 200
    return jsonify({'message':'Task not found'}), 404

@app.route('/api/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = next((task for task in tasks if task.id == id), None)
    if task:
        tasks.remove(task)
        return jsonify({'message':'Task sucessfully deleted'}), 200
    return jsonify({'message':'Task not found'}), 404
    

if __name__ == '__main__':
  app.run(debug=True,port=5000)
