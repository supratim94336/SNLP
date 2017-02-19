from __future__ import division;
import nltk
import string;
import codecs;
import re;
import matplotlib.pyplot as plt;
from math import log10, log1p;
#--In this portion of code we are reading a file and saving the words_list in a varibale
f_deu=codecs.open("/Users/Supra/Downloads/Brown_Corpus.txt", 'r', 'utf-8');
words = [re.sub(r'[^\w\s]','',word) for word in f_deu.read().split(" ")];
#--Creating an empty list where we can save the words in lower case
wordz = [];
wordz = [word.lower() for word in words];
#--Creating a list of words which are appearing after 'of'/'the'
of_lst = [];
for i in range(len(wordz)):
    if(wordz[i] == "of"):
   #if (wordz[i] == "of"):
        of_lst.append(wordz[i + 1]);
count_of = wordz.count("of")
#count_of = wordz.count("of")
uni_of_lst = set(of_lst);
uni_of_lst_new = list(uni_of_lst);
#--Now we are making a list to save the counts of each unique word
count_of_lst = [];
#--Here we are searching for the unique words in the wordlist to count how mant times they are actually present in the text
for word in uni_of_lst_new:
    count = 0;
    for or_word in of_lst:
        if(word == or_word):
            count = count + 1;
    count_of_lst.append(count);
print count_of_lst;
#--Creating MLE probability distribution
prob_dist_of = [(x/(count_of)) for x in count_of_lst];
print prob_dist_of;
#--Calculating entropy
print "Entropy value is: ", sum(-x*log10(x)/log10(2) for x in prob_dist_of);
#--Creating rank and frequency of the words appearing after 'of'/'the'
rank = [];
freq = [];
n = 1
for count in count_of_lst:
    i = count_of_lst.index(max(count_of_lst));
    rank.append(uni_of_lst_new[i]);
    freq.append(max(count_of_lst));
    print "\'",uni_of_lst_new[i],"\'", "with frequency",max(count_of_lst),"is ranked", n;
    count_of_lst.remove(max(count_of_lst));
    uni_of_lst_new.remove(uni_of_lst_new[i]);
    n = n+1;
#--Plotting the first 50 most frequent words appearing after 'of'/'the'
plt.figure();
plt.loglog(freq[:50],label= "Freq vs Rank");
plt.grid(True);
plt.show();