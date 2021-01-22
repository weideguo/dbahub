
from apscheduler.schedulers.blocking import BlockingScheduler


def job(*args):
    print(args)


scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', minute='*/2', hour='*', args=["aaa","bbb"])

try:
    scheduler.start()
except(KeyboardInterrupt, SystemError):
    scheduler.shutdown()




        