import string;
import codecs;
import re;
import matplotlib.pyplot as plt;
from math import log10;
#--Stemming Rules are written in terms of English Language

#--In this portion of code we are reading a file and saving the words_list in a variable
f_deu=codecs.open("/Users/Supra/PycharmProjects/untitled/.idea/Harry_Potter_Eng.txt", 'r', 'utf-8');
words = [re.sub(r'[^\w\s]','',word) for word in f_deu.read().split(" ")];

#--Creating an append list for plotting the words
List_words = [];

#--These are the stemming rules for 'English'
for word in words:
    if (word[len(word)-1:len(word)] == "s" and word[len(word)-2]!="s"):
    #    word = word[0:len(word)-2];
        print word.replace(word[len(word) - 1:len(word)], "");
        List_words.append(word.replace(word[len(word) - 1:len(word)], ""));
    elif word[len(word) - 3:len(word)] == "ous":
        print word.replace(word[len(word) - 3:len(word)], "");
        List_words.append(word.replace(word[len(word) - 3:len(word)], ""));
    elif word[len(word)-2:len(word)] == "es":
      if not word[len(word)-3:len(word)] == "ves":
        print word.replace(word[len(word) - 2:len(word)],"");
        List_words.append(word.replace(word[len(word) - 2:len(word)],""));
      else:
        print word.replace(word[len(word) - 3:len(word)], "f");
        List_words.append(word.replace(word[len(word) - 3:len(word)], "f"));
    elif word[len(word)-3:len(word)-1] == "ing":
        if word!="something" or "thing" or "nothing" or "everything" or "anything":
          if word[len(word)-4] == word[len(word)-5]:
            print word.replace(word[len(word) - 4:len(word)-1], "");
            List_words.append(word.replace(word[len(word) - 4:len(word)-1], ""));
          else:
            print word.replace(word[len(word) - 3:len(word)] , "");
            List_words.append(word.replace(word[len(word) - 3:len(word)] , ""));
    elif word[len(word) - 2:len(word)-1] == "er":
        if word!="father" or "other" or "brother" or "sister" or "mother" or "number":
          print word.replace(word[len(word) - 2:len(word)-1], "");
        List_words.append(word.replace(word[len(word) - 2:len(word)], ""));
    elif word[len(word) - 3:len(word)] == "ers":
        print word.replace(word[len(word) - 3:len(word)], "");
        List_words.append(word.replace(word[len(word) - 3:len(word)], ""));
    elif word[len(word) - 3:len(word)] == "est":
        print word.replace(word[len(word) - 3:len(word)], "");
        List_words.append(word.replace(word[len(word) - 3:len(word)], ""));
    elif word[len(word) - 2:len(word)] == "ed":
        print word.replace(word[len(word) - 2:len(word)], "");
    elif word[len(word) - 2:len(word)] == "al":
        print word.replace(word[len(word) - 2:len(word)], "");
        List_words.append(word.replace(word[len(word) - 2:len(word)], ""));
    elif word[len(word) - 2:len(word)] == "ly":
        print word.replace(word[len(word) - 2:len(word)], "");
        List_words.append(word.replace(word[len(word) - 2:len(word)], ""));
    elif word[len(word) - 3:len(word)] == "ves":
        print word.replace(word[len(word) - 3:len(word)] , "f");
        List_words.append(word.replace(word[len(word) - 3:len(word)] , "f"));
    elif word[len(word) - 3:len(word)] == "ies":
        print word.replace(word[len(word) - 3:len(word)] , "y");
        List_words.append(word.replace(word[len(word) - 3:len(word)] , "y"));
    elif word[len(word) - 3:len(word)] == "ful":
        print word.replace(word[len(word) - 3:len(word)] , "");
        List_words.append(word.replace(word[len(word) - 3:len(word)] , ""));
    elif word[len(word) - 4:len(word)] == "less":
        print word.replace(word[len(word) - 4:len(word)] , "");
        List_words.append(word.replace(word[len(word) - 4:len(word)] , ""));
    elif word[len(word) - 5:len(word)] == "ingly":
        print word.replace(word[len(word) - 5:len(word)] , "y");
        List_words.append(word.replace(word[len(word) - 5:len(word)] , "y"));
    elif word[len(word) - 5:len(word)] == "fully":
        print word.replace(word[len(word) - 5:len(word)] , "");
        List_words.append(word.replace(word[len(word) - 5:len(word)] , ""));
    else:
        print word;
        List_words.append(word);

#--Now we are checking the unique words in words_list
unique_words = set(List_words);
print unique_words;

#--Now we are making a list to save the counts of each unique word
count_lst = [];

#--Here we are searching for the unique words in the wordlist to count how mant times they are actually present in the text
for word in unique_words:
    count = 0;
    for or_word in List_words:
        if(word == or_word):
            count = count + 1;
    print count , "times the word" , word , "is present";
    count_lst.append(count);
    #count_lst.append(log10(count));

#--Now we are ranking the counts of the words
count_lst.sort(reverse=True);

#--Printing thr count and list of words
print count_lst;
print len(count_lst);

#--Here we are plotting the count vs rank graph
#--Here we are plotting the count vs rank graph
plt.figure();
plt.loglog(count_lst);
plt.grid(True);
#plt.plot(count_lst);
plt.show();

