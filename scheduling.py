# note backgroundscheduler seems to be running ~2 seconds fast

from apscheduler.schedulers.background import BackgroundScheduler

Flag = True

def foo():
    print("This is printing at a certain time")
    global Flag
    Flag = False

sch = BackgroundScheduler()
sch.add_job(foo, 'date', run_date = "2023-08-07 21:06:20")
sch.start()

while Flag:
    pass

quit()


