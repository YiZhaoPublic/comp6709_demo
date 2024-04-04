import json
dir_path="test_results_evaluation"
mark_list = [3, 4]
model_list=['GPT4','GPT3','mistrial','llama']
for mark in mark_list:
    print(mark)
    for model_mark in model_list:
        print(model_mark)
        cnt=0
        with open('test_results_evaluation/{}_gpt{}.json'.format(model_mark,mark), 'r') as f:
            data = json.load(f)
        len_data=len(data)
        for item in data:
            if item['better']=='1':
                cnt+=1
        print('mark ', mark, 'model ', model_mark, 'rate', round(cnt/len_data,3))
