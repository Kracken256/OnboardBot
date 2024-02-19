import random


finished_message = 'We are finished! Thanks for your help! A team member will reach out to you soon.'

def get_onboarding_prompt(message_history, model_meta, model_schema, current_data):
    prompt = '''
    [INST]You are helping a user onboard onto a new system that needs data from them.
    I'm going to provide you with the message history so far and with the data model that is required.
    You will respond in JSON with two keys: `followup_response` and `current_data`.
    The `followup_response` will be a string that is a politce, succinct follow-up question to retrieve any missing data.

    For example, if I provide you with : {
        "data_model": {
            "favorite_color": "string",
            "favorite_animal": "int"
        }, "message_history": [
            {
                "role": "user",
                "content": "Red"
            }
        ]
    }
    
    then a good response from you would be:
    
    {
        "followup_response": "I also love red! Whats your favorite animal?",
        "current_data": {
            "favorite_color": "Red"
        }
    }
    
    Always respond in the above shema and make sure to include the `current_data` key even if it is empty.
    Make sure the response can be loaded using `json.loads` in Python.

    [/INST]
    '''
    
    prompt += f' Here is the data model: `{model_schema}`'
    prompt += f' Here is the metadata for the data model: `{model_meta}`'
    prompt += f' Here is the message history so far: `{message_history}`'
    
    return prompt