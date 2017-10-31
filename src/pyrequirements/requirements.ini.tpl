[generate]
source=://requirements.txt

[env:test]
1.cmd=test

[platform:armv7l]
1.pip>luma.oled   =
2.pip>RPi.GPIO    =


[platform:x86]
source=://requirements.txt
1.cmd=echo hello world
2.cmd=echo hi
pip>django = >1.6


[os:Darwin]
pip>django= <1.9