import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pandas as pd

class Watcher:

    DIRECTORY_TO_WATCH = "/Users/hossamtabana/Downloads/track"

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
