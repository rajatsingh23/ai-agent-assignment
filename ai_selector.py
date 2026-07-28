from llm import GeminiClient

class AIContextSelector:
    def __init__(self):
        self.llm = GeminiClient()
    def select(self, files, user_request):
        tree = "\n".join(files)
        print("\nAI Selector is selecting the files\n")
        prompt = f"""
You are helping an AI coding agent

Repository files:
 {tree}

User request:

{user_request}

Return ONLY the file paths that are most relevant.

Rules:
-One file per line.
-No Explanations.
-Do not invent files.
"""
        response = self.llm.generate(prompt)

        return [
            path.strip().strip("-").strip("`").strip()
            for path in response.splitlines()
            if path.strip()
            ]