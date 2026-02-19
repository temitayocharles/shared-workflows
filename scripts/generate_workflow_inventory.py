#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

OWNER = "temitayocharles"


def run(*args: str) -> str:
    return subprocess.check_output(args).decode("utf-8", "ignore")


def classify(path: str, text: str) -> tuple[str, str]:
    if path.startswith("dynamic/"):
        return ("repo-specific", "GitHub-managed dynamic workflow.")
    if (
        "uses: temitayocharles/shared-workflows/.github/workflows/" in text
        or "uses: ./.github/workflows/baseline-reusable.yml" in text
    ):
        return ("shared candidate (already reusable)", "Calls shared-workflows reusable workflow.")
    if "repository-dispatch@" in text:
        return ("shared candidate", "Standard GitOps dispatch pattern; covered by gitops-dispatch.yml.")
    if "setup-qemu-action" in text and "build-push-action" in text and "ghcr.io" in text:
        return ("shared candidate", "Standard GHCR build/push pattern; covered by service-*ci-ghcr workflows.")
    if "actions/setup-python" in text and ("pytest" in text or "python -m pytest" in text):
        return ("shared candidate", "Standard Python test pattern; covered by tests-python/service-python-ci-ghcr.")
    if "actions/setup-go" in text and "go test" in text:
        return ("shared candidate", "Standard Go test pattern; covered by tests-go/service-go-ci-ghcr.")
    if "actions/setup-node" in text and ("npm test" in text or "npm run build" in text):
        return ("shared candidate", "Standard Node test/build pattern; covered by tests-node/service-node-ci-ghcr.")
    return ("repo-specific", "Custom workflow logic.")


def main() -> None:
    repos = json.loads(run("gh", "repo", "list", OWNER, "--limit", "200", "--json", "name,isArchived"))
    rows: list[tuple[str, str, str, str, str]] = []

    for repo_obj in sorted(repos, key=lambda x: x["name"].lower()):
        if repo_obj["isArchived"]:
            continue
        repo = repo_obj["name"]
        workflows = json.loads(run("gh", "api", f"repos/{OWNER}/{repo}/actions/workflows")).get("workflows", [])
        for wf in workflows:
            path = wf["path"]
            text = ""
            if not path.startswith("dynamic/"):
                try:
                    text = run(
                        "gh",
                        "api",
                        f"repos/{OWNER}/{repo}/contents/{path}",
                        "-H",
                        "Accept: application/vnd.github.raw",
                    )
                except subprocess.CalledProcessError:
                    text = ""
            cls, reason = classify(path, text)
            rows.append((repo, wf["name"], path, cls, reason))

    out = [
        "# Workflow Inventory and Classification",
        "",
        "Generated from GitHub Actions workflow metadata across non-archived repositories.",
        "",
        "| Repo | Workflow | Path | Classification | Rationale |",
        "|---|---|---|---|---|",
    ]
    for repo, wf_name, path, cls, reason in rows:
        out.append(f"| `{repo}` | `{wf_name}` | `{path}` | **{cls}** | {reason} |")

    Path("WORKFLOW_INVENTORY.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"Wrote WORKFLOW_INVENTORY.md with {len(rows)} workflow entries")


if __name__ == "__main__":
    main()
