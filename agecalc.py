import datetime

nowDate = datetime.date.today()

birthday = datetime.datetime.strptime("Aug 19 2006", "%b %d %Y").date()

age = int(abs(nowDate - birthday).days / 365)

print(age)