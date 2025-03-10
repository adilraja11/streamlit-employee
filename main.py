import streamlit as st
import pandas as pd
import time
from libs import Employee

def create_dummy_data():
    dummy_employees = [
        ("Alice Johnson", "Product Manager", "Product", 90000),
        ("Bob Smith", "Frontend Engineer", "Engineering", 85000),
        ("Charlie Brown", "UX Designer", "Design", 80000),
        ("David Garcia", "Backend Engineer", "Engineering", 95000),
        ("Eva Martinez", "Mobile Engineer", "Engineering", 92000),
        ("Frank Miller", "QA Engineer", "Quality Assurance", 78000),
        ("Grace Lee", "Frontend Engineer", "Engineering", 87000),
        ("Henry Wilson", "UX Designer", "Design", 81000),
        ("Isabella Davis", "Product Manager", "Product", 93000),
        ("Jack Thomas", "Backend Engineer", "Engineering", 96000),
    ]
    return dummy_employees

st.title("Employee Management System")

if "employee" not in st.session_state:
    # Create the dummy data for initial setup
    employees_data = create_dummy_data()
    employee_list = []

    for data in employees_data:
        full_name, role, department, salary = data
        new_employee = Employee(full_name, role, department, salary)
        employee_data = {
            "ID": new_employee.id,
            "Full Name": new_employee.full_name,
            "Role": new_employee.role,
            "Department": new_employee.department,
            "Salary": new_employee.salary,
            "On Leave": "On Leave" if new_employee.on_leave else "Active"
        }
        employee_list.append(employee_data)

    # Create DataFrame and store it in session_state
    st.session_state.employee = pd.DataFrame(employee_list)

page = st.sidebar.selectbox("Menu", ["Add Employee", "View Employee"])


if page == "Add Employee":
    st.write("### Add Employee")
    full_name = st.text_input("Full Name")
    role = st.selectbox("Role", ["Product Manager", "Frontend Engineer", "UX Engineer", "QA Engineer", "Backend Engineer", "Mobile Engineer", "UX Designer"], index=None)
    department = st.selectbox("Department", ["Product", "Engineering", "Design", "Quality Assurance"], index=None)
    salary = st.number_input("Salary", min_value=0, step=5000)

    submit_btn = st.button("Add Employee")

    if submit_btn:
        if not full_name or not role or not department or salary <= 0:
            st.toast("Please fill in all fields!", icon="❌")
            time.sleep(1)

            st.rerun()
        else:
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
        
        st.toast("Employee added successfully!", icon="✅")
        time.sleep(1)
        
        st.rerun()

elif page == "View Employee":
    st.write("### Employees Master Data")
    st.dataframe(st.session_state.employee)

    st.write("### Request Leave")
    employee_names = st.session_state.employee['Full Name'].tolist()
    selected_employee_name = st.selectbox("Select Employee", employee_names, index=None)
    
    if selected_employee_name:
        # Tombol untuk melakukan leave
        go_on_leave_btn = st.button("Go On Leave")
        return_from_leave_btn = st.button("Return From Leave")

        if go_on_leave_btn:
            st.session_state.employee.loc[st.session_state.employee['Full Name'] == selected_employee_name, 'On Leave'] = "On Leave"
            st.success(f"{selected_employee_name} is now on leave.")
            time.sleep(1)
            st.rerun()
        
        if return_from_leave_btn:
            st.session_state.employee.loc[st.session_state.employee['Full Name'] == selected_employee_name, 'On Leave'] = "Active"
            st.success(f"{selected_employee_name} has returned from leave.")
            time.sleep(1)
            st.rerun()

