# taskmaster_ai/src/orchestrator/orchestrator.py

import logging
from typing import Dict, Any, List
from taskmaster.models import Task, TaskResult
from taskmaster.memory.memory_manager import MemoryManager
import networkx as nx

class Workflow:
    def __init__(self, workflow_id: str, tasks: List[Task], dependencies: Dict[str, List[str]]):
        self.workflow_id = workflow_id
        self.tasks = tasks
        self.dependencies = dependencies

    def to_dict(self):
        return {
            "workflow_id": self.workflow_id,
            "tasks": [task.to_dict() for task in self.tasks],
            "dependencies": self.dependencies
        }

    @classmethod
    def from_dict(cls, data):
        tasks = [Task.from_dict(task_data) for task_data in data["tasks"]]
        return cls(data["workflow_id"], tasks, data["dependencies"])

class Task:
    def __init__(self, task_id: str, task_type: str, input_data: Dict[str, Any], parameters: Dict[str, Any]):
        self.task_id = task_id
        self.task_type = task_type
        self.input_data = input_data
        self.parameters = parameters
        self.status = "Created"

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "task_type": self.task_type,
            "input_data": self.input_data,
            "parameters": self.parameters,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data["task_id"], data["task_type"], data["input_data"], data["parameters"])
        task.status = data.get("status", "Created")
        return task

class Orchestrator:
    def __init__(self, core_engine):
        self.logger = logging.getLogger('Orchestrator')
        self.core_engine = core_engine
        self.memory_manager = MemoryManager(db_path='orchestrator.db')
        self.workflows = self._load_workflows()

    def _load_workflows(self):
        workflows_data = self.memory_manager.get_data('workflows')
        if not workflows_data:
            return {}
        return {workflow_id: Workflow.from_dict(data) for workflow_id, data in workflows_data.items()}

    def _save_workflows(self):
        workflows_data = {workflow_id: workflow.to_dict() for workflow_id, workflow in self.workflows.items()}
        self.memory_manager.store_data('workflows', workflows_data)

    def create_workflow(self, workflow_id: str, tasks: List[Task], dependencies: Dict[str, List[str]]) -> bool:
        try:
            workflow = Workflow(workflow_id, tasks, dependencies)
            self.workflows[workflow_id] = workflow
            self._save_workflows()
            self.logger.debug(f"Workflow {workflow_id} created successfully with tasks: {tasks} and dependencies: {dependencies}")
            return True
        except Exception as e:
            self.logger.error(f"Error creating workflow {workflow_id}: {str(e)}")
            return False

    def execute_workflow(self, workflow_id: str) -> Dict[str, TaskResult]:
        if workflow_id not in self.workflows:
            raise ValueError(f"Workflow {workflow_id} not found")
        
        workflow = self.workflows[workflow_id]
        results = {}
        
        for task in workflow.tasks:
            results[task.task_id] = TaskResult(task.task_id, "Completed", {"dummy": "result"})
            task.status = "Completed"
        
        self._save_workflows()
        return results

    def get_workflow_status(self, workflow_id: str) -> Dict[str, Any]:
        if workflow_id not in self.workflows:
            raise ValueError(f"Workflow {workflow_id} not found")
        
        workflow = self.workflows[workflow_id]
        total_tasks = len(workflow.tasks)
        completed_tasks = sum(1 for task in workflow.tasks if task.status == "Completed")
        pending_tasks = total_tasks - completed_tasks
        
        return {
            "workflow_id": workflow_id,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "is_complete": pending_tasks == 0
        }

    def _create_dependency_graph(self, workflow: Workflow) -> nx.DiGraph:
        graph = nx.DiGraph()
        for task in workflow.tasks:
            graph.add_node(task.task_id)
        for task_id, dependencies in workflow.dependencies.items():
            for dep in dependencies:
                graph.add_edge(dep, task_id)
        return graph