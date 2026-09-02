# Security Policy

Do not submit Apple Account credentials, pairing files, signing certificates,
private keys, provisioning profiles containing personal or device data, App
Store Connect keys, or personal tokens to this repository, issues, pull
requests, or CI artifacts.

The sample app is intentionally unsigned in CI. SideStore and the physical
iPhone handle the device-side signing boundary outside this repository.

If sensitive material is disclosed accidentally, remove the material from
public artifacts, rotate or revoke it where possible, and report the incident
without copying the secret into an issue or commit.
