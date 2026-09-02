import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(spacing: 16) {
            Image(systemName: "arrow.down.app")
                .font(.system(size: 48))
                .foregroundStyle(.tint)

            Text("SideStore Sample")
                .font(.title2.weight(.semibold))

            VStack(spacing: 4) {
                Text("Version (AppVersion.shortVersion)")
                Text("Build (AppVersion.buildNumber)")
            }
            .font(.body.monospaced())
            .accessibilityIdentifier("app-version-build")
        }
        .padding()
    }
}

#Preview {
    ContentView()
}
