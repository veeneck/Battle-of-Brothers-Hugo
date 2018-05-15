---
title: Back to Programming
author: chris
type: post
date: 2014-09-17T13:59:22+00:00
url: /sirchris/back-to-programming/
featured_image: /wp-content/uploads/2014/09/code.png
number:
  - 12
keyevent:
  - Beginning of Engagement
  - Testing Live Maps
  - Passive and Attack Abilities
categories:
  - sirchris
tags:
  - status

---
For the first time in what feels like forever, I was able to get back into actually programming. I had no idea that hiring artists, researching art direction, building design documents, and working with contractors would take so much time, but it does. I can understand why studios have art directors and game designers because those two jobs take up just as much time as programming. Anyways, I was able to spend a full week programming, and here is a video update on where the game is at:
<!--more-->

https://www.youtube.com/watch?v=kXzw2NOFzjk

#### Concept of Engagement

I mentioned in the last update that I wanted to add a game mechanic that I&#8217;m calling engagement. Engagement is a term that means two characters are engaged in hand to hand combat. If a character disengages, or walks away from a character they&#8217;re fighting, then there is some type of penalty. In the video, you can see that the zombie gets an extra attack when the dwarf disengages.

This concept will make you think twice before engaging or disengaging an enemy and it also opens up some the possibility for some cool character attributes. For example, maybe a Ninja character can disengage without penalty. Or maybe character with a spear can attack from a further distance to avoid engaging. Or maybe a magician can use an air spell to push an enemy away, allowing himself or an ally to successfully disengage. I&#8217;ll probably have to add some sort of UI element to signal who&#8217;s engaged with who, but hopefully the programming behind it is now solid.

#### Character Attacks

I plan on having the characters unlock new skills and abilities as they progress in the game, so I started laying the ground work to access those skills. In this update, I gave the dwarf character access to a double attack ability, which just attacks the enemy two times. I also made it so that enemies and the attack icons are highlighted red when an attack action can be performed. The final interface and HUD won&#8217;t look like the demo, but the programming behind it won&#8217;t need to change much.

#### Passive Abilities

Many of the characters will have passive abilities like block, dodge, counterattack, regain mana, etc. In this update you can see the dwarf block an attack, but I laid the foundation for future passive abilities to be added to other characters.

#### The Map

The most noticeable difference between the newest video compared to previous updates it the background map. This is the map to the first level of what will be the final game, and I wanted to start programming with as many final assets as possible. I don&#8217;t have any real character animations just yet, but I will start using the finalized backgrounds just to make sure they work out for the gameplay.

One issue that using this background brought up was that the walkable grid had to have an X and Y offset. The old grid I was using started at the center-top of the screen, but it now has to start at a point on the bridge that isn&#8217;t at the center-top of the screen. That means that not only the grid, but every art asset, like the characters, has to be positioned according to that offset. The grid will have to be positioned differently on every level, so I made sure the code has that flexibility.

#### What&#8217;s Next

I&#8217;d like to add a couple of new good guys to the fight and give them their passive and active abilities. I&#8217;m sticking to the good guys for now, because those are the characters currently being animated. They&#8217;re also probably easier because adding abilities to the bad guys might be tough when it comes to AI.