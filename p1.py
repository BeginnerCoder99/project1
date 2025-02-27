#Created environment project1 in conda
#googled steps to install LaMini-GPT

#installing transformers library from hugging face using pip install transforms torch.
#transformers apparently provides pretrained models
#torch lets you run the models.
#Going to be using GPT-2 and Bert as my LLMs.
#Finished creating repository and pushing this file to it.
#added code to read from prompt text file
#modified the prompt txt to not have new lines between codes.

file = open("AIprompt.txt")
prompt1 = file.readline()
print(prompt1)
prompt2 = file.readline()
print(prompt2)
prompt3 = file.readline()
print(prompt3)