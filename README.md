# 🚀 Fetch Latest Tag Action

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/brainxio/fetch-latest-tag/test-fetch-latest-tag.yml?branch=main&style=for-the-badge)  
Fetch the latest tag of any GitHub repository with this composite GitHub Action!

## ✨ Why This Action?

- 🎯 **Straightforward**: Specify the repo owner and name, and you're set!
- 🥳 **Composite Simplicity**: Directly executes the commands with no additional dependencies.
- 🌟 **Just Works**: A no-nonsense solution to retrieve the latest tag of any repo.

## 🛠️ Usage

1. **Define in your Workflow**  
   Add the following to your `.github/workflows/your-workflow.yml` file:

   ```yaml
   name: 'Fetch Latest Tag Example'
   on: [push]

   jobs:
     fetch-latest-tag:
       runs-on: ubuntu-latest

       steps:
       - name: Checkout code
         uses: actions/checkout@v2

       - name: Fetch Latest Tag
         id: fetch-latest-tag
         uses: brainxio/fetch-latest-tag@main
         with:
           owner: 'octocat'
           repo: 'Hello-World'

       - name: Print Latest Tag
         run: echo "Latest Tag: ${{ steps.fetch-latest-tag.outputs['latest-tag'] }}"
   ```

2. **Inputs**
   - `owner` (required): The owner of the GitHub repository.
   - `repo` (required): The name of the GitHub repository.

3. **Outputs**
   - `latest-tag`: The latest tag name.

### 📦 Example Outputs
```yaml
steps:
- name: Fetch Latest Tag
  id: fetch-latest-tag
  uses: brainxio/fetch-latest-tag@main
  with:
    owner: 'octocat'
    repo: 'Hello-World'

- name: Print Latest Tag
  run: echo "Latest Tag: ${{ steps.fetch-latest-tag.outputs['latest-tag'] }}"
```

The output will be:
```
Latest Tag: v1.0.0
```
