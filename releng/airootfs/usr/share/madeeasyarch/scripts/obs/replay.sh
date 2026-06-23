#!/bin/bash
obs-cmd --websocket obsws://localhost:4455/ryrrweWILiMVvq8I replay save && \
  notify-send -i /usr/share/icons/hicolor/256x256/apps/com.obsproject.Studio.png \
    "1m has been clipped!" "Check out ~/Videos/OBS to see what you clipped"