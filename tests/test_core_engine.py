# taskmaster_ai/tests/test_core_engine.py

import pytest
from src.core.engine import CoreEngine, Task, TaskResult

class MockAgent:
    def process_task(self, task):
        return f"Processed task: {task.task_id}"

def test_core_engine_task_processing():
    engine = CoreEngine()
    engine.register_agent("mock", MockAgent())

    task = Task("1", "mock", {"data": "test"}, {})
    result = engine.process_task(task)

    assert isinstance(result, TaskResult)
    assert result.task_id == "1"
    assert result.result == "Processed task: 1"
    assert result.metadata == {"task_type": "mock"}

def test_core_engine_unknown_agent():
    engine = CoreEngine()

    task = Task("2", "unknown", {"data": "test"}, {})
    result = engine.process_task(task)

    assert isinstance(result, TaskResult)
    assert result.task_id == "2"
    assert result.result is None
    assert "error" in result.metadata