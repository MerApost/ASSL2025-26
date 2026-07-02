# Software Analysis & Design: Individual Project
This repository contains my individual project work for the **Analysis and Design of Software Systems** course at the **Department of Informatics and Telecommunications, National and Kapodistrian University of Athens (NKUA)**.

The project was developed during the **Spring Semester 2025** and focuses on software analysis, requirements modeling, UML diagrams, structured analysis and basic implementation/testing.
 
## Student Information
* Name: **Meropi**
* Surname: **Apostolaki**
* Academic ID number: **1115-2022-00008**
* Email: sdi2200008@di.uoa.gr

## Project Theme

The project is based on modeling the **human body as an organization/system**, using concepts from software analysis and design.

The goal was to represent biological systems and their interactions through software engineering models, such as UML diagrams, data flow diagrams and basic object-oriented code.

## Subprojects delivered on time:
- [x] Sub01
- [x] Sub02
- [x] Sub03
- [x] Sub04
- [x] Sub05
- [x] Sub06

## Subprojects Overview

### Sub01 – Use Case Diagram

In this subproject, I created a **Use Case Diagram** representing the human body as a system/organization.

The diagram includes:

- System boundary
- Actors interacting with the system
- Main use cases
- Associations between actors and use cases
- Include, extend and generalization relationships

This task helped me understand how to identify system actors, define system functionality and represent user-system interactions at a high level.

### Sub02 – Class Diagram

In this subproject, I created a **Class Diagram** that models the human body and its main systems using object-oriented design principles.

The diagram includes:

- The human body as a main class
- Several human body systems as classes
- Attributes and methods
- Abstract class
- Enumeration
- Static attribute
- Relationships such as association, aggregation, composition, dependency and inheritance

This task helped me practice object-oriented analysis and understand how real-world entities can be translated into software classes and relationships.

### Sub03 – Sequence Diagram

In this subproject, I created a **Sequence Diagram** representing the interactions that take place during the breathing process.

The diagram includes:

- Multiple objects/lifelines
- Synchronous messages
- Asynchronous message
- Combined fragment

This task helped me understand how to model dynamic system behavior and the order of interactions between objects over time.

### Sub04 – Statechart Diagram

In this subproject, I created a **Statechart Diagram** based on a class from the previous Class Diagram.

The diagram focuses on the different states of an instance and includes:

- States
- Transitions
- Triggers
- Guards
- Activities

This task helped me understand how to describe the lifecycle and behavior of an object depending on events and conditions.

### Sub05 – Data Flow Diagram

In this subproject, I created a **Level-1 Data Flow Diagram (DFD)** for a selected subsystem.

The diagram includes:

- Processes
- External entity
- Data store
- Data flows

This task helped me practice structured analysis and understand how data moves through a system.

### Sub06 – Python Implementation & Unit Testing

In this subproject, I implemented one class from the Class Diagram using **Python** and created unit tests for it.

The subproject includes:

- A Python class implementation
- At least one attribute and one method
- Unit testing using `pytest`
- A GitHub Actions workflow for automated testing
- A `requirements.txt` file for dependencies

This task helped me connect software design with actual implementation and basic testing practices.

## Resources
## Specifications:
* **[The human body (Britannica)](https://www.britannica.com/science/human-body)**


## Guidelines
* [https://en.wikipedia.org/wiki/Software_requirements](https://en.wikipedia.org/wiki/Software_requirements) (introduction to software requirements)
* [https://en.wikipedia.org/wiki/Software_design](https://en.wikipedia.org/wiki/Software_design) (instroduction to software design)
* [https://en.wikipedia.org/wiki/Systems_development_life_cycle](https://en.wikipedia.org/wiki/Systems_development_life_cycle) (introduction to software development cycle)
* [https://en.wikipedia.org/wiki/Unified_Modeling_Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language) (introduction to UML)
* [https://en.wikipedia.org/wiki/Object-oriented_analysis_and_design](https://en.wikipedia.org/wiki/Object-oriented_analysis_and_design) (object oriented analysis and design)
* [https://en.wikipedia.org/wiki/Use_case_diagram](https://en.wikipedia.org/wiki/Use_case_diagram) (for use case diagrams)
* [https://en.wikipedia.org/wiki/Use_case_diagram](https://en.wikipedia.org/wiki/Use_case_diagram) (for class diagrams)
* [https://www.geeksforgeeks.org/unified-modeling-language-uml-class-diagrams/](https://www.geeksforgeeks.org/unified-modeling-language-uml-class-diagrams/) (for class diagrams)
* [https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/) (for class diagrams)
* [https://developer.ibm.com/articles/the-class-diagram/](https://developer.ibm.com/articles/the-class-diagram/) (for class diagrams)

## Repository Structure

```text
ASSL2025-26/
│
├── Sub01/              # Use Case Diagram
├── Sub02/              # Class Diagram
├── Sub03/              # Sequence Diagram
├── Sub04/              # Statechart Diagram
├── Sub05/              # Data Flow Diagram
├── Sub06/              # Python implementation and unit tests
│
├── requirements.txt    # Python testing dependencies
└── README.md           # Project overview
