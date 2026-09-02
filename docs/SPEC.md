# SideStore Sample Proof App Specification

## 1. 元の目的

This repository provides a minimal, deterministic SwiftUI app that proves the deployment foundation can build an unsigned, device-targeted IPA and later expose an observable installed version on a physical iPhone.

## 2. 期待する最終結果

- An Xcode project with one app scheme named `SideStoreSample`.
- A SwiftUI app with bundle identifier `com.example.SideStoreSample`.
- The app visibly renders `CFBundleShortVersionString` and `CFBundleVersion` from its own bundle.
- A native XCTest target asserts both values are present and non-empty.
- A Release configuration can be built for `iphoneos` with signing disabled by the foundation workflow.

### 完成扱いにしないもの

- A project file that has not been built by Xcode.
- An IPA file by itself without independent structure validation.
- A successful CI build without physical SideStore install, refresh, update, and pairing evidence.
- A claim that the sample app proves Apple's 7-day Personal Team limit is removed.

## 3. ユーザー操作・導線

### Happy Path

1. The maintainer opens or clones this repository on a Windows machine and changes only the app source/version as needed.
2. The deployment foundation's reusable workflow builds the `SideStoreSample` scheme for `iphoneos` with signing disabled.
3. A `v*` tag calls the pinned foundation release workflow, which rebuilds the tag and publishes the validated IPA to a GitHub Release.
4. The release-published workflow generates and validates the AltSource, then deploys it to the repository's stable GitHub Pages URL.
5. The user adds that source to SideStore and installs the published IPA through the documented SideStore flow.
6. The user launches the app and verifies the on-screen version/build label.

### エラー時

- If Xcode cannot find the scheme or the build fails, inspect the workflow's toolchain/build log and correct the project configuration before retrying.
- If the installed label is missing or empty, treat the build as invalid and do not use it for device evidence.
- If a tag/version mismatch or release/source workflow fails, publish nothing from that failed run and fix the version, tag, or foundation ref before retrying.
- If GitHub Pages is not enabled, treat source publication as incomplete; do not claim the AltSource is hosted from an Actions artifact alone.
- SideStore install, refresh, update, and pairing failures are recovered through the foundation repository's operations docs; they are not hidden by changing this app's acceptance criteria.

## 4. 制約条件

- Routine source changes must be possible from Windows; Xcode execution is performed on a GitHub-hosted macOS runner.
- The default build is unsigned and must not require Apple secrets in GitHub.
- The app is a device-targeted proof artifact, not an App Store product.
- The project must remain small enough for deterministic fixture and hosted-run verification.

## 5. 非目標

- App Store distribution or paid Apple Developer Program certificate management.
- Implementing SideStore, LocalDevVPN, pairing recovery, release publication, or AltSource generation in this repository.
- Zero-tap updates.

## 6. 受入条件

- [ ] The `SideStoreSample` scheme builds a device-targeted Release app on a standard GitHub-hosted macOS runner with signing disabled.
- [ ] The native XCTest target passes and confirms non-empty version/build values.
- [ ] The built app visibly reports its bundle version/build when launched on a physical iPhone through SideStore.
- [ ] The app's physical-device evidence is recorded by the foundation repository without storing secrets or pairing files.
- [ ] The sample repository remains separate from the deployment foundation and does not duplicate its deployment implementation.

## 7. 検証方法

- Run the native Xcode test target with `xcodebuild test` on a macOS runner.
- Run the foundation IPA validator against the produced IPA and inspect the build manifest.
- Launch the installed app on a physical iPhone and record the visible version/build in the foundation verification matrix.
- Review tracked files and history for forbidden signing/account material before publishing evidence.
