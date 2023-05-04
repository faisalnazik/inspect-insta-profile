import datetime


def log_decorator(func):
    def wrapper(*args, **kwargs):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{current_time}] Starting {func.__name__}...")
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"[{current_time}] Error occurred during {func.__name__}: {str(e)}")
            raise
        print(f"[{current_time}] {func.__name__} completed.")
        return result

    return wrapper
