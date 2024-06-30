# Requirements Specification Document: TaskMaster AI

## Metadata

**Title:** TaskMaster AI - Requirements Specification Document
**Author:** Jesse Naldo
**Co-Authors:** GPT4o, Perplexity AI, Gemini 1.5 Pro
**Date:** 2024-06-28
**Version:** 1.6

## Table of Contents

- [Requirements Specification Document: TaskMaster AI](#requirements-specification-document-taskmaster-ai)
  - [Metadata](#metadata)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Project Objective](#project-objective)
    - [Development Constraints](#development-constraints)
    - [Potential Benefits](#potential-benefits)
    - [Stakeholders](#stakeholders)
    - [Success Metrics](#success-metrics)
  - [2. Project Overview](#2-project-overview)
    - [2.1. Project Title](#21-project-title)
    - [2.2. Project Goal](#22-project-goal)
    - [2.3.  Key Features:](#23--key-features)
    - [2.4. Feature Prioritization](#24-feature-prioritization)
  - [3. Scope](#3-scope)
    - [3.1. In-Scope](#31-in-scope)
    - [3.2. Out-of-Scope](#32-out-of-scope)
  - [4. Functional Requirements](#4-functional-requirements)
    - [4.1. User Roles](#41-user-roles)
    - [4.2.  Human-AI Collaboration](#42--human-ai-collaboration)
    - [4.3.  Modularity](#43--modularity)
    - [4.4.  Advanced Agentic Concepts](#44--advanced-agentic-concepts)
    - [4.5. State Machines and Orchestration](#45-state-machines-and-orchestration)
    - [4.6.  Memory Management](#46--memory-management)
    - [4.7. Planning and Reflection *(Deferred)*](#47-planning-and-reflection-deferred)
    - [4.8. Explainability and Evaluation *(Deferred)*](#48-explainability-and-evaluation-deferred)
    - [4.9. Robust Testing Framework](#49-robust-testing-framework)
    - [4.10.  Documentation](#410--documentation)
  - [5.  Non-Functional Requirements](#5--non-functional-requirements)
    - [5.1. Performance](#51-performance)
    - [5.2. Reliability](#52-reliability)
    - [5.3. Usability](#53-usability)
    - [5.4. Scalability](#54-scalability)
    - [5.5.  Security](#55--security)
  - [6. System Architecture](#6-system-architecture)
  - [7. User Interface Requirements](#7-user-interface-requirements)
  - [8. Dependencies](#8-dependencies)
    - [8.1. External Systems](#81-external-systems)
    - [8.2. Libraries \& Frameworks](#82-libraries--frameworks)
  - [9. Testing \& Validation](#9-testing--validation)
  - [10. Maintenance \& Support](#10-maintenance--support)
    - [10.1. Maintenance Plan](#101-maintenance-plan)
    - [10.2. Support Protocols](#102-support-protocols)
  - [11. Risks \& Mitigation](#11-risks--mitigation)
  - [12. Success Evaluation](#12-success-evaluation)
  - [13. Documentation](#13-documentation)

## Introduction 

### Project Objective

The primary objective of **TaskMaster AI** is to develop a functional, modular, and maintainable agent framework designed to integrate AI functionalities with human-AI collaboration. The project aims to create a system that assists users in automating tasks, streamlining workflows, and enhancing productivity. 

The long-term vision for TaskMaster AI is to incorporate a wide range of features inspired by popular agentic frameworks, progressively enhancing the system's capabilities and creating a powerful and versatile platform for intelligent task automation.

### Development Constraints

This project is being developed by a solo developer with the following constraints:

* **Limited Coding Experience:** The developer has limited coding experience and is actively working on improving skills. This necessitates a focus on clear explanations, gradual skill development, and breaking down complex tasks into manageable steps.
* **Minimal Financial Resources:** The project relies primarily on open-source AI models, free APIs, and cost-effective tools. Expensive LLM API calls will be minimized during testing, prioritizing unit tests, smaller datasets, and mocking techniques.
* **Limited Time and Energy:** The developer has a busy schedule with college, part-time work, mental health challenges, networking, and a coding bootcamp. Development time will be limited, requiring a focus on essential features and achievable milestones. 

### Potential Benefits

- **Enhanced Coding Skills:** The project provides hands-on experience for improving programming skills, particularly in AI and software development.
- **Showcase Project for Recruiters:** TaskMaster AI serves as a strong portfolio piece to demonstrate technical abilities and initiative to potential employers. 
- **Foundation for Future AI Projects:**  The framework can serve as a foundation for future AI projects, allowing for integration and expansion as skills and resources grow.

### Stakeholders

- **Primary Stakeholder:**  [Your Name], acting as the developer, maintainer, and primary user of TaskMaster AI.
- **Potential Stakeholders:**  This includes future employers, technical recruiters, collaborators, and interested members of the open-source community. 

### Success Metrics

TaskMaster AI's success will be measured by the following criteria, adapted to reflect the project's constraints:

* **Functionality:**
    - **Core Features:** The initial release must successfully implement the core "Must Have" features, providing a functional agent framework capable of task automation and basic workflow management. 
    - **Advanced Features:**  Progress on "Should Have" and "Could Have" features will be evaluated based on the number of features implemented and their level of functionality, given the development constraints. 
* **Performance:**
    - The system achieves acceptable response times for common user interactions, with optimization efforts focused within the constraints of available resources.
* **Usability:** 
    - The user interface, designed for simplicity, allows users to easily interact with the system and understand its core functionality.
* **Reliability:** 
    - The system operates with a reasonable level of stability and has basic error handling to prevent critical failures.
* **Scalability (Future Goal):** 
    - While scalability is a long-term aspiration, the initial development prioritizes a modular design that allows for future scaling as resources and time permit. 

## 2. Project Overview

### 2.1. Project Title 

TaskMaster AI

### 2.2. Project Goal

To develop a functional, modular AI agent framework that integrates with human-AI collaboration for task automation and workflow optimization. The initial development will focus on a set of essential features (Must Have), with plans for future expansion to incorporate advanced capabilities inspired by popular agentic frameworks, as time and resources permit. 

### 2.3.  Key Features:

| Feature                       | Category  | Description                                                                                                                  | 
| ----------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Human-AI Collaboration        | **Must Have** |  Seamless integration with human oversight, enabling task assignment, real-time feedback, and agent behavior adjustment.       |
| Modularity                   | **Must Have** |  System architecture based on distinct, reusable modules (agents, memory, planning, orchestration) for maintainability and extensibility. |
| NLP Agent                    | **Must Have** |  Specializes in NLP tasks like text summarization, information extraction, and response generation using open-source or free models. |
| Technical Agent             | **Must Have**  |  Assists with coding tasks including code generation, debugging, and documentation creation, using readily available tools and APIs. |
| Basic Memory Management      | **Must Have**  |  Implements basic short-term and long-term information storage and retrieval for agents.  |
| Basic Orchestration           | **Must Have**  |  Develops a mechanism to manage task dependencies, sequencing, and parallel execution of agent actions. |
| Data Processing Agent       | **Should Have** |  Focuses on data processing tasks: cleaning, transformation, analysis, visualization, and report generation.  *Development deferred due to time constraints.* |
| Creative Agent              | **Should Have** |  Handles creative tasks such as generating diverse text formats, translating languages, writing creative content, and answering questions informatively. *Development deferred due to time constraints.* |
| Advanced Memory Management   | **Should Have** |  Enhances the memory system with sophisticated storage and retrieval, potentially using vector databases or knowledge graphs.  *Development deferred due to time constraints.*  |
| Advanced Planning & Reflection    | **Should Have** |  Develops components for goal planning, task decomposition, performance analysis, self-evaluation, and adaptive learning, drawing inspiration from AutoGen, Crew AI, Lumos, and AgentOS. *Development deferred due to time constraints.* | 
| Tool Use and Integration     | **Should Have** |  Agents can leverage external tools (e.g., web scraping, APIs) to enhance their capabilities, as seen in AutoGen, Crew AI, and Lumos. *Development deferred due to time constraints.* |
| Code Execution                | **Should Have** |  Enables agents to execute code snippets in a secure environment (e.g., Docker) for tasks involving data processing or complex computations, as demonstrated in AutoGen, Crew AI, and Lumos.  *Development deferred due to time constraints.* |
| Human Proxy Agent           | **Should Have** |  Allows for seamless human feedback and intervention at various stages of task execution, inspired by AutoGen and Crew AI.  *Development deferred due to time constraints.* | 
| Teachable Agents              | **Should Have** |  Agents can learn and adapt based on user feedback and past experiences, potentially using reinforcement learning, inspired by AutoGen. *Development deferred due to time constraints.* | 
| AgentEval Framework          | **Could Have** |  Integrates a framework to evaluate the performance and effectiveness of LLM-powered agents, inspired by AutoGen and Lumos. *Development deferred due to time constraints.*  | 
| LifeOS Manager Agent          | **Could Have** |  Integrates with the Notion API, acting as a virtual assistant within Notion. Manages tasks, projects, and schedules in Notion.  *Development deferred due to time constraints.* |
| Comprehensive Explainability & Evaluation | **Could Have** | Implements tools for transparent agent decision-making and comprehensive performance evaluation metrics. *Development deferred due to time constraints.*  | 

### 2.4. Feature Prioritization

We will use the MoSCoW method for prioritization:

- **Must Have:** Essential for initial release. These features will be the primary focus during development.
- **Should Have:** Important, but not critical for the MVP. Development will be deferred due to time constraints. 
- **Could Have:**  Desirable, considered for future development if time and resources allow. 
- **Won't Have:** Explicitly excluded. 

## 3. Scope

### 3.1. In-Scope

- Designing, developing, testing, documenting, and initially deploying a functional, basic version of TaskMaster AI that fulfills the "Must Have" features, acknowledging all development constraints. 
- Implementing the core agent framework (Core Engine, API Gateway, NLP Agent, Technical Agent).
- Developing a basic command-line interface for human-AI interaction. A simple web-based UI may be considered if time permits.
- Creating a testing framework focused on essential unit and integration tests, with cost-effective strategies to minimize LLM API usage.
- Generating clear and concise documentation for core functionalities.

### 3.2. Out-of-Scope

- **Training Large Language Models (LLMs):** Excluded due to resource demands. Will utilize pre-trained models. 
- **Integration with Social Media APIs:** Excluded due to rate limits, privacy concerns, and API instability.
- **Advanced Features:**  "Should Have" and "Could Have" features are outside the initial scope and will be considered in potential future development stages if time and resources become available. 

## 4. Functional Requirements 

### 4.1. User Roles

* **Administrator:**  Full system access; manages users, configures agents, monitors performance, and accesses logs. 
* **Standard User:** Can create and manage tasks, interact with agents, provide feedback, and view results.  

### 4.2.  Human-AI Collaboration

* **Task Assignment:** The system enables users to assign tasks to specific agents through a command-line interface.
    - **Example:** User assigns the task "Summarize the key points from this meeting transcript." to the NLP agent.
* **Real-Time Feedback:** The system provides basic progress updates to the user as agents execute tasks.
* **Agent Adjustment:** Users can provide feedback during task execution, allowing agents to adapt behavior or output within their limitations. 

### 4.3.  Modularity

* **Discrete Modules:** System architecture uses separate modules for:
    - Agent Modules:  Logic for specific agent types (e.g., NLP, Technical).
    - Memory Management: Handles information storage and retrieval.
    - *Planning & Reflection (Deferred):*  Goal setting, task breakdown, and self-assessment will be considered for future development.
    - Orchestration: Coordinates agent actions, task dependencies, and workflows.
* **Plug-and-Play Functionality:**  New modules can be added or removed without disrupting core functionality.

### 4.4.  Advanced Agentic Concepts

* **NLP Agent:**
    - **Text Summarization:**  Summarizes text, extracting key information, utilizing open-source or free models.
    - **Information Extraction:** Extracts entities, relationships, and facts from unstructured text using available resources.
    - **Response Generation:**  Generates text responses based on input and context, leveraging free or cost-effective models. 
* **Technical Agent:**
    - **Code Generation:** Generates code snippets in Python based on user requirements, using accessible tools and APIs.
    - **Debugging:**  Assists with debugging by identifying potential errors, leveraging static code analysis and available debugging tools. 
    - **Documentation Creation:** Generates basic code documentation using open-source documentation generation tools.
* **Data Processing Agent *(Deferred):* **
    -  *Development of a specialized agent for data processing tasks will be deferred due to time constraints.*
* **Creative Agent *(Deferred):* **
    - *Development of an agent for creative tasks is deferred due to time constraints.* 
* **LifeOS Manager Agent *(Deferred):* **
    - *Integration with Notion and development of a LifeOS Manager Agent is deferred.*  

### 4.5. State Machines and Orchestration

* **Workflow Management:**  The system utilizes a basic state machine to define and manage simple workflows involving multiple agents and tasks.
* **Task Coordination:**  The system manages basic task dependencies to ensure sequential execution when required. 

### 4.6.  Memory Management

* **Short-Term Memory:**  Stores temporary information relevant to ongoing tasks, using a simple in-memory approach.
* **Long-Term Memory:**  Uses a basic file-based approach for storing data, allowing agents to access past interactions and results.
* **Memory Purging:** A time-based purging mechanism will be implemented to remove outdated memory data and manage storage constraints. 

### 4.7. Planning and Reflection *(Deferred)*

* *Development of advanced planning and reflection capabilities is deferred due to time and resource constraints.*
* **Future Consideration:**  
    - Draw inspiration from AutoGen, Crew AI, Lumos, and AgentOS to implement goal planning, task decomposition, and agent self-reflection. 
    - Investigate hierarchical task networks (HTNs) as a potential approach for breaking down complex tasks. 

### 4.8. Explainability and Evaluation *(Deferred)*

* *Implementation of explainability features and comprehensive evaluation metrics is deferred.*
* **Future Consideration:**
    - Research techniques for generating explanations of agent reasoning, potentially using natural language explanations or visualization tools.
    - Explore the AgentEval framework from AutoGen as a potential approach for agent evaluation. 

### 4.9. Robust Testing Framework

* **Comprehensive Test Suite:** A suite of automated tests will be developed to ensure the functionality of the core system.
* **Testing Levels:**
    - **Unit Testing:** Prioritized to verify individual component behavior, using a framework like Pytest.
    - **Integration Testing:**  Focuses on testing core interactions between modules, with strategies to minimize LLM API costs.
    - **Behavior-Driven Development (BDD):**  May be considered for a limited set of user stories, if time permits. 

### 4.10.  Documentation

* **API Reference:**  Provide concise documentation for any public APIs developed for the core system, including error codes and their meanings.
* **User Guide:** A basic user guide will cover installation and usage of the command-line interface. 
* **Developer Guide:** A developer guide will be created to explain the architecture and code for potential future contributors. 

## 5.  Non-Functional Requirements

### 5.1. Performance

- **Response Time:** The system aims for acceptable response times for common user interactions, given the constraints of the chosen AI models and available hardware. 
- **Throughput:**  The system should handle a reasonable number of requests, recognizing that extensive load testing may be limited due to resource constraints.

### 5.2. Reliability

- **Uptime:**  The system strives for stable operation, but high availability configurations are deferred to later stages.
- **Error Handling:**  The system includes basic error handling, logging, and reporting to prevent critical failures and assist in debugging. 

### 5.3. Usability

- **User Interface:** The command-line interface is designed to be clear and easy to use. A simple web-based UI may be considered if time permits.
- **Documentation:** User and developer documentation will be clear, concise, and focused on essential information. 

### 5.4. Scalability

- **Scalability (Future Goal):** The initial design will be modular, allowing for potential scaling in the future as resources allow. Extensive scalability testing and implementation of advanced scaling techniques are deferred.

### 5.5.  Security

- **Authentication & Authorization:** Basic authentication and authorization measures will be implemented, with a focus on securing the core system. Advanced security features are deferred. 
- **Data Encryption:** Sensitive data will be encrypted where necessary, with a focus on practical and achievable solutions.
- **Input Validation & Sanitization:**  Basic input validation will be implemented to prevent common vulnerabilities. 
- **Security Audits (Future Consideration):**  Formal security audits and penetration testing are deferred to a later stage when the system is more mature.

## 6. System Architecture 

*(Refer to the Software Design Document (SDD) for details.)*

## 7. User Interface Requirements 

*(Refer to the UI/UX Design Specification Document for details, noting that the UI may be limited to a command-line interface for the initial release.)*

## 8. Dependencies

### 8.1. External Systems

- **Notion API *(Deferred):*** Integration with the Notion API is deferred due to time constraints.

### 8.2. Libraries & Frameworks

- **Python (3.8+):** Primary backend language.
- **Flask/FastAPI:**  Backend API and web framework. 
- **Groq API:**  Will be used to access Groq's free tier models, including LLama 3 70B and Mixtral 8x7B. 
- **OpenRouter AI API:**  Will be used to access free models like Toppy.
- **Ollama:** Will be used to run open-source AI models locally on a Macbook Pro with an M1 Pro chip.
- **Puppeteer/Selenium:**  Will be explored for automating web interactions with AI services like Perplexity AI. 
- **Open-Source AI Libraries:**  Will prioritize open-source AI/ML libraries (e.g., scikit-learn, Hugging Face Transformers, spaCy) for additional NLP and Technical agent functionalities. 
- *(TensorFlow/PyTorch (Future Consideration):*  May consider using TensorFlow or PyTorch in later stages if project requirements and resources permit.
- **SQLAlchemy (or other lightweight ORM):** Object-Relational Mapping for database interaction.
- **(React (Future Consideration):** React may be used for the web-based UI if time and resources allow.

## 9. Testing & Validation

*(Refer to the Test Plan Document for details, noting the emphasis on cost-effective testing methods.)*

## 10. Maintenance & Support

### 10.1. Maintenance Plan

- **Updates:** Updates and bug fixes will be prioritized based on severity and available time. 
- **Performance Reviews:**  Periodic performance reviews will be conducted as time allows.
- **Long-Term Support:**  Active support will be provided for a reasonable period, recognizing time limitations. 

### 10.2. Support Protocols

- **Documentation:**  User and developer documentation will be updated as needed.
- **(Community Forum (Future):**  A community forum may be considered if the project gains traction and time permits. 
- **Issue Tracker:** A public issue tracker will be used for reporting bugs, suggesting features, and tracking the progress of issue resolution. 

## 11. Risks & Mitigation

| Risk                                     | Mitigation Strategy                                                                                    |
|---------------------------------------|---------------------------------------------------------------------------------------------------------|
| Limited Development Time and Resources |  Prioritize essential features, use open-source tools, and adopt a flexible and iterative development approach. Regularly reassess priorities based on available time and energy. | 
| Lack of Coding Experience |  Focus on continuous learning, break down complex tasks, leverage available resources (documentation, tutorials, community support), and seek assistance when needed. |
| Mental Health Challenges |  Prioritize well-being, set realistic goals, take breaks, practice self-care, and seek support from mental health professionals when necessary. Adjust project timelines and workload as needed to prevent burnout. | 
| Reliance on Free AI Models and APIs | Carefully evaluate the capabilities and limitations of free AI models. Develop fallback strategies or consider using more robust paid services if free models prove insufficient for certain tasks. | 
| Potential Legal and Ethical Issues (Web Scraping, Licensing) | Thoroughly research and comply with all relevant licensing agreements for open-source AI models. Ensure compliance with data privacy regulations when web scraping. Prioritize ethical data usage and model selection. |  

## 12. Success Evaluation 

Success will be evaluated based on the adjusted metrics in Section 1.4 and the completion of the core "Must Have" features within a reasonable timeframe, given the project constraints.

## 13. Documentation  

*(Refer to the Software Design Document (SDD) for the documentation strategy.)* 

