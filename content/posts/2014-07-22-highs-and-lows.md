---
title: Highs and Lows
author: Ryan
type: post
date: 2014-07-22T15:21:54+00:00
url: /sirchris/highs-and-lows/
featured_image: /wp-content/uploads/2014/07/Screen-Shot-2014-07-22-at-11.20.15-AM-1.png
number:
  - 8
keyevent:
  - 64 bit version working.
  - Attack range now attached to flag instead of units.
  - Swift rewrite is 90% complete.
categories:
  - sirryan
tags:
  - status

---
Last update marked the beginning of my conversion to Swift, and this update marks the end &#8212; almost. I continued to be plagued by conversion issues (64 bit this time) and time off (Bachelor party), but also enjoyed faster refactoring and cleaner code. I&#8217;ve now gotten the game back to playable with 10% of the code left to convert. Small details like synchronized walking animations, missing damage over time and other bugs remain, but I finally feel like I&#8217;m in the clear. This is a huge thing because for a second there I was a bit depressed and questioned my choice to convert to Swift.
<!--more-->

{{< youtube ZmwOnejZ6nM >}}

It&#8217;s worth documenting that this rewrite was painful. I did not want to come into work. I was easily distracted. I was bored. I feel like I can usually tough through refactors with ease, but starting from scratch took its toll. So, if you&#8217;re in a similar situation, make sure you&#8217;re ready to see it through.

Equally important to note, I feel like starting my project from scratch was worth it. Now that I&#8217;m finished, I&#8217;m enjoying two huge benefits:

  * Beginner mistakes have been erased. Refactored code is much cleaner, and more flexible now that I know the rough scope of my game.
  * I can write Swift code much quicker than I can write Objective-C code. Also, aside from the odd beta issue, I enjoy writing in Swift more.

In the end, lots of pain up front for future gains.

#### State of the Game

Now that I&#8217;m back to a point where I can work at a normal speed, I expect to take a few days implement the last details to get the game back to where it was. Then, finally, we can start to look forward to what&#8217;s next. Things I have to start considering:

  * Unit upgrades, cost, damage and health along with other balance issues.
  * Short, mid and long range strategies. For example, catapult vs trebuchet.
  * Switching between levels
  * Rough overview of what I&#8217;ll need from an artist.
  * Controllable heroes.

Looking through that list, it&#8217;s nice to realize that a lot of the tasks are game design related. Sure, there will be plenty of code, but it&#8217;s exciting to start thinking about designing a game &#8212; not just developing one.

#### What&#8217;s Next?

I&#8217;m not sure. I&#8217;m going to put some feelers out for artists since I&#8217;ll be in San Francisco for 3 days. I&#8217;d like to start gathering data and talking to people about art in general, so that I&#8217;m not caught by surprise when the time comes to work with an artist. I also hope to research a few other games and see how they handle hit points vs damage. I suspect that I can come up with a rough formula to design against, but I need to learn a bit more first.

Hopefully, I&#8217;ll have something fresh and exciting next update as I have left you all empty handed for the past 6 weeks.