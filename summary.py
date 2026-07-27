class Summary:

    def print_summary(self, updated_files, user_request):

        print("\n===================================")
        print("Execution Summary")
        print("===================================\n")

        print(f"Feature Request:\n- {user_request}\n")

        print(f"Files Modified ({len(updated_files)}):")

        for file in updated_files:
            print(f"- {file}")

        print("\nStatus:")
        print("✓ Repository updated successfully.")