echo "************Kreiranje prozora************"
mkdir MasterRad
cd MasterRad
echo "************Preuzimanje UmlPainter-a************"
git clone https://github.com/lukicmihailo/Projekat
#wget "http://dl.google.com/android/ndk/android-ndk-r8c-linux-x86.tar.bz2"
#wget "http://dl.google.com/android/android-sdk_r21.0.1-linux.tgz" 
echo "************Podesavanje varijabli************"
export ANDROIDSDK="/home/mihailo/conf/android-sdk-linux"
export ANDROIDNDK="/home/mihailo/conf/android-ndk-r8c"
export ANDROIDNDKVER=r8c
export ANDROIDAPI=14
export PATH=$PATH:/home/mihailo/conf/android-sdk-linux/platform-tools
export PATH=$PATH:/home/mihailo/conf/android-sdk-linux/tools
echo "************Preuzimanje python for android************"
git clone git://github.com/kivy/python-for-android
cd python-for-android 
echo "************Instalacija pythona for android************"
./distribute.sh -m "openssl pil kivy"
cd dist/default
echo "************Build aplikacije************"
./build.py --package org.umlpainter --name UmlPainter \--version 1.0 --dir ~/MasterRad/Projekat debug
echo "Instalacija aplikacije na mobilni telefon"
adb install bin/UmlPainter-1.0-debug.apk

