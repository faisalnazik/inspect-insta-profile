import time
import random
import config
import datetime

from decorators import log_decorator


@log_decorator
def pause():
    """Pause the bot's execution for a random sleep time between min_sleep_time and max_sleep_time (in seconds)"""

    sleep_time = random.randint(config.MIN_SLEEP_TIME, config.MAX_SLEEP_TIME)
    print(f"Sleeping for {str(datetime.timedelta(seconds=sleep_time))}")

    # Initialize progress bar
    progress_bar_width = 30
    progress_bar = "[" + " " * progress_bar_width + "]"
    print(progress_bar, end="\r")

    # Calculate total time and remaining time
    remaining_time = sleep_time

    # Update progress bar every second
    for i in range(sleep_time):
        time.sleep(1)
        remaining_time -= 1

        # Update progress bar
        filled_width = int((i / sleep_time) * progress_bar_width)
        empty_width = progress_bar_width - filled_width
        progress_bar = "[" + "#" * filled_width + " " * empty_width + "]"

        # Calculate remaining time and update progress bar
        if remaining_time > 0:
            remaining_time_str = str(datetime.timedelta(seconds=remaining_time))
            progress_bar += f" {remaining_time_str} left"

        print(progress_bar, end="\r")

    print()  # Move to next line after progress bar completes
