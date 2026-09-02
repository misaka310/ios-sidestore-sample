# SideStore Sample

Minimal SwiftUI proof app for a reusable unsigned iOS deployment foundation.

The app is intentionally small: it exposes the bundle's `CFBundleShortVersionString` and `CFBundleVersion` on screen so a physical SideStore install can be checked without Xcode.

## Project contract

- Scheme: `SideStoreSample`
- Bundle identifier: `com.example.SideStoreSample`
- Deployment target: iOS 17.0
- Release configuration: device-targeted and unsigned when built with the foundation workflow
- Native test target: `SideStoreSampleTests`

The bundle identifier is a sample value. A downstream app should choose its own unique identifier before physical-device installation.

## Local development

On macOS, run `make run` to open `SideStoreSample.xcodeproj` in Xcode, then run the `SideStoreSample` scheme. The deployment foundation builds the same scheme on a standard GitHub-hosted macOS runner, so Windows-only source maintenance does not require a personally owned Mac.

The app repository does not contain SideStore, AltSource, release, or signing logic. Those responsibilities stay in the deployment foundation repository.

## Setup

Install Xcode on macOS when you want to open or run the project locally. For the normal Windows-first path, edit the Swift sources here and use the public deployment foundation workflow to build on a standard GitHub-hosted macOS runner.

## Usage

Use the `SideStoreSample` scheme to launch the proof app. The app displays its bundle version and build number. The public build workflow is defined in the [iOS SideStore Deployment Foundation](https://github.com/misaka310/ios-sidestore-deploy) and is called from this repository's CI workflow.

Tags matching `v*` call the pinned foundation release workflow. The workflow rebuilds the exact tag, publishes the unsigned IPA and manifest to a GitHub Release, and verifies the released IPA hash. The current sample release contract is version `1.0.1`, build `2`; update both the workflow inputs and the app's bundle version/build together before creating the next tag.

After a Release is published, the pinned foundation source workflow generates the AltSource and deploys it to GitHub Pages at [source.json](https://misaka310.github.io/ios-sidestore-sample/source.json). GitHub Pages must be enabled with the workflow source in the repository settings before the first release. This URL is the source URL to add in SideStore; the workflow retains prior versions by reading the previously published source.

## Requirements

- Xcode and iOS Simulator for local macOS development.
- A GitHub account for hosted workflow runs.
- GitHub Pages enabled for the repository's Actions workflow when publishing the AltSource.
- A physical iPhone and SideStore only for the separate device-evidence gates.

## Limitations

This is a proof app, not an App Store product and not an implementation of SideStore. A successful build or passing XCTest does not prove signing, installation, refresh, update, or pairing recovery on a physical device.

## Verification boundary

An Xcode build or passing XCTest target proves only the app project contract. It does not prove SideStore installation, 7-day refresh, version updates, or pairing recovery; those require redacted physical-device evidence in the foundation repository.
