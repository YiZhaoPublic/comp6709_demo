import os
import json
import random

mark_list=[3,4]
for mark in mark_list:
    dir_path="responses_gpt{}".format(mark)
    files = os.listdir(dir_path)
    selected_files=random.sample(files,50)

    selected_data_list=[]
    for f in selected_files:
        with open(os.path.join(dir_path,f), 'r') as ff:
            data=json.load(ff)
        selected_data_list.append(data)

    final_json_path = os.path.join('test_data', 'gpt{}.json'.format(mark))
    with open(final_json_path, 'w') as fjson:
        json.dump(selected_data_list, fjson, indent=2)