from nltk.tokenize import RegexpTokenizer
from collections import Counter
import codecs;
import re;
from math import log10;

class SNLP_Functions:
    def getTokens(self, filepath):
        words = []
        f_deu = codecs.open(filepath, 'r', 'utf-8');
        tokens = [re.sub(r'[^\w\s]', '', word) for word in f_deu.read().split(" ")];
        # Lowecase the tokens
        for word in tokens:
            words.append(word.lower())
        return words

    def getDictionary(text):
        dictionary = Counter(text)
        return dictionary

    def getEntropy(text):
        entropy = 0
        dict = getDictionary(text)
        N = sum(dict.values())
        for word in text:
            value = dict.get(word)
            prob = value / N
            entropy += -(prob * log10(prob) / log10(2))
        return entropy

    def getKLDivergence(P, Q):
        dict_p = getDictionary(P)
        N_p = sum(dict_p.values())
        dict_q = getDictionary(Q)
        N_q = sum(dict_q.values())
        V_p = len(dict_p)
        V_q = len(dict_q)

        for word in P:
            kl = 0
            value = dict_p.get(word)
            prob = value / N_p
            p_lid = (prob + 0.1) / (N_p + 0.1 * V_p)

            value_q = dict_q.get(word)
            if value_q is None:
                value_q = 0

            prob_q = value_q / N_q
            q_lid = (prob_q + 0.1) / (N_q + 0.1 * V_q)

            kl += -(p_lid * log10(q_lid / p_lid) / log10(2))

        return kl
