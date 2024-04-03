from transformers import AutoTokenizer

class Tokenizer:
    def __init__(self, tokenizer_name="mistralai/Mixtral-8x7B-Instruct-v0.1"):
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)

    def count_tokens(self, text):
        tokens = self.tokenizer.tokenize(text)
        return len(tokens)
