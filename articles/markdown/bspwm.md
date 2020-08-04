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
script where you can run commmands to change the look and feel of bspwm.
You can also place some startup commands in it.


::: {.note}
Note: bspwm doesn't come with a way to control it. i.e None of your keys
will work You'll need to install a hotkey daemon (software that runs in
the background) such as sxhkd to manipulate windows.
:::
#### Here's mine

MANUALLY DO CODE, IT'S IMPOSSIBLE TO DO IT IN MARKDOWN

#### So what is it doing?

`bspc monitor -d I II III IV V`

This creates 5 workspaces that I can switch between. You can have up to
10 workspaces however I choose to use 5.

CODE

The first command sets the width of the borders around the windows, the
second sets the gap between tiled windows

The third command sets the padded space at the top of the screen.
You\'ll want to set this if you have a bar or else the window will just
cover it

CODE

This first line sets the split ratio. This if you had 1 window and
opened another this would decide what proportion of the screen the
second window would occupy.

#### What about the rest?

The remainder are startup commands. I\'ll try and cover these in another
post
