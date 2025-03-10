import streamlit as st
import pandas as pd
from libs import Employee

st.title("Employee Management System")

if "employee" not in st.session_state:
    st.session_state.employee = pd.DataFrame(columns=["ID", "Full Name", "Role", "Department", "Salary", "On Leave"])

st.write("### Add Employee")
full_name = st.text_input("Full Name")
role = st.selectbox("Role", ["Product Manager", "Frontend Engineer", "UX Engineer", "QA Engineer", "Backend Engineer", "Mobile Engineer", "UX Designer"], index=None)
department = st.selectbox("Department", ["Product", "Engineering", "Design", "Quality Assurance"], index=None)
salary = st.number_input("Salary", min_value=0, step=5000)

submit_btn = st.button("Add Employee")

st.write("### Employee List")
st.dataframe(st.session_state.employee)

if submit_btn:
    new_employee = Employee(full_name, role, department, salary)

    new_employee_data = {
        "ID": new_employee.id,
        "Full Name": new_employee.full_name,
        "Role": new_employee.role,
        "Department": new_employee.department,
        "Salary": new_employee.salary,
        "On Leave": "On Leave" if new_employee.on_leave else "Active"
    }

    new_employee_df = pd.DataFrame([new_employee_data])
    st.session_state.employee = pd.concat([st.session_state.employee, new_employee_df], ignore_index=True)
    
    st.rerun()
