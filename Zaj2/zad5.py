class SimpleChatbot:
    def __init__(self, question):
        self.question = question
        self.counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter >= len(self.question):
            raise StopIteration
        question = self.question[self.counter]
        self.counter += 1
        return question
        
if __name__ == "__main__":
    bot = SimpleChatbot(["Jak się nazywasz?", "Jaki jest Twój ulubiony kolor?"])
    for question in bot:
        print(question)
        input() # Użytkownik wpisuje odpowiedź