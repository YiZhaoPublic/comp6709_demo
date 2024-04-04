### 1. Dataset 
~~~
cd data
ll
>>>alpaca_data.json
~~~

### 2. generating polished intended prompts
~~~
python data_sample_processing_gpt3.py
python data_sample_processing_gpt4.py
python form_test_samples.py
~~~

### 3. Using the original and generated prompts for get text generation
~~~
llama:
python infer_llama_batch.py
~~~
~~~
gpt-3.5:
python test_gpt3.py
~~~

### 4. evaluation
~~~
python evaluation.py
~~~

### 5.Print rate
~~~
python visual_res.py
~~~

### Result
| Polished Prompted by | Text generation by | Rate (Polished > Original) |
|----------------------|--------------------|----------------------------|
| GPT-3.5              | GPT-3.5            | 0.533                      |
|                      | LLaMA-2-Chat-7B    | 0.52                       |
| GPT-4                | GPT-3.5            | 0.8                        |
|                      | LLaMA-2-Chat-7B    | 0.667                      |
