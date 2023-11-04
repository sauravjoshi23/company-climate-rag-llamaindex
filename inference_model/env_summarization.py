import together
import os
from dotenv import load_dotenv
# Load the environment variables from .env
load_dotenv()

# Access the TOGETHER_API variable
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
MODEL_NAME = "togethercomputer/llama-2-70b-chat"
together.api_key = TOGETHER_API_KEY

def create_prompt(system_prompt: str, context: str):
    """https://docs.together.ai/docs/chatbot
    """
    prompt = f"<s>[INST] SYS{system_prompt}<</SYS>>\n\n"

    prompt += context + "[/INST]"

    return prompt

def summarize_text(prompt: str) -> str:

    output = together.Complete.create(
        prompt = prompt, 
        model = MODEL_NAME, 
        max_tokens = 256,
        temperature = 0.7,
        top_k = 50,
        top_p = 0.7,
        repetition_penalty = 1,
        stop = ['</s>']
    )

    return output['output']['choices'][0]['text']


def main(context_list: list) -> list:

    if not TOGETHER_API_KEY:
        print("TOGETHER_API not found in the .env file.")

    sys_prompts = {
       "env_impact": "Your mission is to provide accurate and concise summaries for recycling, CO2 emissions, and renewable energy in bullet points" ,
        #  "bullet_point": "Your mission is to provide accurate and concise summaries of top 4 environmental reports related to companies environmental footprints in 4 bullet points."
    #    "water_impact": "Your task is to deliver precise and succinct summaries of water environmental reports that pertain to a company's efforts in promoting water conservation."
    }

    list_of_ouputs = []
    for context in context_list: # Company's list
        for sys_prompt in sys_prompts.keys():
            prompt = create_prompt(sys_prompt, context)
            output = summarize_text(prompt)
            list_of_ouputs.append(output)
    return list_of_ouputs
    

if __name__ == '__main__':

    # Examples

    # String
    # apple_env_context = (
    #     "Apple Energy, LLC is a wholly-owned subsidiary of Apple Inc. that sells solar energy. "
    #     "As of June 6, 2016, Apple's solar farms in California and Nevada have been declared to provide 217.9 megawatts of solar generation capacity. "
    #     "In addition to the company's solar energy production, Apple has received regulatory approval to construct a landfill gas energy plant in North Carolina. "
    #     "Apple will use the methane emissions to generate electricity.[317] Apple's North Carolina data center is already powered entirely with energy from renewable sources.")

    # File
    # Open the .txt file for reading
    with open('wikipedia_data_sample/apple.txt', 'r') as file:
        # Read the entire content of the file into a string
        file_contents = file.read()

    
    context_list = []
    context_list.append(file_contents)

    outputs = main(context_list)
    for output in outputs:
        print(output)
    