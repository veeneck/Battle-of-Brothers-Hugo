---
title: Refactor, Health Bars and Ranged Combat
author: Ryan
type: post
date: 2015-01-19T14:14:41+00:00
url: /sirryan/refactor-health-bars-and-ranged-combat/
featured_image: /wp-content/uploads/2015/01/final-2.png
keyevent:
  - Refactor FSM
  - Health bars
  - Ranged Combat
number:
  - 15
categories:
  - sirryan
tags:
  - status

---
I&#8217;m finally able to start writing game code, and it is fun. Now that learning and performance issues are almost behind me, I was able to implement  ranged combat and death, which is great to see in action. In addition to that, steady progress has been made on the world map, and early story boards are coming along. This update also marks the end of the first contract with Scott, my illustrator, but we&#8217;ll be entering a second contract shortly.
<!--more-->

{{< youtube _Ba9kK6cebw >}}

#### Performance

As I mentioned in my last update, I have to constantly worry about performance because that will determine how many units I have on screen. I just wanted to make a quick note here that there has been a lot of progress on that front. Between <a href="http://battleofbrothers.com/sirryan/joy-of-debugging-command-swiftc-failed-with-exit-code-1" target="_blank">Swift compiler optimizations</a> and <a href="http://battleofbrothers.com/sirryan/spritekit-cpu-gains-from-caching-enumeratechildnodeswithname" target="_blank">caching enumerateChildNodesWithName</a>, I&#8217;ve seen significant gains.

I haven&#8217;t tried max units again, but I will sometime in the near future. I still have a few ideas to improve things, so we&#8217;ll see how efficient I can get it.

#### Death and Health

I recently began ranged combat, but it was just a rough proof of concept instead of a proper implementation. Over the past two weeks, it has progressed nicely. Let&#8217;s start by seeing it in action.

<div class="inlineimg">
  {{< gfycat data_id="RightDownrightDuckbillcat" >}}
</div>

A couple of things to note:

  * Death animation of enemy.
  * <a href="http://battleofbrothers.com/sirryan/my-take-on-health-bars" target="_blank">All you ever wanted to know about health bars.</a>
  * Rotate to face enemy as he moves.
  * Move and attack commands properly cancel one another out.

There are a bunch of minor details too that can&#8217;t be seen. Specifically, how to notify a squad and unit that you are engaging, attacking, disengaging, or have died. There is a bunch of cleanup to do when changing targets, so I broke that logic out into an `EngageService` to make sure it stays together. I wouldn&#8217;t call this 100% ready to launch, but it is in a good enough spot to move on for now.

#### Refactor

Rewriting code is never sexy, but it is a necessity. I feel like rewrites will never stop happening, even as I start to believe I know what I&#8217;m doing. Anyway, the major change here is to move towards a hierarchical finite state machine. I strongly considered behavior trees, but given my performance issues I thought they would only hurt more. I&#8217;m not confident that I made the perfect choice, but ranged combat was much easier to implement with my new code. So for that reason, I&#8217;m happy about the current state.

#### Next Up

Melee combat. Such a simple goal, but a tough task. To get melee right, I have to do a few experiments with physics and performance. In particular, making sure the units space out correctly so that it looks like natural combat, and so that the player can see what&#8217;s going on. Let&#8217;s see how far I can get.