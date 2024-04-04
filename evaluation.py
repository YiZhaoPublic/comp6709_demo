import os
import json
from tqdm import tqdm
from openai import OpenAI

client = OpenAI(
    api_key='sk-xxxxxxx',
)

PROMPT_TEMPLATE = """
Task Clarification: Your role is to serve as an evaluator or judge. You will receive one instruction and two responses. Your objective is to determine which of the two responses is superior.

The criteria for determining a better response may involve the following two aspects:


1. Evaluating the quality of language in the responses, which one demonstrates better expression through fluency and clear sentences. Superfluous language without enough information should be avoided.
2. An overall assessment to determine which response is superior.

Instruction: {}

Response 0: {}

Response 1: {}

Please return the superior response's ID (0 or 1) purely, without any additional commentary or explanation.
"""

mark_list = [3, 4]
model_list=['GPT3','llama']
for mark in mark_list:
    print(mark)
    for model_mark in model_list:
        print(model_mark)
        with open('test_results/{}_gpt{}.json'.format(model_mark,mark), 'r') as f:
            data = json.load(f)
        res_list = []
        for i, item in tqdm(enumerate(data)):
            prompt=PROMPT_TEMPLATE.format(item["ori_prompt"], item["res_0"],item["res_1"])
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="gpt-4-turbo-preview")
            response=chat_completion.choices[0].message.content

            res_list.append({"index": i, "better": response})
        os.makedirs('test_results_evaluation', exist_ok=True)
        with open("test_results_evaluation/{}_gpt{}.json".format(model_mark,mark), "w") as f:
            json.dump(res_list, f, indent=2)
