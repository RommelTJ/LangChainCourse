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

## Zero-shot Prompting

* A type of prompt in which the model generates an output that it has not been explicitly trained on.
* It relies on the model's ability to understand and interpret natural language.
* These are prompts without examples.
* Limitations: Accuracy. The scope might be limited and we have less control.

## Few-shot prompting

* Model is given a few examples of the result you want
* One-shot prompting
  * Give it 1 example
* Few-shot prompting
  * Give it 2+ examples
* Examples
  * https://www.bluewillow.ai/ prompts
    * Zero-shot
      * Write an image description with adjectives and nouns of a Yorkshire dog running in a winter landscape in Brazil
    * One-shot
      * Write a compressed perfect image description with adjectives and nouns of a Yorkshire dog running in a winter 
      landscape in Brazil:
      Blue dog, shimmering, snow, trees, frosted, ice, movements

      Write a compressed perfect image description with adjectives and nouns of a Yorkshire dog running in a winter
      landscape in Brazil:
    * Few-shot
      * Write a compressed perfect image description with adjectives and nouns of a Yorkshire dog running in a winter
        landscape in Brazil:
        Blue dog, shimmering, snow, trees, frosted, ice

        Write a compressed perfect image description with adjectives and nouns of a Yorkshire dog running in a winter
        landscape in Brazil:
        Red dog, Crying, snow, bees, frosted, ice

        Write a compressed perfect image description with adjectives and nouns of a Yorkshire dog running in a winter
        landscape in Brazil:
        Green dog, crying, snow, bees, frosted, ice

        Now you try writing the image description while generating your own nouns and adjectives. Plug them into a full
        description sentence.

## Chain of Thought Prompting

* Multi-step reasoning and common sense reasoning problems are hard for LLMs.
* Chain of Thought (COT) Prompting aims to decompose problems into multi-step problems to solve these problems.
* Guide the model to solve the problem like a human would
* Chain of Thought Prompting Paper
  * https://arxiv.org/pdf/2201.11903v1.pdf
* Tell it to "Explain step by step" in Zero-shot Prompting or provide it with examples in Few-shot Prompts.

## ReAct

* A paradigm that integrates language models with reasoning and acting capabilities
* This allows for dynamic reasoning and interaction with external environments to perform complex tasks
* Chain of Thoughts (COT) + Actions
* This is the basis of the idea behind LangChain

## Prompt Engineering Quick Tips

* Writing a good prompt
  * Context
    * The more context you provide to a prompt, the better the response
  * Clear, non-ambiguous task
    * Concise, clear tasks
  * Iterations
    * Repeat and refine the prompt
