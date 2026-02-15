# New Service Pipeline Pattern (GitHub Actions)

This repo provides reusable workflow entrypoints used by application repos.

## Recommended Minimal CI for a New Service
Pick the language-specific test workflow + the docker build/push workflow.

Examples in this repo:
- Node tests: `.github/workflows/tests-node.yml`
- Python tests: `.github/workflows/tests-python.yml`
- Go tests: `.github/workflows/tests-go.yml`
- Build + push image: `.github/workflows/docker-build-push.yml`

## Optional Add-ons
- Helm values bump (GitOps pin): `.github/workflows/helm-release-bump.yml`
- Argo refresh/sync: `.github/workflows/deploy-argocd.yml`
- Render deploy (if used): `.github/workflows/render-deploy.yml`

## Typical Flow (Production Mindset, Resource-Friendly)
1. Run unit tests + lint.
2. Build a multi-arch image and push to GHCR with tag `staging-<sha7>`.
3. Update the pinned image tag in `platform-gitops` values file.
4. Argo auto-sync reconciles the cluster.

## Cross-Repo Links
- GitOps: [`temitayocharles/platform-gitops`](https://github.com/temitayocharles/platform-gitops) ([docs/NEW_SERVICE.md](https://github.com/temitayocharles/platform-gitops/blob/main/docs/NEW_SERVICE.md))
- Charts: [`temitayocharles/helm-charts`](https://github.com/temitayocharles/helm-charts) ([docs/NEW_SERVICE.md](https://github.com/temitayocharles/helm-charts/blob/main/docs/NEW_SERVICE.md))
- Vault boundaries: [`temitayocharles/vault-ops`](https://github.com/temitayocharles/vault-ops) ([docs/NEW_SERVICE.md](https://github.com/temitayocharles/vault-ops/blob/main/docs/NEW_SERVICE.md))
- ConfigMaps: [`temitayocharles/configurations`](https://github.com/temitayocharles/configurations)
