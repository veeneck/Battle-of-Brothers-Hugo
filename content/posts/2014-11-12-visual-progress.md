---
title: Visual Progress
author: chris
type: post
date: 2014-11-12T17:00:53+00:00
url: /sirchris/visual-progress/
featured_image: /wp-content/uploads/2014/11/characterscreen.png
keyevent:
  - Added Level Markers
  - Added Battlefield Tiles
  - Added Character Management
status_number:
  - 15
categories:
  - sirchris
tags:
  - status

---
I really enjoyed working on the game over the last few weeks because pretty much everything I did resulted in visual progress. Adding code and manipulating JSON files is good and dandy, but programming is a lot more exciting when I&#8217;m working on something that my family and friends can visually experience.
<!--more-->

In this update, I was able to add battlefield markers to the world map, add tiles to those battlefields, and get started on the character management screen. Check out the video below to see where things are at.

{{< youtube vfJ1bXabS3c >}}

#### Level Markers

I plan on having 20 levels, or battlefields, in the game and 19.5 of those levels are now complete. I needed an easy way to move between levels for testing purposes, so I added markers to the world map that allow me to click on and enter an individual level. And as you can see below, each level helps to illustrate a spot on the world map, so hopefully by the end of the game the player has a good feel for the world and its inhabitants.

<div class="inlineimg">
  <img src="/wp-content/uploads/2014/11/maplevels.jpg" alt="maplevels" width="750" height="566" class="alignnone size-full wp-image-1434" />
</div>

#### Added Tiles to Battlefields

Each battlefield contains an isometric grid, which determines where characters can move. Those grids are custom to each battlefield, so I made 20 JSON files, each of which contains information about a specific battlefield&#8217;s grid. Here&#8217;s a look at two of the grids, with one being pretty straight and rectangular and the other having some obstacles and corners.

<div class="inlineimg">
  <img src="/wp-content/uploads/2014/11/maptiles.jpg" alt="maptiles" width="541" height="746" class="alignnone size-full wp-image-1433" />
</div>

#### Character Management Screen

The character management screen is where the player will be able to upgrade and customize their characters. Right now the management screen allows the player to toggle between a couple characters and assign action points to a character&#8217;s customizable stats. More characters and options will added down the road, and nothing on this screen is finalized, but hopefully the heavy lifting for this page is done and future tweaks won&#8217;t take too much work.

<div class="inlineimg">
  <img src="/wp-content/uploads/2014/11/characterscreen.png" alt="characterscreen" width="625" height="471" class="alignnone size-large wp-image-1432" />
</div>

#### What&#8217;s Next

Progress is starting to speed up on my character animations, so I&#8217;m hoping some of those can make their way into the game. Besides adding any artwork that may or may not arrive, I&#8217;ll be adding more characters to the character management screen, get started on character dialogue, and add the code to show cut scenes.