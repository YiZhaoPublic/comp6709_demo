import os
import json
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "/data/zy/models/llama-2-chat-7b-hf"
model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16).cuda()
tokenizer = AutoTokenizer.from_pretrained(model_path)
tokenizer.use_default_system_prompt = False






def chat_with_llama(model, tokenizer,prompt):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    input_ids = input_ids.to('cuda')
    output = model.generate(input_ids, num_beams=4, no_repeat_ngram_size=2)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    torch.cuda.empty_cache()
    return response




if __name__ == '__main__':
    mark_list=[4]
    for mark in mark_list:
        with open('test_data/gpt{}.json'.format(mark), 'r') as f:
            data=json.load(f)
        res_list=[]
        for i, item in enumerate(data):
            try:
                res_0 = chat_with_llama(model, tokenizer, item["ori_prompt"])
                res_1 = chat_with_llama(model, tokenizer, item["new_prompt"])
                res_list.append({"index": i, "ori_prompt":item["ori_prompt"], "res_0": res_0, "new_prompt":item["new_prompt"],"res_1":res_1})
            except:
                continue
        os.makedirs('test_results', exist_ok=True)
        with open("test_results/llama_gpt{}.json".format(mark), "w") as f:
            json.dump(res_list, f, indent=2)








