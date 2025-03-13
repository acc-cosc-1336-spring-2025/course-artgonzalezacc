def get_hour(epoch_seconds):
    hour = epoch_seconds // 3600 % 24
    return hour

def get_minutes(epoch_seconds):
    minutes = epoch_seconds // 60 % 60
    return minutes

def get_seconds(epoch_seconds):
    seconds_remain = epoch_seconds % 3600
    return seconds_remain % 60