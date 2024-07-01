# taskmaster_ai/tests/test_core_engine.py

import pytest
from taskmaster.core.engine import CoreEngine, Task, TaskResult

def test_core_engine_task_processing():
    engine = CoreEngine()

    task = Task("1", "summarization", {"text": "This is a test."}, {"operation": "summarization"})
    result = engine.process_task(task)

    assert isinstance(result, TaskResult)
    assert result.task_id == "1"
    assert "summary" in result.result
    assert result.metadata == {"task_type": "summarization"}

def test_core_engine_unknown_agent():
    engine = CoreEngine()

    task = Task("2", "unknown", {"data": "test"}, {})
    result = engine.process_task(task)

    assert isinstance(result, TaskResult)
    assert result.task_id == "2"
    assert result.result is None
    assert "error" in result.metadata
    assert "Unsupported agent type" in result.metadata["error"]