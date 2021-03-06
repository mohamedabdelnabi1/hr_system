from sqlite3 import connect


class Department:

    def __init__(self, dept_id, dept_name, loc_id):
        self.dept_id = dept_id
        self.dept_name = dept_name
        self.loc_id = loc_id

    def __str__(self):
        return self.dept_name

    def __repr__(self):
        return self.dept_name


    @staticmethod
    def get_all_deps():

        db_path = "C://sqlite//db//hr.db"
        with connect(db_path) as conn:
            cur = conn.cursor()
            sql = "select * from departments"
            result = cur.execute(sql).fetchall()
            result = [Department(*row) for row in result]

            return result

    def save_to_db(self):
        db_path = "C://sqlite//db//hr.db"
        with connect(db_path) as conn:
            cur = conn.cursor()
            sql = " insert into  departments values (:dept_id, :dept_name, :loc_id)"
            cur.execute(sql,self.__dict__)
            conn.commit()

    def delete_from_db(self):
        db_path = "C://sqlite//db//hr.db"
        with connect(db_path) as conn:
            cur = conn.cursor()
            sql = " delete from departments where department_id = :dept_id "
            cur.execute(sql, self.__dict__)
            conn.commit()




