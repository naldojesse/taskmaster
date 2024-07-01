# taskmaster_ai/tests/test_orchestrator.py

import pytest
from src.core.engine import CoreEngine, Task
from src.orchestrator.orchestrator import Orchestrator
from src.models import TaskResult  # Changed import

@pytest.fixture
def core_engine():
    return CoreEngine()

@pytest.fixture
def orchestrator(core_engine):
    return Orchestrator(core_engine)

def test_create_workflow(orchestrator):
    tasks = [
        Task("1", "summarization", {"text": "Text 1"}, {}),
        Task("2", "sentiment_analysis", {"text": "Text 2"}, {}),
        Task("3", "named_entity_recognition", {"text": "Text 3"}, {})
    ]
    dependencies = {
        "2": ["1"],
        "3": ["1", "2"]
    }
    
    assert orchestrator.create_workflow("workflow1", tasks, dependencies)

def test_execute_workflow(core_engine, orchestrator):
    tasks = [
        Task("1", "summarization", {"text": "Text 1"}, {}),
        Task("2", "sentiment_analysis", {"text": "Text 2"}, {}),
        Task("3", "named_entity_recognition", {"text": "Text 3"}, {})
    ]
    dependencies = {
        "2": ["1"],
        "3": ["1", "2"]
    }
    
    orchestrator.create_workflow("workflow1", tasks, dependencies)
    results = orchestrator.execute_workflow("workflow1")
    
    assert len(results) == 3
    assert all(isinstance(result, TaskResult) for result in results.values())

def test_get_workflow_status(core_engine, orchestrator):
    tasks = [
        Task("1", "summarization", {"text": "Text 1"}, {}),
        Task("2", "sentiment_analysis", {"text": "Text 2"}, {}),
        Task("3", "named_entity_recognition", {"text": "Text 3"}, {})
    ]
    dependencies = {
        "2": ["1"],
        "3": ["1", "2"]
    }
    
    orchestrator.create_workflow("workflow1", tasks, dependencies)
    orchestrator.execute_workflow("workflow1")
    status = orchestrator.get_workflow_status("workflow1")
    
    assert status["workflow_id"] == "workflow1"
    assert status["total_tasks"] == 3
    assert status["completed_tasks"] == 3
    assert status["pending_tasks"] == 0
    assert status["is_complete"] == True

def test_nonexistent_workflow(orchestrator):
    with pytest.raises(ValueError):
        orchestrator.execute_workflow("nonexistent_workflow")
    
    with pytest.raises(ValueError):
        orchestrator.get_workflow_status("nonexistent_workflow")
