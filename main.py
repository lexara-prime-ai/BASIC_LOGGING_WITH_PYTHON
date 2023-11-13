import time

time_format: [str, time] = {
    "hours": time.localtime().tm_hour,
    "minutes": time.localtime().tm_min,
    "seconds": time.localtime().tm_sec
}


class Program:
    def __init__(self, program_version: str):
        self.program_version = program_version
        self.last_run = time.localtime().tm_sec

    def start(self):
        self.log_time(self)
        print("Starting . . . ")
        print(f"Duration: {self.last_run}s")

    @staticmethod
    def log_time(self):
        log_time = f"\r{time_format.get('hours') - 12}:{time_format.get('minutes')}:{time_format.get('seconds')}"
        print(f"Start time::{log_time}")


app = Program("1.0.0")

if __name__ == '__main__':
    Program.start(app)
