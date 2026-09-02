import Foundation

final class AppBundleMarker: NSObject {}

enum AppVersion {
    static var shortVersion: String {
        value(forKey: "CFBundleShortVersionString")
    }

    static var buildNumber: String {
        value(forKey: "CFBundleVersion")
    }

    private static func value(forKey key: String) -> String {
        (Bundle(for: AppBundleMarker.self).object(forInfoDictionaryKey: key) as? String) ?? ""
    }
}
