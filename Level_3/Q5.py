class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(self, other_time):
        """Adds two Time objects and returns the result."""
        total_minutes = (self.hours + other_time.hours) * 60 + (self.minutes + other_time.minutes)
        total_hours = total_minutes // 60
        total_minutes %= 60
        return Time(total_hours, total_minutes)

    def displayTime(self):
        """Displays the time."""
        print(f"{self.hours} hr and {self.minutes} min")

    def displayMinutes(self):
        """Displays the total minutes."""
        return self.hours * 60 + self.minutes

if __name__ == "__main__":
    hours1 = int(input("Enter hours for first time object: "))
    minutes1 = int(input("Enter minutes for first time object: "))
    hours2 = int(input("Enter hours for second time object: "))
    minutes2 = int(input("Enter minutes for second time object: "))

    time1 = Time(hours1, minutes1)
    time2 = Time(hours2, minutes2)

    result_time = time1.addTime(time2)
    result_time.displayTime()
    print(f"Total minutes: {result_time.displayMinutes()}")