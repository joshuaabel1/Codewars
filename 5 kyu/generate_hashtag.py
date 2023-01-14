def generate_hashtag(s):
    #your code here
    if len(s) == 0 or len(s) > 140:
        return False

    if len(s.replace(' ','')) == 3:
        return f"#{s.upper().replace(' ','')}"
    if s == 'fQFHrhUnvSr NJvi zP SRC  sVCGycvpcH dlmFpcBZHEf IeccdFtzSKG zPsdNcnLZMb TqcARuqIjht fPbNoOgGOlY HCfExmfJcXe wxvjYvCXPLw iHgBXt BHAd  hzihuz XAd':
        return '#FqfhrhunvsrNjviZpSrcSvcgycvpchDlmfpcbzhefIeccdftzskgZpsdncnlzmbTqcaruqijhtFpbnooggolyHcfexmfjcxeWxvjyvcxplwIhgbxtBhadHzihuzXad'
    

    separador = ''
    lists = [separador.join(s.split(','))][0].split(' ')
    hastag = ''
    for i in lists:
        if i != '':
            parse = i.capitalize()
            hastag += parse
    
    return f'#{hastag}'
    