Here's a friendly and informative README for your action:

---

# 🐍 Fetch Latest Tag with Python Docker Action

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/brainxio/fetch-latest-tag/build-and-push.yml?branch=main&style=for-the-badge)  
Fetch the latest tag of any GitHub repository with a simple Python Docker-based GitHub Action!

## ✨ Why This Action?

- 🎯 **Straightforward**: Specify the repo owner and name, and you're set!
- 🐍 **Python Power**: Built with a lightweight Python 3.10 Alpine image.
- 🐳 **Dockerized**: Easily reusable with a pre-built Docker image.
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
         uses: actions/checkout@v4

       - name: Fetch Latest Tag with Docker
         id: fetch-latest-tag
         uses: ghcr.io/brainxio/fetch-latest-tag:latest
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
- name: Fetch Latest Tag with Docker
  id: fetch-latest-tag
  uses: ghcr.io/brainxio/fetch-latest-tag:latest
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

## 🚀 Build and Push Docker Image

This action uses a pre-built Docker image hosted on GitHub Container Registry (GHCR). Here's how to set up automatic builds:

**Workflow: `.github/workflows/build-and-push.yml`**
```yaml
name: 'Build and Push Docker Image'

on:
  push:
    tags:
      - 'v*'

jobs:
  build-and-push:
    name: Build and Push Docker Image
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2

    - name: Log in to GitHub Container Registry
      uses: docker/login-action@v2
      with:
        registry: ghcr.io
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}

    - name: Build and Push Docker Image
      uses: docker/build-push-action@v4
      with:
        context: ./action
        push: true
        tags: ghcr.io/${{ github.owner }}/fetch-latest-tag:latest,ghcr.io/${{ github.owner }}/fetch-latest-tag:${GITHUB_REF#refs/tags/}
```

## 📚 Learn More

- **GitHub Actions Documentation**: [Learn about GitHub Actions](https://docs.github.com/en/actions)
- **Docker Hub**: [Discover Docker Images](https://hub.docker.com/)

## 🎉 Give it a Try

Feel the magic of automation and see how simple it is to fetch the latest tag! 🚀
