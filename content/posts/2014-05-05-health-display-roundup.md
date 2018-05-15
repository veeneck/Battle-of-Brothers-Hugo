---
title: Health Display Roundup
author: chris
type: post
date: 2014-05-05T16:59:16+00:00
url: /sirchris/health-display-roundup/
categories:
  - sirchris
tags:
  - design
  - roundup

---
Visually displaying a character&#8217;s health has been around for over 30 years and continues to be a mainstay of video games. From Zelda to Starcraft, these small graphics play a large role in how games are played and how information is communicated. The turn based game I&#8217;m working on will include health bars, so I&#8217;ve been looking into how other successful games have given their characters life. Here is a quick roundup of some of the more popular techniques I&#8217;ve come across.
<!--more-->

#### Bar Above the Head

The good ol&#8217; bar above the head technique is probably one of the most common ways to display health. You can see this in [Battleheart][1] and [Starcraft 2][2] and one thing I like about their implementation is that they both change the color of the bar in order to add a secondary visual cue. This is particularly helpful when you have to make extremely quick decisions, like whether or not to run from a Zerg swarm.

<div class="inlineimg">
  <img class="alignnone size-full wp-image-446" src="http://localhost:8888/wp-content/uploads/2014/05/screen568x568-1.jpeg" alt="screen568x568" width="568" height="320" srcset="http://localhost:8888/wp-content/uploads/2014/05/screen568x568-1.jpeg 568w, http://localhost:8888/wp-content/uploads/2014/05/screen568x568-1-300x169.jpeg 300w" sizes="(max-width: 568px) 100vw, 568px" />
</div>

<div class="inlineimg">
  <img class="alignnone size-full wp-image-447" src="http://localhost:8888/wp-content/uploads/2014/05/starcraft-1.jpg" alt="starcraft" width="497" height="157" srcset="http://localhost:8888/wp-content/uploads/2014/05/starcraft-1.jpg 497w, http://localhost:8888/wp-content/uploads/2014/05/starcraft-1-300x95.jpg 300w" sizes="(max-width: 497px) 100vw, 497px" />
</div>

#### Circular

You don&#8217;t see circular health displays all that much, and I think part of the reason is due to screen real estate, but two games that pull it off are [Ravenmark][3] and [Gratuitous Tank Battles][4].

<div class="inlineimg">
  <img class="alignnone size-full wp-image-449" src="http://localhost:8888/wp-content/uploads/2014/05/ravenmark-1.jpg" alt="ravenmark" width="568" height="320" srcset="http://localhost:8888/wp-content/uploads/2014/05/ravenmark-1.jpg 568w, http://localhost:8888/wp-content/uploads/2014/05/ravenmark-1-300x169.jpg 300w" sizes="(max-width: 568px) 100vw, 568px" />
</div>

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/Gratuitous-Tank-Battles-screenshot-2_thumb-1.jpg" alt="Gratuitous-Tank-Battles-screenshot-2_thumb" width="540" height="300" class="alignnone size-full wp-image-462" srcset="http://localhost:8888/wp-content/uploads/2014/05/Gratuitous-Tank-Battles-screenshot-2_thumb-1.jpg 540w, http://localhost:8888/wp-content/uploads/2014/05/Gratuitous-Tank-Battles-screenshot-2_thumb-1-300x167.jpg 300w" sizes="(max-width: 540px) 100vw, 540px" />
</div>

#### Half Circle

What happens when you introduce the standard health bar to the circular health bar, turn on a little Barry White, and wait 9 months? The half circle health bar is what happens. I&#8217;m not sure pioneered this concept, but Rodeo Games has two great examples in [Warhammer Quest][5] and [Hunters 2][6].

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/warhammer_quest_2-1-1024x581.jpg" alt="warhammer_quest_2" width="625" height="354" class="alignnone size-large wp-image-450" />
</div>

<div class="inlineimg">
  <img class="alignnone size-full wp-image-451" src="http://localhost:8888/wp-content/uploads/2014/05/hunters2-1.jpg" alt="hunters2" width="635" height="305" srcset="http://localhost:8888/wp-content/uploads/2014/05/hunters2-1.jpg 635w, http://localhost:8888/wp-content/uploads/2014/05/hunters2-1-300x144.jpg 300w" sizes="(max-width: 635px) 100vw, 635px" />
</div>

#### Unique and Stylish

Who says health displays have to be simplistic colored bars or circles? I think [The Banner Saga][7] and [Skulls of the Shogun][8] did amazing jobs by making the health displays a part of their game&#8217;s overall artistic style.

<div class="inlineimg">
  <img class="alignnone size-full wp-image-452" src="http://localhost:8888/wp-content/uploads/2014/05/Banner-Saga-1.jpg" alt="Banner Saga" width="792" height="473" srcset="http://localhost:8888/wp-content/uploads/2014/05/Banner-Saga-1.jpg 792w, http://localhost:8888/wp-content/uploads/2014/05/Banner-Saga-1-300x179.jpg 300w, http://localhost:8888/wp-content/uploads/2014/05/Banner-Saga-1-768x459.jpg 768w" sizes="(max-width: 792px) 100vw, 792px" />
</div>

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/skulls-1-1024x591.jpg" alt="skulls" width="625" height="360" class="alignnone size-large wp-image-453" srcset="http://localhost:8888/wp-content/uploads/2014/05/skulls-1-1024x591.jpg 1024w, http://localhost:8888/wp-content/uploads/2014/05/skulls-1-300x173.jpg 300w, http://localhost:8888/wp-content/uploads/2014/05/skulls-1-768x443.jpg 768w, http://localhost:8888/wp-content/uploads/2014/05/skulls-1.jpg 1143w" sizes="(max-width: 625px) 100vw, 625px" />
</div>

#### Unit Count

It would be awesome if we could create massive armies like you see in [Rome Total War][9], but that isn&#8217;t possible for a lot of reasons. A quick and easy way to show that there are multiple units, without actually displaying multiple units, is by adding a number signifying how many units of a single character exist. Below you can see what I&#8217;m talking about in [Might and Magic 6][10] and [Braveland][11].

<div class="inlineimg">
  <img class="alignnone size-full wp-image-454" src="http://localhost:8888/wp-content/uploads/2014/05/might-and-magic-1.jpg" alt="might and magic" width="697" height="489" srcset="http://localhost:8888/wp-content/uploads/2014/05/might-and-magic-1.jpg 697w, http://localhost:8888/wp-content/uploads/2014/05/might-and-magic-1-300x210.jpg 300w" sizes="(max-width: 697px) 100vw, 697px" />
</div>

<div class="inlineimg">
  <img class="alignnone size-full wp-image-455" src="http://localhost:8888/wp-content/uploads/2014/05/braveland-10-1.jpg" alt="braveland-10" width="800" height="450" srcset="http://localhost:8888/wp-content/uploads/2014/05/braveland-10-1.jpg 800w, http://localhost:8888/wp-content/uploads/2014/05/braveland-10-1-300x169.jpg 300w, http://localhost:8888/wp-content/uploads/2014/05/braveland-10-1-768x432.jpg 768w" sizes="(max-width: 800px) 100vw, 800px" />
</div>

 [1]: https://itunes.apple.com/us/app/battleheart/id394057299?mt=8
 [2]: http://us.battle.net/sc2/en/
 [3]: http://ravenmark-saga.com
 [4]: http://www.gratuitoustankbattles.com
 [5]: https://itunes.apple.com/us/app/warhammer-quest/id573516833?mt=8
 [6]: https://itunes.apple.com/us/app/hunters-2/id489463556?mt=8
 [7]: http://stoicstudio.com
 [8]: http://skullsoftheshogun.com
 [9]: http://www.totalwar.com/en_us/
 [10]: http://might-and-magic.ubi.com/heroes-6/
 [11]: http://www.tortugateam.com/en/