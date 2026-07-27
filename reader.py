from pathlib import Path


class RepositoryReader:

    def read_files(self, repo_path, file_list):

        repo = Path(repo_path)

        file_contents = {}

        for file in file_list:
            full_path = repo / file

            try: 
                content = full_path.read_text(encoding="utf-8")

                file_contents[file] = content
            except Exception as e:
                print(f"Could not read {file}: {e}")

        return file_contents
