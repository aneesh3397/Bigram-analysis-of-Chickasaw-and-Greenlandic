#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 10:16:08 2018

@author: aneeshnaik
"""
import operator
import math
import random

def getBigrams(text): #function to generate bigrams from a given text
    text.insert(0,"#START#")
    text.append("#END#")
                
    bigrams=[]
    
    for i in range(0,len(text)-1):
        bigrams.append((text[i],text[i+1]))
        
    return bigrams

def frequencyCount(text): #function that returns frequency counts of individual tokens 
    freq_dictionary = {} 
    for i in range(0, len(text)):
        for j in range(0, len(text[i])):
            if text[i][j] in freq_dictionary:
                freq_dictionary[text[i][j]] += 1
            else:
                freq_dictionary[text[i][j]] = 1
    return(freq_dictionary)
    
def biCount(text): #calculates frequency of bigrams in a list of bigrams:  
    freq_dictionary = {} 
    for i in range(0,len(text)):
        if(text[i] in freq_dictionary):
            freq_dictionary[text[i]] += 1
        else:
            freq_dictionary[text[i]] = 1
    return(freq_dictionary)
    
def rel_freq(text): #function that calculated relative frequency of tokens
    freq = biCount(text)
    num_tokens = sum(freq.values())
    output = {}
    for key in freq:
        output[key] = freq[key]/num_tokens
    sorted_output = list(reversed(sorted(output.items(), key=operator.itemgetter(1))))
    return sorted_output

    #this function takes in the training data and returns a smoothed bigram model
def c_prob(text,v,a): #text = training data, v = frequency counts of individual characters, a = smoothing parameter
    outer_dict = {}
    '''
    create a dictionary of dictionary, outer dictionary contains all 26 latin characters, the inner dictionaries that 
    correspond to each of these contain all possible bigrams that begin with that character.
    '''
    b = getBigrams(text)
    bigrams = biCount(b)
    
    for key in v:
        outer_dict[key] = {}
        for key2 in v:
            outer_dict[key][(key,key2)] = 0
                    
    for key in bigrams:
        outer_dict[key[0]][key] = bigrams[key]
        
    #'smoothing' all bigrams that have a frequency of 0:
    for key in outer_dict:
        for k2 in outer_dict[key]:
            if(outer_dict[key][k2] == 0):
                outer_dict[key][k2] = a
        
    #replace frequencies with conditional probabilites:
    for key in outer_dict:
        sum = 0.0
        for k2 in outer_dict[key]:
            sum = sum + float(outer_dict[key][k2])
        for k2 in outer_dict[key]:
            outer_dict[key][k2] = float(outer_dict[key][k2])/sum

    return(outer_dict)
        
    
def cross_entropy(test,grammar): #function to calculate cross_entropy
    e_sum = 0.0
    test_chars = frequencyCount(test)
    test_chars['#START#'] = 1
    test_chars['#END#'] = 1 
    test_bigrams = getBigrams(test)

            
    for i in range(0,len(test_bigrams)):
        num = grammar[test_bigrams[i][0]][test_bigrams[i]]
        e_sum = e_sum + math.log(num,2)
    return ((-1/len(test))*(e_sum))  

def perplexity(test,grammar): #function to calculate perplexity 
    return pow(2,cross_entropy(test,grammar))


#this function prints out the results of cross-entropy and the perplexity of both sets of test data.
def print_results():
    print('\n')

    print("Grammar: Greenlandic, Test Data: Greenlandic -> ",'\n')
    print("i) Add-one: ")   
    print("-Cross Entropy: ",cross_entropy(green_test,cp_green_add1))
    print("-Perplexity: ",perplexity(green_test,cp_green_add1),'\n')
    print("ii) Lidstone: ")
    print("-Cross Entropy: ",cross_entropy(green_test,cp_green_lid))
    print("-Perplexity: ",perplexity(green_test,cp_green_lid),'\n')
    print("iii) ELE: ")
    print("-Cross Entropy: ",cross_entropy(green_test,cp_green_ELE))
    print("-Perplexity: ",perplexity(green_test,cp_green_ELE),'\n')

    print('\n')

    print("Grammar: Greenlandic, Test Data: Chickasaw -> ",'\n')
    print("i) Add-one: ")
    print("-Cross Entropy: ",cross_entropy(chickasaw_test,cp_green_add1))
    print("-Perplexity: ",perplexity(chickasaw_test,cp_green_add1),'\n')
    print("ii) Lidstone: ")
    print("-Cross Entropy: ",cross_entropy(chickasaw_test,cp_green_lid))
    print("-Perplexity: ",perplexity(chickasaw_test,cp_green_lid),'\n')
    print("iii) ELE: ")
    print("-Cross Entropy: ",cross_entropy(chickasaw_test,cp_green_ELE))
    print("-Perplexity: ",perplexity(chickasaw_test,cp_green_ELE),'\n')

    print('\n')

    print("Grammar: Chickasaw, Test Data: Chickasaw -> ",'\n')
    print("i) Add-one: ")
    print("-Cross Entropy: ",cross_entropy(chickasaw_test,cp_chickasaw_add1))
    print("-Perplexity: ",perplexity(chickasaw_test,cp_green_add1),'\n')
    print("ii) Lidstone: ")
    print("-Cross Entropy: ",cross_entropy(chickasaw_test,cp_chickasaw_lid))
    print("-Perplexity: ",perplexity(chickasaw_test,cp_green_lid),'\n')
    print("iii) ELE: ")
    print("-Cross Entropy: ",cross_entropy(chickasaw_test,cp_chickasaw_ELE))
    print("-Perplexity: ",perplexity(chickasaw_test,cp_green_ELE),'\n')

    print('\n')
    
    print("Grammar: Chickasaw, Test Data: Greenlandic -> ",'\n')
    print("i) Add-one: ")
    print("-Cross Entropy: ",cross_entropy(green_test,cp_chickasaw_add1))
    print("-Perplexity: ",perplexity(chickasaw_test,cp_green_add1),'\n')
    print("ii) Lidstone: ")
    print("-Cross Entropy: ",cross_entropy(green_test,cp_chickasaw_lid))
    print("-Perplexity: ",perplexity(chickasaw_test,cp_green_lid),'\n')
    print("iii) ELE: ")
    print("-Cross Entropy: ",cross_entropy(green_test,cp_chickasaw_ELE))
    print("-Perplexity: ",perplexity(chickasaw_test,cp_green_ELE),'\n')

    

# read in data:
file = open("/Users/aneeshnaik/Documents/greenlandic.txt",'r', encoding='latin-1')
green = file.read()

file = open("/Users/aneeshnaik/Documents/chickasaw.txt",'r', encoding='latin-1')
chickasaw = file.read()

green_list = []
chickasaw_list = []

for i in range(0,len(green)):
    green_list.append(green[i])
    
for i in range(0,len(chickasaw)):
    chickasaw_list.append(chickasaw[i])

green_final = []
chick_final = []

#keep only alphabets and spaces 
for i in range(0,len(green_list)):
  if(green_list[i].isalpha() or green_list[i]==' '):
    green_final.append(green_list[i].lower())
    
for i in range(0,len(chickasaw_list)):
  if(chickasaw_list[i].isalpha() or chickasaw_list[i]==' '):
    chick_final.append(chickasaw_list[i].lower())
    

#split data in to training and test segments:
green_training = []
green_test = []

chickasaw_training = []
chickasaw_test = []

for i in range(0, len(green_final)):
    if(i<6567):
        green_training.append(green_final[i])
    else:
        green_test.append(green_final[i])
        
for i in range(0, len(chick_final)):
    if(i<3884):
        chickasaw_training.append(chick_final[i])
    else:
        chickasaw_test.append(chick_final[i])
        
#obtain frequency counts for characters in training data:        
green_chars = frequencyCount(green_training)
chickasaw_chars = frequencyCount(chickasaw_training)

        
#add start and end markers:
green_chars['#START#'] = 1
green_chars['#END#'] = 1  
chickasaw_chars['#START#'] = 1
chickasaw_chars['#END#'] = 1 
                
                
#generate bigrams for training data:
green_bigrams = getBigrams(green_training)
chickasaw_bigrams = getBigrams(chickasaw_training)


#obtain bigram counts:
b = biCount(green_bigrams)
b2 = biCount(chickasaw_bigrams)


#create a vocabulary that contains all 26 latin characters 
v = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','ó','á','í',' ']

#initialize and set dictionaries that hold character frequencies:
green_freq = {}
chickasaw_freq = {}

for i in range(0,len(v)):
    green_freq[v[i]] = 0
    chickasaw_freq[v[i]] = 0
    
    
green_freq['#START#'] = 0
green_freq['#END#'] = 0
chickasaw_freq['#START#'] = 0
chickasaw_freq['#END#'] = 0
               
             
k = green_chars.keys()
k2 = chickasaw_chars.keys()


for key in green_freq:
    if(key in k):
        green_freq[key] = green_chars[key]
for key in chickasaw_freq:
    if(key in k2):
        chickasaw_freq[key] = chickasaw_chars[key]   
        
        

#obtain smoothing values for add-1, lidstone and ELE smoothing and generate bigram models:                
a = input("Enter smoothing parameter for Add-1 smoothing: ")
cp_green_add1 = c_prob(green_test,green_freq,a)
cp_chickasaw_add1 = c_prob(chickasaw_test,chickasaw_freq,a)

a = input("Enter smoothing parameter for Lidstone smoothing: ")
cp_green_lid = c_prob(green_test,green_freq,a)
cp_chickasaw_lid = c_prob(chickasaw_test,chickasaw_freq,a)

a = input("Enter smoothing parameter for Expected Likelihood Estimation: ")
cp_green_ELE = c_prob(green_test,green_freq,a)
cp_chickasaw_ELE = c_prob(chickasaw_test,chickasaw_freq,a)

print(rel_freq(green_final))
print('\n')
print(rel_freq(chick_final))


print_results()
print('\n')

#generates random text, either Greenlandic or Chickasaw and returns a tuple with the text and it's identity
def gen_random(g,c):
    choice = bool(random.getrandbits(1))
    if (choice == True):
        text = g
        ID = 'greenlandic'
    else:
        text = c  
        ID = 'chickasaw'
        
    start = random.uniform(0,len(text))
    end = random.uniform(start+1,len(text))
    
    return (text[int(start):int(end)],ID)

#identifies the text using relative frequency of ' ':
def identify(unk):
    rf = rel_freq(unk)

    res = " "
    
    for i in range(0,len(rf)):
        if(rf[i][0]==' '):
            if(rf[i][1]>0.08):
                res = "chickasaw"
            else:
                res = "greenlandic"

    return res

#runs above two funtions 10000 times:
def test_10000():
    ones = 0 #ones count instances of correct identification 
    zeros = 0
    for i in range(0,10000):
        unk = gen_random(green_list,chickasaw_list)
        if(identify(unk[0])==unk[1]): #pass text to identify function and compare the result with the true identity
            ones += 1
        else:
            zeros +=1
    print((ones/10000)*100, "%")
            
print("Performance of identifier function:")
test_10000()
    
