# Workflow Inventory and Classification

Generated from GitHub Actions workflow metadata across non-archived repositories.

| Repo | Workflow | Path | Classification | Rationale |
|---|---|---|---|---|
| `a-to-z-of-networking` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `AI-adventure-game` | `CI` | `.github/workflows/ci.yml` | **shared candidate** | Standard Node test/build pattern; covered by tests-node/service-node-ci-ghcr. |
| `AI-adventure-game` | `Deploy (Production)` | `.github/workflows/deploy-production.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `AI-adventure-game` | `Deploy (Staging)` | `.github/workflows/deploy-staging.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `ArgoCD` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `autodesk-project` | `CI` | `.github/workflows/ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `cila-health-infrastructure-gitops` | `Infrastructure Lint` | `.github/workflows/lint.yaml` | **repo-specific** | Custom workflow logic. |
| `cila-health-microservices` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `cila-health-microservices` | `Device Ingestion CI` | `.github/workflows/ci.yaml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `cila-health-microservices` | `Dependabot Updates` | `dynamic/dependabot/dependabot-updates` | **repo-specific** | GitHub-managed dynamic workflow. |
| `cila-health-monolith` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `cila-health-monolith` | `Laravel CI` | `.github/workflows/ci.yaml` | **repo-specific** | Custom workflow logic. |
| `cila-health-monolith` | `Dependabot Updates` | `dynamic/dependabot/dependabot-updates` | **repo-specific** | GitHub-managed dynamic workflow. |
| `configurations` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `devops-mission-control` | `CI` | `.github/workflows/ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `devops-portfolio` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `devops-portfolio` | `Deploy to Render` | `.github/workflows/deploy-to-render.yml` | **repo-specific** | Custom workflow logic. |
| `devops-portfolio` | `Build and Push Multi-Arch Docker Image` | `.github/workflows/docker-build-push.yml` | **shared candidate** | Standard GHCR build/push pattern; covered by service-*ci-ghcr workflows. |
| `devops-portfolio` | `ui-smoke` | `.github/workflows/ui-smoke.yml` | **repo-specific** | Custom workflow logic. |
| `devops-portfolio` | `Copilot` | `dynamic/copilot-swe-agent/copilot` | **repo-specific** | GitHub-managed dynamic workflow. |
| `devops-portfolio` | `pages-build-deployment` | `dynamic/pages/pages-build-deployment` | **repo-specific** | GitHub-managed dynamic workflow. |
| `DevOps-Projects` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `dotfiles` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `emergent-lab` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `emergent-lab` | `.github/workflows/ci-cd.yml` | `.github/workflows/ci-cd.yml` | **shared candidate** | Standard GHCR build/push pattern; covered by service-*ci-ghcr workflows. |
| `Fast-Kubernetes` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `fintech-account-service` | `ci` | `.github/workflows/ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `fintech-account-service` | `Update GitOps` | `.github/workflows/dispatch-gitops.yaml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `fintech-analytics-service` | `ci` | `.github/workflows/ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `fintech-analytics-service` | `Update GitOps` | `.github/workflows/dispatch-gitops.yaml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `fintech-audit-service` | `ci` | `.github/workflows/ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `fintech-audit-service` | `Update GitOps` | `.github/workflows/dispatch-gitops.yaml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `fintech-docs` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `fintech-frontend` | `ci` | `.github/workflows/ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `fintech-frontend` | `Update GitOps` | `.github/workflows/dispatch-gitops.yaml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `fintech-gitops` | `Update Image Tags` | `.github/workflows/update-images.yaml` | **repo-specific** | Custom workflow logic. |
| `fintech-infra` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `fintech-notification-service` | `ci` | `.github/workflows/ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `fintech-notification-service` | `Update GitOps` | `.github/workflows/dispatch-gitops.yaml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `fintech-transaction-service` | `ci` | `.github/workflows/ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `fintech-transaction-service` | `Update GitOps` | `.github/workflows/dispatch-gitops.yaml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `fintech-user-service` | `ci` | `.github/workflows/ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `fintech-user-service` | `Update GitOps` | `.github/workflows/dispatch-gitops.yaml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `foodshare-app` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `Geth-prysm-go-peeer` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `hello-k8s` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `helm-charts` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `infra-environments` | `Infra Environments CI` | `.github/workflows/terraform-live-ci.yml` | **repo-specific** | Custom workflow logic. |
| `kubectl-mcp-server` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `kubectl-mcp-server` | `Build & Publish Multi-Arch Docker Image` | `.github/workflows/docker-multiarch.yml` | **shared candidate** | Standard GHCR build/push pattern; covered by service-*ci-ghcr workflows. |
| `kubectl-mcp-server` | `Publish to agentregistry` | `.github/workflows/publish-to-agentregistry.yml` | **repo-specific** | Custom workflow logic. |
| `kubectl-mcp-server` | `Publish to npm and GitHub Packages` | `.github/workflows/publish-to-npm.yml` | **repo-specific** | Custom workflow logic. |
| `kubectl-mcp-server` | `Publish to PyPI` | `.github/workflows/publish-to-pypi.yml` | **repo-specific** | Custom workflow logic. |
| `kubernetes-debugging` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `kubernetes-practice-lab` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `local-business-website-production` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `mindbridge-nigeria` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `mindbridge-nigeria` | `🚀 CI/CD Pipeline - Build, Test & Deploy` | `.github/workflows/ci-cd.yml` | **shared candidate** | Standard Node test/build pattern; covered by tests-node/service-node-ci-ghcr. |
| `musicvibe-cicd-project` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `musicvibe-cicd-project` | `MusicVibe CI` | `.github/workflows/ci-cd-pipeline.yml` | **shared candidate** | Standard Node test/build pattern; covered by tests-node/service-node-ci-ghcr. |
| `my-terraform-k8s` | `Boardgame CI` | `.github/workflows/ci-cd-pipeline.yml` | **repo-specific** | Custom workflow logic. |
| `ops-tool` | `CI` | `.github/workflows/ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `platform-gitops` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `shared-workflows` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `shared-workflows` | `Baseline Reusable` | `.github/workflows/baseline-reusable.yml` | **repo-specific** | Custom workflow logic. |
| `shared-workflows` | `ArgoCD Sync` | `.github/workflows/deploy-argocd.yml` | **repo-specific** | Custom workflow logic. |
| `shared-workflows` | `Docker Build & Push` | `.github/workflows/docker-build-push.yml` | **repo-specific** | Custom workflow logic. |
| `shared-workflows` | `GitOps Repository Dispatch` | `.github/workflows/gitops-dispatch.yml` | **shared candidate** | Standard GitOps dispatch pattern; covered by gitops-dispatch.yml. |
| `shared-workflows` | `Helm Release Bump` | `.github/workflows/helm-release-bump.yml` | **repo-specific** | Custom workflow logic. |
| `shared-workflows` | `Render Deploy` | `.github/workflows/render-deploy.yml` | **repo-specific** | Custom workflow logic. |
| `shared-workflows` | `Service CI (Go + GHCR)` | `.github/workflows/service-go-ci-ghcr.yml` | **shared candidate** | Standard GHCR build/push pattern; covered by service-*ci-ghcr workflows. |
| `shared-workflows` | `Service CI (Go Quality + Build)` | `.github/workflows/service-go-quality-build.yml` | **shared candidate** | Standard Go test pattern; covered by tests-go/service-go-ci-ghcr. |
| `shared-workflows` | `Service CI (Node + GHCR)` | `.github/workflows/service-node-ci-ghcr.yml` | **shared candidate** | Standard GHCR build/push pattern; covered by service-*ci-ghcr workflows. |
| `shared-workflows` | `Service CI (Python + GHCR)` | `.github/workflows/service-python-ci-ghcr.yml` | **shared candidate** | Standard GHCR build/push pattern; covered by service-*ci-ghcr workflows. |
| `shared-workflows` | `Service CI (Python Lint + Unit + Integration Matrix)` | `.github/workflows/service-python-lint-unit-matrix.yml` | **shared candidate** | Standard Python test pattern; covered by tests-python/service-python-ci-ghcr. |
| `shared-workflows` | `Go Tests` | `.github/workflows/tests-go.yml` | **shared candidate** | Standard Go test pattern; covered by tests-go/service-go-ci-ghcr. |
| `shared-workflows` | `Node Tests` | `.github/workflows/tests-node.yml` | **shared candidate** | Standard Node test/build pattern; covered by tests-node/service-node-ci-ghcr. |
| `shared-workflows` | `Python Tests` | `.github/workflows/tests-python.yml` | **shared candidate** | Standard Python test pattern; covered by tests-python/service-python-ci-ghcr. |
| `stack-to-k8s` | `Lab 8 Lite Validation Test` | `.github/workflows/test-lab-8-lite.yml` | **repo-specific** | Custom workflow logic. |
| `stack-to-k8s` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `TCA-InfraForge-GitOps` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `TCA-InfraForge-GitOps` | `🚀 TCA-InfraForge Development Platform` | `.github/workflows/deploy-argocd.yml` | **repo-specific** | Custom workflow logic. |
| `tca-infraforge-k8s-documentation` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `tca-infraforge-k8s-documentation` | `pages-build-deployment` | `dynamic/pages/pages-build-deployment` | **repo-specific** | GitHub-managed dynamic workflow. |
| `temitayocharles` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `temitayocharles.github.io` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `temitayocharles.github.io` | `pages-build-deployment` | `dynamic/pages/pages-build-deployment` | **repo-specific** | GitHub-managed dynamic workflow. |
| `terraform-aws-eks-operation-scheduler` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `terraform-module` | `Terraform CI` | `.github/workflows/terraform-ci.yml` | **repo-specific** | Custom workflow logic. |
| `ultimate-devops-platform` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `ultimate-docker-k8s-lab` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `ultimate-docker-k8s-lab` | `Build and Push Multi-Arch Docker Image` | `.github/workflows/docker-build.yml` | **repo-specific** | Custom workflow logic. |
| `utilities-scripts` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `vault-ops` | `Baseline CI` | `.github/workflows/baseline-ci.yml` | **shared candidate (already reusable)** | Calls shared-workflows reusable workflow. |
| `virtual-vacation` | `Build and Push Multi-Arch Images` | `.github/workflows/build-and-push-images.yml` | **repo-specific** | Custom workflow logic. |
| `virtual-vacation` | `.github/workflows/build-base-images.yml` | `.github/workflows/build-base-images.yml` | **repo-specific** | Custom workflow logic. |
| `virtual-vacation` | `.github/workflows/build-consolidated-images.yml` | `.github/workflows/build-consolidated-images.yml` | **repo-specific** | Custom workflow logic. |
| `virtual-vacation` | `SonarQube Code Quality & Security Scan` | `.github/workflows/sonarqube-scan.yml` | **shared candidate** | Standard Python test pattern; covered by tests-python/service-python-ci-ghcr. |
| `virtual-vacation` | `Dependabot Updates` | `dynamic/dependabot/dependabot-updates` | **repo-specific** | GitHub-managed dynamic workflow. |
