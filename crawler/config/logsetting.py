import logging
import logging.config

LOGGING_CONFIG = {
    'version': 1,

    'formatters': {
        'default': {
             'format':  '%(asctime)s - %(levelname)s - %(message)s'
        },
    },
    'handlers': {
        'consoleHandler': {
            'formatter': 'default',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
        },
        'logfileHandler': {
            'formatter': 'default',
            'class': 'logging.FileHandler',
            'filename': 'crawler.log',
        },
    },
    'loggers': {
        'clsE': {
            'handlers': ['consoleHandler','logfileHandler'],
            'level': 'DEBUG',
            'propagate': 'no',
        },
        'clsF': {
            'handlers': ['consoleHandler','logfileHandler'],
            'level': 'DEBUG',
            'propagate': 'no',
        },
        'callhoge': {
            'handlers': ['consoleHandler','logfileHandler'],
            'level': 'DEBUG',
            'propagate': 'no',
        },
        'CategorySetter': {
            'handlers': ['consoleHandler','logfileHandler'],
            'level': 'INFO',
            'propagate': 'no',
        },
        'CategorySetterExe': {
            'handlers': ['consoleHandler','logfileHandler'],
            'level': 'INFO',
            'propagate': 'no',
        },
        'CategoryValidator': {
            'handlers': ['consoleHandler','logfileHandler'],
            'level': 'INFO',
            'propagate': 'no',
        },
        'Urls2csv': {
            'handlers': ['consoleHandler','logfileHandler'],
            'level': 'ERROR',
            'propagate': 'no',
        },
        'Urls2Json': {
            'handlers': ['consoleHandler','logfileHandler'],
            'level': 'ERROR',
            'propagate': 'no',
        },
        'Url2CsvWriter': {
            'handlers': ['consoleHandler','logfileHandler'],
            'level': 'ERROR',
            'propagate': 'no',
        },
        'Url2JsonWriter': {
            'handlers': ['consoleHandler','logfileHandler'],
            'level': 'ERROR',
            'propagate': 'no',
        },
        'List2File': {
            'handlers': ['consoleHandler','logfileHandler'],
            'level': 'ERROR',
            'propagate': 'no',
        },
        'StdScoreler': {
            'handlers': ['consoleHandler','logfileHandler'],
            'level': 'ERROR',
            'propagate': 'no',
        },
        'GoogSearchScrapyer': {
            'handlers': ['consoleHandler','logfileHandler'],
            'level': 'ERROR',
            'propagate': 'no',
        }
    },
    'root': {
        'level': 'NOTSET',
        'handlers': ['consoleHandler','logfileHandler'],
    },
}

def configure_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
