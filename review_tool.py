import anthropic

client = anthropic.Anthropic()

def summarize_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=500,
        messages=[
            {"role": "user", "content": f"Summarize this file:\n\n{content}"}
        ],
    )

    return "".join(block.text for block in response.content if block.type == "text")

def batch_summarize(file_paths):
    results = {}
    for i in range(len(file_paths)):
        path = file_paths[i]
        results[path] = summarize_file(path)
    return results

if __name__ == "__main__":
    files = ["README.md"]
    summaries = batch_summarize(files)
    for path, summary in summaries.items():
        print(f"{path}: {summary}")
