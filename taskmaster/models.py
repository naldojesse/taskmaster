from typing import Dict, Any

class Task:
    def __init__(self, task_id: str, task_type: str, input_data: Dict[str, Any], parameters: Dict[str, Any]):
        self.task_id = task_id
        self.task_type = task_type
        self.input_data = input_data
        self.parameters = parameters
        self.status = "Created"  # Added this line

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "task_type": self.task_type,
            "input_data": self.input_data,
            "parameters": self.parameters,
            "status": self.status  # Ensure status is included in the dictionary
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data["task_id"], data["task_type"], data["input_data"], data["parameters"])
        task.status = data.get("status", "Created")  # Ensure status is set from the dictionary
        return task

class TaskResult:
    def __init__(self, task_id: str, result: Any, metadata: Dict[str, Any]):
        self.task_id = task_id
        self.result = result
        self.metadata = metadata
