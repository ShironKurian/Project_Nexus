import unittest
import json
from app import app

class TaskManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.task_data = {
            'task_name': 'Test Task',
            'task_description': 'This is a test task'
        }

    def test_create_task(self):
        response = self.client.post('/tasks', data=json.dumps(self.task_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('task_name', response.get_json())

    def test_get_tasks(self):
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

    def test_update_task(self):
        # First create a task
        post_response = self.client.post('/tasks', data=json.dumps(self.task_data), content_type='application/json')
        task_id = post_response.get_json()['id']

        # Then update it
        update_data = {
            'task_name': 'Updated Task',
            'task_description': 'Updated description'
        }
        put_response = self.client.put(f'/tasks/{task_id}', data=json.dumps(update_data), content_type='application/json')
        self.assertEqual(put_response.status_code, 200)
        self.assertEqual(put_response.get_json()['task_name'], 'Updated Task')

    def test_delete_task(self):
        # Create a task
        post_response = self.client.post('/tasks', data=json.dumps(self.task_data), content_type='application/json')
        task_id = post_response.get_json()['id']

        # Then delete it
        delete_response = self.client.delete(f'/tasks/{task_id}')
        self.assertEqual(delete_response.status_code, 204)

if __name__ == '__main__':
    unittest.main()