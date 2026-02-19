# Shared Workflows


## Start Here
- Read [START_HERE.md](START_HERE.md) for the chronological playbook.

Central library of reusable GitHub Actions workflows and composite actions.

## Usage
In an app repo, check out this repository and call composite actions:
```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/checkout@v4
        with:
          repository: temitayocharles/shared-workflows
          path: ./.shared-workflows
      - uses: ./.shared-workflows/.github/actions/docker-push
        with:
          image_name: temitayocharles/my-app
          context: .
          dockerfile: Dockerfile
          tags: latest
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
```

## Included Workflows
- `docker-build-push.yml`
- `service-go-ci-ghcr.yml`
- `service-go-quality-build.yml`
- `service-python-ci-ghcr.yml`
- `service-python-lint-unit-matrix.yml`
- `service-node-ci-ghcr.yml`
- `gitops-dispatch.yml`
- `tests-python.yml`
- `tests-node.yml`
- `tests-go.yml`
- `helm-release-bump.yml`
- `deploy-argocd.yml`
- `render-deploy.yml`

## Composite Actions
- `gitleaks`
- `vault-init`
- `docker-build`
- `docker-push`
- `helm-bump`
- `argocd-sync`
- `trivy-scan`
- `checkov-scan`
- `snyk-scan`
- `sonarqube-scan`
- `quality-gate`

## Dependency Graph
```
app repo
  -> shared-workflows (actions + workflows)
  -> app-configs (non-secret config)
  -> helm-library (charts + values)
  -> gitops-control-plane (ArgoCD Applications)
  -> Vault (secrets)
```


## Architecture Maps
- [DEPENDENCY_LADDER.md](./DEPENDENCY_LADDER.md)
- [ARCHITECTURE.md](./ARCHITECTURE.md)
- [WORKFLOW_INVENTORY.md](./WORKFLOW_INVENTORY.md)
