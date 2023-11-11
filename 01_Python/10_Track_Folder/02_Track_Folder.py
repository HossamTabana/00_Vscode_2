import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sqlite3

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
        if event.is_directory:
            return None
        elif event.event_type == 'modified':
            conn = sqlite3.connect('file_changes.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO db_track (timestamp, file, event_type) VALUES (?, ?, ?)",
                           (time.time(), event.src_path, event.event_type))
            conn.commit()
            conn.close()

    def on_modified(self, event):
        self.process(event)

if __name__ == '__main__':
    conn = sqlite3.connect('file_changes.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS db_track (
        id INTEGER PRIMARY KEY,
        timestamp REAL,
        file TEXT,
        event_type TEXT
    )
    """)
    conn.commit()
    conn.close()
    
    w = Watcher()
    w.run()
