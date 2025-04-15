from flask import Flask, request, jsonify, render_template
import psycopg2
from psycopg2.extras import DictCursor
import os
print(f"Current working directory: {os.getcwd()}")
app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = psycopg2.connect(
        host="terraform-20250409173832660600000001.ckpw4u04e172.us-east-1.rds.amazonaws.com",
        database="taskmanager",
        user="root",
        password="Password123"
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

# Create Task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task_name = data.get('task_name')
    task_description = data.get('task_description')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (task_name, task_description) VALUES (%s, %s) RETURNING id;",
                (task_name, task_description))
    task_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'id': task_id, 'task_name': task_name, 'task_description': task_description}), 201

# Retrieve Tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=DictCursor)
    cur.execute("SELECT * FROM tasks;")
    tasks = cur.fetchall()
    cur.close()
    conn.close()

    # Adjust the returned structure to match what the frontend expects
    return jsonify([{'id': task['id'], 'task_name': task['task_name'], 'task_description': task['task_description']} for task in tasks])

# Update Task
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    task_name = data.get('task_name')
    task_description = data.get('task_description')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("UPDATE tasks SET task_name = %s, task_description = %s WHERE id = %s;",
                (task_name, task_description, id))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({'id': id, 'task_name': task_name, 'task_description': task_description})

# Delete Task
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = %s;", (id,))
    conn.commit()
    cur.close()
    conn.close()

    return '', 204

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)