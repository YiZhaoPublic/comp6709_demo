import os
import json
from tqdm import tqdm
from openai import OpenAI

client = OpenAI(
    api_key='sk-xxxxxx',
)

mark_list = [3, 4]
for mark in mark_list:
    with open('test_data/gpt{}.json'.format(mark), 'r') as f:
        data = json.load(f)
    res_list = []
    for i, item in tqdm(enumerate(data[:15])):
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": item["ori_prompt"]}],
            model="gpt-3.5-turbo",
        )
        res_0 = chat_completion.choices[0].message.content

        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": item["new_prompt"]}],
            model="gpt-3.5-turbo",
        )
        res_1 = chat_completion.choices[0].message.content

        res_list.append({"index": i, "ori_prompt": item["ori_prompt"], "res_0": res_0, "new_prompt": item["new_prompt"], "res_1": res_1})
    os.makedirs('test_results', exist_ok=True)
    with open("test_results/GPT3_gpt{}.json".format(mark), "w") as f:
        json.dump(res_list, f, indent=2)
