from sqlite3 import connect


class Employee:

    def __init__(self, emp_id, emp_name, email, hire_date, job_id, salary, dept_id):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.email = email
        self.hire_date = hire_date
        self.job_id = job_id
        self.salary = salary
        self.dept_id = dept_id

    def __repr__(self):
        return self.emp_name

    def __str__(self):
        return self.emp_name

    @staticmethod
    def get_all_emps():
        db_path = "C://sqlite//db//hr.db"
        with connect(db_path) as conn:
            cur = conn.cursor()
            sql = "select employee_id, last_name, email, hire_date, job_id, salary, department_id from Employees"
            result = cur.execute(sql).fetchall()
            result = [Employee(*row) for row in result]

            return result

    def delete_emp(self):
        db_path = "C://sqlite//db//hr.db"
        with connect(db_path) as conn:
            cur = conn.cursor()
            sql = " delete from Employees where employee_id = :emp_id "
            cur.execute(sql, self.__dict__)
            conn.commit()


    def save_to_db(self):
        db_path = "C://sqlite//db//hr.db"
        with connect(db_path) as conn:
            cur = conn.cursor()
            sql = " insert into  Employees (employee_id, last_name, email, hire_date, job_id, salary, department_id) values (:emp_id, :emp_name, :email, :hire_date, :job_id, :salary, :dept_id)"
            cur.execute(sql,self.__dict__)
            conn.commit()