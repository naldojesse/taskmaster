# taskmaster/core/engine.py

import logging
from typing import Dict, Any, List
from taskmaster.models import Task, TaskResult
from taskmaster.memory.memory_manager import MemoryManager
from taskmaster.orchestrator.orchestrator import Orchestrator

class AgentFactory:
    @staticmethod
    def create_agent(agent_type: str):
        if agent_type in ["nlp", "summarization", "sentiment_analysis", "named_entity_recognition"]:
            from taskmaster.agents.nlp_agent import NLPAgent
            return NLPAgent()
        elif agent_type == "technical":
            from taskmaster.agents.technical_agent import TechnicalAgent
            return TechnicalAgent()
        else:
            raise ValueError(f"Unsupported agent type: {agent_type}")

class CoreEngine:
    def __init__(self):
        self.logger = logging.getLogger('CoreEngine')
        self.agent_registry = {}
        self.memory_manager = MemoryManager()
        self.orchestrator = Orchestrator(self)

    def register_agent(self, agent_type: str):
        if agent_type not in self.agent_registry:
            self.agent_registry[agent_type] = AgentFactory.create_agent(agent_type)

    def process_task(self, task: Task) -> TaskResult:
        try:
            if task.task_type not in self.agent_registry:
                self.register_agent(task.task_type)

            agent = self.agent_registry[task.task_type]
            
            # Retrieve context from memory
            context = self.memory_manager.get_data(task.task_id) or {}
            
            # Add context to task parameters
            task.parameters['context'] = context
            
            result = agent.process_task(task)
            
            # Store result in memory
            self.memory_manager.store_data(task.task_id, result)
            
            return TaskResult(task.task_id, result, {"task_type": task.task_type})
        except Exception as e:
            self.logger.error(f"Error processing task {task.task_id}: {str(e)}")
            return TaskResult(task.task_id, None, {"error": str(e)})

    def handle_error(self, error: Exception, context: Dict[str, Any]):
        self.logger.error(f"Error: {str(error)}, Context: {context}")
        # Implement more sophisticated error handling here