class Teacher:
    def _init(self, firstname, lastname, department, year):
        self.firstname=firstname
        self.lastname=lastname
        self.department=department
        self.year=year

    def _str(self):
        return f"Firstname is: {self.firstname}"\
            f"Lastname is: {self.lastname}"\
                f"Department is: {self.department}"\
                    f"Year is: {self.year}"