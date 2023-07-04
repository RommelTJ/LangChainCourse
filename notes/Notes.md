# Notes

## Token Limitation Strategies

* Let's assume 1 word = 1 token
* The token limit includes both the prompt and response.
* We can divide the token limit between prompt and response.
* Summarization problem
  * Langchain: load_summarize_chain
* Strategies
  * Stuffing
    * Push everything into the prompt without any alterations
  * Map Reduce
    * All the documents map to a prompt of instruction + context
    * Then, that is mapped via the LLM call to get a summary
    * Finally, the summaries are reduced via an LLM call to a final summary
    * Advantages: Can scale and run in parallel
    * Disadvantages: Costs and there is possible loss of information
  * Refine
    * Similar to the fold function
    * The function to apply is a summarizing function
    * The initial value is an empty document
    * The list of documents are summarized using the function similar to fold left.
