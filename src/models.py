from typing import Dict, Any

class Task:
    def __init__(self, task_id: str, task_type: str, input_data: Dict[str, Any], parameters: Dict[str, Any]):
        self.task_id = task_id
        self.task_type = task_type
        self.input_data = input_data
        self.parameters = parameters
        self.status = "Created"  # Added this line

class TaskResult:
    def __init__(self, task_id: str, result: Any, metadata: Dict[str, Any]):
        self.task_id = task_id
        self.result = result
        self.metadata = metadata
