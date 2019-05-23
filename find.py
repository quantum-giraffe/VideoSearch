def search(desired_word:str, filename:str):
    desired_word = desired_word.lower().rstrip().lstrip()
    with open(filename) as file:
        text = [list(g) for b,g in groupby(file, lambda x: bool(x.strip())) if b]

    Subtitle = namedtuple('Subtitle', 'start end content')

    desired_times = []

    for blocks in text:
        if len(blocks) >= 2: # на всякий случай
            start_end, *content_raw = blocks 
            start, end = start_end.split(' --> ')
            end = end.rstrip('\n')
            if start.count(':') == 1:
                x = time.strptime(start.split('.')[0],'%M:%S')
                start = datetime.timedelta(minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
            elif start.count(':') == 2:
                x = time.strptime(start.split('.')[0],'%H:%M:%S')
                start = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
            if end.count(':') == 1:
                x = time.strptime(end.split('.')[0],'%M:%S')
                end = datetime.timedelta(minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
            elif end.count(':') == 2:
                x = time.strptime(end.split('.')[0],'%H:%M:%S')
                end = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
                
            content_clear = [x.lower().lstrip('\"').rstrip('\n') for x in content_raw]
            content = ' '.join(content_clear)
            if desired_word in content:
                desired_times.append([start, end])
    return desired_times