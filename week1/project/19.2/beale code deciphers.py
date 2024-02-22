class Decipher:
    def __init__(self, text, keys):
        self.keys = keys
        self.key_index = 0
        self.text = text.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.key_index >= len(self.keys):
            raise StopIteration

        current_key = self.keys[self.key_index]
        if current_key >= len(self.text):
            raise StopIteration

        current_element = self.text[current_key ]
        self.key_index += 1
        return current_element[0]
def read_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text

    filename = "code_decipher.txt"
    text = read_file(filename)
    print(text)
def generate_key_list(message, text):
    current=0
    while current< len(text):
        yield func(message,text[current])
        current+=1

def func(text,s):
    current=0
    while current< len(text):
        if text[current][0]== s:
            return current
        current+=1

if __name__ == "__main__":

    keys=[4, 93, 52, 12, 41, 23, 9, 1, 34, 2, 11, 111, 6, 13, 24, 99, 100, 30, 10, 26, 16, 29, 155, 32, 37, 61, 15, 42, 3, 633, 27, 70, 77, 45, 55, 43, 35, 108, 103, 56, 159, 166, 7, 8, 174, 36]
    text= read_file("code_decipher")
    iterator = Decipher(text, keys)
    result=""
    for element in iterator:
        result+=element
    print(result)
    text=text.split()
    generator =generate_key_list(text,result)
    for key in generator :
        keys.append(key)
    print(keys)