import argparse

from explorer import RepositoryExplorer
from ai_selector import AIContextSelector
from reader import RepositoryReader
from planner import Planner
from editor import Editor
from writer import RepositoryWriter
from summary import Summary

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--repo", required=True, help="Path to repository")

    args = parser.parse_args()

    user_request = "Improve the application so users can better organise and search their notes."
    print(f"[PROMPT] - {user_request}")

    print("Scanning repository...\n")

    #Step 1: Explore Repository
    explorer = RepositoryExplorer()
    files = explorer.explore(args.repo)

    #Step 2: Select Relevant Files
    selector = AIContextSelector()
    selected_files = selector.select(files, user_request)

    print("Selected Files:")

    for file in selected_files:
        print(f"- {file}")

    #Step 3: Read File Contents
    reader = RepositoryReader()
    file_contents = reader.read_files(
        args.repo,
        selected_files
    )

    #Step 4: Create Plan
    task = {
        "request": user_request,
        "files": file_contents
    }
    
    planner = Planner()
    print("\nGenerating implementation plan...\n")
    plan = planner.create_plan(task)
    print(plan)


    #Step 5: Edit Files
    editor = Editor()
    writer = RepositoryWriter()

    #created for summary
    updated_files = []
    print("\nUpdating files...\n")
    for path, code in file_contents.items():

        print(f"Editing {path}...")

        updated_code = editor.edit_files(
            path,
            code,
            user_request
        )

        writer.write_file(
        args.repo,
        path,
        updated_code
        )
        updated_files.append(path)

        print(f"Updated {path}")
    print("\n Repository updated successfully.")

    summary = Summary()

    summary.print_summary(
        updated_files,
        user_request
    )

if __name__ == "__main__":
    main()