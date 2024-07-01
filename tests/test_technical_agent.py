# taskmaster_ai/tests/test_technical_agent.py

import pytest
from taskmaster.agents.technical_agent import TechnicalAgent
from taskmaster.core.engine import Task

@pytest.fixture
def technical_agent():
    return TechnicalAgent()

def test_code_generation(technical_agent):
    task = Task("1", "code_generation", {"requirements": "Create a function to calculate factorial"}, {"language": "python"})
    result = technical_agent.process_task(task)
    assert "code" in result
    assert "language" in result
    assert result["language"] == "python"
    assert "def main():" in result["code"]
    assert "# TODO: Implement Create a function to calculate factorial" in result["code"]

def test_code_review(technical_agent):
    task = Task("2", "code_review", {"code": "def add(a,b):\n    return a+b"}, {"language": "python"})
    result = technical_agent.process_task(task)
    assert "review_comments" in result
    assert "language" in result
    assert result["language"] == "python"
    assert len(result["review_comments"]) > 0
    assert "line" in result["review_comments"][0]
    assert "comment" in result["review_comments"][0]

def test_bug_identification(technical_agent):
    task = Task("3", "bug_identification", {"code": "def divide(a, b):\n    return a / b"}, {"language": "python"})
    result = technical_agent.process_task(task)
    assert "bugs" in result
    assert "language" in result
    assert result["language"] == "python"
    assert len(result["bugs"]) > 0
    assert "line" in result["bugs"][0]
    assert "description" in result["bugs"][0]

def test_unsupported_task_type(technical_agent):
    task = Task("4", "unsupported_task", {"code": "print('Hello, World!')"}, {"language": "python"})
    result = technical_agent.process_task(task)
    assert "error" in result
    assert "Unsupported task type" in result["error"]