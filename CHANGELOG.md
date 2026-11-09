# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- `greet()` now accepts a `punctuation` argument (default `"!"`); `greet("Hee", ".")` returns `Hello, Hee.` instead of always ending with `!`.

### Fixed
- `greet()` now uses `world` for blank names; previously `greet(" ")` returned `Hello, !`, now it returns `Hello, world!`.

## [0.1.0] - 2026-11-09

### Added
- `greet()` function returning `Hello, <name>!` and a command-line greeting program.
