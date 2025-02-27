#Created environment project1 in conda
#googled steps to install LaMini-GPT

#installing transformers library from hugging face using pip install transforms torch.
#transformers apparently provides pretrained models
#torch lets you run the models.
#Going to be using GPT-2 and T5 as my LLMs.
#Finished creating repository and pushing this file to it.
#added code to read from prompt text file
#modified the prompt txt to not have new lines between codes.
#verified it stores the prompts correctly.
#Attempted to import the model but ran into issues
#used from transformers import GPT2LMHeadModel, GPT2Tokenizer
#This should import the model and tokenizer(machine translator)
#having to install transformers since the module isn't found despite earlier pip install.
#pip install transformers.
#The T5tokenizer isn't working, stating I needed the sentencepiece library
#using pip install sentencepiece
#pip install mentioned possible issues with package
#issue is needs cmake?
#using command conda install -c conda-forge cmake
#didn't work, installing sentencepiece directly through conda
#conda install -c conda-forge sentencepiece
#went through big loading process for T5 first time, did not do so afterwords
#updated tokenizer to stop printing out the legacy behavior message
#cleanup of printing behavior
#transitioning printing to output file
#Concatenated all responses to print out.
#Updating to only one string instead of 6 separate responses.


from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

with open("AIprompt.txt") as file:
    prompt1 = file.readline()
    prompt2 = file.readline()
    prompt3 = file.readline()
print(prompt1, prompt2, prompt3, "\n\n")


model_name = "gpt2"
tokenizer1 = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def generate_text1(prompt, max_length = 30):
    inputs = tokenizer1(prompt, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(**inputs, max_length=max_length, num_return_sequences=1,
        pad_token_id=tokenizer1.eos_token_id)
    return tokenizer1.decode(output[0], skip_special_tokens=True)

response = "This is AI 1's response: \n" + generate_text1(prompt1) + "\n\n"
response += generate_text1(prompt2) + "\n\n"
response += generate_text1(prompt3) + "\n\n"

model_name2 = "t5-small"
tokenizer2 = T5Tokenizer.from_pretrained(model_name2, legacy = True)
model = T5ForConditionalGeneration.from_pretrained(model_name2)
def generate_text2(prompt, max_length = 30):
    inputs = tokenizer2(prompt, return_tensors="pt", padding=True, truncation=True)
    output = model.generate(**inputs, max_length=max_length)
    return tokenizer2.decode(output[0], skip_special_tokens=True)

response += "This is AI 2's response: \n" + generate_text2(prompt1) + "\n\n"
response += generate_text2(prompt2) + "\n\n"
response += generate_text2(prompt3) + "\n\n"

f = open("AIoutput.txt", "w")
#TotalResponse = response1+response2+response3+response4+response5+response6
f.write(response)
f.close()
print("Done")
