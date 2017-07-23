# ML-NLP


The Parity App uses the following Natural Language Processing and Machine Learning routines for answering the users queries.

## Algoritms Implemented:
### 1. For Message Summary:
#### (a) KL Divergence : (Implemented from scratch)
 Greedily adds sentences to a summary so long as it decreases the KL Divergence.
#### (b) LexRank : (Implemented from scratch) 
 It creates a graph amongst all sentences of the messages and chooses the best sentences to create the summary based on the set threshold.
  
#### (c) Gensim:
A opensource python library providing various functions including summary generation.
        
### 2. For Keyword Extraction:
#### (a) Rapid Automatic Keyword Extraction(RAKE):
It calculates the score of phrases and words based on the frequency of occurrence, after removing stop words and punctuation
          
#### (b) Multigrain LDA :
Built on top of LDA it is used to identify global topics (across multiple documents) and local topics (in the same topic documents). Further Reading: http://www.cs.cmu.edu/~pengtaox/poster/uai2013poster.pdf, https://arxiv.org/abs/0801.1063
 
#### (c) Gensim :
A opensource python library providing various functions including keyword Extraction

### 3. Representative Messages:
#### (a) Gensim :
A opensource python library provides keyword tokens

  
