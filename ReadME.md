# p1.py AI headline response
The program will read from a AIprompt.txt file three seperate lines. It will then feed these lines into two separate AI models before printing them out to the AIoutput.txt file. 

## Installation
You need to pip install transformers, selenium, and sentencepiece

## How to Use
Write three separate lines of information you want an AI to respond to in AIprompt.txt file. After that run program p1.py making sure AIprompt.txt is in the same directory as p1.py file. The program will then print the responses to a file called AIoutput.txt or create the file if it is not already present.

## Notes 
The program uses built in AI models from transformers torch library along with a tokenizer from the sentencepiece library to translate the AI response to english. The ideal step to make after this is to automate it to be able to read an entire file instead of simply reading from exactly three lines. As it stands, the program is too specific to the project and can't stand alone without being reworked.