# Prompt Engineering

## What is Language Modeling?

* A prediction of what should be the next word (words with the highest probability)
* Formal definition
  * Given a sequence of words: x1, x2, ..., xt
  * Compute the probability distribution of the next word: P(xt+1 | x1, x2, ..., xt) 
    * I.E. What is the probability of xt+1 given the previous words.
    * Note that the word xt+1 has to be in the vocabulary (notated with "v")
* Large Language Model (LLM)
  * A language model trained on a huge amount of data
  * It guesses word after word after word based on probability

## What is a Prompt? Composition of a formal prompt

* A prompt is a specific input or task given to a language model to generate a desired output.
* Components of a Prompt
  * Instructions
    * Which tasks need to be performed
  * Context
    * Additional information to fine-tune the instruction
  * Input Data
    * The data that the model will process
  * Output Indicator
    * It signals the AI model that we expect a response now.

