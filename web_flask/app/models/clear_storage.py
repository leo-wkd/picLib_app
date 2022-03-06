import os

def clear_old_contents(dir):
    for file in os.listdir(dir):
        os.remove(os.path.join(dir, file))