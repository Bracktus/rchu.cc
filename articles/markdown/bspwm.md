---
title: my bspwm setup
date: 31-07-2020
---

[bspwm](https://github.com/baskerville/bspwm) is a manual tiling window
manager (WM).

Basically when you open a new window the WM decides the size and
position of the window. Tiling means that none of the windows overlap,
they 'tile' next to each other in a sort of grid formation. There are
many great tiling window managers out there but I use bspwm.

When bspwm starts up it runs a script named `bspwmrc`. It's a bash
script where you can run commands to change the look and feel of bspwm.
You can also place some startup commands in it.


::: {.note}
Note: bspwm doesn't come with a way to control it. i.e None of your keys
will work You'll need to install a hotkey daemon (software that runs in
the background) such as sxhkd to manipulate windows.
:::
## Here's mine

~~~

#!/bin/sh

bspc monitor -d I II III IV V

#Spacing
bspc config border\_width         5
bspc config window\_gap          12
bspc config top\_padding         40

#Misc
bspc config split\_ratio          0.52
bspc config borderless\_monocle   true
bspc config gapless\_monocle      true

#Colours
bspc config focused\_border\_color "#B0BFD1"

#Rule
bspc rule -a Gimp desktop='^8' state=floating follow=on
bspc rule -a Chromium desktop='^2'
bspc rule -a mplayer2 state=floating
bspc rule -a Kupfer.py focus=on
bspc rule -a Screenkey manage=off
bspc rule -a Zathura state=tiled

#Autostart----------------------------------

#Kill if already running 
killall -9 sxhkd dunst picom
pkill -f music-notification.py

#Launching daemons
sxhkd &
dunst &
picom -b 
python3 ~/bin/music-notification.py &

#Setting wallpaper
feh --bg-scale --no-fehbg ~/pics/wallpapers/aleksovannaCrybaby.jpg

#Launching bar
~/.config/polybar/launch.sh

#Airing anime fetcher
python3 ~/bin/anime/getJSON.py

~~~

## So what is it doing?

`bspc monitor -d I II III IV V`

This creates 5 workspaces that I can switch between. You can have up to
10 workspaces however I choose to use 5.

~~~

#Spacing
bspc config border\_width         5
bspc config window\_gap          12
bspc config top\_padding         40

~~~

The first command sets the width of the borders around the windows, the
second sets the gap between tiled windows

The third command sets the padded space at the top of the screen.
You\'ll want to set this if you have a bar or else the window will just
cover it


~~~

#Misc
bspc config split\_ratio          0.52
bspc config borderless\_monocle   true
bspc config gapless\_monocle      true

~~~


This first line sets the split ratio. This if you had 1 window and
opened another this would decide what proportion of the screen the
second window would occupy.

## What about the rest?

The remainder are startup commands. I\'ll try and cover these in another
post
