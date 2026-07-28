from pathlib import Path

class RepositoryWriter:
    def write_file(self, repo_path, file_path, update_code):
        full_path = Path(repo_path) / file_path
        print("Writer is updating the code")
        full_path.write_text(
            update_code,
            encoding="utf-8"
        )