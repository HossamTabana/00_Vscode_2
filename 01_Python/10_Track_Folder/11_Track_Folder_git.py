import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class GitHandler(FileSystemEventHandler):
    def __init__(self):
        self.version = 1
    
    def on_modified(self, event):
        if event.is_directory:
            return
        self.git_add_and_commit()

    def git_add_and_commit(self):
        subprocess.run(["git", "add", "."])
        commit_message = f"v{self.version}"
        subprocess.run(["git", "commit", "-m", commit_message])
        print(f"Committed with message: {commit_message}")
        self.version += 1

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = GitHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    
    print(f"Starting observer on {path}")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
