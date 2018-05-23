---
title: A Month of Combat
author: Ryan
type: post
date: 2015-10-01T20:46:47+00:00
url: /sirryan/a-month-of-combat/
featured_image: /wp-content/uploads/2015/11/Screen-Shot-2015-11-13-at-4.45.05-PM-e1447451181588.png
status_number:
  - 25
keyevent:
  - Port combat to iOS9
  - Line of sight for melee.
  - 100 units fighting.
categories:
  - sirryan
tags:
  - status

---
This update is similar to <a href="http://battleofbrothers.com/sirryan/a-month-of-pathfinding" target="_blank">my last update</a> in that I spent a month trying to improve the framework of a more complicated portion of the codebase. Last time was pathfinding, this time is combat. In addition to improving combat, I wanted to focus on data integrity and porting combat pathfinding to iOS9 / GameplayKit.

_Note: This post has been backdated to keep the documentation accurate &#8212; the game was in this state as of Oct. 1st._

<!--more-->

<div class="inlineimg">
  {{< youtube Gtj9s2cUAn0 >}}
</div>

#### A Sampling of Combat Issues

Combat has a bunch of tricky issues that need to be tackled. Among them are:

  * Only attack enemies you can see.
  * Try to avoid units by walking around them instead of through them.
  * AI and UI have to use the same code.
  * Range overlays have to be dynamic.
  * UI should lock certain abilities when engaged.
  * Units engaged while walking should stop walking and defend.
  * Unit attacked by multiple enemies should remain engaged until last enemy defeated.
  * What happens after combat?
  * Data integrity for all units tracking who is attacking, who has died, and who is engaging.

As you can imagine, things get complicated quickly. I had to tackle each item one at a time to avoid being overwhelmed. I&#8217;ve taken quite a mental beating between this update and last.

#### Implementing Line of Sight

One of the more interesting tasks with line of sight for combat. Each unit should be able to see an enemy before walking towards them. This will prevent units from walking through their friends just to get to a target. Steering behaviors can help avoid friendlies, but in order to prevent units from walking in circles, you can&#8217;t rely on steering behaviors alone. With that in mind, the logic works like this:

  * Look through all enemy units and sort them by distance.
  * Take the top X units, and see if you have line of sight.
  * _Note_: Since LoS is intensive, X will depend on device / CPU.
  * Pick the closet target and engage.
  * Run the steps above every 1 second.
  * If a change in target occurs, clear any state data and engage new target.
  * While walking, use steering behaviors to partially avoid other units.

#### Attacked From Both Sides

Units will often be close to one another, so combat between multiple squads has to look decent. I started by tackling a unit surrounded on both sides.

<div class="inlineimg">
  {{< gfycat data_id="GleefulSameFinwhale" >}}
</div>

While not finished, the results are promising. To take it a step further, I had to run the simulation multiple times from multiple directions because it has to always work. The end goal is for squads to keep their shape to some extent, which will also have the side effect of keeping things balanced.

#### Cutscenes

A quick note on cutscenes &#8212; they are still being worked on, and are getting better each iteration.  As of this update, a proof of concept of the final scene 2 is finished. The same style will then be applied to each scene. After that, sound design will go in. Finally, voice will be done. I&#8217;ll make periodic updates just to track the status.

#### Where Does This Leave Us?

In a decent spot. Combat isn&#8217;t close to done, but it is no in a place that I can iterate on. In particular, the state machine has been cleaned up significantly and is easier to read. Also, I&#8217;m more confident that the data is accurate. To test it, I have characters logging when they are attacking air, or stuck doing nothing. Those log items are almost non-existent now.

For the next month I&#8217;ll be adding more combat features like catapults and improved AI. I&#8217;ll also be tackling a huge refactor to abilities with the goal of making them reusable, easy to construct, easy to modify, and usable by AI. That will be a huge departure from what powers the commands now. Finally, I&#8217;ll set up level two and also get a proof of concept working for experience and levels.