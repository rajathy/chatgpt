import openai
import os

openai.api_key_path = "/Users/rajath/openai.key"

def generate_response(prompt, file_path):
    with open(file_path, "r") as f:
        file_contents = f.read()

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt+file_contents,
        max_tokens=200,
        n=1,
        stop="\n\n",
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message

input_message = "Generate junit test case for this java file:\n\n"

fileContent = open('file', 'r')
Lines = fileContent.readlines()

for line in Lines:
    print("processing file :"+line.strip())
    response = generate_response(input_message, line.strip())
    junitFile = open("src/test/java/Test"+ tempFile, "w")
    junitFile.write(response)
    junitFile.close()
