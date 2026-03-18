# AGENTS.md

Welcome to the **arbol-categorias** repository. This file provides critical context and guidelines for AI agents and developers operating in this codebase.

## 0. Repository Purpose & Architecture
**CRITICAL:** This repository is a read-only visual mirror. Its sole purpose is to display the category tree managed in `rc-easy-matches-dl`.
*   **Source of Truth:** `/Users/abustamantev/Documents/github/rc-easy-matches-dl/notebooks/classification_engine/rc_tree.json` (specifically on the `main` branch).
*   **DO NOT** manually edit `rc_tree.json`, `readme.md`, or `index.html` to add or modify categories.
*   **ALWAYS** use the provided python script to sync changes from the source repository.

## 1. Build, Lint, and Test Commands

This project is a static web application built with plain HTML, CSS, and JavaScript. It does not use a bundler, a package manager, or a testing framework.

*   **Build / Update (CRITICAL)**: To update the repository with the latest categories, run the sync script:
    ```bash
    python3 update_tree.py
    ```
    This script will fetch the JSON from the source repo, update `rc_tree.json`, regenerate `readme.md`, and rebuild `index.html`.
*   **Run Locally**: To serve the project locally and prevent potential CORS issues with local files, use a basic HTTP server:
    ```bash
    python3 -m http.server 8000
    ```
    Access at `http://localhost:8000`.
*   **Lint**: There are no automated linters configured. Follow the manual code style guidelines below.
*   **Test**: Testing is manual. Run the `update_tree.py` script, serve the directory locally, load `index.html` in a browser, and confirm the Markmap tree renders correctly and interactively.

## 2. Code Style Guidelines

### General Architecture
*   **Simplicity**: Maintain the current simple architecture. Do not introduce package managers (`package.json`), build tools, or heavy frameworks (React, Vue) unless explicitly instructed by the user.

### HTML & CSS
*   Use semantic HTML5. Maintain proper indentation.
*   CSS is housed within the `<style>` block in `<head>`.
*   Avoid adding external CSS frameworks (like Tailwind or Bootstrap). Rely on standard CSS and the existing Markmap rendering.

### JavaScript & Data Handling
*   We use `markmap-autoloader` via unpkg/jsdelivr CDN to automatically render Markdown into a mindmap.
*   The raw Markdown tree data is injected into a `<script type="text/template">` inside a `<div class="markmap">` tag.
*   **Data Updates**: The tree data is updated ONLY by running `update_tree.py`. Do not write JS to fetch the JSON dynamically, as GitHub Pages needs the static HTML for SEO and immediate rendering.

### Python Script (`update_tree.py`)
*   Use standard library only (`json`, `subprocess`, `sys`, `os`).
*   Ensure explicit UTF-8 encoding when reading and writing files.
*   Maintain clear function separation for fetching, transforming, and writing files.

### External Rules Configuration
*   **Cursor Rules**: Not currently implemented.
*   **Copilot Rules**: Not currently implemented.
