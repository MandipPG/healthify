from datetime import datetime


def is_valid_input(week_config):
  count = 0;
  format = "%H:%M"
  for day in week_config:
    for slot in day:
      count += len(slot)
      if "start_time" not in slot.keys() or "end_time" not in slot.keys() or datetime.strptime(slot["start_time"], format) >= datetime.strptime(slot["end_time"], format):
        raise Exception("Please enter the valid Inputs")
  if count ==  0:
    return True
  return False
