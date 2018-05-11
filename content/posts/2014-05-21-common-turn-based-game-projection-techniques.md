---
title: Common Turn Based Game Projection Techniques
author: chris
type: post
date: 2014-05-21T16:53:09+00:00
url: /2014/05/21/common-turn-based-game-projection-techniques/
categories:
  - sirchris
tags:
  - design
  - learning

---
A couple commonly used projection techniques for turn based video games are [orthographic][1] and [isometric][2] projection. I&#8217;m in the process of figuring out which technique I&#8217;ll be using for my tactics game and I&#8217;ve been looking into the pros and cons of each method and how they&#8217;ve been used in previous games. Here&#8217;s what I&#8217;ve discovered so far.

<!--more-->

#### Orthographic Projection

The orthographic projection is the view that pretty much every old school game like Mario, Zelda, and Civilization 1 used. Simply put, this technique places the camera above the action. You can see this technique commonly used in games with a top down view or a birds eye view.

The birds eye view places the camera directly over the character&#8217;s head and can be seen in older games like Civilization 1 and recent games like [Hunters][3] and [Warhammer Quest][4].

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/civilization1-1.jpg" alt="civilization1" width="640" height="400" class="alignnone size-full wp-image-533" srcset="http://localhost:8888/wp-content/uploads/2014/05/civilization1-1.jpg 640w, http://localhost:8888/wp-content/uploads/2014/05/civilization1-1-300x188.jpg 300w" sizes="(max-width: 640px) 100vw, 640px" />
</div>

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/hunters2-1.jpg" alt="hunters2" width="635" height="305" class="alignnone size-full wp-image-451" srcset="http://localhost:8888/wp-content/uploads/2014/05/hunters2-1.jpg 635w, http://localhost:8888/wp-content/uploads/2014/05/hunters2-1-300x144.jpg 300w" sizes="(max-width: 635px) 100vw, 635px" />
</div>

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/warhammer_quest_2-1-1024x581.jpg" alt="warhammer_quest_2" width="625" height="354" class="alignnone size-large wp-image-450" />
</div>

The top down view moves the camera point of view up a little bit, which allows us to give the screen and characters some depth. Some examples of this view in practice are Might and Magic 3, [Hero Academy][5], and [Braveland][6].

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/Heroes-of-Might-and-Magic-III-1.jpg" alt="Heroes-of-Might-and-Magic-III" width="600" height="450" class="alignnone size-full wp-image-529" srcset="http://localhost:8888/wp-content/uploads/2014/05/Heroes-of-Might-and-Magic-III-1.jpg 800w, http://localhost:8888/wp-content/uploads/2014/05/Heroes-of-Might-and-Magic-III-1-300x225.jpg 300w, http://localhost:8888/wp-content/uploads/2014/05/Heroes-of-Might-and-Magic-III-1-768x576.jpg 768w" sizes="(max-width: 600px) 100vw, 600px" />
</div>

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/Hero-Academy-1.png" alt="Hero-Academy" width="720" height="480" class="alignnone size-full wp-image-530" srcset="http://localhost:8888/wp-content/uploads/2014/05/Hero-Academy-1.png 960w, http://localhost:8888/wp-content/uploads/2014/05/Hero-Academy-1-300x200.png 300w, http://localhost:8888/wp-content/uploads/2014/05/Hero-Academy-1-768x512.png 768w" sizes="(max-width: 720px) 100vw, 720px" />
</div>

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/braveland-10-1.jpg" alt="braveland-10" width="800" height="450" class="alignnone size-full wp-image-455" srcset="http://localhost:8888/wp-content/uploads/2014/05/braveland-10-1.jpg 800w, http://localhost:8888/wp-content/uploads/2014/05/braveland-10-1-300x169.jpg 300w, http://localhost:8888/wp-content/uploads/2014/05/braveland-10-1-768x432.jpg 768w" sizes="(max-width: 800px) 100vw, 800px" />
</div>

The orthographic point of view is what I have been primarily experimenting with so far and the pros for this technique are that everything is completely grid based at a 1:1 scale, making programming calculations easier, and fewer character animations are needed, which saves on artwork. I think the main downside of this point of view, especially the top down style, is that the artwork and animations can look a little awkward and cheesy.

#### Isometric Projection

Isometric projection is commonly referred to as 2.5D and this technique creates the illusion of 3D in a 2D world by using angles. Instead of the straight 90 degree angles that are used in orthographic projection, isometric projection uses slopes to give each tile a diamond shape. Examples of this in practice can be seen in Final Fantasy Tactics, [Ravenmark][4], [Banner Saga][7] and UFO.

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/final-fantasy-tactids-1.jpg" alt="final-fantasy-tactids" width="640" height="480" class="alignnone size-full wp-image-531" srcset="http://localhost:8888/wp-content/uploads/2014/05/final-fantasy-tactids-1.jpg 640w, http://localhost:8888/wp-content/uploads/2014/05/final-fantasy-tactids-1-300x225.jpg 300w" sizes="(max-width: 640px) 100vw, 640px" />
</div>

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/ravenmark-1.jpg" alt="ravenmark" width="568" height="320" class="alignnone size-full wp-image-449" srcset="http://localhost:8888/wp-content/uploads/2014/05/ravenmark-1.jpg 568w, http://localhost:8888/wp-content/uploads/2014/05/ravenmark-1-300x169.jpg 300w" sizes="(max-width: 568px) 100vw, 568px" />
</div>

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/Banner-Saga-1.jpg" alt="Banner Saga" width="792" height="473" class="alignnone size-full wp-image-452" srcset="http://localhost:8888/wp-content/uploads/2014/05/Banner-Saga-1.jpg 792w, http://localhost:8888/wp-content/uploads/2014/05/Banner-Saga-1-300x179.jpg 300w, http://localhost:8888/wp-content/uploads/2014/05/Banner-Saga-1-768x459.jpg 768w" sizes="(max-width: 792px) 100vw, 792px" />
</div>

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/ufo-1.gif" alt="ufo" width="640" height="400" class="alignnone size-full wp-image-532" />
</div>

I personally think isometric projection looks better for most turn based games, but it does add more programming difficulty and artwork, both of which cost time and money. I plan on experimenting with this technique over the next couple of weeks and I&#8217;ll keep you posted on what I learn.

#### Further Reading

If you&#8217;re looking to learn more about different projection techniques, here are some of the better resources that I&#8217;ve come across

  * [Amit&#8217;s Game Programming Information (Amazing Resource for Tile Based Games)][8]
  * [Isometric Tiles Introduction][9]
  * [A layman&#8217;s Guide to Projection in Videogames][10]
  * [Isometric Tile Math][11]
  * [Creating Isometric World Primer][12]
  * [The Best Looking Isometric Games][13]

 [1]: http://en.wikipedia.org/wiki/Orthographic_projection
 [2]: http://en.wikipedia.org/wiki/Isometric_projection
 [3]: http://www.rodeogames.co.uk/hunters-episode-one/
 [4]: http://www.rodeogames.co.uk/warhammer-quest/
 [5]: http://origin-www.robotentertainment.com/games/heroacademy/
 [6]: http://www.tortugateam.com/en/
 [7]: http://stoicstudio.com
 [8]: http://www-cs-students.stanford.edu/~amitp/gameprog.html#tiles
 [9]: http://flarerpg.org/tutorials/isometric_intro/
 [10]: http://www.significant-bits.com/a-laymans-guide-to-projection-in-videogames
 [11]: http://clintbellanger.net/articles/isometric_math/
 [12]: http://gamedevelopment.tutsplus.com/tutorials/creating-isometric-worlds-a-primer-for-game-developers--gamedev-6511
 [13]: http://kotaku.com/5991061/the-best-looking-isometric-games