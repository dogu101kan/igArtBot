import openai

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

def caption(prompt, key):
    
    openai.api_key = key

    return generate_response("write sentece about " + prompt)
    