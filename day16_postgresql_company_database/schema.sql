CREATE TABLE IF NOT EXISTS departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS employees (
    employee_id SERIAL PRIMARY KEY,
    employee_code VARCHAR(20) NOT NULL UNIQUE,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    department_id INTEGER NOT NULL,
    job_title VARCHAR(100) NOT NULL,
    salary NUMERIC(12, 2) NOT NULL CHECK (salary >= 0),
    hire_date DATE NOT NULL,
    manager_id INTEGER,

    CONSTRAINT fk_employee_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id),

    CONSTRAINT fk_employee_manager
        FOREIGN KEY (manager_id)
        REFERENCES employees(employee_id)
);

CREATE TABLE IF NOT EXISTS projects (
    project_id SERIAL PRIMARY KEY,
    project_name VARCHAR(150) NOT NULL,
    department_id INTEGER NOT NULL,
    budget NUMERIC(14, 2) NOT NULL CHECK (budget >= 0),
    start_date DATE NOT NULL,

    CONSTRAINT fk_project_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

CREATE TABLE IF NOT EXISTS employee_projects (
    employee_id INTEGER NOT NULL,
    project_id INTEGER NOT NULL,
    assigned_at DATE NOT NULL DEFAULT CURRENT_DATE,
    role VARCHAR(100),

    PRIMARY KEY (employee_id, project_id),

    CONSTRAINT fk_assignment_employee
        FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_assignment_project
        FOREIGN KEY (project_id)
        REFERENCES projects(project_id)
        ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_employees_department
ON employees(department_id);

CREATE INDEX IF NOT EXISTS idx_employees_email
ON employees(email);

CREATE INDEX IF NOT EXISTS idx_projects_department
ON projects(department_id);

CREATE INDEX IF NOT EXISTS idx_employee_projects_employee
ON employee_projects(employee_id);

CREATE INDEX IF NOT EXISTS idx_employee_projects_project
ON employee_projects(project_id);