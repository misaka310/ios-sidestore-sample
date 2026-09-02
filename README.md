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

Open `SideStoreSample.xcodeproj` in Xcode on macOS and run the `SideStoreSample` scheme. The deployment foundation builds the same scheme on a standard GitHub-hosted macOS runner, so Windows-only source maintenance does not require a personally owned Mac.

The app repository does not contain SideStore, AltSource, release, or signing logic. Those responsibilities stay in the deployment foundation repository.

## Verification boundary

An Xcode build or passing XCTest target proves only the app project contract. It does not prove SideStore installation, 7-day refresh, version updates, or pairing recovery; those require redacted physical-device evidence in the foundation repository.
