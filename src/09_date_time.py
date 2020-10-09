import datetime
import locale

if __name__ == '__main__':
    d1 = datetime.date(2019, 3, 10)
    print(d1)
    time1 = datetime.time(23, 10, 10)
    print(time1)
    print(datetime.date.today())
    print(datetime.date.max)
    print(datetime.date.min)
    print(datetime.time.max)
    print(datetime.time.min)
    print()
    dt = datetime.datetime(29, 10, 10, 10, 10, 10)
    print(dt)
    print(datetime.datetime.today())
    print(dt.date().day)
    print(datetime.datetime.now())
    dt_temp = dt.now().replace(year=2000)
    print(dt_temp)
    dt3 = datetime.datetime.strptime("30/08/2018", "%d/%m/%Y")
    print(dt3)
    dt4 = datetime.datetime.strptime("29/03/2000/10/03/50", "%d/%m/%Y/%H/%M/%S")
    print(dt4)
    locale.setlocale(locale.LC_ALL, "")
    print(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S (%A)"))
    print(datetime.datetime.now().strftime("%d/%B/%Y %H:%M:%S (%a)"))
    td = datetime.timedelta(days=3, hours=2, minutes=30, seconds=50)
    print(td)
    td1 = datetime.timedelta(days=1, hours=1, minutes=20, seconds=20)
    print(td1)
    print(td - td1)
