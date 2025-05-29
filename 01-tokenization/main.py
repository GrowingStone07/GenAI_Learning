import tiktoken

# fetching encoder as gpt-4o model
enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hi Asutosh, You are learning GenAI."
tokens = enc.encode(text)

print(f'Tokens : {tokens}')

Tokens = [12194, 1877, 11841, 71, 11, 1608, 553, 7524, 11820, 17527, 13]
decoded = enc.decode(Tokens)


print(f'Decoded Text : {decoded}')
