---
title: Trial and Error is a Necessity for Game Development
author: Ryan
type: post
date: 2014-05-20T14:51:08+00:00
url: /2014/05/20/trial-and-error-is-a-necessity-for-game-development/
categories:
  - sirryan
tags:
  - design

---
While working on the catapult for my game, I came across the first of many design problems I will face. Turns out it is much easier to critique another game&#8217;s design than it is to create your own with confidence. In my situation, I was deciding between a player controlled catapult and an automated catapult. I was so torn that I <a href="http://www.reddit.com/r/gamedesign/comments/25eakp/when_is_player_control_no_longer_fun/" target="_blank">posed the question to /r/gamedesign</a> and had to write the code for each. Let&#8217;s look at the results.

<!--more-->

#### Player Controlled Catapult

My personal take on player controlled elements is that they must not be tedious. Then on top of that, they must offer something above and beyond what the automated controls offer. One comment from the reddit thread summed this up perfectly:

> Another way to look at it is the visceral satisfaction angle. Clicking a catapult and having it do slight damage to a few enemies isn&#8217;t very satisfying, while clicking a catapult and having in demolish an enemy that was resisting all the automatic fire is very satisfying. Totally aside from it being a skill-based mechanic or not, making an extra, different action should yield an extra, different result.
> 
> ConPhlebas&#8221;

Now, here is the implementation:

{{< youtube qd6n5HyrvG0 >}}

While timing the shot with the movement of the enemy is neat, it gets old quickly. Additionally, I spent more time focusing on the catapult and had less situational awareness of incoming enemies and of how my other units were performing. Ultimately, I would only want to fire the catapult if I absolutely had to, which means it is not particularly fun. Even if I implemented a grand explosion, the mechanic may have been somewhat rewarding but still not fun at its core.

#### Automated Catapult

The idea behind an automated catapult is that it is just another &#8220;tower&#8221; that is built because of a strategic decision. You can see how it would handle below (on a slower reload cycle in the real game):

{{< youtube P-exQRpricc >}}

When the player doesn&#8217;t have to worry about the catapult, their focus switches from an individual mechanic to the overall strategy of the game.

#### The Winner Is

For me, the winner became clear as soon as I implemented a player controlled catapult and saw how much it distracted from the core gameplay. The joy I get out of tower defense games is in the setting up and adapting a perfect defense, and automated catapults fulfilled that desire. I would feel cheated if I lost because of a player controlled mechanic. Now, some games successfully offer limited use emergency actions &#8212; I just want my catapults to be core components of the defense rather than a crutch. Additionally, those emergency actions are usually click to activate with no skill needed.

The interesting part of this exercise is how there really is no correct answer. There are tower war games that have player controlled shooting and upgrades as a primary feature. It all depends on what type of game you want to make, and where the player should be focusing. In hindsight, this seems obvious, but that wasn&#8217;t the case when I was initially evaluating the choices. More importantly, it took a day to implement the player controlled catapult. How many more development hours will be used on experimental behaviors? Clearly prototyping is an [important element of game design][1] and a [skill in itself][2], so it must be factored into scope.

 [1]: http://www.gamasutra.com/view/feature/179501/rapid_prototyping_tips_for_.php
 [2]: http://devmag.org.za/2014/01/08/rapid-game-prototyping-tips-for-programmers/