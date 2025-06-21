import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import json
from utils import create_new_json, read_tasks, generate_new_id, save_tasks, load_tasks

class TestUtils(unittest.TestCase):
    @patch("os.path.exists", return_value=False)
    @patch("builtins.open", new_callable=mock_open)
    def test_create_new_json_creates_file(self, mock_file, mock_exists):
        create_new_json()
        mock_file.assert_called_with("tasks.json", "w")
        handle = mock_file()
        handle.write.assert_called()  # Should write something

    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "title": "Test", "description": "desc", "due_date": "2025-06-21"}]')
    def test_read_tasks_reads_file(self, mock_file):
        tasks = read_tasks()
        self.assertIsInstance(tasks, list)
        self.assertEqual(tasks[0]["id"], 1)

    def test_generate_new_id_empty(self):
        self.assertEqual(generate_new_id([]), 1)

    def test_generate_new_id_nonempty(self):
        tasks = [{"id": 1}, {"id": 2}, {"id": 5}]
        self.assertEqual(generate_new_id(tasks), 6)

    @patch("utils.read_tasks", return_value=[])
    @patch("builtins.open", new_callable=mock_open)
    @patch("utils.Task")
    def test_save_tasks_success(self, mock_task, mock_file, mock_read):
        mock_task.return_value.to_dict.return_value = {"id": 1, "title": "t", "description": "d", "due_date": "2025-06-21"}
        save_tasks("t", "d", "2025-06-21")
        mock_file.assert_called_with("tasks.json", "w")
        handle = mock_file()
        handle.write.assert_called()

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_load_tasks_file_not_found(self, mock_file):
        with patch("builtins.print") as mock_print:
            load_tasks()
            mock_print.assert_any_call("No tasks found")

    @patch("builtins.open", new_callable=mock_open, read_data="[]")
    def test_load_tasks_no_tasks(self, mock_file):
        with patch("builtins.print") as mock_print:
            load_tasks()
            mock_print.assert_any_call("No tasks to show.")

if __name__ == "__main__":
    unittest.main()
