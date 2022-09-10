# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Add `bootstrap_arch_linux` step.
- Add `generate_fstab` step.
- Add `select_time_zone` step.
- Add `update_time_zone` step.
- Add `generate_adjtime` step.
- Add `select_locales` step.

### Changed
- Improve `Log.message()` from `Runner.run()`.
- Improve timing of calling `end` step.
- Rename `Runner.name` to `Runner.description`.
- Improve descriptions in steps.
- Improve `Log.message()`.
- Change the message format in `Step.main()`.
- Add `description` member to `Environment`.
- Change the message format in `Runner.run()`.

### Fixed
- Fix incorrect syntax in `Dockerfile` for dev container.
- Fix incorrect assignment in `select_pacman_mirrors` step.

## [22.09.0a1] - 2022-09-10
### Added
- Add `CHANGELOG.md`.

[Unreleased]: https://github.com/sakkke/muos/compare/v22.09.0a1...HEAD
[22.09.0a1]: https://github.com/sakkke/muos/releases/tag/v22.09.0a1