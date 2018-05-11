---
title: Piecing It Together
author: Ryan
type: post
date: 2015-04-17T13:19:29+00:00
url: /2015/04/17/piecing-it-together/
featured_image: /wp-content/uploads/2015/04/farm-e1429197046269-2.png
number:
  - 20
keyevent:
  - Detailed polish to cutscene.
  - A rough "game"
categories:
  - sirryan
tags:
  - status

---
For the past year I&#8217;ve been working on a bunch of different code bases learning new concepts. For this update, I decided to piece together a first build of my &#8220;game&#8221; to get rid of redundant bits of code. I&#8217;m left with an app that has menus, navigation, saving, loading, and cutscenes. While it&#8217;s still far from an enjoyable game, it&#8217;s cool stuff to have a foundation to work with.

<!--more-->

To see everything in motion, check out the video below.

<div class="inlineimg">
  [youtube=https://www.youtube.com/watch?v=JsXEl37M_HY&w=740&theme=light]
</div>

#### Bringing Cutscenes To The Next Level

The original plan for this update was to do another round of polish on the story. Fortunately, I had a friend in town &#8212; Brian from <a href="http://secretpowers.com" target="_blank">Secret Powers</a>. He specializes in trailer / movie making / special effects, so was able to provide just the critique I needed. He actually came up with the gif below to show how much better the story could be.

<div class="inlineimg">
  [gfycat data_id=&#8221;OddballTastyEgg&#8221; data_autoplay=true data_controls=false]
</div>

Now that I&#8217;ve seen the true potential, I have a better idea of what direction to go. Also, I&#8217;m considering working with Brian on trailers and cutscenes for the game because the improvement is so noticeable.

#### Foundation of a Game

Because I&#8217;m on hold until I find out to what extent I&#8217;ll be working with Brian, I decided to move back to code. I took each of my separate projects (story, battle, tests) and started merging them into one code base. That provided the appearance of a game as you can see below:

<div class="inlineimg">
  [gfycat data_id=&#8221;ColossalFemaleCobra&#8221; data_autoplay=true data_controls=false]
</div>

The cool part about this is that the following now work reliably:

  * Saving
  * Loading
  * Scene management and caching
  * Conditional scene ordering
  * Data accessors (i.e: what troops are currently in my army)
  * Basic UI framework (propagating buttons, action callbacks, etc)

I haven&#8217;t finished bringing the battle into this project yet, so that is where I&#8217;ll pick up. Once that is complete, it will feel like I have a real project that I&#8217;m building off of.

#### Other Things in Motion

I&#8217;m moving on to my last week with Scott, our illustrator. With this completed, design and thought has been put into all maps, merchants, heroes, upgrades, camps, and units. I&#8217;m in a fairly good spot, and even though it is over budget the time restriction on this contract has been nice to enforce scope.

Aside from that, I&#8217;ll be starting music in a couple of weeks, and I have postponed voice because of the story uncertainty mentioned above. Nothing is planned for sound yet. My rough thinking is that when music is done, I&#8217;ll just focus and get a fun, functional game working. Then, I&#8217;ll revisit working with contractors to add that much needed polish.