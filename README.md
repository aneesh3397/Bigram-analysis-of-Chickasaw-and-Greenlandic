# Bigram-analysis-of-Chickasaw-and-Greenlandic

This project explores what surface level phenomenon can be discovered by training a bigram model on a short text of either Chickasaw or Greenlandic. 


The models captured some obvious surface level characteristics of both languages. For 
example, the prevalence of the character sequence 'aa' is very common in both languages,
more so in Greenlandic. This was reflected in the relatively high conditional probability 
values for (a|a): ('a', 'a'): 0.24701 for Greenlandic and 0.0679 for Chickasaw. 
The same was found for the sequence 'nn' in both. Another feature captured 
was the fact that a lot of words ended with the character 'a' in Chickasaw: P('a', ' '): 0.2360
The model also captured the tendency of words to end with 't' in both these languages. 

One big difference that was captured was the total lack of 'b's in Greenlandic, as can be 
seen in the conditional probability distributions below (Chickasaw shows some variation
while Greenlandic does not):
    
Chickasaw:
{('b', 'a'): 0.47368421052631576, ('b', 'b'): 0.017543859649122806, ('b', 'c'): 0.017543859649122806, 
('b', 'd'): 0.017543859649122806, ('b', 'e'): 0.017543859649122806, ('b', 'f'): 0.017543859649122806, 
('b', 'g'): 0.017543859649122806, ('b', 'h'): 0.017543859649122806, ('b', 'i'): 0.05263157894736842, 
('b', 'j'): 0.017543859649122806, ('b', 'k'): 0.017543859649122806, ('b', 'l'): 0.017543859649122806, 
('b', 'm'): 0.017543859649122806, ('b', 'n'): 0.017543859649122806, ('b', 'o'): 0.017543859649122806, 
('b', 'p'): 0.017543859649122806, ('b', 'q'): 0.017543859649122806, ('b', 'r'): 0.017543859649122806, 
('b', 's'): 0.017543859649122806, ('b', 't'): 0.017543859649122806, ('b', 'u'): 0.017543859649122806, 
('b', 'v'): 0.017543859649122806, ('b', 'w'): 0.017543859649122806, ('b', 'x'): 0.017543859649122806, 
('b', 'y'): 0.017543859649122806, ('b', 'z'): 0.017543859649122806, ('b', ' '): 0.017543859649122806, 
('b', '#START#'): 0.017543859649122806, ('b', '#END#'): 0.017543859649122806}

 Greenlandic:
{('b', 'a'): 0.034482758620689655, ('b', 'b'): 0.034482758620689655, ('b', 'c'): 0.034482758620689655, 
('b', 'd'): 0.034482758620689655, ('b', 'e'): 0.034482758620689655, ('b', 'f'): 0.034482758620689655, 
('b', 'g'): 0.034482758620689655, ('b', 'h'): 0.034482758620689655, ('b', 'i'): 0.034482758620689655, 
('b', 'j'): 0.034482758620689655, ('b', 'k'): 0.034482758620689655, ('b', 'l'): 0.034482758620689655, 
('b', 'm'): 0.034482758620689655, ('b', 'n'): 0.034482758620689655, ('b', 'o'): 0.034482758620689655, 
('b', 'p'): 0.034482758620689655, ('b', 'q'): 0.034482758620689655, ('b', 'r'): 0.034482758620689655, 
('b', 's'): 0.034482758620689655, ('b', 't'): 0.034482758620689655, ('b', 'u'): 0.034482758620689655, 
('b', 'v'): 0.034482758620689655, ('b', 'w'): 0.034482758620689655, ('b', 'x'): 0.034482758620689655, 
('b', 'y'): 0.034482758620689655, ('b', 'z'): 0.034482758620689655, ('b', ' '): 0.034482758620689655, 
('b', '#START#'): 0.034482758620689655, ('b', '#END#'): 0.034482758620689655}

 
There are many ways one could use the information above to write code that can 
look at a piece of text and tell whether it's in Greenlandic or Chickasaw. One
obvious way would be to look for 'b's; if we find any we know the text is in Chickasaw.
However this is risky because we might have Chickasaw text that happens to not use any
'b's. A better way might be to make use of the polysynthetic nature of Greenlandic, 
which leads to less spaces. Any text that needs to be identified will have spaces. 
The relative frequency of ' ' was found to be 0.0640 for Greenlandic and 0.1466 for 
Chickasaw. If we simply calculate the relative frequency of ' ' in a given text and it
happens to be > 0.1, we can assume that the text is in Chickasaw. This method works 
remarkably well; the functions below generate a random string of text from either 
the Greenlandic or Chickasaw texts, and feed it to a function that identifies the 
text using the relative frequency of ' '. A third function runs this 10000 times
and on average the function correctly identifies the text 98% of the time. 

The lidstone smoothing with a parameter of 0.0001 performed the 
best. In general, the smaller the smoothing parameter, the better the performance. This makes 
sense because by increasing the probability of unseen events, the sum that is used to calculate
cross entropy also increases because the probabilities are added. MLE would not work well for 
this task because that would involve simply finding the most common bigrams and giving those
the highest probabilities. Such a model would not take into account the conditional probabilities
of the characters, which is what makes the bigram model effective and allows it to somewhat capture
the structure of a given language.
