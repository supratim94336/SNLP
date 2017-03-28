from __future__ import division;
import nltk
import matplotlib.pyplot as plt
from math import log10;
from nltk.corpus import brown
from collections import Counter

#nltk.download()
#corpus import brown
#brown.words
words = []
of_lst_frequency = []
of_lst_unique =[]
of_lst = []

tokens = brown.words(categories='romance')

# Lowecase the tokens
for word in tokens:
   words.append(word.lower())

# Getting list of words before word 'of'
for i in range(0,len(words)-1):
   if(words[i] == "the" and i!=len(words)-1):
       of_lst.append(words[i+1])

of_count_dictionary = Counter(of_lst)
print(of_count_dictionary)

''''
#Creating list of Unique Words in 'of_lst' and list of corresponding frequency in of_lst_frequency
for word in of_lst:
   if word not in of_lst_unique:
       of_lst_unique.append(word)
       of_lst_frequency.append(of_lst.count(word))
print(of_lst_unique)
print(of_lst_frequency)


# Conditional probability distribution of word 'of'
of_cp =[]
for word in of_lst_unique:
   f = of_lst_frequency[of_lst_unique.index(word)]
   of_cp.append(f/words.count("the"))
'''''

# Conditional probability distribution of word 'of'
of_cp =[]
for word, count in of_count_dictionary.items():
   of_cp.append(count/words.count("the"))


print(of_cp)
print(max(of_cp))

of_entropy = sum(-x*log10(x)/log10(2) for x in of_cp)
print(of_entropy)


values = sorted(map(int,of_count_dictionary.values()), reverse = 'true')[:50]
print values
''''
count_of_lst_alt = of_lst_frequency;
rank = [];
freq = [];
n = 1
for count in of_lst_frequency:
   i = of_lst_frequency.index(max(of_lst_frequency));
   #print prob_dist_of[i];
   rank.append(of_lst_unique[i]);
   freq.append(max(of_lst_frequency));
   print("\'",of_lst_unique[i],"\'", "with frequency",max(of_lst_frequency),"is ranked", n);
   of_lst_frequency.remove(max(of_lst_frequency));
   of_lst_unique.remove(of_lst_unique[i]);
   n = n+1;

plt.figure();
plt.loglog(freq,label= "Freq vs Rank");
plt.grid(True);
plt.show();
'''''
