def main(desired_word: str, season=3, size=10):
    file_links = {i:{} for i in range(1,18)}
    file_links[3] = {
        1: 'http://movies4.fox-fan.ru/video2/hbOM7u3ZVh_G-ttvim3O1w/1558644845/familyguy/3/original/301.mp4',
        2: 'http://movies1.fox-fan.ru/video2/TlzzC3uqvhP_CIN7rYrB3w/1558644994/familyguy/3/original/302.mp4',
        3: 'http://movies1.fox-fan.ru/video2/5PisgSyLodljZ6gemrGcCA/1558645041/familyguy/3/original/303.mp4',
        4: 'http://movies5.fox-fan.ru/video2/dY9wNNB-WtJ698y9kk36Zw/1558645095/familyguy/3/original/304.mp4',
        5: 'http://movies1.fox-fan.ru/video2/a8fJVRsnf-Wm49j7WlVSzg/1558645239/familyguy/3/original/305.mp4',
        6: 'http://movies4.fox-fan.ru/video2/99Zoh0HVmAe5SQl2Ec-sXw/1558645310/familyguy/3/original/306.mp4',
        7: 'http://movies4.fox-fan.ru/video2/cpujEb3IzPJcoSlfIs0zsg/1558645356/familyguy/3/original/307.mp4',
        8: 'http://movies4.fox-fan.ru/video2/c4tX8PIX_tlXfdY34imdmw/1558645386/familyguy/3/original/308.mp4',
        9: 'http://movies5.fox-fan.ru/video2/JUTGZ-XwwDnZ3hpzqui80Q/1558645410/familyguy/3/original/309.mp4',
        10: 'http://movies1.fox-fan.ru/video2/eMVJClLb7aFiXWDKpvs9WQ/1558645443/familyguy/3/original/310.mp4',
        11: '',
        12: '',
        13: '',
        14: '',
        15: '',
        16: '',
        17: '',
        18: '',
        19: '',
        20: '',
        21: '',
        22: ''  
    }
    def get_links(season: int, series: int):
        season = str(season)
        series = '0' + str(series) if series < 10 else str(series)
        response = requests.get('http://familyguy.fox-fan.tv/series.php?id=' + str(season) + str(series) + '&voice=9') 
        parsed_html = BeautifulSoup(response.text, 'html.parser') 
        parser = Parser()
        file_link = ''
        sub_link = ''
        for script in parsed_html.find_all('script', type="text/javascript"): 
            tree = parser.parse(script.string) 
            fields = {getattr(node.left, 'value', ''): getattr(node.right, 'value', '') 
                      for node in nodevisitor.visit(tree)
                      if isinstance(node, ast.Assign)}
            try:
                file_link = file_links.get(int(season), {'':''}).get(int(series), '')
                # file_link = fields['file'].replace('\'','').replace('\"','')
                sub_link = fields['subtitle'].replace('\'','').replace('\"','')
            except:
                pass
        return file_link, sub_link
    
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






    season = 3
    desired_word = 'Peter'
    ans = []
    for series in list(file_links[season].keys()):
        file_link, sub_link = get_links(season, series)
        season_name = str(season)
        series_name = '0' + str(series) if series < 10 else str(series)
        exists = os.path.isfile(r"downloads/{}.vtt".format(season_name + series_name))
        if not(exists):
            urllib.request.urlretrieve(sub_link, r"downloads/{}.vtt".format(season_name + series_name))

        starts_ends = search(desired_word, r'downloads/{}.vtt'.format(season_name + series_name))
        for start_end in starts_ends:
            if file_link != '':
                ans.append([file_link, series, start_end[0], start_end[1]])
    ans = [ans[i] for i in random.sample(range(len(ans)), size)]
    return ans