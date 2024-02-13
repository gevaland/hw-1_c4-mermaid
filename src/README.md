# HOW TO - Automatic SVG Generation from Mermaid Diagrams

> This guide explains how to automatically generate SVG images from Mermaid `.mmd` files and save them in the `./docs/` directory every time changes are pushed to your GitHub repository.

### 1. Create a GitHub Actions Workflow

In your GitHub repository, navigate to the Actions tab and create a new workflow, or directly create a new file under .github/workflows/, for example, .github/workflows/mermaid-to-svg.yml.

### 2. Configure the Workflow

Add the following content to your mermaid-to-svg.yml file:

```yaml
name: Generate SVG from Mermaid

on:
  push:
    paths:
      - 'src/*.mmd'

jobs:
  mermaid-to-svg:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '20'

      - name: Install Mermaid CLI
        run: npm install -g @mermaid-js/mermaid-cli

      - name: Generate SVG images
        run: |
          mkdir -p ./docs/
          mmdc -i ./src/c4-components.mmd -o ./docs/c4-components.svg
          mmdc -i ./src/c4-containers.mmd -o ./docs/c4-containers.svg
          mmdc -i ./src/c4-context.mmd -o ./docs/c4-context.svg
          mmdc -i ./src/mindmap.mmd -o ./docs/mindmap.svg

      - name: Commit and push if changed
        run: |
          git config --global user.email "action@github.com"
          git config --global user.name "GitHub Action"
          git add ./docs/*.svg
          git commit -m "Automatically updated SVG diagrams" || echo "No changes to commit"
          git push
```

This script sets up a GitHub Action to automatically generate SVG images from your .mmd files whenever changes are pushed to those files.

### 3. Adjust Workflow Permissions

To allow the GitHub Action to commit changes to your repository, you need to adjust the workflow permissions:

- Go to Settings > Actions > General in your GitHub project.
- Scroll down to Workflow permissions.
- Select `Read and Write` permissions.

### 4. Push Changes and Verify

Push your changes to the `.github/workflows/mermaid-to-svg.yml` file to your repository. The GitHub Action will run automatically on the next push that modifies any `.mmd` file in the `./src/` directory, generating SVG images and committing them to the `./docs/` directory.
