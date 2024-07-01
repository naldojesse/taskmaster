# taskmaster_ai/tests/test_memory_manager.py

import pytest
from taskmaster.memory.memory_manager import MemoryManager

@pytest.fixture
def memory_manager():
    return MemoryManager(':memory:')  # Use in-memory SQLite database for testing

def test_store_and_retrieve_data(memory_manager):
    key = "test_key"
    data = {"value": "test_value"}
    
    assert memory_manager.store_data(key, data)
    retrieved_data = memory_manager.get_data(key)
    assert retrieved_data == data

def test_update_data(memory_manager):
    key = "test_key"
    initial_data = {"value": "initial_value"}
    updated_data = {"value": "updated_value"}
    
    assert memory_manager.store_data(key, initial_data)
    assert memory_manager.store_data(key, updated_data)
    
    retrieved_data = memory_manager.get_data(key)
    assert retrieved_data == updated_data

def test_clear_data(memory_manager):
    key = "test_key"
    data = {"value": "test_value"}
    
    assert memory_manager.store_data(key, data)
    assert memory_manager.clear_data(key)
    assert memory_manager.get_data(key) is None

def test_clear_all_data(memory_manager):
    key1 = "test_key1"
    key2 = "test_key2"
    data1 = {"value": "test_value1"}
    data2 = {"value": "test_value2"}
    
    assert memory_manager.store_data(key1, data1)
    assert memory_manager.store_data(key2, data2)
    
    assert memory_manager.clear_all_data()
    assert memory_manager.get_data(key1) is None
    assert memory_manager.get_data(key2) is None

def test_nonexistent_key(memory_manager):
    assert memory_manager.get_data("nonexistent_key") is None