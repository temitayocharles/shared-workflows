# Start Here

This repo holds reusable GitHub Actions workflows and composite actions.

## 1. What This Repo Is
Shared CI/CD building blocks used by application repos to keep pipelines consistent.

## 2. Repo Map (What Lives Where)
- `.github/workflows/`: reusable workflow entrypoints.
- `.github/actions/`: composite actions (gitleaks, vault, docker, helm bump, argocd, etc.).
- `docs/`: usage docs and examples.

## 3. How to Use in an App Repo
1. Add a workflow that references this repo via `uses: temitayocharles/shared-workflows/.github/workflows/<workflow>.yml@<ref>`.
1. Provide required inputs and secrets.
1. Commit and push.

## 4. Troubleshooting
- If a workflow fails, verify required inputs and secrets exist in the app repo.
- Ensure the ref points to a valid tag or branch.
