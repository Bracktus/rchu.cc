---
title: spotify on linux
date: 01-08-2020
---

I use spotify, I think it's a pretty good service. I've tried 3 different forms of spotify on my system.

1. Using the official desktop app
2. Using spotifyd (spotify premium only)
3. Using ncspot (spotify premium only)

The desktop app is pretty decent. It comes with desktop notifications and just works out of the box. If you dislike the look of it you can use [spicetify](https://github.com/khanhas/spicetify-cli) to customise it. This include changing the colours and layout of the client, removing unnecessary features and even injecting additional functionality. 

[Spotifyd](https://github.com/Spotifyd/spotifyd) is a spotify daemon. Basically it's an instance of spotify that runs in the background. It's super lightweight so it doesn't come with a client. You'll need to install one like [spotify-tui](https://github.com/Rigellute/spotify-tui) or just use your phone with spotify connect to queue songs. It doesn't come with desktop notifications so you can use the spotify API or [playerctl](https://github.com/altdesktop/playerctl) to create your own. 

[ncspot](https://github.com/hrkfdn/ncspot) is what I currently use. It's a ncurses spotify client. It's lightweight and runs in your terminal. Like spotifyd it doesn't come with desktop notification so you'll need to use the method below to add them. You can customise the colours and *some* of the keybindings in `~/.config/ncspot/config.toml`.  I've set up some global keybinds with playerctl that pause/resume skip and rewind. 

[Here's](https://rchu.cc/examples/spotify.notif.py) how I added desktop notifications to spotifyd and ncspot.

Check [this](https://wiki.archlinux.org/index.php/Spotify) out for more info on spotify on linux.
