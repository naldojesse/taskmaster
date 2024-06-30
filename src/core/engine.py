# taskmaster_ai/src/core/engine.py

import logging
from typing import Dict, Any

class Task:
    def __init__(self, task_id: str, task_type: str, input_data: Dict[str, Any], parameters: Dict[str, Any]):
        self.task_id = task_id
        self.task_type = task_type
        self.input_data = input_data
        self.parameters = parameters

class TaskResult:
    def __init__(self, task_id: str, result: Any, metadata: Dict[str, Any]):
        self.task_id = task_id
        self.result = result
        self.metadata = metadata

class CoreEngine:
    def __init__(self):
        self.logger = logging.getLogger('CoreEngine')
        self.agent_registry = {}

    def register_agent(self, agent_type: str, agent):
        self.agent_registry[agent_type] = agent

    def process_task(self, task: Task) -> TaskResult:
        try:
            agent = self.agent_registry.get(task.task_type)
            if not agent:
                raise ValueError(f"No agent registered for task type: {task.task_type}")
            
            result = agent.process_task(task)
            return TaskResult(task.task_id, result, {"task_type": task.task_type})
        except Exception as e:
            self.logger.error(f"Error processing task {task.task_id}: {str(e)}")
            return TaskResult(task.task_id, None, {"error": str(e)})

    def handle_error(self, error: Exception, context: Dict[str, Any]):
        self.logger.error(f"Error: {str(error)}, Context: {context}")
        # Implement more sophisticated error handling here