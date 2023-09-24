from powerpoint import getInfo
from summarize.GPTSummarize import clarifai_api_call

text = getInfo("test.pdf")
clarify = "Can you clean up and summarize this for me?:"
concatenated_string = clarify + "\n"
# print(clarifai_api_call(concatenated_string))

for i in text:
    concatenated_string += i 

print(concatenated_string)
print(clarifai_api_call(concatenated_string))