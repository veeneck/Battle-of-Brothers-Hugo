---
title: Core Improvement
author: chris
type: post
date: 2014-10-22T17:50:10+00:00
url: /2014/10/22/core-improvement-2/
featured_image: /wp-content/uploads/2014/10/Screen-Shot-2014-10-22-at-1.48.20-PM.png
number:
  - 14
keyevent:
  - Scene Management
  - Loading and Saving
  - View on iPad
categories:
  - sirchris
tags:
  - status

---
As planned after the last update, I was able to add scene management, loading and saving functionality, and the ability to view the game on a physical device. There are also some pretty cool new battleground maps and my first character sprite .png animation to check out below.

<!--more-->

https://www.youtube.com/watch?v=WU4BMbqniDU&feature=youtu.be

#### Character Sprites

The first character sprite .png files for the runemage character arrived and I&#8217;m very pleased with how they turned out. The first batch of images are just test files (not fully detailed) for walk, die, hit and idle animations. Here&#8217;s a demo of the die animation.

https://www.youtube.com/watch?v=POOK34cDbmo&feature=youtu.be

#### Scene Management

Corona uses their [composer functionality][1] for scene management, and that allows you to easily transition between scenes. In my video example you can see how I transition between the world map scene, which is always running and loaded into memory, and battleground scenes, which are loaded and destroyed dynamically.

I also started tracking memory usage and the so far I&#8217;m well under the most commonly used mobile devices memory limits. I did have to go through my code and ensure that memory is being freed up when scenes, sprites, audio, etc. are destroyed, but so far Corona has made that pretty easy to handle.

#### Viewing on an iPad

This is just a single item but it took me way too much time to get the demo running on an iPad. From getting a business dev license (needed a DUNS number), to having Corona make a proper build (needed to upgrade to a paid plan), to debugging basic issues (needed to fix code issues), it took awhile to get this thing running. But I can play the demo on my iPad now and that process should go much smoother from here on out.

#### Loading and Saving

Character attributes and game state can now be loaded and saved, which will be necessary for the real game.

#### Next Time Around

I&#8217;ll continue to add any animations as they come in, but I&#8217;m going to continue down the path of adding core functionality to the game. This work is a little boring and not flashy, but it needs to get done. The features I hope to get to are:

  * Saving Files to a Device (this is a little different from the dev environment)
  * Character Management Screen
  * Character Dialogue
  * Code to Show Cut Scenes

 [1]: http://docs.coronalabs.com/api/library/composer/index.html