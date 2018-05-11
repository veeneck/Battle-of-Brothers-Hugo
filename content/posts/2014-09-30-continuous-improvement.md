---
title: Continuous Improvement
author: chris
type: post
date: 2014-09-30T19:37:01+00:00
url: /2014/09/30/continuous-improvement/
featured_image: /wp-content/uploads/2014/09/ortho_blackKnight_03-1.png
number:
  - 13
  - 13
keyevent:
  - Added Disengage/Bash
  - Added Abilities Over Time
  - Added New Class
  - Added Disengage/Bash
  - Added Abilities Over Time
  - Added New Class
categories:
  - sirchris
tags:
  - status

---
As planned, I was able to continue programming over the last two weeks and add some more features and a new character to the demo. I also spent a little time working on some new character concepts, battlegrounds, and animation preparation.

<!--more-->

https://www.youtube.com/watch?v=Yv_7GOVxA1E&feature=youtu.be

#### Added Ability Points

Each character will have different abilities, ranging from basic attack to ultimate attacks, and those abilities will be limited by some form of power or resource management. I don&#8217;t know how that&#8217;s going to exactly play out, but that doesn&#8217;t mean I can&#8217;t set up the code for when I do know. Right now, each character starts with a few resource points and each ability requires points to be used. A character regains a point after each turn, so they can save up points by not using stronger attacks during their attack phases.

#### Added Disengage/Bash

I explained the concept of engagement in [the last update][1], and this time around I added the functionality to disengage. The idea is that some characters will have an ability to disengage from combat without being penalized. In the video example I added a bash ability to the warrior class that does direct damage and also allows him to disengage with the enemy. This could be a useful ability to get him out of a tight spot or to help a friend in need.

#### Added Abilities over Time/StoneStance

Most actions and effects happen immediately but some will be on a delay. Poison, for example, would be a lingering effect that does most of its damage over consecutive turns and not when it is initially inflicted. I added that type of functionality by implementing the stone stance ability to the warrior class. This ability is a self-buff that the warrior class casts to greatly increase the chances that he blocks an enemy melee attack. It would come in handy if he&#8217;s low on life or expecting to get beat down by a bunch of baddies.

#### Added an Archer

I don&#8217;t think the final game is going to have a pure archer type of class, but that&#8217;s one of the animations I had on hand and ready to go. It was less important to add a specific game character as it was to see how long it took me to get another character into the game. A few weeks ago I completely re-wrote my character creation classes so that the code is as modular and reusable as possible. Things turned out great and I was able to get the new character in there in less than a day.

#### Added Abilities to the Archer

For similar reasons as adding the archer class, I wanted to see how long it took me to add new abilities to a class. Again, things went very smoothly with the new code and I was able to add an attack, double attack, and flaming arrow attack to the archer. The animations are pretty cheesy, but adding the real animations will only take a few lines of code when they arrive.

#### More Artwork

I continued to work with an illustrator and animator on character concepts, level designs, and animations. As far as progress goes, level and character designs are about 40% complete, and the animations are 5-10% complete. Here is some concept work of the first evil character making his way into the game.

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/09/concepts_chaosKnight_01.jpg" alt="concepts_chaosKnight_01" width="800" height="383" class="alignnone size-full wp-image-1327" srcset="http://localhost:8888/wp-content/uploads/2014/09/concepts_chaosKnight_01.jpg 1000w, http://localhost:8888/wp-content/uploads/2014/09/concepts_chaosKnight_01-300x144.jpg 300w, http://localhost:8888/wp-content/uploads/2014/09/concepts_chaosKnight_01-768x368.jpg 768w" sizes="(max-width: 800px) 100vw, 800px" />
</div>

#### Coming Up

It&#8217;s hard to plan what&#8217;ll be going on over the next couple of weeks, because [the enemy][2] is getting married. I&#8217;m pretty sure this is where I&#8217;ll pull ahead in the competition because he isn&#8217;t prepared to handle married life and especially kids if they&#8217;re in the immediate future.

With the development time I do get over the next couple weeks, I plan on adding some more core functionality to the game. I&#8217;m waiting on the animation artwork to catch up with the programming I&#8217;ve done so far and I think I should spend some time on loading/saving game state, dialogue screens, character upgrade screens, and other functionality that will definitely make it into the game.

 [1]: http://battleofbrothers.com/sirchris/back-to-programming
 [2]: http://battleofbrothers.com/sirryan