import os
import json
import random
from tqdm import tqdm
from openai import OpenAI

client = OpenAI(
    api_key='sk-xxxxx',
)

with open("data/alpaca_data.json", "r") as f:
    data=json.load(f)

sample_data = random.sample(data, 200)

PROMPT_TEMPLATE="""
Task Clarification: You are tasked with the refinement of a provided sentence, known as the "original prompt," which serves as an instruction or task directive. Often, the original prompt might be overly simplistic, leading to potential misunderstandings when interpreted by language models. Your role is to enhance the clarity and precision of this prompt through a rewrite. During this rewrite, it's essential to infer and expand upon the underlying intentions of the original prompt to make it more comprehensive.

Additionally, while retaining the original question's essence, you are encouraged to suggest specific angles or areas the language model might explore in response to or in fulfillment of the task.

For instance, if the original prompt is: "Could you create a travel itinerary for my trip to Hong Kong?", the refined version might be: "Could you develop a detailed travel itinerary for my trip to Hong Kong, incorporating accommodation recommendations, a list of must-see landmarks, suggestions for dining experiences, and advice on navigating local transportation options?"

The revised prompt should be presented succinctly as a single text string, without any supplementary commentary or explanation.

The input original prompt is: {}
 
Please present the revised prompt as a single text string, without any additional commentary or explanation.
"""

os.makedirs('responses_gpt4', exist_ok=True)
for i, item in tqdm(enumerate(sample_data)):
    if not item['input']:
        ori_prompt=item['instruction']
        output=item['output']
        prompt=PROMPT_TEMPLATE.format(ori_prompt,output)
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user","content": prompt}],
            model="gpt-4-turbo-preview",
        )
        polished_prompt = chat_completion.choices[0].message.content
        item_up={"ori_prompt":ori_prompt, "new_prompt":polished_prompt}
        with open('responses_gpt4/{}.json'.format(i), 'w') as f_i:
            json.dump(item_up, f_i, indent=2)
