# taskmaster_ai/src/orchestrator/orchestrator.py

import logging
from typing import Dict, Any, List
from src.core.engine import Task, TaskResult
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
        try:
            workflow = self.workflows.get(workflow_id)
            if not workflow:
                raise ValueError(f"Workflow {workflow_id} not found")

            graph = self._create_dependency_graph(workflow)
            execution_order = list(nx.topological_sort(graph))
            results = {}

            for task_id in execution_order:
                task = next(task for task in workflow.tasks if task.task_id == task_id)
                task_result = self.core_engine.process_task(task)
                results[task_id] = task_result

            return results
        except Exception as e:
            self.logger.error(f"Error executing workflow {workflow_id}: {str(e)}")
            return {}

    def _create_dependency_graph(self, workflow: Workflow) -> nx.DiGraph:
        graph = nx.DiGraph()
        for task in workflow.tasks:
            graph.add_node(task.task_id)
        for task_id, dependencies in workflow.dependencies.items():
            for dep in dependencies:
                graph.add_edge(dep, task_id)
        return graph

    def get_workflow_status(self, workflow_id: str) -> Dict[str, Any]:
        workflow = self.workflows.get(workflow_id)
        if not workflow:
            return {"error": f"Workflow {workflow_id} not found"}

        graph = self._create_dependency_graph(workflow)
        completed_tasks = set()
        pending_tasks = set(graph.nodes())
        
        for task in workflow.tasks:
            if self.core_engine.memory_manager.get_data(task.task_id):
                completed_tasks.add(task.task_id)
                pending_tasks.remove(task.task_id)

        return {
            "workflow_id": workflow_id,
            "total_tasks": len(workflow.tasks),
            "completed_tasks": len(completed_tasks),
            "pending_tasks": len(pending_tasks),
            "is_complete": len(pending_tasks) == 0
        }