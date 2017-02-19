import codecs;
import re;
import matplotlib.pyplot as plt;
#--In this portion of code we are reading a file and saving the words_list in a varibale
vocab = []
f_deu1=codecs.open("/Users/Supra/Downloads/Materials/train/train1.txt", 'r', 'utf-8');
train1 = [re.sub(r'[^\w\s]','',word) for word in f_deu1.read().split(" ")];
vocab.append(len(set(train1)))
f_deu2=codecs.open("/Users/Supra/Downloads/Materials/train/train2.txt", 'r', 'utf-8');
train2 = [re.sub(r'[^\w\s]','',word) for word in f_deu2.read().split(" ")];
vocab.append(len(set(train2)))
f_deu3=codecs.open("/Users/Supra/Downloads/Materials/train/train3.txt", 'r', 'utf-8');
train3 = [re.sub(r'[^\w\s]','',word) for word in f_deu3.read().split(" ")];
vocab.append(len(set(train3)))
f_deu4=codecs.open("/Users/Supra/Downloads/Materials/train/train4.txt", 'r', 'utf-8');
train4 = [re.sub(r'[^\w\s]','',word) for word in f_deu4.read().split(" ")];
vocab.append(len(set(train4)))
f_deu5=codecs.open("/Users/Supra/Downloads/Materials/train/train5.txt", 'r', 'utf-8');
train5 = [re.sub(r'[^\w\s]','',word) for word in f_deu5.read().split(" ")];
vocab.append(len(set(train5)))
f_deu6=codecs.open("/Users/Supra/Downloads/Materials/test/test.txt", 'r', 'utf-8');
test = [re.sub(r'[^\w\s]','',word) for word in f_deu6.read().split(" ")];
u_t = set(test)

def search(train_words,test_words):
    uniq_train = set(train_words)
    uniq_test = set(test_words)
    p = len(uniq_test)
    k = p
    for te_word in uniq_test:
        for tr_word in uniq_train:
            if(tr_word==te_word):
                k = k - 1
            else:
                continue
    return k
OOV_rate = []
oov_train1 = float(search(train1,test))/float(len(u_t))
print(oov_train1)
OOV_rate.append(oov_train1)
oov_train2 = float(search(train2,test))/float(len(u_t))
print(oov_train2)
OOV_rate.append(oov_train2)
oov_train3 = float(search(train3,test))/float(len(u_t))
print(oov_train3)
OOV_rate.append(oov_train3)
oov_train4 = float(search(train4,test))/float(len(u_t))
print(oov_train4)
OOV_rate.append(oov_train4)
oov_train5 = float(search(train5,test))/float(len(u_t))
print(oov_train5)
OOV_rate.append(oov_train5)

print(vocab)
plt.figure();
plt.plot(vocab,OOV_rate,label = 'OOV Plot')
plt.ylabel('OOV Rate')
plt.xlabel('Vocab Size')
plt.grid(True);
plt.show();