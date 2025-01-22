class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    @classmethod
    def from_string(cls, time_str):
        try:
            hours, minutes = map(int, time_str.split(':'))
            if 0 <= hours < 24 and 0 <= minutes < 60:
                return cls(hours, minutes)
            else:
                raise ValueError
        except ValueError:
            print("Invalid time format. Please enter time as HH:MM (24-hour format).")
            return None

    def add_time(self, other_time):
        total_minutes = self.minutes + other_time.minutes
        total_hours = self.hours + other_time.hours + total_minutes // 60
        total_minutes %= 60
        total_hours %= 24  # Ensure hours wrap around after 24
        return Time(total_hours, total_minutes)

    def display_time(self):
        print(f"{self.hours} hr and {self.minutes} min")

    def display_minutes(self):
        return self.hours * 60 + self.minutes

if __name__ == "__main__":
    while True:
        time_str1 = input("Enter the first time (HH:MM): ")
        time1 = Time.from_string(time_str1)
        if time1:
            break

    while True:
        time_str2 = input("Enter the second time (HH:MM): ")
        time2 = Time.from_string(time_str2)
        if time2:
            break

    result_time = time1.add_time(time2)
    print("Combined time:")
    result_time.display_time()
    print(f"Total minutes: {result_time.display_minutes()}")
