import psycopg2


class DataBase:
    employees = ['']

    def get_db(self):
        conn = psycopg2.connect(dbname='peventreader', user='postgres', password='hDWFNt2c', host='localhost',
                                port='40005')

        cur = conn.cursor()
        select = f'SELECT * FROM pku WHERE ' \
                 f'dev = 20 AND unittype = 3 ' \
                 f'ORDER BY id DESC'
        cur.execute(select)
        full_fetch = cur.fetchall()
        cur.close()
        conn.close()
        return full_fetch

    def get_employees_list(self):
        db = self.get_db()
        for record in db:
            if record[10] not in self.employees:
                self.employees.append(record[10])
        return self.employees






