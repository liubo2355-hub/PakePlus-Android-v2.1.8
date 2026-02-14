[app]

# (str) Title of your application
title = 学生点名系统

# (str) Package name
package.name = studentrollcall

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to ignore (let empty to ignore nothing)
#source.exclude_exts = spec

# (list) List of directory to ignore (let empty to ignore nothing)
#source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
# Do not prefix with './'
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 1.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Valid options are: landscape, portrait, portrait-reverse or landscape-reverse
orientation = portrait

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PYTHON, NAME2:ENTRYPOINT_TO_PYTHON2

#
# OSX Specific
#

#
# author = © Copyright Info

# change the major version of python used by the app
osx.python_version = 3

# Kivy version to use
osx.kivy_version = 1.9.1

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
# Supported formats are: #RRGGBB #AARRGGBB or one of the following names:
# red, blue, green, black, white, gray, cyan, magenta, yellow, lightgray,
# darkgray, grey, lightgrey, darkgrey, aqua, fuchsia, lime, maroon, navy,
# olive, purple, silver, teal.
#android.presplash_color = #FFFFFF

# (string) Presplash animation using Lottie format.
# see https://lottiefiles.com/ for examples and https://airbnb.design/lottie/
# for general documentation.
# Lottie files can be created using various tools, like Adobe After Effect or Synfig.
#android.presplash_lottie = "path/to/lottie/file.json"

# (str) Adaptive icon of the application (used if Android API level is 26+ at runtime)
#icon.adaptive_foreground.filename = %(source.dir)s/data/icon_fg.png
#icon.adaptive_background.filename = %(source.dir)s/data/icon_bg.png

# (list) Permissions
# (See https://python-for-android.readthedocs.io/en/latest/buildoptions/#build-options-1 for all the supported syntaxes and properties)
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (list) features (adds uses-feature -tags to manifest)
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
#android.api = 33

# (int) Minimum API your APK / AAB will support.
#android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk = 23b

# (int) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi.
#android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT executable to use, this is only required to build an APK with ant
#ant =

# (str) Android entry point, default is ok for Kivy-based app.
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Full name including package path of the Java class that implements Android Activity
# use that parameter together with android.entrypoint to set custom Java class instead of PythonActivity
#android.activity_class_name = org.kivy.android.PythonActivity

# (str) Extra xml to write directly inside the <manifest> element of AndroidManifest.xml
# use that parameter to provide a filename from where to load your custom XML code
#android.extra_manifest_xml = ./src/android/extra_manifest.xml

# (str) Extra xml to write directly inside the <application> element of AndroidManifest.xml
# use that parameter to provide a filename from where to load your custom XML arguments:
#android.extra_manifest_application_arguments = ./src/android/extra_manifest_application_arguments.xml

# (str) The name of the string resource file (without extension) used for
# defining the names of permissions that are displayed to the user.
#android.permission_strings_filename = ./src/android/strings.xml

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# In past, was `android.arch` as we weren't supporting builds for multiple archs at the same time.
android.archs = arm64-v8a, armeabi-v7a

# (int) overrides automatic versionCode computation (used in build.gradle)
# this is not the same as app version and should only be edited if you know what you're doing
# android.numeric_version = 1

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) XML file for custom backup rules (see official auto backup documentation)
# android.backup_rules =

# (str) If you need to insert variables into your AndroidManifest.xml file,
# you can do so with the manifestPlaceholders property.
# This property takes a map of key-value pairs. (via a string)
# Usage example : android.manifest_placeholders = [myCustomUrl:\"org.kivy.customurl\"]
# android.manifest_placeholders = [:]

# (bool) disables the compilation of py to pyc/pyo files when packaging
# android.no-compile-pyo = True

# (str) The format used to package the app for release mode; one of apk or aab.
android.release_artifact = apk

#
# Python for android (p4a) specific
#

# (str) python-for-android fork to use, defaults to upstream (kivy)
#p4a.fork = kivy

# (str) python-for-android branch to use, defaults to master
#p4a.branch = master

# (str) python-for-android specific commit to use, defaults to HEAD, must be within p4a.branch
#p4a.commit = HEAD

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
#p4a.source_dir =

# (str) The directory in which python-for-android should look for your own build recipes (if any)
#p4a.local_recipes =

# (str) Filename to the hook for p4a
#p4a.hook =

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (int) port number to specify an explicit port for WebView (WebView bootstrap)
#android.wv.port = 8000

# (bool) Indicate whether you want the screen to stay on
#android.keep_screen_on = True

# (bool) Indicate whether the keyboard should be hidden by default
#android.hide_keyboard = False

# (str) The filename of the Java class to use as a WebView client (WebView bootstrap)
#android.wv.client =

# (str) The filename of the Java class to use as a WebChromeClient (WebView bootstrap)
#android.wv.chrome_client =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
# android.skip_update = False

# (bool) If True, then automatically accept SDK license
# agreements. This is intended for automation only.
#android.accept_sdk_license = False

# (list) The list of libraries to add to the build
#android.libraries =

# (list) The list of maven repositories to add to the build
#android.maven_repositories =

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpython3.so symbolic link when possible
#android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
#android.arch = armeabi-v7a

# (bool) If True, the build will produce a debug build
#android.debug = False

# (str) Python for android directory to use.
#p4a.setup =

# (str) The dist directory to use
#p4a.dist_name = myapp-0.1

# (list) List of plugins to enable.
#plugins =

#
# Buildozer specific
#

# (bool) If True, then download and setup the build requirements
# (android sdk, ndk, etc.) even if they are already present
#buildozer.android_sdk = False

# (str) Directory where buildozer should store the downloaded files
#buildozer.download_dir = 

# (bool) If True, use the color in the output
#buildozer.color = True

# (int) Log level (0 = error only, 1 = info, 2 = debug)
#log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
#warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
#buildozer.build_dir = .buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
#buildozer.bin_dir = bin

#
# Generic for buildozer
#

# (list) List of additional directories to consider for changes detection
#additional_src_dirs =

# (int) Timeout in seconds for getting a lock before cleaning the buildozer cache.
#cache_timeout = 10

# (str) Path to buildozer's log file
#log_filename = buildozer.log

# (bool) Force using a specific target even if another exists.
#force_target =

#
# Generic target for buildozer
#

# (str) Target to use, android or ios.
#default_target = android

# (list) Target specific custom recipes directories
#recipes_dir =

# (int) Maximum depth to go into dependencies while checking if they need a build.
#max_depth_deps = 100

# (str) Environment key to use for storing the target data.
#target_data_key = target

# (bool) If True, then build the target even if the source code hasn't changed.
#always_build = False

# (bool) Allow download of prebuilt dependencies
#allow_prebuilt_deps = True

#
# Local target specific
#

# (str) Command to execute the local target.
#local.command = python main.py

# (list) List of file patterns to exclude when building the local target.
#local.exclude_patterns =

#
# iOS target specific
#

# (str) Name of the certificate to use for signing the debug version
# Get a list of available identities: buildozer ios list_identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = %(ios.codesign.debug)s

# (str) The development team to use for signing
#ios.development.team =

# (bool) If True, then use the same directory for builds, even if the
# source code changes.
#ios.same_build_dir = False

# (int) Log level (0 = error only, 1 = info, 2 = debug)
#ios.log_level = 2

# (list) List of architectures to build for, choices: arm64, x86_64
#ios.archs = arm64, x86_64

# (str) Name of the iOS SDK to use
#ios.sdk = iphoneos

# (str) Minimum iOS version supported
#ios.min_version = 9.0

# (str) Name of the iOS Simulator SDK to use
#ios.simulator.sdk = iphonesimulator

# (bool) Enable bitcode for the build
#ios.enable_bitcode = False

# (bool) If True, copies the app to iTunes after building
#ios.itunes = False

# (bool) If True, copies the app to the device after building
#ios.device = False

# (str) UUID of the device to use
#ios.device_uuid =

# (bool) If True, starts the app on the device after building
#ios.start_app = False

# (bool) If True, start the app in the simulator after building
#ios.simulator = False

# (str) Simulator device type to use
#ios.simulator.device = iPhone 11

# (str) Simulator SDK to use
#ios.simulator.sdk = iphonesimulator

# (list) List of frameworks to link with
#ios.frameworks =

# (list) List of libraries to link with
#ios.libraries =

# (list) List of resources to include
#ios.resources =

# (list) List of plist entries to add
#ios.plist_entries =

# (list) List of files to include in the app
#ios.include_files =

# (list) List of directories to include in the app
#ios.include_dirs =

# (list) List of xcassets to include
#ios.xcassets =

# (list) List of entitlements to include
#ios.entitlements =

# (list) List of schemes to include
#ios.schemes =

# (list) List of pods to include
#ios.pods =

# (list) List of podspecs to include
#ios.podspecs =

# (list) List of pod repositories to include
#ios.pod_repositories =

# (str) Name of the podfile to use
#ios.podfile =

# (str) Path to the xcode project file
#ios.xcode_project =

# (str) Path to the xcode workspace file
#ios.xcode_workspace =

# (str) Name of the scheme to use
#ios.scheme =

# (str) Name of the configuration to use
#ios.configuration = Release

# (bool) If True, then clean the xcode project before building
#ios.clean = False

# (bool) If True, then archive the xcode project after building
#ios.archive = False

# (str) Path to the export options plist file
#ios.export_options =

# (bool) If True, then upload the app to App Store Connect after building
#ios.upload = False

# (str) Username to use for App Store Connect upload
#ios.upload.username =

# (str) Password to use for App Store Connect upload
#ios.upload.password =

# (str) Provider short name to use for App Store Connect upload
#ios.upload.provider_short_name =

# (str) Team ID to use for App Store Connect upload
#ios.upload.team_id =

# (bool) If True, then upload the app to TestFlight after building
#ios.testflight = False

# (str) Username to use for TestFlight upload
#ios.testflight.username =

# (str) Password to use for TestFlight upload
#ios.testflight.password =

# (str) Provider short name to use for TestFlight upload
#ios.testflight.provider_short_name =

# (str) Team ID to use for TestFlight upload
#ios.testflight.team_id =

# (str) Name of the group to use for TestFlight upload
#ios.testflight.group_name =

# (bool) If True, then notify the testers after uploading to TestFlight
#ios.testflight.notify = True

# (str) What to submit to TestFlight, options are: 'app', 'dsym' or 'both'
#ios.testflight.submit = app

# (bool) If True, then use the Apple Transporter app for uploading
#ios.use_transporter = False

# (str) Path to the Apple Transporter app
#ios.transporter_path =

# (bool) If True, then use the legacy transporter for uploading
#ios.use_legacy_transporter = False

# (str) Path to the legacy transporter
#ios.legacy_transporter_path =

# (int) Number of retries when uploading
#ios.upload_retries = 3

# (int) Delay between retries when uploading
#ios.upload_retry_delay = 10

# (bool) If True, then skip the upload if the app already exists
#ios.skip_upload_if_exists = False

# (bool) If True, then skip the upload if the app version already exists
#ios.skip_upload_if_version_exists = False

# (bool) If True, then skip the upload if the app build number already exists
#ios.skip_upload_if_build_exists = False

# (list) List of files to upload
#ios.upload_files =

# (list) List of directories to upload
#ios.upload_dirs =

# (list) List of files to exclude from upload
#ios.upload_exclude_patterns =

# (list) List of directories to exclude from upload
#ios.upload_exclude_dirs =

# (list) List of additional metadata files to upload
#ios.metadata_files =

# (list) List of additional screenshot files to upload
#ios.screenshot_files =

# (list) List of additional app preview files to upload
#ios.app_preview_files =

# (list) List of additional app trailer files to upload
#ios.app_trailer_files =

# (list) List of additional app icon files to upload
#ios.app_icon_files =

# (list) List of additional app logo files to upload
#ios.app_logo_files =

# (list) List of additional app banner files to upload
#ios.app_banner_files =

# (list) List of additional app header files to upload
#ios.app_header_files =

# (list) List of additional app footer files to upload
#ios.app_footer_files =

# (list) List of additional app background files to upload
#ios.app_background_files =

# (list) List of additional app image files to upload
#ios.app_image_files =

# (list) List of additional app video files to upload
#ios.app_video_files =

# (list) List of additional app audio files to upload
#ios.app_audio_files =

# (list) List of additional app document files to upload
#ios.app_document_files =

# (list) List of additional app text files to upload
#ios.app_text_files =

# (list) List of additional app data files to upload
#ios.app_data_files =

# (list) List of additional app archive files to upload
#ios.app_archive_files =

# (list) List of additional app database files to upload
#ios.app_database_files =

# (list) List of additional app configuration files to upload
#ios.app_configuration_files =

# (list) List of additional app resource files to upload
#ios.app_resource_files =

# (list) List of additional app binary files to upload
#ios.app_binary_files =

# (list) List of additional app source files to upload
#ios.app_source_files =

# (list) List of additional app test files to upload
#ios.app_test_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app test binary files to upload
#ios.app_test_binary_files =

# (list) List of additional app test source files to upload
#ios.app_test_source_files =

# (list) List of additional app test documentation files to upload
#ios.app_test_documentation_files =

# (list) List of additional app test configuration files to upload
#ios.app_test_configuration_files =

# (list) List of additional app test resource files to upload
#ios.app_test_resource_files =

# (list) List of additional app test data files to upload
#ios.app_test_data_files =

# (list) List of additional app