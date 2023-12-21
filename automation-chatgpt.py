import openai
import subprocess

#replace 'YOUR_API_KEY' with your OpenAI API key
API_KEY = "" #get yours at: https://platform.openai.com/account/api-keys
openai.api_key = API_KEY

def generate_python_script():
    prompt = input("Provide a brief description of your Python code:\n")
    prompt = prompt + ". Generate only the Python script, no explanations or anything else. I just want the script."

    print("-----------------------------------Generating-----------------------------------\n")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    #extract the content from the response
    content = response['choices'][0]['message']['content']

    print("-----------------------------------Result-----------------------------------\n\n")

    #remove code block formatting
    content = content.replace("```python", "")
    content = content.replace("```", "")
    print(content)

    #write the content to a Python file
    with open('generated_script.py', 'w') as f:
        f.write(content)

    return 'generated_script.py'

def execute_python_script(script_name):
    print("\n\n-----------------------------------Executing-----------------------------------")

    #open a new command prompt and execute the Python script, then pause to keep the window open
    subprocess.run(['start', 'cmd', '/k', 'python', script_name], shell=True)

if __name__ == "__main__":
    script_name = generate_python_script()
    execute_python_script(script_name)
