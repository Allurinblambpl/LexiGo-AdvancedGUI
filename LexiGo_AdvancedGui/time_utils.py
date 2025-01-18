import time

class TimeUtils:
    def __init__(self):
        self.start_time = time.time()

    def update(self):
        elapsed_time = time.time() - self.start_time
        print(f"Time elapsed: {elapsed_time:.2f} seconds")
