.. :changelog:

*******
History
*******

.. towncrier release notes start

0.14.0 (2025-10-22)
===================

Features
--------

- Allow rewriting repo and owner (#0)


0.13.0 (2025-10-22)
===================

Features
--------

- Switch to Coveralls Github action (#88)


Bugfixes
--------

- Fix Bitbucket url parse and add bitbucket.com to recognized domains (#107)
- Remove fix-encoding-pragma from pre-commit hooks as it is deprecated (#119)


0.12.0 (2023-09-24)
===================

Features
--------

- Add github/gitlab username:access_token parse support (#21)
- Migrate to bump-my-version (#79)


Bugfixes
--------

- Fix Gitlab URLs with branch (#42)
- Align tox.ini with github actions (#71)


0.11.1 (2023-08-04)
===================

Bugfixes
--------

- Remove debug print statements (#66)


0.11.0 (2023-08-03)
===================

Features
--------

- Add parsing variable for user to gitlab parser (#47)
- Add support for Python 3.8+ (#48)


Bugfixes
--------

- Update tests invocation method to avoid future breakages (#29)
- Update linting tools and fix code style (#34)
- Add more github use cases (#43)
- Fix parsing generic git url (#46)


0.10.0 (2020-12-05)
===================

Features
--------

- General matching improvements (#18)
- Update tooling, drop python2 (#10213)

0.9.2 (2018-10-27)
==================

* Removed "s" from the base platform regex
* Fix license classifier in setup.py
* Update meta files

0.9.1 (2018-01-20)
==================

* First fork release
