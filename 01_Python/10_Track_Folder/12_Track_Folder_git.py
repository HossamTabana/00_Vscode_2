import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class GitHandler(FileSystemEventHandler):
    def __init__(self, directory):
        self.directory = directory
        self.version = 1
        
        # Check if the directory is already a git repository
        if not os.path.exists(os.path.join(directory, ".git")):
            self.git_init()
            print(f"Initialized git repository in {directory}")
        else:
            print(f"Directory {directory} is already a git repository")

    def on_modified(self, event):
        if event.is_directory:
            return
        self.git_add_and_commit()

    def git_init(self):
        subprocess.run(["git", "init"], cwd=self.directory)

    def git_add_and_commit(self):
        subprocess.run(["git", "add", "."], cwd=self.directory)
        commit_message = f"v{self.version}"
        subprocess.run(["git", "commit", "-m", commit_message], cwd=self.directory)
        print(f"Committed with message: {commit_message}")
        self.version += 1

if __name__ == "__main__":
    # Specify the path to the directory you want to watch
    path_to_watch = "/path/to/your/folder"

    event_handler = GitHandler(path_to_watch)
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=True)
    
    print(f"Starting observer on {path_to_watch}")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
