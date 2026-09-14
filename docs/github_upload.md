# Uploading to GitHub

## Recommended: GitHub Desktop

1. Unzip `StatOrch_GitHub.zip`.
2. Open GitHub Desktop → **File → Add Local Repository** (or create one from the folder).
3. Review the files, commit, and **Publish repository**.
4. Before making it public, replace the anonymous citation metadata, choose a license, and update `repository-code` in `CITATION.cff`.

## Command line

```bash
git init
git add .
git commit -m "Initial StatOrch research release"
git branch -M main
git remote add origin <YOUR_REPO_URL>
git push -u origin main
```

## Before public release

- choose a license;
- replace anonymous author/repository placeholders;
- add any raw result release only with a provenance manifest;
- never commit raw external datasets unless redistribution is explicitly permitted;
- keep the claim language aligned with `docs/claim_scope.md`.
