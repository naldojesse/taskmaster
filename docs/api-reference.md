# API Reference

## Introduction
Welcome to the TaskMaster AI API reference. This document provides detailed information about the available API endpoints, request/response formats, and examples to help you integrate with TaskMaster AI.

## Base URL
The base URL for all API requests is:
```
https://your-domain.com/api/v1
```
**Note:** Replace `https://your-domain.com` with your actual domain.

## Authentication
All API requests require an API key for authentication. Include the API key in the `Authorization` header:
```
Authorization: Bearer YOUR_API_KEY
```
**Note:** Replace `YOUR_API_KEY` with your actual API key.

## Endpoints

### Tasks

#### Create a Task
- **Endpoint:** `/tasks`
- **Method:** `POST`
- **Description:** Creates a new task.
- **Request Body:**
```json
{
  "description": "Task description",
  "agent_type": "nlp" // or "technical"
  // Other task-specific parameters
}
```
- **Response:**
```json
{
  "task_id": "generated_task_id",
  "status": "created"
}
```

#### Retrieve Tasks
- **Endpoint:** `/tasks`
- **Method:** `GET`
- **Description:** Retrieves a list of tasks or a specific task by ID.
- **Request Parameters:**
  - `task_id` (optional): The ID of the task to retrieve.
- **Response:**
  - If `task_id` is provided:
  ```json
  {
    "task_id": "task_id_1",
    "description": "Task 1 description",
    "agent_assigned": "nlp",
    "status": "in_progress"
    // Other task details
  }
  ```
  - Otherwise:
  ```json
  [
    {
      "task_id": "task_id_1",
      "description": "Task 1 description",
      "agent_assigned": "nlp",
      "status": "in_progress"
      // Other task details
    },
    // ... more tasks
  ]
  ```

#### Update a Task
- **Endpoint:** `/tasks/{task_id}`
- **Method:** `PUT`
- **Description:** Updates an existing task.
- **Request Body:**
```json
{
  "description": "Updated task description",
  "status": "completed"
  // Other updatable fields
}
```
- **Response:**
```json
{
  "task_id": "task_id_1",
  "status": "updated"
}
```

#### Delete a Task
- **Endpoint:** `/tasks/{task_id}`
- **Method:** `DELETE`
- **Description:** Deletes a task.
- **Response:**
```json
{
  "task_id": "task_id_1",
  "status": "deleted"
}
```

### Agents

#### Retrieve Agents
- **Endpoint:** `/agents`
- **Method:** `GET`
- **Description:** Retrieves information about available agents and their capabilities.
- **Response:**
```json
[
  {
    "agent_id": "nlp_agent",
    "type": "nlp",
    "capabilities": ["summarization", "information_extraction", "response_generation"],
    "status": "available"
  },
  {
    "agent_id": "technical_agent",
    "type": "technical",
    "capabilities": ["code_generation", "debugging", "documentation"],
    "status": "available"
  }
]
```

### Memory

#### Retrieve Memory Data
- **Endpoint:** `/memory`
- **Method:** `GET`
- **Description:** Retrieves long-term memory data. Access is restricted based on user roles and permissions.
- **Response:**
```json
{
  "memory_records": [
    {
      "record_id": "record_id_1",
      "agent_id": "nlp_agent",
      "task_id": "task_id_1",
      "data": "Stored data",
      "timestamp": "2023-10-01T12:00:00Z"
    },
    // ... more records
  ]
}
```

### Orchestrator

#### Manage Workflows
- **Endpoint:** `/orchestrator`
- **Method:** `POST`
- **Description:** Manages workflows and task dependencies. Admin access only.
- **Request Body:**
```json
{
  "workflow_name": "New Workflow",
  "tasks": [
    {
      "task_id": "task_id_1",
      "dependencies": ["task_id_2"]
    },
    // ... more tasks
  ]
}
```
- **Response:**
```json
{
  "workflow_id": "workflow_id_1",
  "status": "created"
}
```

## Error Handling
Standardized error responses are returned in JSON format, including HTTP status codes and descriptive error messages.

### Error Response Format
```json
{
  "status": 400,
  "error": "Bad Request",
  "message": "Invalid input data.",
  "code": "INVALID_INPUT",
  "details": {
    "field": "username",
    "issue": "Username is required"
  }
}
```

## Examples

### Example: Create a Task
**Request:**
```bash
curl -X POST https://your-domain.com/api/v1/tasks \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "description": "Summarize the meeting notes",
    "agent_type": "nlp"
  }'
```
**Note:** Replace `https://your-domain.com` with your actual domain and `YOUR_API_KEY` with your actual API key.

**Response:**
```json
{
  "task_id": "generated_task_id",
  "status": "created"
}
```

### Example: Retrieve All Tasks
**Request:**
```bash
curl -X GET https://your-domain.com/api/v1/tasks \
  -H "Authorization: Bearer YOUR_API_KEY"
```
**Note:** Replace `https://your-domain.com` with your actual domain and `YOUR_API_KEY` with your actual API key.

**Response:**
```json
[
  {
    "task_id": "task_id_1",
    "description": "Summarize the meeting notes",
    "agent_assigned": "nlp",
    "status": "in_progress"
  },
  // ... more tasks
]
```

## Conclusion
This API reference provides the necessary details to interact with the TaskMaster AI system. For further assistance, please refer to the [User Guide](user-guide.md) or contact our support team.
