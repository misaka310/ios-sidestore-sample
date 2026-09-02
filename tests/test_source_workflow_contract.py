import json
from pathlib import Path


WORKFLOW = Path(__file__).parents[1] / ".github" / "workflows" / "release-sample.yml"
SOURCE = Path(__file__).parents[1] / "source" / "source.json"


def test_sample_source_publishes_after_a_release_to_a_stable_pages_url() -> None:
    content = WORKFLOW.read_text(encoding="utf-8")

    assert "publish_source: true" in content
    assert "pages: write" in content
    assert "id-token: write" in content
    assert "misaka310/ios-sidestore-deploy/.github/workflows/release.yml@bb34ee49283e01f82c28a9c2277d5ebbdf8b6c28" in content
    assert "source_path: source/source.json" in content
    assert "source_url: https://misaka310.github.io/ios-sidestore-sample/source.json" in content


def test_sample_source_template_is_a_safe_empty_source() -> None:
    source = json.loads(SOURCE.read_text(encoding="utf-8"))

    assert source == {
        "apps": [],
        "description": "A public AltSource for the proof application.",
        "name": "SideStore Deployment Foundation",
        "news": [],
        "subtitle": "Unsigned iOS app releases for SideStore.",
    }
