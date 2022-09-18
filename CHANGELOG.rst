Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on `Keep a
Changelog <https://keepachangelog.com/en/1.0.0/>`__, and this project
adheres to `PEP 440 <https://peps.python.org/pep-0440/>`__.

`Unreleased <https://github.com/sakkke/muos/compare/v22.09.0a3...HEAD>`__
-------------------------------------------------------------------------

Added
~~~~~

-  Add a VSCode extension for Git.
-  Add ``install-devdeps`` task to ``Makefile``.
-  Add ``install-sh-workflow``.
-  Add ``deploy-docs-draft`` job.
-  Add VSCode extensions for ``*.rst``.
-  Add ``CODE_OF_CONDUCT.rst``.
-  Add ``CONTRIBUTING.rst``.
-  Add draft ``silent_install.py``.
-  Add ``sphinx.ext.napoleon``.
-  Add ``Disk`` class.
-  Add ``SelectStep`` class.

Changed
~~~~~~~

-  Make tags trigger in ``deploy-test-pypi-workflow``.
-  Clean up workflows.
-  Rename a job ``deploy-test-pypi`` to ``publish-test-pypi``.
-  Convert to src layout.
-  Move ``netlify-cli`` to ``tools`` directory.
-  Move ``hooks`` and ``install-hooks.sh`` to ``scripts`` directory.
-  Rename files containing dashes to underscores.
-  Convert Markdown to reStructedText.
-  Update ``post_install.sh``.
-  Replace ``description`` with ``name`` in some files.
-  Update step names.

Removed
~~~~~~~

-  Remove ``say-hello-workflow``.

`22.09.0a3 <https://github.com/sakkke/muos/compare/v22.09.0a2...v22.09.0a3>`__ - 2022-09-17
-------------------------------------------------------------------------------------------

.. _added-1:

Added
~~~~~

-  Update post create command for dev container.
-  Add a VSCode extension for ``.toml``.
-  Add ``sphinx`` as a development dependency.
-  Initialize Sphinx.
-  Add a VSCode extension for ``Dockerfile``.
-  Add ``nodejs`` and ``npm`` to dev container.
-  Add ``netlify-cli`` to dev container.
-  Add CircleCI CLI to dev container.
-  Initialize Netlify.
-  Add ``deploy-docs`` workflow.
-  Add CircleCI status badge to ``README.md``.
-  Add social image to ``README.md``.
-  Add heading “Links” to ``README.md``.
-  Add ``sphinx-rtd-theme`` as a development dependency.
-  Add ``Makefile``.
-  Add ``pytest`` as a development dependency.
-  Add ``run-tests-workflow``.
-  Add ``.vscode/settings.json``.
-  Add ``pytest-codecov`` as a development dependency.
-  Add ``pytest-cov`` as a development dependency.
-  Add ``GitPython`` as a development dependency.
-  Add Codecov status badge to ``README.md``.
-  Add ``deploy-test-pypi-workflow``.

.. _changed-1:

Changed
~~~~~~~

-  Update the format of ``Log.message()``.
-  Fix typo in a member name in ``Runner``.

`22.09.0a2 <https://github.com/sakkke/muos/compare/v22.09.0a1...v22.09.0a2>`__ - 2022-09-11
-------------------------------------------------------------------------------------------

.. _added-2:

Added
~~~~~

-  Add ``bootstrap_arch_linux`` step.
-  Add ``generate_fstab`` step.
-  Add ``select_time_zone`` step.
-  Add ``update_time_zone`` step.
-  Add ``generate_adjtime`` step.
-  Add ``select_locales`` step.
-  Add ``select_main_locale`` step.
-  Add ``update_locale_gen`` step.
-  Add ``generate_locales`` step.
-  Add ``select_keymap`` step.
-  Add ``update_vconsole_conf`` step.
-  Add ``update_hostname`` step.
-  Add ``update_passwords`` step.
-  Add ``install_grub`` step.
-  Initialize Git Hooks.
-  Add ``enable_systemd_services`` step.
-  Add ``install_networkmanager`` step.
-  Add shell scripts for dev.
-  Add ``make_bootx64_efi`` step.

.. _changed-2:

Changed
~~~~~~~

-  Improve ``Log.message()`` from ``Runner.run()``.
-  Improve timing of calling ``end`` step.
-  Rename ``Runner.name`` to ``Runner.description``.
-  Improve descriptions in steps.
-  Improve ``Log.message()``.
-  Change the message format in ``Step.main()``.
-  Add ``description`` member to ``Environment``.
-  Change the message format in ``Runner.run()``.

Fixed
~~~~~

-  Fix incorrect syntax in ``Dockerfile`` for dev container.
-  Fix incorrect assignment in ``select_pacman_mirrors`` step.

`22.09.0a1 <https://github.com/sakkke/muos/releases/tag/v22.09.0a1>`__ - 2022-09-10
-----------------------------------------------------------------------------------

.. _added-3:

Added
~~~~~

-  Add ``CHANGELOG.md``.
