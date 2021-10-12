from OOP.Project.table.table import Table


class Outside_table(Table):
    def __init__(self, table_number, capacity):
        super().__init__(table_number, capacity)

        if 51 <= self.table_number <= 100:
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")



