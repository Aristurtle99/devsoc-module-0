import os
import json
from datetime import datetime
api_key = os.environ.get("groq_api_key")
from groq import Groq
client = Groq(api_key=api_key)
results =[]




def read_prompts(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        read_lines = f.readlines()
    lines = []
    for line in read_lines:
        
        stripped_line = line.strip()
        if stripped_line:
            lines.append(stripped_line)
        
    return lines

prompts = read_prompts("text.txt")
results = []
for prompt in prompts:
    print(f"Sending prompt: {prompt[:40]}")
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content":prompt}
        ],
    )
    response =response.choices[0].message.content
    print("  → got response")
    results.append({"prompt": prompt, "response": response})

date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
file_name = f"results_{date_time}.json"
with open(file_name, "w") as f:
    json.dump(results, f, indent=4)

print(f"{len(results)} results saved to {file_name}")

#print(response)



