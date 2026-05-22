from loadable import Loadable

class Meeting(Loadable):
    def __init__(self):
        self.kind = self.get_name()
        self.attendance_mode = "Online"
        self.start_date = ""
        self.end_date = ""
    
    @classmethod
    def get_name(cls):
        return cls.__name__