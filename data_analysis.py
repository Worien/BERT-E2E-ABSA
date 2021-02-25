
from __future__ import absolute_import, division, print_function

import csv
import logging
import os
import sys
from io import open

from seq_utils import *

#set_type =  test
#data_dir =  ./data/laptop14
def _get_all_tags(data_dir, set_type, tagging_schema):
    examples = []
    print("data_dir = ", data_dir)
    print("set_type = ", set_type)
    file = os.path.join(data_dir, "%s.txt" % set_type)
    class_count = np.zeros(3)
    allWordsWithSentiment = []
    with open(file, 'r', encoding='UTF-8') as fp:
        sample_id = 0
        for line in fp:
            sent_string, tag_string = line.strip().split('####')
            words = []
            tags = []
            for tag_item in tag_string.split(' '):
                eles = tag_item.split('=')
                if len(eles) == 1:
                    raise Exception("Invalid samples %s..." % tag_string)
                elif len(eles) == 2:
                    word, tag = eles
                else:
                    word = ''.join((len(eles) - 2) * ['='])
                    tag = eles[-1]
                print('%s-%s' %(word, tag))
                words.append(word)
                tags.append(tag)
                if tag != 'O':
                    allWordsWithSentiment.append(word)
    print("allWordsWithSentiment = ", allWordsWithSentiment)
    return allWordsWithSentiment

_get_all_tags(data_dir='./data/laptop14', set_type='test', tagging_schema='BIEOS')