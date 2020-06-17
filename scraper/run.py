import time
import os

from apscheduler.schedulers.background import BackgroundScheduler

from main import main


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    # scheduler.add_job(main, 'interval', seconds=10800)
    scheduler.add_job(main, 'interval', seconds=1800)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        # This is here to simulate application activity (which keeps the main thread alive).
        while True:
            # time.sleep(10799)
            time.sleep(1799)
    except (KeyboardInterrupt, SystemExit):
        # Not strictly necessary if daemonic mode is enabled but should be done if possible
        scheduler.shutdown()
