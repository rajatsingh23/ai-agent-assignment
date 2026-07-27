from pathlib import Path;

class RepositoryExplorer:
    IGNORED_DIRECTORIES = {
        ".git",
        "node_modules",
        "dist",
        "build",
        "coverage",
    }

    #File types we care about
    ALLOWED_EXTENSIONS = {
        ".js",
        ".json",
        ".md",
    }

    def explore(self, repo_path):
        repo = Path(repo_path)
        files = []

        for item in repo.rglob('*'):

            if item.is_dir():
                continue

            if any(part in self.IGNORED_DIRECTORIES for part in item.parts):
                continue

            if item.suffix not in self.ALLOWED_EXTENSIONS:
                continue

            files.append(item.relative_to(repo).as_posix())

        return sorted(files)