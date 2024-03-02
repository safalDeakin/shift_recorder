
class Shift:
    def __init__(self, id, start_time, date, role):
        self.id = id
        self.start_time = start_time
        self.date = date
        self.role = role
        self.end_time = ""
    id:int
    start_time:str
    end_time:int
    date:str
    role:str
    