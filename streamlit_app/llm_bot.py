# Description: This file contains the logic for the LLM bot
def dummy_bot(msg):
    return "Dummy bot: I'm a dummy bot"

def echo_bot(msg):
    return 'Echo: {}'.format(msg)

def simple_llm(msg):
    return 'Simple LLM: {}'.format(msg)

def createmail(content, product, about, action, role, persona, painpoint, length, language):


# Azure OpenAI setup
    api_base = "https://oneitaiwestus.openai.azure.com/" # Add your endpoint here
#    api_key = os.getenv("OPENAI_API_KEY") # Add your OpenAI API key here
    deployment = "gpt4o" # Add your deployment ID here
    api_version = "2024-02-15-preview"
    api_key = "34956c127e814bfa9dc37e02ffc3b27b"
    
    class BringYourOwnDataAdapter(requests.adapters.HTTPAdapter):

        def send(self, request, **kwargs):
            request.url = f"{api_base}/openai/deployments/{deployment}/extensions/chat/completions?api-version={api_version}"
            return super().send(request, **kwargs)

    session = requests.Session()

    # Mount a custom adapter which will use the extensions endpoint for any call using the given `deployment_id`
    session.mount(
        prefix=f"{api_base}/openai/deployments/{deployment}",
        adapter=BringYourOwnDataAdapter()
    )
    client = AzureOpenAI(api_version=api_version, azure_endpoint=api_base, api_key=api_key)
    
    
# Azure AI Search setup
    search_endpoint = "https://oneitaisearchs1.search.windows.net"; # Add your Azure AI Search endpoint here
#    search_key = os.getenv("SEARCH_KEY"); # Add your Azure AI Search admin key here
    search_index_name = "lmspublic"; # Add your Azure AI Search index name here
    search_key = "QZMIdUZycLKffQ2tgiHjRkrknJ4fDEhdhTCvVYDjJCAzSeCbcmVW"
#    setup_byod(deployment_id)
    logging.info('Python HTTP trigger function processed a request.')

    
    
    if not content:
        content = "Tell me what I can ask you about?"
    message_text = [{"role": "user", "content": "Tell me about leica products?"}]
    if not product:
        product = "Stellaris 8"
    if not about:
        about = "best solution for cancer research, rapid procedures, flexibility and manoeuvrability"
    if not action:
        action = "call your salerep now for enhanced discount"
    if not role:
        role = "Microsopy Expert"
    if not persona:
        persona = "Buying Manager"
    if not painpoint:
        painpoint = "maximize use of systems, simplify workflows, better medical outcomes"
    if not length:
        length = "250"
    if not language:
        message_text = [{"role": "user", "content": f"Write about {product}. The email main objective is to {action}. Your main target audience are {persona}. Their main pain point is {painpoint}. Write as a {role}. Limit the response to {length} words"}]
    else: 
        message_text = [{"role": "user", "content": f"Write about {product}. The email main objective is to {action}. Your main target audience are {persona}. Their main pain point is {painpoint}. Write as a {role}. Limit the response to {length} words"},{"role": "user", "content": f"Write the answer in {language}"}]


    print(message_text)



    completion = client.chat.completions.create(
        model=deployment,
        messages=message_text,
        temperature=0,
        top_p=1,
        max_tokens=800,
        stop=None,
        stream=False,
        #response_format={"type": "json_object"},
        extra_body={
            "data_sources": [  # camelCase is intentional, as this is the format the API expects
                {
                "type": "azure_search",
                "parameters": {
                    "endpoint": "https://oneitaisearchs1.search.windows.net",
                    "index_name": "lmspublic",
                    "semantic_configuration": "default",
                    "query_type": "semantic",
                    "fields_mapping": {},
                    "in_scope": True,
                    "role_information": "You are marketing content expert. You help come up with creative content ideas and content like marketing emails, blog posts, tweets, ad copy and product descriptions. You write in a straight-forward and friendly yet professional tone but can tailor your writing style that best works for a user-specified audience. If you do not know the answer to a question, respond by saying \"I do not know the answer to your question.\". Output your answer in the form of an email to a customer. Define Subject message, pre-header text and text message. Email to be sent with email automation system with logo and header image. Provide a title and subtitle before introducing message without initial greeting. Do not add references to the response.",
                    "filter": None,
                    "strictness": 3,
                    "top_n_documents": 5,
                    "authentication": {
                        "type": "api_key",
                        "key": "QZMIdUZycLKffQ2tgiHjRkrknJ4fDEhdhTCvVYDjJCAzSeCbcmVW"
                    },
                    "embedding_dependency": {
                        "type": "deployment_name",
                        "deployment_name": "ada2"
                    }

                }
                }
            ]

        
        }
   

    )
    logging.info(completion)
    #jcomp = json.dumps(completion, indent=2)
    #parsed_response = json.loads(completion)
#    contents = [message['content'] for message in parsed_response]
    return (f"{completion.choices[0].message.role}: {completion.choices[0].message.content}")
