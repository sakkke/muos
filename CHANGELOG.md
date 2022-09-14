# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Update post create command for dev container.
- Add a VSCode extension for `.toml`.
- Add `sphinx` as a development dependency.
- Initialize Sphinx.
- Add a VSCode extension for `Dockerfile`.
- Add `nodejs` and `npm` to dev container.
- Add `netlify-cli` to dev container.
- Add CircleCI CLI to dev container.
- Initialize Netlify.
- Add `deploy-docs` workflow.

### Changed
- Update the format of `Log.message()`.
- Fix typo in a member name in `Runner`.

## [22.09.0a2] - 2022-09-11
### Added
- Add `bootstrap_arch_linux` step.
- Add `generate_fstab` step.
- Add `select_time_zone` step.
- Add `update_time_zone` step.
- Add `generate_adjtime` step.
- Add `select_locales` step.
- Add `select_main_locale` step.
- Add `update_locale_gen` step.
- Add `generate_locales` step.
- Add `select_keymap` step.
- Add `update_vconsole_conf` step.
- Add `update_hostname` step.
- Add `update_passwords` step.
- Add `install_grub` step.
- Initialize Git Hooks.
- Add `enable_systemd_services` step.
- Add `install_networkmanager` step.
- Add shell scripts for dev.
- Add `make_bootx64_efi` step.

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

[Unreleased]: https://github.com/sakkke/muos/compare/v22.09.0a2...HEAD
[22.09.0a2]: https://github.com/sakkke/muos/compare/v22.09.0a1...v22.09.0a2
[22.09.0a1]: https://github.com/sakkke/muos/releases/tag/v22.09.0a1
