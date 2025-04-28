# sentiment.py

from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch
from base import BaseComponent

class SentimentAnalyzer(BaseComponent):
    def __init__(self):
        self.classifier1 = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
        self.tokenizer2 = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
        self.model2 = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
        self.labels2 = ['negative', 'neutral', 'positive']

    def run(self, prompts):
        return self.analyze(prompts)

    def classify_roberta(self, text):
        inputs = self.tokenizer2(text, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model2(**inputs)
        scores = outputs.logits.softmax(dim=1).squeeze()
        predicted_class = torch.argmax(scores).item()
        return self.labels2[predicted_class]

    def analyze(self, prompts):
        response = "This is AI 1's response (DistilBERT SST-2):\n"
        for i, prompt in enumerate(prompts, 1):
            result = self.classifier1(prompt)[0]
            label = result['label'].lower()
            if label not in {"positive", "negative"}:
                label = "neutral"
            response += f"Prompt {i}: {label}\n"

        response += "\nThis is AI 2's response (Twitter-RoBERTa):\n"
        for i, prompt in enumerate(prompts, 1):
            label = self.classify_roberta(prompt)
            response += f"Prompt {i}: {label}\n"

        return response
