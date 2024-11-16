
from project import tasks, addTask, listTasks, deleteTask
def main():
    test_addTask()
    test_listTasks_empty()

    test_deleteTask_valid()
    test_deleteTask_invalid()
    test_deleteTask_non_numeric()


def test_addTask(monkeypatch):
    inputs = iter(["Buy groceries"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    addTask()
    assert tasks == ["Buy groceries"]

def test_listTasks_empty(capsys):
    tasks.clear()
    listTasks()
    captured = capsys.readouterr()
    assert "There are no tasks currently" in captured.out



def test_deleteTask_valid(monkeypatch, capsys):
    tasks.clear()
    tasks.extend(["Buy groceries", "Walk the dog"])
    listTasks()
    inputs = iter(["1"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    deleteTask()
    captured = capsys.readouterr()
    assert "Task 'Buy groceries' has been removed" in captured.out
    assert tasks == ["Walk the dog"]

def test_deleteTask_invalid(monkeypatch, capsys):
    tasks.clear()
    tasks.extend(["Buy groceries", "Walk the dog"])
    listTasks()
    inputs = iter(["3"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    deleteTask()
    captured = capsys.readouterr()
    assert "Task number 3 was not found." in captured.out
    assert tasks == ["Buy groceries", "Walk the dog"]

def test_deleteTask_non_numeric(monkeypatch, capsys):
    tasks.clear()
    tasks.extend(["Buy groceries", "Walk the dog"])
    listTasks()
    inputs = iter(["abc"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    deleteTask()
    captured = capsys.readouterr()
    assert "Invalid input" in captured.out
    assert tasks == ["Buy groceries", "Walk the dog"]
