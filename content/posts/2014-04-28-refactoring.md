---
title: Refactoring
author: chris
type: post
date: 2014-04-28T18:24:53+00:00
url: /2014/04/28/refactoring/
featured_image: /wp-content/uploads/2014/04/Screen-Shot-2014-04-28-at-1.19.20-PM-1.png
keyevent:
  - Make code object oriented
  - Add enemies to fight
  - Re-calculate move distance
  - Make code object oriented
  - Add enemies to fight
  - Re-calculate move distance
number:
  - 3
  - 3
categories:
  - sirchris
tags:
  - status

---
When I left off two weeks ago, I had the goal of adding some bad guys to fight my valiant knight. The good news is that those bad guys can now be seen and attacked, but the bad news is that for every step forward, I&#8217;ve had to take about 0.9 steps back. If learning was the name of the game before my first update, refactoring is the name of the game this time around. I knew there was going to be a price to pay for plunging into my game without much thought given to organization and structure, and it was time to pay the piper.

But in an effort to stay positive about game development, let&#8217;s celebrate the visual progress I&#8217;ve made.

<!--more-->

#### Bad Guys & Health Bars

As you can see, there is not one, but three very scary ogres for my hero to fight. Each character also has a health bar displayed above them that moves along with the character and accurately displays total health.

<div class="inlineimg">
  <img class="alignnone size-full wp-image-424" src="http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-28-at-1.19.13-PM-1.png" alt="Screen Shot 2014-04-28 at 1.19.13 PM" width="704" height="451" srcset="http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-28-at-1.19.13-PM-1.png 704w, http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-28-at-1.19.13-PM-1-300x192.png 300w" sizes="(max-width: 704px) 100vw, 704px" />
</div>

#### Range Calculations and Enemies in Range

The hero&#8217;s movement grid now shrinks after he moves and enemies light up when they are in attacking range.

<div class="inlineimg">
  <img class="alignnone size-full wp-image-425" src="http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-28-at-1.19.20-PM-1.png" alt="Screen Shot 2014-04-28 at 1.19.20 PM" width="600" height="381" srcset="http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-28-at-1.19.20-PM-1.png 600w, http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-28-at-1.19.20-PM-1-300x191.png 300w" sizes="(max-width: 600px) 100vw, 600px" />
</div>

#### Fight

The hero has an animation sequence that swings his sword. And if you look closely, you&#8217;ll also see a -5 above the ogre, which is a separate animation sequence displaying the amount of damage taken.

<div class="inlineimg">
  <img class="alignnone size-full wp-image-426" src="http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-28-at-1.19.24-PM-1.png" alt="Screen Shot 2014-04-28 at 1.19.24 PM" width="600" height="381" srcset="http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-28-at-1.19.24-PM-1.png 600w, http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-28-at-1.19.24-PM-1-300x191.png 300w" sizes="(max-width: 600px) 100vw, 600px" />
</div>

So there is some visual progress to show, but the real improvement has been in the codebase. Besides a few helper functions, I had to re-write pretty much every line of code. And once that code was re-written, I would add a new feature and then have to re-write the code again. This isn&#8217;t too unexpected, because it&#8217;s hard for me to mentally plan what I have to do when I&#8217;ve never done it before.

My main goal these past two weeks was to make the codebase as object-oriented as possible. It seems like game code gets unwieldy extremely quickly, so I have to make an effort to keep the codebase nice and neat before it becomes completely unmanageable . Knights and ogres inherit from a Character class. Movement and damage are handled in specialized classes. Each scene, or game level, is an instance of the Scene class, which pulls many of its functions from a SceneHelper class. Scene variables, including the background and character information are all dynamically loaded from scene specific JSON files.

And while I have most of the core areas set up as their own classes, I still have some organizational questions to solve. For example, now that I can see that my characters all have some similar animation sequences, should they still handle the sprite animation individually, or should the base character class inherit from some type of sprite animation class?

Anyways, during the next two weeks I&#8217;ll probably play around with core code organization a little bit more and I&#8217;ll also delve into the realm of artificial intelligence. My game now knows that it&#8217;s the ogre&#8217;s turn to make a move after the knight attacks, but I have to give the ogre a brain to decide what move to make. I&#8217;ve seen [Ryan really struggle with AI][1] over the past week or two, so I might be in for a little brain pain.

 [1]: http://battleofbrothers.com/sirryan/its-not-all-sunshine-and-rainbows