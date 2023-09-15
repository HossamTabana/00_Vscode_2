import sys
import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sqlite3
from datetime import datetime

class Watcher:
    DIRECTORY_TO_WATCH = "/Users/hossamtabana/Downloads/track"
    LOG_DIRECTORY = "/Users/hossamtabana/Downloads/log"  # Define your log directory path here

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

    # Using a dictionary to implement a cooldown period
    processed_files = {}

    @staticmethod
    def process(event):
        print(f"Event detected for {event.src_path}")  # Diagnostic print

        if event.is_directory:
            return None

        # Avoid reacting to changes in the log directory
        if Watcher.LOG_DIRECTORY in event.src_path:
            return None

        # Implementing a cooldown for each file
        current_time_seconds = time.time()
        if event.src_path in Handler.processed_files:
            last_processed_time = Handler.processed_files[event.src_path]
            if current_time_seconds - last_processed_time < 10:  # 10 second cooldown
                print(f"Ignoring {event.src_path} due to cooldown")  # Diagnostic print
                return
        Handler.processed_files[event.src_path] = current_time_seconds
        
        current_time = datetime.fromtimestamp(current_time_seconds).strftime('%Y-%m-%d %H:%M:%S')
        timestamp_for_filename = datetime.fromtimestamp(current_time_seconds).strftime('%Y%m%d%H%M%S')
        
        file_info = os.stat(event.src_path)
        
        file_created_date = datetime.fromtimestamp(file_info.st_ctime).strftime('%Y-%m-%d %H:%M:%S')
        file_updated_date = datetime.fromtimestamp(file_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        file_name = os.path.basename(event.src_path)
        file_path = event.src_path

        if event.event_type == 'modified':
            conn = sqlite3.connect('file_changes.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO db_track (timestamp, file_created_date, file_path, file_updated_date, file_name, event_type) VALUES (?, ?, ?, ?, ?, ?)",
                           (current_time, file_created_date, file_path, file_updated_date, file_name, event.event_type))
            conn.commit()
            conn.close()

            # Copy and rename the file
            new_filename = f"{file_name}_updated{timestamp_for_filename}"
            shutil.copy2(file_path, os.path.join(Watcher.LOG_DIRECTORY, new_filename))

    def on_modified(self, event):
        self.process(event)

if __name__ == '__main__':
    conn = sqlite3.connect('file_changes.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS db_track (
        id INTEGER PRIMARY KEY,
        timestamp TEXT,
        file_created_date TEXT,
        file_path TEXT,
        file_updated_date TEXT,
        file_deleted_date TEXT,
        file_name TEXT,
        event_type TEXT
    )
    """)
    conn.commit()
    conn.close()

    w = Watcher()
    w.run()
