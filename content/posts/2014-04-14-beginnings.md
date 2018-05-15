---
title: Beginnings
author: chris
type: post
date: 2014-04-14T17:48:47+00:00
url: /2014/04/14/beginnings/
featured_image: /wp-content/uploads/2014/04/Screen-Shot-2014-04-14-at-12.57.57-PM-1.png
number:
  - 2
keyevent:
  - Learn Corona and Lua Basics
  - Display Scenes and Sprites
  - 'Implement A* and Allowable Movement Algorithms'
categories:
  - sirchris
tags:
  - status

---
I&#8217;m two weeks into game development and I&#8217;ve realized that making a game will require a lot of learning and hard work, and this is going to be a lot of fun. I know so little about game development that it&#8217;s difficult to even know where to start. What should be a seemingly simple task, like animating and moving a sprite, can be challenging due to amateur hour mistakes.
<!--more-->

But whenever I overcome one of those challenges, I am elated. There is something amazing about seeing your work visually come to life. I made a knight move! I&#8217;m not writing a billing system or some database software where numbers are calculated and input boxes drawn. I made a knight. And he moves! I feel like Tom Hanks in Cast Away [when he created fire][1]. Anyways, to get into the nitty gritty, here&#8217;s how things have played out for me so far.

**I took a lot of Corona and Lua Tutorials**
  
I use [RescueTime][2] to track my work habits and about 60% of my time was spent on tutorials. I&#8217;ve had too many problems in the past with jumping into things I didn&#8217;t understand, so I spent a solid week understanding basics of the Lua language and [Corona framework][3]. I went through a ton of documentation and videos , and some of the concepts I really focused on before working on any type of game were:

  * The Lua Syntax &#8211; I recommend [Programming in Lua][4] by Roberto Ierusalimschy
  * [Event Listeners][5]
  * [Storyboarding and Scene Management][6]
  * [How to make Lua Object Oriented][7]

After I had a handle on the basics of Corona and Lua, I decided it was time to strike it out on my own.

**I started my Game**
  
The experts say to build what you like and what I like are turn based strategy games. XCOM, Might and Magic, Great Little War Game, Hunters, and The Banner Saga are all games that I love to play. Those same games are all too complicated and in depth for a solo beginner developer with a small budget and in one year&#8217;s time, but I do hope to draw inspiration from them and add a new game to the genre.

I&#8217;ll probably spend the next month or two playing around with the concepts and functionality commonly found in grid turn based strategy games, so you&#8217;ll understand why I&#8217;m building what I&#8217;m building. A few of the key tasks that I accomplished in this last week were:

**Load a Background Image and Draw a Grid**
  
All of my game levels will probably take place on some sort of a grid, so I played around with backgrounds and grids. I may have to end up using individual tile images to draw my grids, but I started by overlaying transparent individual tile objects on top of a single background image. Each tile then has an event listener attached to it to know when it is clicked.

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-14-at-11.08.35-AM-1.png" alt="Screen Shot 2014-04-14 at 11.08.35 AM" width="771" height="512" class="alignnone size-full wp-image-319" srcset="http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-14-at-11.08.35-AM-1.png 771w, http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-14-at-11.08.35-AM-1-300x199.png 300w, http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-14-at-11.08.35-AM-1-768x510.png 768w" sizes="(max-width: 771px) 100vw, 771px" />
</div>

**Sprite Animation**
  
Animating a character took longer than it should have because I didn&#8217;t understand exactly how [Corona and TexturePacker worked together][8]. After makings things more confusing than they should have been, I did end up with a pretty sweet looking knight.

**Pathfinding using Jumper and A**
  
A* is a common pathfinding algorithm and Roland Yonaba made it about 10 times faster with his [Jumper library][9]. I implemented that library so that my character knows the most efficient way to move from point A to point B, making sure to avoid any obstacles in their way.

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-14-at-12.57.57-PM-1.png" alt="Screen Shot 2014-04-14 at 12.57.57 PM" width="762" height="445" class="alignnone size-full wp-image-320" srcset="http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-14-at-12.57.57-PM-1.png 762w, http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-14-at-12.57.57-PM-1-300x175.png 300w" sizes="(max-width: 762px) 100vw, 762px" />
</div>

**Algorithm for Allowable Movement**
  
Characters will only be allowed to move a certain distance each turn, so I needed an algorithm to calculate and highlight which tiles the hero can move to.

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-14-at-11.09.38-AM-1.png" alt="Screen Shot 2014-04-14 at 11.09.38 AM" width="761" height="574" class="alignnone size-full wp-image-321" srcset="http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-14-at-11.09.38-AM-1.png 761w, http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-14-at-11.09.38-AM-1-300x226.png 300w" sizes="(max-width: 761px) 100vw, 761px" />
</div>

In case you ever need to do this yourself, the code I&#8217;m using is:

https://gist.github.com/codepaladin/10665797

This is going to get more complicated when more obstacles are added, but that&#8217;s going to be a problem for another day.

**Intro and Scene Management**
  
Corona has an easy and understandable way to separate your game by scenes by using their [Composer API][10]. What I did was set my project up so that there are two scenes: the intro menu screen and the first level. This basic scene functionality can be built upon in the future to easily separate splash screens, game levels, character stat screens, etc.

**What&#8217;s Next**
  
The next thing I&#8217;d like to do is add a bad guy for my hero to fight. That means the hero and enemy will have to have attributes like hit points, strength, toughness, magic resistance, weapons, armor etc. It also means I have to turn my spaghetti code into clean object oriented code before things get too crazy.

Until next time.

 [1]: https://www.youtube.com/watch?v=IS7Og1zvdy8
 [2]: http://www.rescuetime.com
 [3]: http://battleofbrothers.com/sirchris/why-i-chose-the-corona-sdk-over-sprite-kit-unity-or-cocos2d-x
 [4]: http://www.amazon.com/Programming-Third-Edition-Roberto-Ierusalimschy/dp/859037985X
 [5]: http://www.omidahourai.com/2013-06-27/improve-runtime-event-listeners-by-using-closures-lua-corona-sdk
 [6]: http://www.develephant.net/a-simple-storyboard-framework-for-corona-sdk-part-1/
 [7]: http://www.omidahourai.com/from-zero-to-oo-ardentkids-guide-to-object-oriented-lua-with-corona-sdk
 [8]: http://battleofbrothers.com/sirchris/animating-sprites-from-a-texture-packer-image
 [9]: https://github.com/Yonaba/Jumper
 [10]: http://coronalabs.com/blog/2014/01/21/introducing-the-composer-api-plus-tutorial/