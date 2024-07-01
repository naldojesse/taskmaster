# taskmaster/cli/cli.py

import sys
import os
import argparse
import json
from taskmaster.core.engine import CoreEngine
from taskmaster.models import Task

class CLI:
    def __init__(self):
        self.core_engine = CoreEngine()
        self.parser = self.create_parser()

    def create_parser(self):
        parser = argparse.ArgumentParser(description="TaskMaster AI CLI")
        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        # Create workflow command
        create_parser = subparsers.add_parser("create", help="Create a new workflow")
        create_parser.add_argument("workflow_id", type=str, help="Unique identifier for the workflow")
        create_parser.add_argument("tasks", type=str, help="JSON string representing the list of tasks")
        create_parser.add_argument("dependencies", type=str, help="JSON string representing task dependencies")

        # Execute workflow command
        execute_parser = subparsers.add_parser("execute", help="Execute a workflow")
        execute_parser.add_argument("workflow_id", type=str, help="Identifier of the workflow to execute")

        # Get workflow status command
        status_parser = subparsers.add_parser("status", help="Get the status of a workflow")
        status_parser.add_argument("workflow_id", type=str, help="Identifier of the workflow to check")

        return parser

    def run(self):
        args = self.parser.parse_args()

        if args.command == "create":
            self.create_workflow(args)
        elif args.command == "execute":
            self.execute_workflow(args)
        elif args.command == "status":
            self.get_workflow_status(args)
        else:
            print("Invalid command. Use -h for help.")

    def create_workflow(self, args):
        try:
            tasks = self.validate_tasks(args.tasks)
            dependencies = self.validate_dependencies(args.dependencies)

            task_objects = [Task(t["id"], t["type"], t["input_data"], t["parameters"]) for t in tasks]
            
            success = self.core_engine.orchestrator.create_workflow(args.workflow_id, task_objects, dependencies)
            
            if success:
                print(f"Workflow '{args.workflow_id}' created successfully.")
            else:
                print(f"Failed to create workflow '{args.workflow_id}'.")
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error creating workflow: {str(e)}")

    def execute_workflow(self, args):
        try:
            results = self.core_engine.orchestrator.execute_workflow(args.workflow_id)
            print(f"Workflow '{args.workflow_id}' execution results:")
            for task_id, result in results.items():
                print(f"Task {task_id}: {result.result}")
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error executing workflow: {str(e)}")

    def get_workflow_status(self, args):
        try:
            status = self.core_engine.orchestrator.get_workflow_status(args.workflow_id)
            print(f"Workflow '{args.workflow_id}' status:")
            for key, value in status.items():
                print(f"{key}: {value}")
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error getting workflow status: {str(e)}")

    def validate_tasks(self, tasks_json):
        try:
            tasks = json.loads(tasks_json)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format for tasks.")

        if not isinstance(tasks, list):
            raise ValueError("Tasks must be a list of dictionaries.")

        for task in tasks:
            if not isinstance(task, dict):
                raise ValueError("Each task must be a dictionary.")
            required_keys = {"id", "type", "input_data", "parameters"}
            if not all(key in task for key in required_keys):
                raise ValueError(f"Task is missing required keys. Required: {required_keys}")

        return tasks

    def validate_dependencies(self, dependencies_json):
        try:
            dependencies = json.loads(dependencies_json)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format for dependencies.")

        if not isinstance(dependencies, dict):
            raise ValueError("Dependencies must be a dictionary.")

        for key, value in dependencies.items():
            if not isinstance(value, list):
                raise ValueError(f"Dependencies for task {key} must be a list.")

        return dependencies

def main():
    cli = CLI()
    cli.run()
