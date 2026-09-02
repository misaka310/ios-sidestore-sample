from pathlib import Path


WORKFLOW = Path(__file__).parents[1] / ".github" / "workflows" / "build-unsigned-sample.yml"
PROJECT = Path(__file__).parents[1] / "SideStoreSample.xcodeproj" / "project.pbxproj"


def test_public_workflow_runs_native_tests_and_calls_pinned_foundation() -> None:
    content = WORKFLOW.read_text(encoding="utf-8")

    assert "runs-on: macos-14" in content
    assert "timeout-minutes: 30" in content
    assert "xcodebuild test" in content
    assert "awk" in content
    assert "No eligible iOS Simulator destination" in content
    assert "CODE_SIGNING_ALLOWED=NO" in content
    assert "misaka310/ios-sidestore-deploy/.github/workflows/reusable-build-unsigned-ipa.yml@651057fa1754c694d464709efed3c9806cafde07" in content
    assert "foundation_ref: 651057fa1754c694d464709efed3c9806cafde07" in content
    assert "scheme: SideStoreSample" in content
    assert "artifact_name: sidestore-sample" in content


def test_xcode_project_declares_ios_sdk() -> None:
    content = PROJECT.read_text(encoding="utf-8")

    assert "SDKROOT = iphoneos;" in content
