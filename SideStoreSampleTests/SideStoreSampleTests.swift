import XCTest
@testable import SideStoreSample

final class SideStoreSampleTests: XCTestCase {
    func testAppBundleVersionAndBuildAreNonEmpty() {
        XCTAssertFalse(AppVersion.shortVersion.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty)
        XCTAssertFalse(AppVersion.buildNumber.trimmingCharacters(in: .whitespacesAndNewlines).isEmpty)
    }
}
