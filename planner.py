from llm import GeminiClient

class Planner:
    def __init__(self):
        self.llm = GeminiClient()

    def create_plan(self, task):
        files = task["files"]
        user_request = task["request"]
        context = ""

        for path, content in files.items():

            context += f"""
==================================================

File:
{path}

Content:

{content}

"""
        prompt = f"""
You are an expert software engineer.
A user wants the following feature:

{user_request}

Repository context:

{context}


Your task:

1. Explain what kind of project this is.
2. List ONLY the files that probably need to change.
3. Explain why each file needs to change.
4. Describe the implementation plan.

Return Markdown.
"""
        return self.llm.generate(prompt)