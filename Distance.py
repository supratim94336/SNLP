import codecs
import re
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt

f_deu = codecs.open("/Users/Supra/Downloads/Materials/poem.txt", 'r', 'utf-8')
words = [re.sub(r'[^\w\s]', '', word) for word in f_deu.read().split(" ")]

w_l = WordNetLemmatizer()
words_normal = [w_l.lemmatize(t) for t in words]

for i in range(len(words_normal)):
    if words_normal[i] == "your" or words_normal[i] == "youl":
        words_normal[i] = "you"
t_u = words_normal.count("you")

t_u_p = float(t_u)/float(len(words_normal))
k = 1
dist_lst = []
while(k<=50):
  counter = 0
  for i in range(1,len(words_normal) - k):
      if words_normal[i] == "you":
          if words_normal[i+k] == "you":
              counter += 1
  print(counter/(len(words_normal) - k + 1))
  dist_lst.append((float(counter)/(float(len(words_normal) - k + 1)))*(float(1)/(float(t_u_p**2))))
  k=k+1

plt.figure()
plt.plot(dist_lst, label="Occurrence of the word you vs distance")
plt.ylabel('Distance')
plt.xlabel('Freq of occurrence of u')
plt.grid(True)
plt.show()