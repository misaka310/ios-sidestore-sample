# Repository instructions

## 仕様の正本

- 仕様の正本: `docs/SPEC.md`
- 仕様変更時は実装前に正本を更新し、実装・テスト・検証も同じ変更で更新する。
- The deployment contract is defined by the deployment-foundation repository consumed by this app; this repository owns only the proof app.
- Do not add Apple Account credentials, pairing files, signing certificates/private keys, provisioning profiles, App Store Connect keys, or personal tokens.

## Repository purpose

This repository is the minimal SwiftUI proof app consumed by a reusable unsigned IPA workflow. It is not the deployment foundation and must not duplicate deployment logic.

## Verification

- The native Xcode test target must prove that the app bundle exposes non-empty version/build values.
- A successful local or hosted build is not physical-device evidence for SideStore installation, refresh, update, or pairing recovery.
