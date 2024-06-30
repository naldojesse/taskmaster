# taskmaster_ai/tests/test_nlp_agent.py

import pytest
import logging

# Configure logging to print to stdout for the test
logging.basicConfig(level=logging.DEBUG)

from src.agents.nlp_agent import NLPAgent
from src.core.engine import Task

@pytest.fixture
def nlp_agent():
    return NLPAgent()

def test_summarization(nlp_agent):
    task = Task("1", "summarization", {"text": "This is a long text that needs to be summarized."}, {"operation": "summarization"})
    result = nlp_agent.process_task(task)
    print(f"Summarization result: {result}")  # Keep this line for debugging
    assert "summary" in result
    expected_summary = "Summary: This is a long text that needs to be summarized...."
    assert result["summary"] == expected_summary

def test_sentiment_analysis(nlp_agent):
    task = Task("2", "sentiment_analysis", {"operation": "sentiment_analysis"}, {"text": "I love this product!"})
    result = nlp_agent.process_task(task)
    assert "sentiment" in result
    assert "confidence" in result
    assert result["sentiment"] in ["positive", "negative", "neutral"]
    assert 0 <= result["confidence"] <= 1

def test_named_entity_recognition(nlp_agent):
    task = Task("3", "named_entity_recognition", {"operation": "named_entity_recognition"}, {"text": "John Doe works at OpenAI."})
    result = nlp_agent.process_task(task)
    assert "entities" in result
    assert len(result["entities"]) > 0
    assert "type" in result["entities"][0]
    assert "text" in result["entities"][0]

def test_unsupported_task_type(nlp_agent):
    task = Task("4", "unsupported_task", {"operation": "unsupported_task"}, {"text": "This task type is not supported."})
    result = nlp_agent.process_task(task)
    assert "error" in result
    assert "Unsupported task type" in result["error"]