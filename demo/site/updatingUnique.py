def update_bar(self):
    # if len(self.sorted_unique)/self.window > 0.15:
    #   self.bar = self.bar + jump
    #   print("Updating bar to +",self.bar)
    # elif len(self.sorted_unique)/self.window < 0.05:
    #   self.bar = self.bar - jump
    #   print("Updating bar to -",self.bar)
    freq=[]
    for x in self.unique:
        if x in self.word_freq_allwords:
            freq.append(self.word_freq_allwords[x])
    if(len(freq)>0):
        self.bar = sum(freq)/len(freq)
    print("updating bar value to :" , self.bar)



##============This is for updating all=========================

def update_bar(self):
    # if len(self.sorted_unique)/self.window > 0.15:
    #   self.bar = self.bar + jump
    #   print("Updating bar to +",self.bar)
    # elif len(self.sorted_unique)/self.window < 0.05:
    #   self.bar = self.bar - jump
    #   print("Updating bar to -",self.bar)
    if len(self.all_word_freq)>0:
        self.bar = sum(self.all_word_freq)/len(self.all_word_freq)
    print("updating bar value to :" , self.bar)