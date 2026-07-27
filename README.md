# AI Agent Assignment

## Overview

This project implements a simple AI coding agent in Python. The agent
analyses a JavaScript/Node.js repository, identifies relevant files for
a requested feature, generates an implementation plan using an LLM
(Gemini), updates the code, writes the changes back to the repository,
and prints a summary of the execution.

The project is intentionally modular so that each component has a single
responsibility and can be extended independently.

------------------------------------------------------------------------

# Architecture

    User Request
          │
          ▼
    Repository Explorer
          │
          ▼
    Context Selector
          │
          ▼
    Repository Reader
          │
          ▼
    Planner (Gemini)
          │
          ▼
    Editor (Gemini)
          │
          ▼
    Repository Writer
          │
          ▼
    Execution Summary

## Components

### `agent.py`

The entry point of the application. It orchestrates the complete
workflow by coordinating all other modules.

### `explorer.py`

Scans the repository recursively and returns a list of project files
while ignoring unnecessary directories such as `node_modules`, `.git`,
`dist`, etc.

### `context_selector.py`

Filters the discovered files and selects those that are most relevant to
application logic (for example controllers, routes, models,
configuration files, and `package.json`).

### `reader.py`

Reads the selected files from disk and stores their contents in memory
for later processing.

### `llm.py`

Provides a small wrapper around the Gemini API so the rest of the
application is independent of the underlying LLM provider.

### `planner.py`

Uses Gemini to: - understand the repository, - explain the project, -
identify files that are likely to require modification, - generate a
short implementation plan.

### `editor.py`

Receives a single file together with the user's request and asks Gemini
to generate the updated source code. It only returns code and does not
write anything to disk.

### `writer.py`

Writes the generated source code back into the repository.

### `summary.py`

Prints a concise execution summary including the feature request and the
files modified.

------------------------------------------------------------------------

# Agent Workflow

1.  Accept the repository path and feature request.
2.  Explore the repository recursively.
3.  Select the most relevant source files.
4.  Read the selected files into memory.
5.  Generate an implementation plan using Gemini.
6.  Send each selected file to Gemini for modification.
7.  Write the updated code back to disk.
8.  Display an execution summary.

------------------------------------------------------------------------

# How the Repository is Explored

The repository exploration process is intentionally lightweight:

-   Recursively scans the repository using `pathlib`.
-   Ignores generated folders and dependencies such as:
    -   `node_modules`
    -   `.git`
    -   `dist`
    -   `build`
    -   `coverage`
-   Collects only relevant source files.
-   Returns relative file paths so the project remains portable across
    operating systems.

The Context Selector then narrows the file list using simple heuristics
by prioritising common backend folders such as:

-   `controllers`
-   `routes`
-   `models`
-   `config`

and important files such as:

-   `package.json`
-   `server.js`
-   `app.js`

------------------------------------------------------------------------

# Assumptions

-   The repository is a JavaScript/Node.js project.
-   The Gemini API key is configured correctly.
-   The selected files contain enough context for Gemini to generate
    accurate modifications.
-   The user provides a clear feature request.

------------------------------------------------------------------------

# Trade-offs

## Simplicity over completeness

The Context Selector currently uses rule-based heuristics instead of
semantic code analysis. This keeps the implementation simple and easy to
understand.

## One file at a time

The Editor updates one file per LLM request. This reduces prompt
complexity and makes debugging easier, although it increases the number
of API requests.

## Direct overwrite

The Writer currently overwrites files directly. A production
implementation would create backups or generate patches before applying
changes.

## Planner output

The Planner currently returns human-readable Markdown. A future
improvement would be returning structured JSON so downstream modules can
consume the output programmatically.

## Limited project understanding

The Editor primarily edits one file at a time. Providing additional
supporting context from related files would improve the quality of
generated code and better resemble production AI coding assistants.

------------------------------------------------------------------------

# Future Improvements

-   Return structured JSON from the Planner.
-   Use Planner output to edit only the required files.
-   Provide supporting context when editing files.
-   Generate diffs instead of overwriting files.
-   Add rollback support.
-   Add automated validation and test execution after modifications.
-   Support additional programming languages and frameworks.
# AI Agent Assignment

## Overview

This project implements a modular AI coding agent in Python that
analyses a Node.js repository, identifies relevant files for a requested
feature, generates an implementation plan using Gemini, updates the
selected files, writes the changes back to the repository, and prints a
summary of the execution.

The focus of the project is to demonstrate a clean, modular architecture
where each component has a single responsibility.

------------------------------------------------------------------------

# Architecture

``` text
                 User Request
                      │
                      ▼
              Repository Explorer
                      │
                      ▼
              Context Selector
                      │
                      ▼
              Repository Reader
                      │
                      ▼
                  Planner
                      │
                      ▼
                   Editor
                      │
                      ▼
             Repository Writer
                      │
                      ▼
              Execution Summary
```

## Components

### `agent.py`

The application's entry point. It orchestrates the complete workflow by
coordinating all modules.

### `explorer.py`

Recursively scans the repository and collects project files while
ignoring directories such as `node_modules`, `.git`, `dist`, `build`,
and `coverage`.

### `context_selector.py`

Uses simple rule-based heuristics to select files that are most likely
to be relevant, such as:

-   `controllers`
-   `routes`
-   `models`
-   `config`
-   `package.json`
-   `server.js`

### `reader.py`

Reads the selected files from disk and stores their contents in memory.

### `llm.py`

A lightweight wrapper around the Gemini API used by both the Planner and
the Editor.

### `planner.py`

Analyses the selected repository files and generates:

-   a brief understanding of the project,
-   files that are likely to be modified,
-   a short implementation plan.

The planner output is intended for the user and is **not** used to drive
the editing process.

### `editor.py`

Processes one selected file at a time together with the user's request
and generates updated source code using Gemini.

### `writer.py`

Writes the generated source code back to the repository.

### `summary.py`

Prints a concise execution summary showing the feature request and the
files that were modified.

------------------------------------------------------------------------

# Agent Workflow

1.  Accept the repository path.
2.  Explore the repository recursively.
3.  Select relevant source files using rule-based heuristics.
4.  Read the selected files into memory.
5.  Generate a brief implementation plan.
6.  Send each selected file individually to the LLM for modification.
7.  Write the generated code back to the repository.
8.  Print an execution summary.

------------------------------------------------------------------------

# How the Repository is Explored

The repository is explored using Python's `pathlib` module.

The Explorer:

-   recursively scans the project,
-   ignores generated folders and dependencies,
-   returns relative file paths.

The Context Selector then narrows the list by selecting commonly used
backend folders and important project files. This reduces the amount of
code sent to the language model while keeping the implementation
straightforward.

------------------------------------------------------------------------

# Assumptions

-   The target repository is a JavaScript/Node.js project.
-   A valid Gemini API key is configured.
-   The Context Selector chooses files that contain sufficient
    information for the requested feature.
-   The generated code is reviewed before being used in production.

------------------------------------------------------------------------

# Trade-offs

## Rule-based file selection

Relevant files are selected using predefined folder and file names
instead of semantic code analysis. This keeps the implementation simple
but may include files that are not strictly required.

## One file per request

The Editor updates one file at a time. This simplifies debugging and
prompt design but increases the number of API calls.

## Planner is informational

The Planner generates a human-readable execution plan. Its output is
displayed to the user but is not used to determine which files the
Editor modifies.

## Direct file overwrite

The Writer overwrites the original files directly. A production
implementation would create backups or generate patches before applying
changes.

------------------------------------------------------------------------

# Future Improvements

-   Return structured JSON from the Planner instead of Markdown.
-   Provide additional read-only context from related files while
    editing a file.
-   Generate patches/diffs instead of overwriting files.
-   Create automatic backups before writing changes.
-   Execute tests after modifications to validate the generated code.
-   Improve file selection using semantic repository analysis instead of
    rule-based heuristics.
