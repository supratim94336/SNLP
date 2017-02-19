import codecs;
import re;
#--In this portion of code we are reading a file and saving the words_list in a varibale
f_deu1=codecs.open("/Users/Supra/Downloads/Materials/train/train1.txt", 'r', 'utf-8');
train1 = [re.sub(r'[^\w\s]','',word) for word in f_deu1.read().split(" ")];
f_deu6=codecs.open("/Users/Supra/Downloads/Materials/test/test.txt", 'r', 'utf-8');
test = [re.sub(r'[^\w\s]','',word) for word in f_deu6.read().split(" ")];
def bigrammer(train):
  q_bi = []
  for i in range(0,len(train)-1):
    p=[]
    p = [train[i],train[i+1]]
    q_bi.append(p)
  return q_bi

def trigrammer(train):
  q_tri = []
  for i in range(1,len(train)-2):
    p=[]
    p = [train[i],train[i+1],train[i+2]]
    q_tri.append(p)
  return q_tri

uniq_bi_train = set(map(tuple, bigrammer(train1)))
uniq_tri_train = set(map(tuple, trigrammer(train1)))
uniq_bi_test = set(map(tuple, bigrammer(test)))
uniq_tri_test = set(map(tuple, trigrammer(test)))
print(uniq_bi_test)
print(uniq_bi_train)
def search_poly(train_words,test_words):
    p = len(test_words)
    k = p
    for te_word in test_words:
        for tr_word in train_words:
            if(tr_word==te_word):
                k = k - 1
            else:
                continue
    return k
print(len(uniq_bi_test))
print(search_poly(uniq_bi_train,uniq_bi_test))
print(search_poly(uniq_tri_train,uniq_tri_test))
