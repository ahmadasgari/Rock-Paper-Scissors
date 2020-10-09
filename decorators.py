from datetime import datetime


def log_time(func):
    def wrap_function(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        duration = end_time - start_time
        hour = duration.seconds // 3600
        minute = duration.seconds // 60
        seconds = duration.seconds % 60

        print(
            f"Total time: {hour}:{minute}:{seconds}"
        )
        return result
    return wrap_function

