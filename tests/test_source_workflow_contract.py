import json
from pathlib import Path


WORKFLOW = Path(__file__).parents[1] / ".github" / "workflows" / "publish-source-sample.yml"
SOURCE = Path(__file__).parents[1] / "source" / "source.json"


def test_sample_source_publishes_after_a_release_to_a_stable_pages_url() -> None:
    content = WORKFLOW.read_text(encoding="utf-8")

    assert "release:" in content
    assert "types: [published]" in content
    assert "permissions:" in content
    assert "pages: write" in content
    assert "id-token: write" in content
    assert "misaka310/ios-sidestore-deploy/.github/workflows/publish-source.yml@b041c61" in content
    assert "source_path: source/source.json" in content
    assert "source_url: https://misaka310.github.io/ios-sidestore-sample/source.json" in content
    assert "release_tag: ${{ github.event.release.tag_name }}" in content


def test_sample_source_template_is_a_safe_empty_source() -> None:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))

    assert source == {
        "apps": [],
        "description": "A public AltSource for the proof application.",
        "name": "SideStore Deployment Foundation",
        "news": [],
        "subtitle": "Unsigned iOS app releases for SideStore.",
    }
