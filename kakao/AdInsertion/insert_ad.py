def to_sec(time_string):
    # 'hh:mm:ss'
    hours, mins, secs = map(int, time_string.split(':'))
    return 3600*hours + 60*mins + secs

def to_time_format(secs):
    hours, mins_secs = divmod(secs, 3600)
    # hours = str(hours) if hours >= 10 else f'0{hours}'
    mins, secs = divmod(mins_secs, 60)
    # mins = str(mins) if mins >= 10 else f'0{mins}'
    # secs = str(secs) if secs >= 10 else f'0{secs}'
    return f'{hours:02}:{mins:02}:{secs:02}'

def insert_ad(play_time, adv_time, logs):

    # Step 1
    # log_start_sec, log_end_sec
    log_start_sec = []
    log_end_sec = []
    for log in logs:
        start, end = log.split('-')
        log_start_sec.append(to_sec(start))
        log_end_sec.append(to_sec(end))
    # play_time_sec
    play_time_sec = to_sec(play_time)
    # adv_time_sec
    adv_time_sec = to_sec(adv_time)
    # total_time list of length (play_time_sec+1)
    total_time = [0] * (play_time_sec + 1)

    # Step 2
    # total_time -> total_time[x] = (watches started at time x) - (watches ended at time x)
    for start, end in zip(log_start_sec, log_end_sec):
        total_time[start] += 1
        total_time[end] -= 1

    # Step 3
    # total_time[x] = watches that contains x to x+1
    for idx, val in enumerate(total_time):
        if idx == 0:
            continue
        total_time[idx] += total_time[idx-1]

    # Step 4
    # total_time[x] = accumulated watching time contating 0 ~ (x+1)
    for idx, val in enumerate(total_time):
        if idx == 0:
            continue
        total_time[idx] += total_time[idx-1]

    # Step 5
    # total_time[y] - total_time[x] = accumulated watching time between (x+1) ~ (y+1)
    max_watching_time = total_time[adv_time_sec-1]
    adv_insertion_time = 0
    for adv_end_time in range(adv_time_sec-1, play_time_sec):
        if adv_end_time >= adv_time_sec:
            accumulated_watching_time = total_time[adv_end_time] - total_time[adv_end_time-adv_time_sec]
            if accumulated_watching_time > max_watching_time:
                max_watching_time = accumulated_watching_time
                adv_insertion_time = adv_end_time - adv_time_sec + 1

    return to_time_format(adv_insertion_time)



if __name__ == '__main__':
    from play_info import play_info1, play_info2, play_info3

    for play_info in [play_info1, play_info2, play_info3]:
        if insert_ad(play_info.play_time, play_info.adv_time, play_info.logs) == play_info.result:
            print("Passed a test case!")
        else:
            print("Failed a test case!")
