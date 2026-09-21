INSERT INTO departments (department_name)
VALUES
    ('IT'),
    ('Finance'),
    ('Human Resources'),
    ('Operations'),
    ('Marketing')
ON CONFLICT (department_name) DO NOTHING;


INSERT INTO employees
(
    employee_code,
    full_name,
    email,
    department_id,
    job_title,
    salary,
    hire_date
)
VALUES
(
    'EMP001',
    'Ali Khan',
    'ali.khan@company.com',
    (SELECT department_id FROM departments WHERE department_name = 'IT'),
    'Junior Python Developer',
    65000,
    '2026-01-15'
),
(
    'EMP002',
    'Sara Ahmed',
    'sara.ahmed@company.com',
    (SELECT department_id FROM departments WHERE department_name = 'Finance'),
    'Financial Analyst',
    85000,
    '2025-11-10'
),
(
    'EMP003',
    'Usman Shah',
    'usman.shah@company.com',
    (SELECT department_id FROM departments WHERE department_name = 'IT'),
    'Database Administrator',
    120000,
    '2024-06-20'
),
(
    'EMP004',
    'Ayesha Malik',
    'ayesha.malik@company.com',
    (SELECT department_id FROM departments WHERE department_name = 'Human Resources'),
    'HR Specialist',
    75000,
    '2025-02-01'
),
(
    'EMP005',
    'Hamza Ahmed',
    'hamza.ahmed@company.com',
    (SELECT department_id FROM departments WHERE department_name = 'Operations'),
    'Operations Engineer',
    95000,
    '2024-09-12'
)
ON CONFLICT (employee_code) DO NOTHING;


INSERT INTO projects
(
    project_name,
    department_id,
    budget,
    start_date
)
VALUES
(
    'Internal Automation Platform',
    (SELECT department_id FROM departments WHERE department_name = 'IT'),
    2500000,
    '2026-01-01'
),
(
    'Financial Reporting System',
    (SELECT department_id FROM departments WHERE department_name = 'Finance'),
    1500000,
    '2026-02-15'
),
(
    'HR Portal',
    (SELECT department_id FROM departments WHERE department_name = 'Human Resources'),
    1000000,
    '2026-03-01'
);