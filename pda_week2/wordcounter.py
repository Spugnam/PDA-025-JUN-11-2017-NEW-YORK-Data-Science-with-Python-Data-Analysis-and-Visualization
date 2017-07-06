from sys import argv
script, target, number = argv

class mystr(str):
    
    def replace_all(self, char_to_replace, replacements):
        for i in range(len(char_to_replace)):
            self = self.replace(char_to_replace[i], replacements[i%len(replacements)])
        return self
    
    def split_all(self, char_to_split):
        self = self.replace_all(char_to_split,char_to_split[0])
        return self.split(char_to_split[0])  
    
def wordCounter(file_name):
    dictio = {}
    f = open(file_name, 'r')
    for line in f.readlines():
        line = line.strip()
        line = mystr.replace_all(mystr(line), ".,?!\';:", [' '])
        line = line.lower()
        line = mystr.split_all(mystr(line), [' '])
        for word in line:
            if word in dictio and word != '':
                dictio[word]+=1
            else:
                dictio[word]=1
    f.close()
    dictio = dictio.items()
    return sorted(list(dictio), key = lambda x: x[1], reverse = True)

diction = wordCounter(target)
for i in range(int(number)):
    print(diction[i])