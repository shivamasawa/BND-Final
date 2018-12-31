import sys
from configs.config import STAGING_URL
envor = 'prod'
def get_env_url():
    if get_envor(envor) == 'prod':
        env = 'prod'
    elif get_envor(envor) == 'qa':
        env = 'qa'
    else:
        env = 'stg'
        
    if env == 'qa':
        env_url = 'http://bnd.us-east1-dev-media-web2.ttr01.com/'
    elif env == 'stg':
        env_url = STAGING_URL
    elif env == 'prod':
        env_url = 'https://www.businessnewsdaily.com/'
    return env_url

def get_envor(envor):
    return envor

def get_env():
    '''if len(sys.argv) == 2:
        env = sys.argv[1].lower()
        if 'android' in env or 'ip' in env:
            env = 'stg'
    elif len(sys.argv) == 3:
        env = sys.argv[1].lower()
    else:
        env = 'prod'''
    if envor == 'prod':
        env = 'prod'
    else:
        env = 'stg'
    
    return env

def get_browser():
    if len(sys.argv) < 3:
        browser = 'chrome'
    else:
        browser = sys.argv[2].lower()
    return browser