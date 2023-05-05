from datetime import time
import datetime
import time
# TypeError: unsupported operand type(s) for -: 'datetime.time' and 'datetime.time'

a = int(input(datetime.datetime.now().replace(microsecond=0)))
b = int(input(datetime.datetime.now().replace(microsecond=0)))
print(b-a)

outhours = input('Enter the hour: ')
outminutes = input('Enter the minutes: ')
inhours = input('Enter the hour: ')
inminutes = input('Enter the minutes: ')
start_time=time(outhours,outminutes)
end_time=time(inhours,inminutes)
delta = end_time - start_time
sec = delta.total_seconds()

min = sec / 60
print('difference in minutes:', min)

hours = sec / (60 * 60)
print('difference in hours:', hours)
import dateutil
class Calculation:
    name=input("enter name: ")
    date = time.asctime(time.localtime(time.time()))
    date = str(date)
    outtime=datetime.datetime.strptime(raw_input('specify time in HHMM format: '), "%H%M")
    intime=datetime.datetime.strptime(raw_input('specify time in HHMM format: '), "%H%M")
    def calculate_time(self):
        startdelta = datetime.timedelta(hours=self.intime.hours, minutes=self.intime.minutes, seconds=self.intime.seconds)
        enddelta = datetime.timedelta(hours=self.outtime.hours, minutes=self.outtime.minutes, seconds=self.outtime.seconds)
        return (enddelta-startdelta).seconds/3600

    def __str__(self):
        return "%s" %self.name
obj=Calculation()
obj.calculate_time()
print(obj)
