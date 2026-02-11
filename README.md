# Reusable Pipelines

Central library of production-grade reusable GitHub Actions workflows.

## Usage
In an app repo:
```yaml
jobs:
  build:
    uses: temitayocharles/reusable-pipelines/.github/workflows/docker-build-push.yml@main
    with:
      image_name: temitayocharles/my-app
      context: .
      dockerfile: Dockerfile
    secrets:
      registry_username: ${{ secrets.DOCKERHUB_USERNAME }}
      registry_password: ${{ secrets.DOCKERHUB_TOKEN }}
```

## Included Workflows
- `docker-build-push.yml`
- `tests-python.yml`
- `tests-node.yml`
- `tests-go.yml`
- `helm-release-bump.yml`
- `deploy-argocd.yml`
- `render-deploy.yml`
