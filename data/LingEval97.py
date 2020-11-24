import re

from data.annotated import AnnotatedTextDataset
class LingEval97Dataset(AnnotatedTextDataset):
    NAME = 'lingeval97'
    LANGUAGE_PAIR = ('en', 'de')
    # WORD_COUNT = (2953738, 2864487)
    WORD_COUNT = (1.03115776, 1)

    URLS = [( "lingeval97.tar.gz","https://drive.google.com/uc?export=download&id=1uSsn3mylLj8i_cdIdgBbDnWgNT9lfJmL")]
    RAW_SPLITS = {
        'train': [
            ('lingeval97.en', 'lingeval97.de')
        ],
        'valid': [
            ('lingeval97.en', 'lingeval97.de')
        ],
        'dev': [
            ('lingeval97.en', 'lingeval97.de')
        ],
        'test': [
            ('lingeval97.en', 'lingeval97.de')
        ]


    }
    SPLITS = {
        'train': 'train.tok',
        'valid': 'valid.tok',
        'dev': 'dev.tok',
        'test': 'test.tok'
    }
