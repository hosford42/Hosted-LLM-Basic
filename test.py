from llm import llm_chain

# Test the LLM
input_text = "Write a hello world program in Python."
output = llm_chain(input_text)
print(output)
