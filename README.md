# Frappe Introduction Topics

## Objective
Understand the Frappe structure, how to create DocTypes, child DocTypes, file structures, and all types of customization and CRUD operations.

## Table of Contents
1. [Overview](#overview)
2. [Steps](#steps)
   - [Step 1: Create a DocType named “Student”](#step-1-create-a-doctype-named-student)
   - [Step 2: Create a DocType named “Program”](#step-2-create-a-doctype-named-program)
   - [Step 3: Create a DocType named “Course”](#step-3-create-a-doctype-named-course)
   - [Step 4: Create a DocType named “Topics”](#step-4-create-a-doctype-named-topics)
   - [Step 5: Create custom CRUD APIs](#step-5-create-custom-crud-apis)
3. [Role Permissions and Restrictions](#role-permissions-and-restrictions)
4. [Contact](#contact)

## Overview
This project aims to provide an introduction to the Frappe framework. It includes creating and customizing DocTypes and implementing CRUD operations.

## Steps

### Step 1: Create a DocType named “Student”
Create a DocType named “Student” with the following fields:
- **First Name**
- **Middle Name**
- **Last Name**
- **Full Name** (read-only, concatenated from First, Middle, and Last Name)
- **Naming Series** (select field with at least 3 series, e.g., `STU-YYYY-MM-DATE-0001`)
- **Create User Button** (creates a user with email and role student)
- **Student Email Address** (with validations)
- **Date of Birth** (with validations)
- **Gender**
- **Nationality**
- **Blood Group** (select field)
- **Link to Default Address** (from CRM Module of ERPNext)
- **HTML Field** (shows combined address from Address DocType)
- **Joining Date** (prefilled with today’s date)
- **Active** (checkbox to indicate if the student is active)

### Step 2: Create a DocType named “Program”
Create a DocType named “Program” with the following fields:
- **Program Name** (Data field)
- **Description** (Text field)
- **Start Date** (Date field)
- **End Date** (Date field)
- **Duration** (Float field, in months)
- **Total Credits** (Float field, sum of all course credits)
- **Status** (Select field: Planned, Ongoing, Completed)
- **Instructor** (Link field to Employee DocType, filtered by Instructor type)
- **Participants** (Table field with Participant subfield linking to Student DocType and a preview button to show participant's profile pic)
- **Courses** (Table field with Course subfield linking to Course DocType)

### Step 3: Create a DocType named “Course”
Create a DocType named “Course” with the following fields:
- **Course Name**
- **Course Code**
- **Credits**
- **Academic Year** (link)
- **Topics** (child table linking to Topics DocType)

### Step 4: Create a DocType named “Topics”
Create a DocType named “Topics” with the following fields:
- **Topic Name**
- **Topic Description**

### Step 5: Create custom CRUD APIs
- Implement custom CRUD APIs for the above DocTypes.
- Include validations ensuring link field values are present.
- Ensure proper error messages and code responses.

## Role Permissions and Restrictions
- Set up role permissions and restrictions for all users, including instructors and students, according to their roles in the system.

## Contact
For any queries or further information, please contact:
- **Name:** Bhargav Jitendra Kasundra
- **Email:** bhargav111.kasundra@gmail.com
- **GitHub:** https://github.com/bhargav051/
