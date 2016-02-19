CRAWLER_CONFIG={
    'directory' : {
        'transaction': './tmp',
#        'exepath': 'ls',
        'jsonoutput': './result.json',
        'noncategorizedurls': './list',
    },
    'subprocess' : {
        'name': 'ls',
    }
#    'settings': {
#        'transactiondir': './tmp',
#        'exepath': 'ls',
#        'outputjson': './result.json',
#        'noncaturls': './list',
#    },
}

def configureCrawler():
    return CRAWLER_CONFIG
