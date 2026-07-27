from pathlib import Path

class ContextSelector:

    IMPORTANT_FILES = [
        "package.json",
        "server.js",
        "app.js",
        "index.js"
    ]

    IMPORTANT_FOLDERS = [
        "routes",
        "controllers",
        "models",
        "config"
    ]

    def select(self, files):
        selected = []

        for file in files:
            filename = Path(file).name

            if filename in self.IMPORTANT_FILES:
                selected.append(file)
                continue

            parts = Path(file).name

            if filename in self.IMPORTANT_FILES:
                selected.append(file)
                continue

            parts = Path(file).parts

            if any(folder in parts for folder in self.IMPORTANT_FOLDERS):
                selected.append(file)

        return selected