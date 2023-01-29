
import re

def domain_name(url):
    # use a regular expression to extract the domain name from the url
    match = re.search(r'(https?://)?(www\d?\.)?(?P<domain>[\w-]+)\.', url)
    if match:
        return match.group('domain')
    else:
        # if no domain name is found, return an empty string
        return ''
    # return domain_name