# Architecture Decision Records (ADR)

## Table of Contents - Architectural Decision Records (ADR) 

- [Architecture Decision Records (ADR)](#architecture-decision-records-adr)
  - [Table of Contents - Architectural Decision Records (ADR)](#table-of-contents---architectural-decision-records-adr)
  - [1. Introduction](#1-introduction)
  - [2. ADR-001: Backend Framework](#2-adr-001-backend-framework)
  - [3. ADR-002: Database Management System](#3-adr-002-database-management-system)
  - [4. ADR-003: Message Queue](#4-adr-003-message-queue)
  - [5. ADR-004:  Agent Capability Representation](#5-adr-004--agent-capability-representation)
  - [6. ADR-005: API Authentication and Authorization](#6-adr-005-api-authentication-and-authorization)
  - [7. ADR-006: User Interface Design](#7-adr-006-user-interface-design)
  - [8. ADR-007: Memory Purging Strategy](#8-adr-007-memory-purging-strategy)
  - [9.  ADR-008: Deployment Architecture](#9--adr-008-deployment-architecture)
  - [10.  ADR-009:  Workflow Orchestration Approach](#10--adr-009--workflow-orchestration-approach)
  - [11. Conclusion](#11-conclusion)

## 1. Introduction

This document records the key architectural decisions made during the development of TaskMaster AI. Each decision includes the context, decision, and rationale to provide a clear understanding of why certain choices were made. These decisions serve as a reference point for ongoing development, helping ensure transparency and consistency in future design choices.  By documenting design decisions and rationales, ADRs provide a shared understanding of the system's architecture and prevent conflicting or contradictory decisions as the project progresses.

## 2. ADR-001: Backend Framework

- **Context**: We need a backend framework to handle core logic, API requests, and user interactions.
- **Options:**
    - **Flask:** A lightweight and flexible micro-framework that offers a simple and beginner-friendly way to build web applications. 
    - **FastAPI:** A modern, high-performance framework designed for building APIs with automatic data validation, interactive documentation, and asynchronous capabilities.  
- **Decision:** Use Flask.
- **Rationale:**  Flask was chosen due to its simplicity, ease of use, and extensive community support.  As a solo developer with limited coding experience, Flask's gentler learning curve and abundant resources are valuable. While FastAPI offers impressive performance and features, it might be more complex to implement for the initial release. 

## 3. ADR-002: Database Management System

- **Context**:  We need a database management system for persistent storage of tasks, agent memory, and system configurations.
- **Options:**
    - **SQLite:**  A lightweight, serverless, and embedded database that is suitable for small projects and resource-constrained environments.  
    - **Redis:** An in-memory data store that offers very fast read and write operations, making it excellent for caching and managing short-term memory. 
    - **MongoDB:**  A document-oriented NoSQL database known for its flexibility, scalability, and support for large datasets. 
    - **Neo4j:**  A graph database that is designed for storing and querying data with complex relationships, making it a good choice for knowledge graphs or applications that require advanced reasoning capabilities.
- **Decision:** Use SQLite initially.
- **Rationale:**  SQLite was chosen for its simplicity and ease of use for initial development, given the project's resource constraints. It will be used for long-term memory and system configuration storage. The other options will be considered as the system scales and requires more advanced features or greater performance.  
    - **Redis:**  Considered if high performance and in-memory data storage become essential, especially for caching and managing short-term memory. 
    - **MongoDB:**  Considered if you need to handle larger datasets or more flexible data structures (documents) in the future.
    - **Neo4j:**  Considered if you plan to implement knowledge graph-based features in the future (e.g., for advanced agent reasoning). 

## 4. ADR-003: Message Queue

- **Context:**  We may need a message queue to facilitate asynchronous communication between system components, potentially for long-running tasks or when handling concurrency issues. 
- **Options:**
    - **RabbitMQ:** A mature and robust message broker that supports a variety of messaging patterns and provides persistence, making it reliable for mission-critical applications. 
    - **ZeroMQ:**  A lightweight and high-performance messaging library that offers flexibility and direct control over messaging patterns but requires a deeper understanding of networking and messaging concepts. 
- **Decision:** Use ZeroMQ for initial development.
- **Rationale:**  ZeroMQ was chosen due to its high performance, lightweight design, and ease of integration with Python. As the project is initially small and the need for complex messaging patterns is less critical, ZeroMQ's simplicity and speed are advantageous. RabbitMQ will be considered for future development if more complex messaging features or robust message persistence are required. 
    - **RabbitMQ:**  Considered if the project requires more complex messaging features or robust message persistence. 

## 5. ADR-004:  Agent Capability Representation

- **Context:** We need a method to represent and manage the capabilities of agents in a way that allows for effective task matching and agent selection. 
- **Options:**
    - **Simple Text List:**  Store capabilities as a simple comma-separated list. 
    - **Structured Dictionary:**  Use a dictionary to map capability names to proficiency levels or other metadata. 
- **Decision:** Use a structured dictionary.
- **Rationale:** A structured dictionary provides a more flexible and extensible approach to representing agent capabilities. It allows for assigning proficiency levels, adding additional metadata (e.g., timestamps, sources), and easily expanding the capabilities as new agent types are introduced.  A simple text list would be less flexible and more difficult to manage.  
    - **Simple Text List:**  This approach would be less flexible, more difficult to manage, and could make it challenging to represent additional metadata.

## 6. ADR-005: API Authentication and Authorization

- **Context:**  We need a secure authentication and authorization mechanism to protect the API from unauthorized access and prevent malicious use.
- **Options:**
    - **Basic API Keys:**  A simple and straightforward method using API keys that are generated and distributed to users.
    - **JWT (JSON Web Tokens):** A more robust and standardized authentication method that uses tokens to verify user identity and permissions.
    - **OAuth 2.0:**  A widely used protocol for delegated authentication and authorization, suitable for integrating with third-party services. 
- **Decision:**  Use basic API keys for initial development.
- **Rationale:**  Basic API keys are a simple and practical solution for the initial version of the project, given its resource constraints and scope.  JWT or OAuth 2.0 will be considered for future development stages when more robust authentication and authorization are needed.

## 7. ADR-006: User Interface Design

- **Context:**  The system will initially use a command-line interface (CLI). We need to design a future web-based UI that provides a user-friendly and consistent experience across both interfaces.
- **Options:**
    - **Focus on CLI:**  Prioritize the CLI and develop the web UI as a later enhancement.
    - **Parallel Development:**  Design and develop the CLI and web UI in parallel, ensuring a consistent user experience. 
- **Decision:**  Focus on CLI initially, with web UI development deferred until resources allow.
- **Rationale:**  Given the limited time and resources, the CLI will be the priority, allowing for quicker validation and testing.  The web UI will be developed as a future enhancement, leveraging the existing CLI design and functionality. 
    - **Web UI Development:** The web UI will be developed in a way that leverages the existing CLI design and functionality.  This includes mapping CLI commands to equivalent actions in the web UI to ensure a consistent user experience for those familiar with the CLI and facilitate a smooth transition.

## 8. ADR-007: Memory Purging Strategy

- **Context:**  We need to manage the growth of long-term memory by removing outdated, irrelevant, or low-value data. 
- **Options:**
    - **Time-Based Purging:**  Automatically remove data older than a certain threshold.
    - **Relevance-Based Purging:**  Use algorithms to assess the relevance of stored data based on current tasks and goals. 
    - **Usage-Based Purging:**  Purge data based on its frequency of access.
- **Decision:**  Implement a time-based purging mechanism for the initial release.
- **Rationale:**  Time-based purging is the simplest and most straightforward approach to manage memory growth.  More sophisticated purging strategies, like relevance-based or usage-based approaches, will be considered for future development as the system becomes more complex.  
    - **Limitations:** Time-based purging can lead to the removal of relevant data if the time threshold is too short.  Relevance-based or usage-based approaches could be explored in future development to address these limitations. 

## 9.  ADR-008: Deployment Architecture

- **Context:** We need to determine the deployment architecture for TaskMaster AI, considering scalability, cost, and ease of management.
- **Options:**
    - **Local Deployment:**  Deploy the system on the developer's local machine.
    - **Cloud Deployment:** Deploy the system on a cloud platform (e.g., AWS, Azure, GCP). 
- **Decision:**  Deploy on the developer's local machine initially.
- **Rationale:**  Local deployment is the most cost-effective and straightforward approach for initial development and testing.  Cloud deployment will be considered as the system scales and requires more robust infrastructure.  

## 10.  ADR-009:  Workflow Orchestration Approach

- **Context:**  We need to determine the approach for managing task dependencies and workflow execution. 
- **Options:**
    - **Simple Queue:**  Use a simple task queue and manage dependencies explicitly. 
    - **Directed Acyclic Graph (DAG):**  Represent workflows as DAGs to define task dependencies and execution order.
    - **Workflow Management Libraries:**  Leverage dedicated workflow management libraries (e.g., Apache Airflow, Prefect) to simplify workflow orchestration. 
- **Decision:** Use DAGs implemented with the `networkx` library for initial development.
- **Rationale:**  Using DAGs provides a clear and flexible way to represent workflows and dependencies, while the `networkx` library offers a straightforward and efficient approach for DAG implementation in Python.  More advanced workflow management libraries (e.g., Apache Airflow) will be considered in the future if the system requires complex workflows or extensive orchestration capabilities.

## 11. Conclusion

This document captures the key architectural decisions made during the development of TaskMaster AI.  By documenting these choices, we aim to ensure transparency, consistency, and a clear understanding of the system's design for future development and maintenance.  These decisions will guide the project's evolution, balancing the need for immediate functionality with the potential for future enhancements and scalability. 