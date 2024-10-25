from langchain import LLMChain
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Set up the model and tokenizer
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Set up the LLM chain
llm_chain = LLMChain(llm=model, tokenizer=tokenizer)
