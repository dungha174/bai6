print ("Hà Mạnh Dũng")
print("235752021610006")
class ReverseString:
    def __init__(self, sentence):
        self.sentence = sentence
    
    def reverse_words(self):
        words = self.sentence.split()
        reversed_sentence = ' '.join(reversed(words))
        return reversed_sentence

# Ví dụ sử dụng class ReverseString
sentence = 'hello .py'
reverse_string = ReverseString(sentence)
result = reverse_string.reverse_words()
print("Chuỗi đảo ngược:", result)

