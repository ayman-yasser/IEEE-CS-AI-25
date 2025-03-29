# Employee Database - README

## Overview
This file, **EmployeeDatabase.xlsx**, contains structured employee data designed for efficient management and reporting. It helps organize and analyze employee information, making it useful for HR tasks and decision-making.

## File Format
- **File Type:** Excel Spreadsheet (.xlsx)
- **Sheets:** Includes a primary sheet named "Employee Records"

## Data Fields
The file includes the following key details for each employee:
- **Employee ID**: A unique number assigned to each employee.
- **Name**: The full name of the employee.
- **Department**: The team or division the employee belongs to (HR, IT, Finance, Sales, Marketing).
- **Job Title**: The employee's official role.
- **Date of Joining**: The start date of employment (should not be in the future).
- **Salary**: The employee’s pay, which should always be a positive number.
- **Email**: A properly formatted email address (e.g., example@example.com).
- **Phone Number**: A valid contact number.
- **Status**: Indicates whether the employee is "Active" or "Inactive."

## Key Features
### Data Entry & Organization
- Contains at least 50 employee records.
- Uses clear formatting, including bold headers and optimized column widths.

### Data Accuracy & Validation
- Drop-down menus for **Department** and **Job Title** fields to maintain consistency.
- Salary field accepts only positive numeric values.
- Email addresses must follow a standard format.
- The **Date of Joining** cannot be set in the future.
- Employee **Status** is limited to "Active" or "Inactive."

### Sorting & Filtering
- Employees can be **sorted** based on **Department** and **Date of Joining** to arrange records in a meaningful way.
- A **filtering** option is available to display employees hired after a specified year, making it easier to analyze recent hires or specific time frames.

### Functions & Lookups
- **IF statements** are used to categorize employees based on salary:
  - If **Salary > $5000**, the employee is classified as **"Senior"**.
  - Otherwise, the employee is classified as **"Junior"**.
- **VLOOKUP** is implemented to fetch department-specific information from a separate sheet, ensuring consistency and reducing manual entry errors.

### Visual Indicators
- Employees earning below $3,000 are highlighted in red.
- Employees who joined within the last six months are highlighted in green.

### Summarization & Analysis
- A **summary report** provides an overview of employee distribution across departments.
- Data is **grouped by the year of joining** to track hiring patterns over time.



