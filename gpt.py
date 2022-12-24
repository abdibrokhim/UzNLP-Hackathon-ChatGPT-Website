import openai


def to_gpt(promt):

    openai.api_key = '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'

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=str(f"{promt}"),
        max_tokens=50,
        temperature=0.5,
    )   

    res = response.choices[0].text

    return res

to_gpt('Assalomu aleykum in English')