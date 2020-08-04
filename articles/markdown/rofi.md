---
title: custom rofi menus
date: 05-08-2020
---

[rofi](https://github.com/davatorium/rofi) is a multipurpose menu application. It switches windows, launches apps, and much more.

One interesting function of rofi is creating custom menus. In order to do so you need to use the `-dmenu` flag on rofi.

First you'll need to pass in your options you want to display on the screen. 

After selection is chosen, the choice is outputed in `STDOUT`. This means that you can take the input and perform an action based on the output.

It'll be clearer if you see an example.

Below is a script using rofi to take a screenshot.

FULL CODE

### So how does it work?

FIRST FEW LINES

First we define the command. I also specify a theme so that it looks nice. 

OPTIONS SECTION

Next we store each selection in a variable. This will be what the user sees in the menu. We then store all of the options in a variable each separated by 1 line. 

CASE SWITCH

This is then piped into the rofi command we defined earlier.

`echo -e` outputs our options without displaying the newline characters. 

`-p` is to set the prompt text and `-i` makes it case insensitive.

Once the user makes a selection, the output is then stored.
We then can use a switch case statement to perform an action based on which option was picked.

Here's a gif of the script in action.

![rofi menu](https://rchu.cc/img/rofi/rofi.gif)

The basic idea of this can be used for anything you can think of. Sky's the limit.