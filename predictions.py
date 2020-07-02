#!/usr/bin/env python3
from ximilar.client import RecognitionClient
import os
import pandas as pd

client = RecognitionClient(token="f563142df5a77daef3553912537d96ef8e392143")

task, status = client.get_task(task_id='3a5ce748-2436-4e57-814c-cf1d953d9c65')

print(os.listdir('./test'))

df = pd.read_csv('./test.csv')

df.insert(2, "target")
        


# # you can send image in _file, _url or _base64 format
# # the _file format is intenally converted to _base64 as rgb image
# result = task.classify([{'_file': './test/216.jpg'}])

# # the result is in json/dictionary format and you can access it in following way:
# best_label = result['records'][0]['best_label']

# print(best_label)