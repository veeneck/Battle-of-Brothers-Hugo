---
title: Another Shot at the Intro Video
author: chris
type: post
date: 2015-03-17T14:40:01+00:00
url: /sirchris/another-shot-at-the-intro-video/
featured_image: /wp-content/uploads/2015/03/Screen-Shot-2015-03-12-at-4.05.26-PM.png
status_number:
  - 22
keyevent:
  - Intro Video Take 2
  - Music Beginnings
categories:
  - sirchris
tags:
  - stat
  - status

---
I said I wouldn’t do it, but I couldn’t help myself and took another crack at the intro video. The main practical reason is because the game’s music is being composed, and it kind of all derives from the intro song. The main impractical reason is because I hated the first video and couldn’t help myself from trying again. Here’s look at the second attempt.
<!--more-->

<div style="clear:both">
  &nbsp;
</div>

<div class="inlineimg">
  {{< youtube 4DMJj8iye_g >}}
</div>

The main difference between this attempt and the first try is that the storyteller only shows in the beginning and the end of the video. That in itself cuts a full minute from the video and makes it flow so much better. Doing that also allows me to highlight the artwork, which probably wasn’t being shown at a large enough scale on mobile devices. Finally, I fixed most of the timing issues so each sentence/image/transition is similar. There are still a few bugs to work out, but I’m much happier with this attempt.

I want to give a big thank you to Rand, who [commented on the last status update][1] on what was and wasn’t working in the first video. Your feedback was very helpful and I appreciate it.

#### Music

As I said in the opening paragraph, [Brendon Williams][2] is starting to work on the game’s music and the first piece he wants to score is the title song. The intro movie leads into the title, so I had to have the intro done, or at least part of it, for him to get started on the song. We’ve brainstormed a few ideas for how the music will generally work throughout the game. The game’s world has very distinct lands and battlefields, and Brendon is going to try to match the music to the flavor of the lands and artwork. I’m looking forward to seeing what he comes up with, because he’s really going to help with bringing the world to life.

#### Some Little Things

I added a button to “Begin Story” that transitions from the title screen to the first level of the game.

<div class="inlineimg">
  {{< gfycat data_id="CookedSpicyCoqui" >}}
</div>

This was important to me because I can start to actually experience the game as the end-user will. My goal right now is to create a playable game for the first 4 game levels, and the game starts with the transition from the title screen to the world map or first level.

I also played around with how the battlefield markers will be first displayed and how they will transition between states (won vs. lost etc.) There is still some work to do with this, but here’s a look so far.

<div class="inlineimg">
  {{< gfycat data_id="EuphoricChiefAngwantibo" >}}
</div>

#### Scene Management

This section isn’t sexy, but it did take up a good chunk of my time and is worth writing about. With Corona SDK and a lot of frameworks, scene management is used to efficiently manage and transition between scenes. A scene is a self contained part of the game, like the intro screen, world map screen, battlefield screen, etc. Well, my first attempt at the game didn’t exactly use Corona’s scene management functionality correctly, and that was causing some memory issues, delay issues, and ugly code. I cleaned my code up and now have my 5 major scenes(so far) properly split out.

One thing to mention in case any Corona programmers are reading this is that Corona doesn’t appear to support any type of multi threading. The problem with that is when I transition between scenes there is a long pause while the next scene is being loaded. You can pre-load scenes using composer.loadScene(), but that causes all other operations to stop and doesn’t help the game move along any quicker. If anybody knows of a way to pre-load scenes without causing a delay in the game’s execution, I’d love to know.

#### Next Time

As I noted in the scene management section, there are some delays between transitioning between screens that I’m going to experiment with. I’ll need to complete the world map animations so I have a better idea of how much texture memory it uses. I’ll also continue to work on the first level to get a feel for the memory requirements there and to see what types of memory saving short cuts might be available.

 [1]: http://battleofbrothers.com/sirchris/intro-video-artwork-and-audio#comment-1131
 [2]: https://soundcloud.com/brendonmcwilliams