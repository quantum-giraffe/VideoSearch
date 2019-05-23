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
            file_link = file_links.get(int(season), {}).get(int(series), '')
            # file_link = fields['file'].replace('\'','').replace('\"','')
            sub_link = fields['subtitle'].replace('\'','').replace('\"','')
        except:
            pass
    return file_link, sub_link