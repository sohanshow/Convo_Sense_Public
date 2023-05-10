from nltk.stem import WordNetLemmatizer
import nltk
import spacy.cli
# import operator
import spacy
import numpy as np
import spacy
# spacy.cli.download("en_core_web_lg")
nlp = spacy.load("en_core_web_lg")
# nltk.download('omw-1.4')
# nltk.download('wordnet')
# nltk.download('punkt')

from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
lemmatizer = WordNetLemmatizer()
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')

class DW:
    def __init__(self, window, file_path, profession):
        self.window = window
        self.window_text = ""
        self.text = ''
        self.word_freq_allwords = dict()
        self.word_count=0
        self.input_freq = dict()
        self.unique = set()
        self.oov=set()
        self.count = 0
        self.word_pos= dict()
        self.word_profession= dict()
        self.word_profession_guest = dict()
        self.sorted_unique=[]
        self.sorted_unique_guest=[]
        self.load_vocab(file_path)
        self.user_inputs(profession)
        self.lastPointer = 0
        self.isNotOutOfWindow = True
        self.profession= profession[0]
        self.profession_guest = profession[1]
        #=============================================Adding the profanity filter=======================================================
        self.bannedList = ["add", "adding", "was", "Okay", "everything","hey", "hi", "yo", "yea", "yeah", "yes", "fuck", "sex", "faggot", "maybe", "huh", "ho", "penis", "bottoming", "about", "whoa", "wo", "umm", "um", "does", "click", "shit", "ass", "dick", "whore", "bitch"]



    def user_inputs(self, profession):
        self.bar= 10000
        self.profession= profession[0]
        self.profession_guest = profession[1]



    def get_unique(self):

        self.unique= set()
        self.all_word_freq = []
        self.input_freq = dict()
        self.word_pos = dict()
        #self.unique=set()
        self.all_word_freq = []
        doc = nlp(self.window_text)
        for token in doc:
            self.word_count+=1
            #if(self.word_count%self.window==0):
            #self.update_bar()

            token = str(token)
            if not token.isalpha():
                continue
            if token in self.bannedList:
                continue
            t = lemmatizer.lemmatize(token)
            try:
                if t in self.word_freq_allwords:
                    self.all_word_freq.append(self.word_freq_allwords[t])
                    if self.word_freq_allwords[t] < self.bar:
                        self.count = self.count+1
                        self.word_pos[token]=self.count
                        if token not in self.input_freq:
                            self.word_profession[token] = self.get_word_profession(t,self.profession)
                            self.word_profession_guest[token] = self.get_word_profession(t,self.profession_guest)
                            self.input_freq[token] = 1
                            self.unique.add(token)
                        else:
                            self.input_freq[token] = self.input_freq[token] + 1
                            self.unique.add(token)
                else:
                    self.oov.add(token)
            except ValueError:
                continue

        sorted_unique=[]
        sorted_unique_guest = []
        temp_unique =list(set(self.unique))
        if len(temp_unique)>1:
            for u in temp_unique:
                tempBuf = self.word_pos[u] % self.window
                sorted_unique_guest.append((u, (float(self.input_freq[u])/self.word_freq_allwords[u]) * ((-0.00022*tempBuf*tempBuf) + 0.00138*tempBuf + 0.99883) * (1-self.word_profession_guest[u] )))
                sorted_unique.append((u, (float(self.input_freq[u])/self.word_freq_allwords[u]) * ((-0.00022*tempBuf*tempBuf) + 0.00138*tempBuf + 0.99883) * (1-self.word_profession[u] )))
                # occurence / freq * how recent it appeared * relevance_score

                # else:
                #   sorted_unique.append((u, (self.input_freq[u]/self.word_freq_allwords[u]) * self.word_pos[u] ))


        sorted_unique_guest = sorted(sorted_unique_guest,key=lambda k: k[1],reverse = True)
        sorted_unique = sorted(sorted_unique,key=lambda t: t[1],reverse = True)

        print(sorted_unique_guest)
        self.sorted_unique_guest = [u[0] for u in sorted_unique_guest]
        self.sorted_unique = [u[0] for u in sorted_unique]



    def load_vocab(self,file_path):
        freq_file = open(file_path, encoding='utf-8')
        freq_file.readline()
        while True:
            line = freq_file.readline()
            if not line:
                break

            line = line.split(",")
            self.word_freq_allwords[line[0].strip().lower()] = int(line[1].replace(',','').strip())



    def text_input(self,text):
        if self.text != "":
            self.update_bar()
        #self.text = self.text + " " + text
        self.window_text = text

        # if (len(self.text.split(" "))> self.window):
        #     isNotOutOfWindow = False
        #     self.window_text=" ".join(self.text.split(" ")[-self.window-1:])
        # else:
        #     self.window_text = self.text


        # print('#################################################################')
        # print('This is the full text: ', self.text)
        # print('#################################################################')

        # if (self.lastPointer > self.window):
        #     workingText = self.text.split()
        #     extracted_sentence = " ".join(workingText[self.lastPointer:])
        #     # print("EXTRACED: ", extracted_sentence)
        #     # print(self.lastPointer)
        #     self.window_text= extracted_sentence
        # else:
        #     self.window_text = self.text

        # self.lastPointer = len(self.text.split())
        # print('#################################################################')
        # print('This is the window text: ', self.window_text)
        # print('#################################################################')
        self.get_unique()

    def get_person_names(self):
        doc2 = nlp(self.window_text)
        # Identify the persons
        persons = [ent.text for ent in doc2.ents if ent.label_ == 'PERSON']
        temp= []
        for x in persons:
            if x not in temp:
                temp.append(x)

        persons = temp
        # Return persons
        return persons

    def get_sentence(self,word):
        # sent_text = nltk.sent_tokenize(self.window_text)
        # for y in range(len(sent_text)):
        #     if word.lower() in sent_text[y].lower():
        #         if(y-1>=0):
        #             return str(sent_text[y-1]  + sent_text[y])
        #         else:
        #             return str(sent_text[y])
        # return "none"
        try:
            words = self.window_text.split()
            last_occurance = len(words) - 1 - words[::-1].index(word)

            start_index = max(0, last_occurance - 5)
            end_index = min(len(words), last_occurance + 5 +1)

            extracted = words[start_index:end_index]
            return ' '.join(extracted)
        except ValueError:
            return word

    def get_word_profession(self,word,prof):
        return nlp(word).similarity(nlp(prof))


    def update_bar(self):
        if len(self.all_word_freq) > 0:
            self.bar = sum(self.all_word_freq)/len(self.all_word_freq)
            self.bar = self.bar + 500
        print("Updating the bar to:" , self.bar)

    def get_relevant_def(self,word,list_of_def):
        row=[]
        rel_sent = self.get_sentence(word)
        for prof in list_of_def:
            row.append(nlp(prof).similarity(nlp(rel_sent)))
        print(rel_sent)
        return list_of_def[row.index(max(row))]

    def display_info(self):
        print("{:30s} {:30s} {:30s} {:30s}".format("word",  "Frequency" ,"Frequency in Data", "Score of word"))

        for x in self.sorted_unique:
            print("{:30s} {:8.1f} {:8.1f} {:8.4f}".format(x,self.input_freq[x] , self.word_freq_allwords[x]  , self.input_freq[x]/self.word_freq_allwords[x] * self.word_pos[x] * (1-self.word_profession[x]) ))

    def display_info_guest(self):
        print("{:30s} {:30s} {:30s} {:30s}".format("word",  "Frequency" ,"Frequency in Data", "Score of word"))

        for x in self.sorted_unique_guest:
            print("{:30s} {:8.1f} {:8.1f} {:8.4f}".format(x,self.input_freq[x] , self.word_freq_allwords[x]  , self.input_freq[x]/self.word_freq_allwords[x] * self.word_pos[x] * (1-self.word_profession_guest[x]) ))

