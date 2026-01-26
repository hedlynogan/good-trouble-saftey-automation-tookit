# Git Flow Workflow

## Branch Structure

This project uses the **Git Flow** branching model for organized development.

```
main (production-ready)
  └─ develop (integration branch)
      ├─ feature/mac_ai (Mac Desktop refactoring)
      ├─ feature/ios_docs (future: iOS documentation)
      ├─ feature/android_enhancements (future: Android improvements)
      └─ feature/* (other features)
```

## Branch Descriptions

### `main`
- **Purpose**: Production-ready code
- **Protected**: Should only receive merges from `develop` or `hotfix/*`
- **Tags**: Version tags (v1.0.0, v1.1.0, etc.)
- **Status**: Stable, tested, ready for public use

### `develop`
- **Purpose**: Integration branch for ongoing development
- **Base for**: All feature branches
- **Receives**: Completed features via merge or pull request
- **Status**: Latest development state, should be stable but may have new features

### `feature/*`
- **Purpose**: Individual feature development
- **Naming**: `feature/<descriptive-name>`
- **Base**: Branch from `develop`
- **Merge to**: `develop` when complete
- **Examples**:
  - `feature/mac_ai` - Mac Desktop Apple Intelligence integration
  - `feature/ios_triggers` - iOS trigger documentation
  - `feature/multilingual_audio` - Additional language support

### `release/*` (optional, future)
- **Purpose**: Prepare for production release
- **Naming**: `release/v<version>`
- **Base**: Branch from `develop`
- **Merge to**: Both `main` and `develop`
- **Example**: `release/v1.0.0`

### `hotfix/*` (optional, for urgent fixes)
- **Purpose**: Emergency fixes to production
- **Naming**: `hotfix/<issue-description>`
- **Base**: Branch from `main`
- **Merge to**: Both `main` and `develop`
- **Example**: `hotfix/critical-location-bug`

## Workflow

### Starting a New Feature

1. **Ensure `develop` is up to date**
   ```bash
   git checkout develop
   git pull origin develop
   ```

2. **Create feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Work on your feature**
   ```bash
   # Make changes
   git add .
   git commit -m "Descriptive commit message"
   ```

4. **Push feature branch** (optional, for collaboration)
   ```bash
   git push -u origin feature/your-feature-name
   ```

### Completing a Feature

1. **Ensure feature is complete and tested**
   - All changes committed
   - Tests passing (if applicable)
   - Documentation updated

2. **Update from `develop`**
   ```bash
   git checkout develop
   git pull origin develop
   git checkout feature/your-feature-name
   git merge develop
   # Resolve conflicts if any
   ```

3. **Merge feature to `develop`**
   ```bash
   git checkout develop
   git merge --no-ff feature/your-feature-name
   git push origin develop
   ```

4. **Delete feature branch** (optional, after merge)
   ```bash
   git branch -d feature/your-feature-name
   git push origin --delete feature/your-feature-name
   ```

### Creating a Release

1. **Create release branch from `develop`**
   ```bash
   git checkout develop
   git checkout -b release/v1.0.0
   ```

2. **Finalize release**
   - Update version numbers
   - Update CHANGELOG.md
   - Final testing
   - Bug fixes only (no new features)

3. **Merge to `main` and tag**
   ```bash
   git checkout main
   git merge --no-ff release/v1.0.0
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin main --tags
   ```

4. **Merge back to `develop`**
   ```bash
   git checkout develop
   git merge --no-ff release/v1.0.0
   git push origin develop
   ```

5. **Delete release branch**
   ```bash
   git branch -d release/v1.0.0
   ```

### Hotfix Workflow

1. **Create hotfix from `main`**
   ```bash
   git checkout main
   git checkout -b hotfix/critical-bug
   ```

2. **Fix the issue**
   ```bash
   # Make fixes
   git commit -m "Fix critical bug"
   ```

3. **Merge to `main`**
   ```bash
   git checkout main
   git merge --no-ff hotfix/critical-bug
   git tag -a v1.0.1 -m "Hotfix version 1.0.1"
   git push origin main --tags
   ```

4. **Merge to `develop`**
   ```bash
   git checkout develop
   git merge --no-ff hotfix/critical-bug
   git push origin develop
   ```

5. **Delete hotfix branch**
   ```bash
   git branch -d hotfix/critical-bug
   ```

## Current Project Status

### Active Branches

| Branch | Status | Description |
|--------|--------|-------------|
| `main` | Stable | Last release: Test Plan and ShortcutTutorial |
| `develop` | Active | Integration branch (currently same as main) |
| `feature/mac_ai` | **In Progress** | Mac Desktop-first refactoring with Apple Intelligence |

### Current Work: `feature/mac_ai`

**Branch**: `feature/mac_ai`
**Status**: Active development
**Description**: Refactor project to use Mac Desktop as primary development platform

**Changes in this branch**:
- Mac Desktop positioned as primary shortcut creation platform
- Apple Intelligence integration (Use Model, Writing Tools, Create Image)
- iCloud sync workflow documentation
- iOS documentation refocused on deployment and triggers
- Comprehensive Mac Desktop testing plan

**Next steps**:
1. Complete Mac Desktop documentation with screenshots
2. Create iOS deployment guides
3. Test iCloud sync workflow
4. Merge to `develop` when complete
5. Eventually release to `main`

## Best Practices

### Commit Messages

Follow conventional commits format:

```
<type>: <subject>

<body>

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Example**:
```
feat: Add Mac Desktop shortcut creation guide

- Create comprehensive Mac Desktop development documentation
- Include Apple Intelligence feature usage
- Add iCloud sync setup instructions

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

### Branch Naming

- Use lowercase and hyphens: `feature/mac-desktop-docs`
- Be descriptive: `feature/ios-back-tap-trigger` not `feature/ios-fix`
- Use prefixes: `feature/`, `hotfix/`, `release/`

### Merging Strategy

- Use `--no-ff` (no fast-forward) for feature merges to `develop`
- This preserves branch history and makes it clear when features were merged
- Example: `git merge --no-ff feature/mac_ai`

### Testing Before Merge

Before merging to `develop`:
- [ ] All files committed
- [ ] Documentation updated
- [ ] No merge conflicts
- [ ] Changes tested (if applicable)
- [ ] Follows project guidelines (see .claude/CLAUDE.md)

## Quick Reference

```bash
# Start new feature
git checkout develop
git pull origin develop
git checkout -b feature/new-feature

# Work on feature
git add .
git commit -m "feat: Add new functionality"
git push -u origin feature/new-feature

# Finish feature
git checkout develop
git pull origin develop
git checkout feature/new-feature
git merge develop              # Update feature with latest develop
git checkout develop
git merge --no-ff feature/new-feature
git push origin develop
git branch -d feature/new-feature

# Current status
git branch -a                   # List all branches
git log --oneline --graph --all # Visual branch history
```

## Visualization

```
main:       A---B---C-----------M (release)
                 \             /
develop:          D---E---F---G---H
                   \         /
feature/mac_ai:     I---J---K
```

- `A, B, C`: Production releases on main
- `D, E, F, G, H`: Development commits on develop
- `I, J, K`: Feature work on feature/mac_ai
- `M`: Merge of develop to main (release)

## Resources

- [Git Flow Original Article](https://nvie.com/posts/a-successful-git-branching-model/)
- [Atlassian Git Flow Tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [GitHub Flow](https://guides.github.com/introduction/flow/) (simpler alternative)

## Notes for This Project

Since this is a **documentation-focused project** (not traditional software):
- "Releases" are when documentation is complete and tested
- "Testing" means following documentation on actual devices
- Feature branches can be long-lived for major documentation efforts
- Consider creating pull requests from features to `develop` for review

---

**Last Updated**: January 25, 2026
**Current Active Feature**: `feature/mac_ai` - Mac Desktop refactoring
