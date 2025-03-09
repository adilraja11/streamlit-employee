import streamlit as st
import pandas as pd
from libs import Employee, Department, OnLeave

# Data Karyawan
data_karyawan = [
    ("Alice Johnson", "Product Manager", 90000, 5000, 5, "Product", "New York"),
    ("Bob Smith", "Frontend Engineer", 85000, 4000, 4, "Engineering", "San Francisco"),
    ("Charlie Brown", "UX Designer", 80000, 3500, 3, "Design", "Boston"),
    ("David Garcia", "Backend Engineer", 95000, 6000, 6, "Engineering", "Seattle"),
    ("Eva Martinez", "Mobile Engineer", 92000, 5500, 4, "Engineering", "Los Angeles"),
    ("Frank Miller", "QA Engineer", 78000, 3000, 5, "Quality Assurance", "Chicago"),
    ("Grace Lee", "Frontend Engineer", 87000, 4500, 2, "Engineering", "Austin"),
    ("Henry Wilson", "UX Designer", 81000, 3700, 4, "Design", "Denver"),
    ("Isabella Davis", "Product Manager", 93000, 5200, 7, "Product", "Miami"),
    ("Jack Thomas", "Backend Engineer", 96000, 6200, 8, "Engineering", "San Jose")
]

# Membuat objek departemen
departments = {
    "Product": Department("Product"),
    "Engineering": Department("Engineering"),
    "Design": Department("Design"),
    "Quality Assurance": Department("Quality Assurance")
}

# Membuat objek Employee dan OnLeave
employees = []
for data in data_karyawan:
    full_name, role, salary, bonus_hire, years_exp, department_name, location = data
    # Membuat objek OnLeave sesuai status
    on_leave = OnLeave(full_name, role)
    
    # Mengaitkan departemen sesuai dengan nama departemen
    department = departments[department_name]
    
    # Membuat objek Employee dan menambahkannya ke dalam daftar
    employee = Employee(full_name, role, salary, bonus_hire, years_exp, department, location)
    employees.append(employee)

st.title("Employee Management System")

for employee in employees:
    st.write(employee)

table_data = st.dataframe(employees)