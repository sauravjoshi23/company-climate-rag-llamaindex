from llama_index import download_loader
from env_summarization import *
from data_layer import *

WikipediaReader = download_loader("WikipediaReader")
loader = WikipediaReader()

def read_data_source(company_name) -> dict:
    """Read data from Wikipedia
    """
    try:
        documents = loader.load_data(pages=[company_name])
        wikipedia_page_text = documents[0].text
        return wikipedia_page_text
    except:
        return None

def save_data(file_name: str, data: str):
    # Open the file for writing
    with open(f"{file_name}.txt", "w") as file:
        # Write the string to the file
        file.write(data)
    

def data_retriever(company_name: str) -> dict:

    # source_text = read_data_source(company_name)
    # if not source_text:
        # return None # When data is not found
    source_text = data_layer(company_name)
    
    # Store data for debugging reasons
    # save_data("wikipedia_sample_data/" + company_name, source_text)
    
    # CALL MONGO DB AND LAMMA-INDEX:
    # # TODO
        
    context_list = []
    context_list.append(source_text)
    print(context_list)
    outputs = summarizer(context_list) # return array of length 3
    output_dict = {}
    prompts_name = ['summary', 'good_for_climate', 'bad_for_climate']
    for output_name, output in zip(outputs, prompts_name):
        output_dict[output] = output_name


    return output_dict



if __name__ == '__main__':

    # Example
    output_dict = data_retriever('Microsoft')
    print(output_dict)
