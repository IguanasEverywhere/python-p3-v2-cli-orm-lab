from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")


def find_employee_by_id():
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    if employee:
        print(employee)
    else:
        print(f'Employee {id_} not found')


def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id = int(input("Enter the employee's department id: "))
    try:
        new_employee = Employee.create(name, job_title, department_id)
        print (f"Success: {new_employee}")
    except Exception as exc:
        print(f"Error creating employee: {exc}")


def update_employee():
    id_ = input("Enter the employee's id: ")
    employee_to_update = Employee.find_by_id(id_)
    if employee_to_update:
        try:
            new_name = input("Enter the employee's new name: ")
            new_job_title = input("Enter the employee's new job title: ")
            new_department_id = int(input("Enter the employee's new department id: "))
            employee_to_update.name = new_name
            employee_to_update.job_title = new_job_title
            employee_to_update.department_id = new_department_id
            Employee.update(employee_to_update)
            print(f"Success: {employee_to_update}")
        except Exception as exc:
            print(f"Error updating employee: {exc}")
    else:
        print(f"Employee {id_} cannot be found")


def delete_employee():
    id_ = input("Enter the employee's id: ")
    employee_to_delete = Employee.find_by_id(id_)
    if employee_to_delete:
        employee_to_delete.delete()
        print(f"Employee {id_} deleted")
    else:
        print(f"Employee {id_} not found")


def list_department_employees():
    dept_id = input("Enter the department's id: ")
    found_dept = Department.find_by_id(dept_id)
    if found_dept:
        dept_employees = found_dept.employees()
        for employee in dept_employees:
            print(employee)
    else:
        print(f"Department {dept_id} not found")