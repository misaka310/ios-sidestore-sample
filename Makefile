.PHONY: run test

run:
	open SideStoreSample.xcodeproj

test:
	xcodebuild -project SideStoreSample.xcodeproj -scheme SideStoreSample -destination 'platform=iOS Simulator,name=iPhone 16' test
