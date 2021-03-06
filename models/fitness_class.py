class FitnessClass:
    def __init__(self, class_type, date, time, duration, instructor, capacity, location, id = None):
        self.class_type = class_type
        self.date = date
        self.time = time
        self.duration = duration
        self.instructor = instructor
        self.capacity = capacity
        self.location = location
        self.id = id

    def formatted_date(self):
        return self.date.strftime("%d/%m/%Y")

    def formatted_time(self):
        return self.time.strftime("%H:%M") 