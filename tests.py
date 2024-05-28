import pytest
import requests

BASE_URL = 'http://localhost:5000'
tasks = []

def test_create_task():
  new_task_data = {'name':'New Task', 'description':'Description of New Task'}
  response = requests.post(f'{BASE_URL}/api/tasks', json=new_task_data)
  assert response.status_code == 201
  response_json = response.json()
  assert "message" in response_json
  assert "id" in response_json
  tasks.append(response_json['id'])

def test_get_tasks():
  response = requests.get(f'{BASE_URL}/api/tasks')
  assert response.status_code == 200
  response_json = response.json()
  assert "tasks" in response_json
  assert "total_tasks" in response_json
  assert len(response_json['tasks']) == response_json['total_tasks']

def test_get_task():
  response = requests.get(f'{BASE_URL}/api/tasks/{tasks[0]}')
  assert response.status_code == 200
  response_json = response.json()
  assert "id" in response_json
  assert "name" in response_json
  assert "description" in response_json
  assert "status" in response_json

def test_update_task():
  update_task_data = {'name':'Updated Task', 'description':'Description of Updated Task', 'status':True}
  response = requests.put(f'{BASE_URL}/api/tasks/{tasks[0]}', json=update_task_data)
  assert response.status_code == 200
  response_json = response.json()
  assert "message" in response_json

def test_delete_task():
  response = requests.delete(f'{BASE_URL}/api/tasks/{tasks[0]}')
  assert response.status_code == 200
  response_json = response.json()
  assert "message" in response_json