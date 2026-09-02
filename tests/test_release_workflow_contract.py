from pathlib import Path


WORKFLOW = Path(__file__).parents[1] / ".github" / "workflows" / "release-sample.yml"


def test_sample_release_is_tagged_and_pins_the_foundation_release_workflow() -> None:
    content = WORKFLOW.read_text(encoding="utf-8")

    assert "push:" in content
    assert "tags:" in content
    assert "- v*" in content
    assert "contents: write" in content
    assert "misaka310/ios-sidestore-deploy/.github/workflows/release.yml@b575be80b482a6b7cd6918724da9d053b7618fef" in content
    assert "app_ref: ${{ github.ref }}" in content
    assert "release_tag: ${{ github.ref_name }}" in content
    assert "app_version: \"1.0.1\"" in content
    assert "build_number: \"2\"" in content
    assert "scheme: SideStoreSample" in content
    assert "project_path: SideStoreSample.xcodeproj" in content


def test_sample_release_workflow_does_not_pass_signing_secrets() -> None:
    content = WORKFLOW.read_text(encoding="utf-8")

    assert "secrets:" not in content
    assert "CODE_SIGNING" not in content
