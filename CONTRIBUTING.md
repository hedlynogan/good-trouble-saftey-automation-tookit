# Contributing to Good Trouble Safety Automation Toolkit

Thank you for your interest in contributing to this project! This toolkit helps keep people safe during encounters, and community contributions make it better for everyone.

## How You Can Contribute

### Reporting Bugs

If you find a bug or issue with the workflow:

1. Check existing [issues](https://github.com/hedlynogan/good-trouble-saftey-automation-tookit/issues) to avoid duplicates
2. Open a new issue using the bug report template
3. Include your device model, OS version, and steps to reproduce

### Suggesting Features

Have an idea to improve the toolkit?

1. Open a feature request issue
2. Describe the problem you're trying to solve
3. Explain your proposed solution
4. Specify which platform(s) the feature applies to (iOS, Android, or both)

### Improving Documentation

Documentation improvements are always welcome:

- Clarifying existing instructions
- Adding screenshots to the step-by-step guides
- Translating documentation to other languages
- Fixing typos or unclear wording

Place iOS documentation in `doc/ios/` and Android documentation in `doc/android/`.

### Contributing Audio Files

If you can provide legal rights audio recordings in additional languages:

1. Ensure the content is accurate and reviewed by someone familiar with local laws
2. Use MP3 format for compatibility with both platforms
3. Follow the naming convention: `legal_rights_[language_code]_complete.mp3`
4. Open a pull request with the new audio file

---

## Platform-Specific Contributions

### iOS (Shortcuts)

When contributing iOS-related changes:

- Test on actual iOS devices when possible
- Include screenshots showing Shortcuts actions
- Document which iOS version(s) you tested on
- Note any Siri or accessibility considerations

### Android (Tasker)

When contributing Tasker-related changes:

**Exporting Tasks:**
1. In Tasker, long-press on your task
2. Select "Export" > "Export As XML"
3. Use the naming convention: `GoodTrouble_[TaskName].tsk.xml`

**Exporting Profiles:**
1. In Tasker, long-press on your profile
2. Select "Export" > "Export As XML"
3. Use the naming convention: `GoodTrouble_[ProfileName].prf.xml`

**Guidelines for Tasker contributions:**
- Test on multiple Android versions if possible
- Document required permissions clearly
- Note any plugin dependencies (AutoInput, etc.)
- Avoid manufacturer-specific features when possible
- Include comments in your tasks explaining each action
- Test with battery optimization both enabled and disabled

**Before submitting Tasker files:**
- Remove any personal data (phone numbers, names, etc.)
- Replace personal values with variable placeholders
- Test the import process on a clean Tasker installation

---

## Pull Request Process

1. Fork the repository
2. Create a branch for your changes
3. Make your changes
4. Test thoroughly (especially any workflow changes)
5. Submit a pull request with a clear description

### PR Description Should Include

- Which platform(s) are affected
- What the change does
- How you tested it
- Any breaking changes or dependencies

---

## Code of Conduct

Please read and follow our [Code of Conduct](CODE_OF_CONDUCT.md). We are committed to providing a welcoming and inclusive environment for all contributors.

## Questions?

Open an issue if you have questions about contributing.
