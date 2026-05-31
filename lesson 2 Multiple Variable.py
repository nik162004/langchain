from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["topic", "language"],
    template="Teach {topic} using {language} examples."
)

prompt = template.format(topic="Loops", language="Python")

print(prompt)