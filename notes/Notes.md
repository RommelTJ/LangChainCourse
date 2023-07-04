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

## Memory

* Co-reference Resolution
  * A task of identifying all the phrases in a text refer to the same thing.
  * Ex: "Him" == "Harrison Chase"
  * The underlying insight for all of the Langchain solutions regarding memory.
* If you have a longer conversation, ChatGPT cannot remember it due to its context limit.
* Strategies used by Langchain
  * ConversationBufferMemory
    * Save a buffer of all the history in a chat and pass it to the context of the prompt
    * Simple to use
    * Challenges with large conversations because things don't fit in the Buffer
    * https://python.langchain.com/docs/modules/memory/how_to/buffer
  * ConversationBufferWindowMemory
    * Keeps a list of conversations over time. 
    * Uses last-k interactions where we choose the "k" value.
    * Useful to avoid surpassing the token limit.
    * https://python.langchain.com/docs/modules/memory/how_to/buffer_window
  * Entity Memory
    * Remembers things about specific entities.
    * Builds a knowledge base about entities over time.
    * Stored in an entity store.
    * https://python.langchain.com/docs/modules/memory/how_to/entity_summary_memory
  * Conversation Knowledge Graph Memory
    * Uses a Knowledge-graph to recreate memory.
    * You can save context and load context variables.
    * https://python.langchain.com/docs/modules/memory/how_to/kg
  * ConversationSummaryMemory
    * Every interaction with the LLM is summarized.
    * New calls are made with the new summaries.
    * The Langchain implementation is using few-shot prompting
      * Ex: 'What do you know about him? where him is defined in a previous line'
    * https://python.langchain.com/docs/modules/memory/how_to/summary
  * ConversationSummaryBufferMemory
    * Keeps a buffer of recent interactions (as-is)
    * When we get to the buffer limit, all interactions in the buffer are saved in a summary.
    * It uses both the summary and recent messages.
    * https://python.langchain.com/docs/modules/memory/how_to/summary_buffer
  * ConversationTokenBufferMemory
    * Keeps a list of conversations over time.
    * Uses last-k interactions where we choose the "k" value, but based on tokens.
    * Useful to avoid surpassing the token limit.
    * If you exceed the token limit, Langchain will flush some messages (oldest first).
    * https://python.langchain.com/docs/modules/memory/how_to/token_buffer
  * VectorStore-backed Memory
    * Using a Vector-store like Pinecone and Weaviate
    * Every interaction is embedded and turn into a vector.
    * Vectors are stored in the Vector-store.
    * Everytime a user makes a query to the LLM, it embeds the query into a vector.
    * Then, it finds the k-closest vectors to the query of the user.
    * Those are returned as context to the LLM.
    * We don't have guarantees that the vectors are in any order.
    * This is what the RetrievalQA Chain does.
    * Advantage: Because of the database, we can store a massive amount of data/conversations with no issue.
    * Disadvantage: Latency. It takes time to embed, make API calls to the Vector-store, and perform similarity search.
    * Disadvantage: Money. It costs money to make all these API calls.
    * https://python.langchain.com/docs/modules/memory/how_to/vectorstore_retriever_memory
