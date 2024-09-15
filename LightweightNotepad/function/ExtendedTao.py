from lunar_python import Tao


class ExtendedTao(Tao):
    def to_numeric_string(self):
        year = self.getYear()
        month = self.getMonth()
        day = self.getDay()
        print(f"Year: {year}, Month: {month}, Day: {day}")
        return year, month, day
