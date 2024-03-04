import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
from langchain_community.llms import OpenAI

os.environ['OPENAI_API_KEY'] = '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' # cb-llm
llm = OpenAI(temperature = 0.6)

def generate_restaurant_name_and_items(cuisine):
    # Chain 1
    prompt_template_name = PromptTemplate(
    input_variables = ['cuisine'],
    template = "I want to open a restaurant for {cuisine} food. Suggest a fancy name for the same."
)
    name_chain = LLMChain(llm = llm, prompt = prompt_template_name, output_key = "restaurant_name")

# Chain 2
    prompt_template_items = PromptTemplate(
    input_variables = ['restaurant_name'],
    template = "Suggest some menu items for {restaurant_name}. Return it as comma seperated values"
)
    food_items_chain = LLMChain(llm = llm, prompt = prompt_template_items, output_key = "menu_items")

    chain = SequentialChain(
    chains = [name_chain, food_items_chain],
    input_variables = ['cuisine'],
    output_variables = ['restaurant_name', 'menu_items']
)

    response = chain({'cuisine': cuisine})
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))