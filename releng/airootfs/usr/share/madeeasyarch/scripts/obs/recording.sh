#!/bin/bash
obs-cmd --websocket obsws://localhost:4455/ryrrweWILiMVvq8I recording toggle && \
  notify-send -i /usr/share/icons/hicolor/256x256/apps/com.obsproject.Studio.png \
    "Recording toggled!"