import os
import json

def read_tasks(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r') as f:
        try:
            return json.load(f)
        except:
            return []

def write_tasks(path, tasks):
    with open(path, 'w') as f:
        json.dump(tasks, f, indent=2)
