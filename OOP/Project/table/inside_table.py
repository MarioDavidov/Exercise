from OOP.Project.table.table import Table


class Inside_table(Table):
    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

        if 1 >= self.table_number <= 50:
            raise ValueError("Inside table's number must be between 1 and 50 inclusive!")

