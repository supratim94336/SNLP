import string;
import codecs;
import re;
import matplotlib.pyplot as plt;
from math import log10;

#--In this portion of code we are reading a file and saving the words_list in a varibale
f_deu=codecs.open("/Users/Supra/PycharmProjects/untitled/.idea/Harry_Potter_Eng.txt", 'r', 'utf-8');
#f_deu=codecs.open("/Users/Supra/PycharmProjects/untitled/.idea/Harry_Potter_French.txt", 'r', 'utf-8');
#f_deu=codecs.open("/Users/Supra/PycharmProjects/untitled/.idea/Harry_Potter_Deutsch.txt", 'r', 'utf-8');
words = [re.sub(r'[^\w\s]','',word) for word in f_deu.read().split(" ")];

#--Now we are checking the unique words in words_list
unique_words = set(words);
print unique_words;

#--Now we are making a list to save the counts of each unique word
count_lst = [];
#count_log_lst = [];

#--Here we are searching for the unique words in the wordlist to count how mant times they are actually present in the text
for word in unique_words:
    count = 0;
    for or_word in words:
        if(word == or_word):
            count = count + 1;
    print count , "times the word" , word , "is present";
    count_lst.append(count);
    #count_lst.append(log10(count));

#--Now we are ranking the counts of the words
count_lst.sort(reverse=True);

print count_lst;
print len(count_lst);

#--Here we are plotting the count vs rank graph
plt.figure();
plt.loglog(count_lst,label="Word vs Freq Stemmed Eng");
plt.grid(True);
#plt.plot(count_lst);
plt.show();

