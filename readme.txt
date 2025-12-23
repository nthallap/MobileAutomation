How to uninstall appium
--------------------------------------------------
http://appium.io/

Step 1 : Check if node is installed on your system
    node -v

Step 2 : Install node.js
    https://nodejs.org/en/download/
    https://brew.sh/
    brew install node

Step 3 : Check if node is installed
    node -v
    npm -v

Step 4 : Install appium
    npm install -g appium

Step 5 : Check appium is installed
    appium -v

Step 6 : Start appium
    appium

Installing appium with appium desktop client

Step 1 : Download appium desktop client - http://appium.io/
   https://github.com/appium/appium-desktop

Step 2 : Double click on the .dmg file to install appium desktop client

Step 3 : Start appium desktop client


Appium-Doctor
https://www.npmjs.com/package/appium-...
https://github.com/appium/appium-doctor

npm install appium-doctor -g


How to uninstall appium

If installed through node.js
npm uninstall -g appium

If installed Appium Desktop Client
Delete the app

#AppiumStepByStep

HIT SUBSCRIBE & BELL TO GET NEW VIDEOS


===============================================
================================================

ANDROID SDK SETUP FOR APPIUM AUTOMATION
Detailed Video Tutorial Link :
https://www.youtube.com/watch?v=82KXSli1wPA&list=PLhW3qG5bs-L8npSSZD6aWdYFQ96OEduhk&index=5

PREREQUISITES
Java installed on system
JAVA_HOME is set in environment variables
 command to check : java -version
An android mobile device
Connecting cable
200 MB to 1 GB of free space

ERRORS
Error Description :
error could not find or load main class com.android.sdklib.tool.sdkmanager.sdkmanagercli
Solution:
using 7zip to extract worked great. Windows zip manager must have an issue when extracting the files

Error Description :
Warning: Could not create settings
java.lang.IllegalArgumentException
        at com.android.sdklib.tool.sdkmanager.SdkManagerCliSettings.＜init＞   (SdkManagerCliSettings.java:428)
        ...(and so on)

Solution:
create folder "cmdline-tools" inside
"android-sdk" folder and cut-paste the "tools" foder into "cmdline-tools" folder. Here is how they relate to each other:
...\android-sdk\cmdline-tools\tools\...

Step 1 : Download SDK tools
 https://developer.android.com/studio
----------------------------------------------------------------------------------
Step 2 : Unzip folder & Extract platform tools
----------------------------------------------------------------------------------
Step 3 : Set environment variables
 ANDROID_HOME = location of sdk folder
 Path : append path of platform_tools folder
----------------------------------------------------------------------------------
Step 4 : Check command adb devices on command line
----------------------------------------------------------------------------------
Step 5 : Make device ready
enable developer mode
make USB Debugging on
----------------------------------------------------------------------------------
Step 6 : Connect device to computer system thorugh USB cable
if asked enable USB Debbugging
----------------------------------------------------------------------------------
Step 7 : Run command adb devices
  adb = android debug bridge
 Check your device id displayed
----------------------------------------------------------------------------------
