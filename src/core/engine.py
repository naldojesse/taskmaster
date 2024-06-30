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

class AgentFactory:
    @staticmethod
    def create_agent(agent_type: str):
        if agent_type in ["nlp", "summarization", "sentiment_analysis", "named_entity_recognition"]:
            from src.agents.nlp_agent import NLPAgent
            return NLPAgent()
        elif agent_type == "technical":
            from src.agents.technical_agent import TechnicalAgent
            return TechnicalAgent()
        else:
            raise ValueError(f"Unsupported agent type: {agent_type}")

class CoreEngine:
    def __init__(self):
        self.logger = logging.getLogger('CoreEngine')
        self.agent_registry = {}

    def register_agent(self, agent_type: str):
        if agent_type not in self.agent_registry:
            self.agent_registry[agent_type] = AgentFactory.create_agent(agent_type)

    def process_task(self, task: Task) -> TaskResult:
        try:
            if task.task_type not in self.agent_registry:
                self.register_agent(task.task_type)

            agent = self.agent_registry[task.task_type]
            result = agent.process_task(task)
            return TaskResult(task.task_id, result, {"task_type": task.task_type})
        except Exception as e:
            self.logger.error(f"Error processing task {task.task_id}: {str(e)}")
            return TaskResult(task.task_id, None, {"error": str(e)})

    def handle_error(self, error: Exception, context: Dict[str, Any]):
        self.logger.error(f"Error: {str(error)}, Context: {context}")
        # Implement more sophisticated error handling here