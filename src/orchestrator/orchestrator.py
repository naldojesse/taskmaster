# taskmaster_ai/src/orchestrator/orchestrator.py

import logging
from typing import Dict, Any, List
from src.models import Task, TaskResult
import networkx as nx

class Workflow:
    def __init__(self, workflow_id: str, tasks: List[Task], dependencies: Dict[str, List[str]]):
        self.workflow_id = workflow_id
        self.tasks = tasks
        self.dependencies = dependencies

class Orchestrator:
    def __init__(self, core_engine):
        self.logger = logging.getLogger('Orchestrator')
        self.core_engine = core_engine
        self.workflows = {}

    def create_workflow(self, workflow_id: str, tasks: List[Task], dependencies: Dict[str, List[str]]) -> bool:
        try:
            workflow = Workflow(workflow_id, tasks, dependencies)
            self.workflows[workflow_id] = workflow
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
            # Here, you'd typically dispatch the task to the appropriate agent
            # For now, we'll just create a dummy result and mark the task as completed
            results[task.task_id] = TaskResult(task.task_id, "Completed", {"dummy": "result"})
            task.status = "Completed"  # Add this line to mark the task as completed
        
        return results

    def _create_dependency_graph(self, workflow: Workflow) -> nx.DiGraph:
        graph = nx.DiGraph()
        for task in workflow.tasks:
            graph.add_node(task.task_id)
        for task_id, dependencies in workflow.dependencies.items():
            for dep in dependencies:
                graph.add_edge(dep, task_id)
        return graph

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
