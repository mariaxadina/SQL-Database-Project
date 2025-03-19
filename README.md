# SQL Database 

## Description

The chosen topic for the "Database Fundamentals" course project is the Management System of the Association of Mathematics and Computer Science Students. For such an association, keeping track of volunteers, projects, and sponsors is very important for both current and future ASMI volunteers. Therefore, a well-structured database can play a crucial role in facilitating this management process. With a well-designed database, we will be able to record and track essential information, such as volunteers' personal data, their contributions to different projects, details about completed projects, and maintaining good relationships with sponsors. The project was developed using Oracle SQL Developer. I chose this tool because it is easy to use and provides a rich set of tools for database development as well as data modeling functions.

## Model Rules
### I. VOLUNTEERS – TASKS
A volunteer can take on multiple tasks or none.
A task can have multiple volunteers, either within the same project or across different projects, but at least one (projects cannot proceed if their assigned tasks are not taken by volunteers).
### II. POSITIONS – VOLUNTEERS
A volunteer may hold a leadership position or none (remaining a simple volunteer).
A leadership position can be held by multiple volunteers (the term lasts for one calendar year) or none if ASMI rules have not been followed by the person in charge.
### III. DEPARTMENTS – VOLUNTEERS
A department can have multiple volunteers, but at least one.
A volunteer belongs to only one department where they are active.
### IV. PROJECTS – TASKS
A project consists of multiple tasks, but at least one.
A task belongs to a project or none (e.g., tasks related to organizing interdepartmental outings).
### V. LOCATIONS – PROJECTS
A project can take place at multiple locations, as it is organized annually.
A location can host multiple projects or none.
### VI. SPONSORS – PROJECTS
A sponsor can fund multiple projects, but at least one project must have a sponsor.
A project can have multiple sponsors or none (some projects do not require sponsorship).

## Entity-Relationship Diagram (ERD)

<p><img src="https://github.com/mariaxadina/SQL-Database-Project/blob/main/images/1.png" width="100%"/></p>

##  Conceptual Diagram

<p><img src="https://github.com/mariaxadina/SQL-Database-Project/blob/main/images/2.png" width="100%"/></p>

## Interface

The interface for the database, built with Python and Flask, serves as the bridge between the user and the database, allowing for seamless interaction with the data. Here's a description of the key features:

### Content listing with sorting options (all tables)

<p><img src="https://github.com/mariaxadina/SQL-Database-Project/blob/main/images/3.png" width="100%"/></p>

### Modify and add information(delete option for each record)

<p><img src="https://github.com/mariaxadina/SQL-Database-Project/blob/main/images/5.png" width="100%"/></p>

### Displaying the result of a query that retrieves information from at least 3 tables and filters it using at least 2 conditions

<p><img src="https://github.com/mariaxadina/SQL-Database-Project/blob/main/images/6.png" width="100%"/></p>

