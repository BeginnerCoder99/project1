
#I've decided to use BeautifulSoup for the scrapeing with lxml as the parser
#first using pip install requests beautifulsoup4 lxml in cmd shell.
#double checked that created new branch and inside it for github.
#importing requests and re for HTTP requests and text cleaning
#It does appaear to be working, but having issues with sites
#using selenium as a website emulator to identify if website security or coding issue
#pip install --upgrade selenium
#not working, using pip install webdriver-manager
#I keep running into anti-bot protection on websites
#Found websites without bot protection
#Had to encode unicode to get around windows bug with txt files.
#updating program for project 3
#Minor cleanup including making sure still working, removing excess structure in outputfile.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re

options = webdriver.ChromeOptions()
options.add_argument('--headless')  
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--ignore-certificate-errors')
#website emulation but no browser cause headless

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


with open("url_list.txt") as file:
    url1 = file.readline()
    url2 = file.readline()
    url3 = file.readline()
urlList = [url1, url2, url3]
#reads first three then puts into array as urls

output = ""
#creates empty string
#for loop iterates through urlList array until done for each array
for x in urlList:
    driver.get(x)
    print("\nScraping website at", x)
    #had issue with one site not using headers but specialy containers
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
        )
    except:
        print("Timeout waiting for heading to load")
    #times out if no h1 headers are found

    #parses through the page
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    headings = soup.find_all(['h1', 'h2', 'h3'])
    print("Total headings found: ", len(headings))

# Limit the number of headings processed to 20
    max_headings = 20
    for i, h in enumerate(headings):
        if i >= max_headings:
            break
        text = re.sub(r'\s+', ' ', h.get_text()).strip()
        output = output + text + "\n"
driver.quit()

#writes to file output, encoded to ensure no unicode errors
with open("urlOutput.txt", "w", encoding="utf-8") as f:
    f.write(output)


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

#Attempt to rework the program for project 3
#Ai models are both freeform, trying to force response
#Got working examples, but defaults to neutral
#Switching from T5 and GPT-2 to distilbert and RoBerta
#Both are still in the transformers library so fairly easy swtich
#updating it to read the entire file and then output everything in case of more than 3 prompts.
#This part of project 3 is now finished.
#Combining project 1 and 2 now in order to finish project 3.
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch

# Read prompts
with open("urlOutput.txt") as file:
    prompts = [line.strip() for line in file if line.strip()]


# Load first model: DistilBERT SST-2
classifier1 = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

# Load second model: Twitter RoBERTa sentiment
tokenizer2 = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
model2 = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
labels2 = ['negative', 'neutral', 'positive']

def classify_roberta(text):
    inputs = tokenizer2(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model2(**inputs)
    scores = outputs.logits.softmax(dim=1).squeeze()
    predicted_class = torch.argmax(scores).item()
    return labels2[predicted_class]

# Build the response
response = "This is AI 1's response (DistilBERT SST-2):\n"
for i, prompt in enumerate(prompts, 1):
    result = classifier1(prompt)[0]
    label = result['label'].lower()
    if label not in {"positive", "negative"}:
        label = "neutral"
    response += f"Prompt {i}: {label}\n"

response += "\nThis is AI 2's response (Twitter-RoBERTa):\n"
for i, prompt in enumerate(prompts, 1):
    label = classify_roberta(prompt)
    response += f"Prompt {i}: {label}\n"

# Save to file
with open("AIoutput.txt", "w") as f:
    f.write(response)

print("Done")
