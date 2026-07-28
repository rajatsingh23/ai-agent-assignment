from llm import GeminiClient


class Editor:

    def __init__(self):
        self.llm = GeminiClient()

    def edit_files(self, file_path, current_code, user_request):
        prompt = f"""
You are an expert software engineer.

Your task is to modify the following file.

File Path:
{file_path}

Current Code:

```javascript
{current_code}
```

User Request:

{user_request}

Rules:

Modify ONLY this file.
Preserve the existing coding style and formatting where possible.
Do not remove existing functionality unless it is required.
Do not add explanations or comments about your changes.
Return ONLY the complete updated source code.
Do NOT wrap the code in Markdown code fences (```).
"""
        return self.llm.generate(prompt)