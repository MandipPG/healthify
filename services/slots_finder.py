from datetime import datetime
from utils.helper_funtions import is_valid_input


def get_next_n_slots(week_config, current_time, n=1):
    next_n_slots = []
    current_day_index = current_time.weekday()
    is_first_iteration = True
    is_first_day = True
    format = "%Y-%m-%d %H:%M:%S"

    if is_valid_input(week_config):
        return next_n_slots

    while len(next_n_slots) < n:
        if not is_first_iteration:
            current_day_index = 0  # to reset the starting index of week_config to consider the whole week config now.
        for day in week_config[current_day_index: 7]:
            for slot in day:
                result = dict()
                start_time = slot["start_time"].split(':')
                end_time = slot["end_time"].split(':')
                if (is_first_day and current_time.hour >= int(start_time[0]) and current_time.minute >= int(
                        start_time[1])) or (not is_first_day):
                    start = datetime(current_time.year, current_time.month, current_time.day, int(start_time[0]), int(start_time[1]))
                    end = datetime(current_time.year, current_time.month, current_time.day,
                                              int(end_time[0]), int(end_time[1]))
                    result["start_time"] = start.strftime(format)
                    result["end_time"] = end.strftime(format)
                    if len(next_n_slots) < n:
                        next_n_slots.append(result)
                    else:
                        break;
            is_first_day = False
            current_time = datetime(current_time.year, current_time.month, current_time.day + 1, 0, 0)
        is_first_iteration = False

    return next_n_slots
