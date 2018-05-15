---
title: A Wobbly Foundation
author: Ryan
type: post
date: 2015-05-12T16:49:29+00:00
url: /2015/05/12/a-wobbly-foundation/
number:
  - 21
keyevent:
  - Battle start and end.
  - Main menu polish.
  - Started with composer.
categories:
  - sirryan
tags:
  - status

---
An unsteady foundation is still a foundation, right? I&#8217;ve continued my work of porting all code into a single project. You can roughly play the game from start to level 2 right now. This means loading, saving, world map, placing troops, enemy waves, game over state, resuming, story, and more. There is a lot of core code in place.
<!--more-->

The only catch? It&#8217;s not stable yet. Memory leaks, timing issues and missing assets are still common. I&#8217;ll keep iterating on this next update. And when I get bored with that, I incrementally polish different screens. During this update, I revisited the main menu and world map.

<div class="inlineimg">
  [youtube=https://www.youtube.com/watch?v=8wekuzwkWG0&w=740&theme=light]
</div>

#### Laying a Foundation

When I say that I&#8217;m laying a foundation, here are some specifics on what I mean.

  * Sizing all assets needed for the first 3 levels, and making sure they&#8217;re fine on all devices.
  * Testing button sizes and making sure their click region is large enough.
  * Adding functionality like propagation to buttons, which SpriteKit does not have built in.
  * Larger placeholder assets for music and video streaming, to see how memory and loading is affected.
  * Playing with volume control on music, and trying to keep music playing between scenes.
  * Tons of memory issues / leaks between scenes.
  * Fix common crashes in combat to get an alpha playable.
  * Come up with some sort of basic, reusable UI pattern.
  * Fix redundant problems in the code.

There is plenty more to add to that list, but you get the idea. Once the first 3 levels are rock solid, adding every additional level will just be more of the same. So, I&#8217;m just trying to get to a decent, bug free code base for general game navigation along with basic combat functionality. At that point, I can bring in co-workers for a super early alpha to test on different devices. From there, I&#8217;ll spend months working on an in depth combat layer in preparation for a beta.

#### Main Menu

Since I now have all of the art and music for a main menu, I decided to start making it functional. Technically, this means a few things:

  * Detect if it&#8217;s the first time playing, and show different logos (i.e.: company logo) accordingly.
  * Make the music transition smoothly when going to the loading screen, or directly into story scene.
  * Create up to 3 new save files, and allow the user to delete them.

Have a look at the first draft below. Everything, including the title, are subject to change. But, I now have a decent foundation to work with here.

<div class="inlineimg">
  {{< gfycat data_id="NeedyPositiveKiskadee" >}}
</div>

One of the nice things about implementing the main menu is that I took my time. I set no deadlines, so I was not rushed. I played around with movement and light. I learned tricks in Pixelmator. The code is clean and reusable. Overall, it felt really good to get something to a decent state. So much in game development is overwhelming that this was a welcome change.

#### World Map

The problem with the world map is that it is too cartoony when compared to the rest of the game. Everything is serious and somber, and then you have this happy world map breaking the flow. So, before having the art redone, I&#8217;m playing with ways to make everything look more consistent. Here is that first attempt.

The old world map.

<div class="inlineimg">
  {{< gfycat data_id="ColossalFemaleCobra" >}}
</div>

The new world map.

<div class="inlineimg">
  {{< gfycat data_id="PertinentFamousGlowworm" >}}
</div>

There is definitely some progress, but it isn&#8217;t there yet. Having icons designed could be a huge help. Also, I&#8217;ll be reaching out to Brian for help on this one to see if he has any tricks up his sleeves.