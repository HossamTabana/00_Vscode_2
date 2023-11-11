I need to adjust below code instead of excel I need to do the following :
1. create a db file and saved in the same folder of vscode .
2. create a table named db_track
3. insert in that table when update happened in the folder ( file name, file date, update date, file path .. and all available information)
4. check when we run the python code if the db and table has been exist or not if already exsist add new row in the table for any changes tracked.
5. run this python code on daily basis when the computer is on and keep it running to check and track the changes using task schedule using batch file to run the python code.
6. make a second script for select statement for the table in the db to check if everything working fine :

import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pandas as pd

class Watcher:

    DIRECTORY_TO_WATCH = "/path/to/my/folder"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Observer Stopped due to keyboard interrupt")
        except Exception as e:
            self.observer.stop()
            print(f"Observer Stopped due to error: {e}")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def process(event):
        """
        Event is an object which contains information about the event type (modification, creation, deletion) and path to the modified file.
        """
        if event.is_directory:
            return None

        elif event.event_type == 'modified':
            # Log to Excel or SQL here
            data = {'timestamp': [time.time()], 'file': [event.src_path], 'event': [event.event_type]}
            df = pd.DataFrame(data)
            with pd.ExcelWriter('log.xlsx', engine='openpyxl', mode='a') as writer:
                df.to_excel(writer, index=False)

    def on_modified(self, event):
        self.process(event)


if __name__ == '__main__':
    w = Watcher()
    w.run()