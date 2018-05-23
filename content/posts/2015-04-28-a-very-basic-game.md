---
title: A Very Basic Game
author: chris
type: post
date: 2015-04-28T18:50:52+00:00
url: /sirchris/a-very-basic-game/
featured_image: /wp-content/uploads/2015/04/Screen-Shot-2015-04-28-at-10.31.33-AM.png
status_number:
  - 24
keyevent:
  - Battlefield Animations
  - Custom Battlefield Events
categories:
  - sirchris
tags:
  - status

---
Even though I [missed my goal][1] of releasing a game after a year of development, I still have a pretty solid foundation to build upon. And by foundation I mean an intro video, start screen, working world map, and very basic, yet playable battlefields. There’s still a lot of work to do, but here’s a look at those key foundation areas put together in the form of a simple game.
<!--more-->

<div style="clear:both">
  &nbsp;
</div>

<div class="inlineimg">
  {{< youtube HZudQYZOd7I >}}
</div>

I know the script is cheesy, the fonts are awful, and the interface is amateur hour, but there is a lot going on behind the scenes that is worth talking about.

#### Battlefield Background Movement

I wasn’t initially planning to add any type of background movement to the battlefields, but I did a trial run on just the first level to see if movement helped. To understand what I’m talking about, take a look at the first battle scene.

<div class="inlineimg">
  <img src="/wp-content/uploads/2015/04/01_castleBridge_on3.jpg" alt="01_castleBridge_on3" width="800" height="505" class="alignnone size-full wp-image-2086"  />
</div>

This image is completely flat and there is no movement in the background. And here’s a look at that same image with a little bit of movement added.

<div class="inlineimg">
  {{< gfycat data_id="SharpMagnificentAnt" >}}
</div>

You’ll notice that the rocks in the background are moving, their shadows are moving, and the shadows are layered behind the bridge. It’s not a huge difference, but I do think it adds a level of polish to the game. Here’s a look at another scene which not only has the floating rocks but also a portal animation.

<div class="inlineimg">
  {{< gfycat data_id="WaryKlutzyAsianporcupine" >}}
</div>

There are also scenes which have water like:

<div class="inlineimg">
  <img src="/wp-content/uploads/2015/04/19_BeackDock_02.jpg" alt="19_BeackDock_02" width="800" height="505" class="alignnone size-full wp-image-2084" />
</div>

I haven’t animated the water scenes yet, but you can imagine how adding some basic movement adds immersion and improves the game. I’ve decided to go ahead and add these animations to the game and that required a bit of code that can be reused across battlefields. A good amount of artwork was also required because the original illustrations were drawn as flat images which weren&#8217;t prepped for any type of movement. The first 5 battlefields are fully finished, but there are still another 17 to go.

#### Battlefield Custom Actions and Scripting

If you’ve ever played a game like Final Fantasy Tactics then you understand the importance of dialogue and actions that take place on the battlefield. If you haven’t, then here’s a quick clip of what I’m talking about (skip to about 7:00).

<div class="inlineimg">
  {{< youtube o1qo4dXku1c >}}
</div>

The use of in-game characters and animations to tell a story is perfect for my game because it doesn&#8217;t require any extra artwork. I’m already over budget so anything I can do myself is a big bonus.

<div class="inlineimg">
  <img src="/wp-content/uploads/2015/04/Screen-Shot-2015-04-28-at-10.31.33-AM.png" alt="Screen Shot 2015-04-28 at 10.31.33 AM" width="650" height="374" class="alignnone size-full wp-image-2081" />
</div>

Although the lines are cheesy and the interface ugly, I&#8217;ve built a solid storytelling foundation that can be polished and scaled to re-use throughout the game. I can add dialogue, custom events, and even player choices to help tell the game’s story. The backend is extremely flexible and this all comes at the low low cost of $0, which is perfect for my already over budget game.

#### World Map

Two critical parts of the world map that are functional now are the placement of battle markers and the drawing of the hero&#8217;s path.

<div class="inlineimg">
  {{< gfycat data_id="HospitableBlueGodwit" >}}
</div>

Each battle that takes place in the world is marked by an evil flag that will take the user to the appropriate battlefield when clicked. When the battle is won, the evil flag is be replaced by a flag indicating that the battle was won. A path is then drawn to the next battle, where a new evil flag is placed.

The locations of the flags and the paths are all stored in JSON, and although I only have 4 levels finished, it won&#8217;t be too much work to add the rest of the battles and paths to the game.

#### Intro Scene

I didn&#8217;t show the intro scene in the gameplay video and haven’t made any artistic changes to the intro scene since [the last time I discussed it][2], but here’s a look at the final sequence with a place holder voiceover and a nearly finished version of the intro music, which has turned out awesome.

<div class="inlineimg">
  {{< youtube W2cFz4Hz7Mg >}}
</div>

What’s been difficult with the scene over the last couple of weeks was experimenting with the possibility of having the intro being played back as a video versus rendering the scene with code. I would prefer to just play it back as a video, but I just don’t think it’s feasible with the Corona SDK. Corona doesn’t allow you embed videos into the game and uses a device’s media player for playback. That makes it hard to make scenes skippable and a seamless part of the game experience. That’s really kind of a bummer, but I don’t see a viable workaround.

#### Start Screen

The start screen has a lot of placeholder information and won’t look this ugly, but it was important to make it functional just to start getting a feel for the user experience. There are a few different start screen states depending on where the player is at in the game or if it’s a new game. To get that properly working I had to make sure the game can save to and load from a file correctly. So far so good and one thing I’m happy about is that the same art and music assets used at the end of the intro video are re-used for the start screen. That helps me save some time and money in a way that makes sense without cheapening the game experience.

#### Next Time

I’ve been working pretty frantically to get the game to this state, and when I do that I end up writing crappy code. I’m going to need to refactor a lot of what I’ve written in order to make sure the foundation is stable. This week is also the last week that I have with the illustrator, so I&#8217;ll be working with him closely to get any critical art assets completed.

 [1]: http://battleofbrothers.com/sirchris/one-year-later-late-and-over-budget
 [2]: http://battleofbrothers.com/sirchris/music-memory