#!/usr/bin/env python3
from models.__init__ import CONN, CURSOR

class Owner:
    def __init__(self, name, age, experience=0, id=None):
        self.id = id
        self.name = name
        self.age = age
        self.experience = experience

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age
        else:
            raise TypeError('Age must be an integer')

    def __repr__(self):
        return f'<Owner name={self.name} >'

    def save(self):
        sql = """
            INSERT INTO owners(name, age, experience)
            VALUES (?,?,?)
        """
        CURSOR.execute(sql, (self.name, self.age, self.experience))
        CONN.commit()

        self.id = CURSOR.lastrowid

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS owners(
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                experience INTEGER
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS owners;"
        CURSOR.execute(sql)
        CONN.commit()
       
    @classmethod
    def create(cls, name, age, experience):
        new_owner = cls(name=name, age=age, experience=experience)
        new_owner.save()
        return new_owner

    @classmethod
    def create_instance(cls, row):
        return cls(name=row[1], experience=row[3], age=row[2],id=row[0])

    @classmethod
    def all(cls):
        sql = "SELECT * FROM owners;"
        owner_rows = CURSOR.execute(sql).fetchall()
        return [cls.create_instance(row) for row in owner_rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM owners
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return cls.create_instance(row)
        else:
            return None