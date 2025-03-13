import value_return

def main():
    epoch_seconds = 1741832545
    
    hour = value_return.get_hour(epoch_seconds)
    minutes = value_return.get_minutes(epoch_seconds)
    seconds = value_return.get_seconds(epoch_seconds)

    print(hour, ":", minutes, ":", seconds)

main()