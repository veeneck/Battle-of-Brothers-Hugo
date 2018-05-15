---
title: The Battlefield UI
author: chris
type: post
date: 2015-05-27T17:40:59+00:00
url: /2015/05/27/the-battlefield-ui/
number:
  - 25
keyevent:
  - Updated Battlefield UI
categories:
  - sirchris
tags:
  - status

---
Many of my UI elements have been pretty ugly so far, but those days are soon coming to an end. I’ve now received pretty much all of the game’s artwork and in the last few weeks I started implementing the UI portion of that work. There’s still plenty of polish to add, but here’s a look at the battlefield UI in its current state.
<!--more-->

<div class="inlineimg">
  [youtube=https://www.youtube.com/watch?v=YNWhzubZDwc&w=740&theme=light]
</div>

The biggest change in the last few weeks is that I’ve finished my contract with [Scott Pellico][1], the game’s illustrator. I’ve been working with Scott for the last 8 months, so it’s weird to no longer have another person on my team. You can see some of the work that Scott created for both my brother and I [on his portfolio site][2], and I highly recommend hiring him if you’re looking for a talented and hard-working illustrator.

Things came down to the wire with Scott, but I think I have about 95% of the completed artwork I’ll need for my game. While I’m going to miss working with Scott, I’m really excited to implement some of the work he’s created. My UI has gotten quite the overhaul over that last few weeks and I’m really enjoying the process of turning a prototype into a reality. There’s still a lot of work to do, but here’s breakdown of the new and improved UI elements I’ve recently implemented.

#### Chat Bubble

I plan on using chat bubbles for the in-game dialogue between characters so it was pretty important that those don’t look ugly. As always, Scott delivered.

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2015/05/chatbubble-300x187.png" alt="chatbubble" width="300" height="187" class="alignnone size-medium wp-image-2117" />
</div>

#### Health Bar</strong>

Each character starts with a health bar consisting of 5 bubbles. The good guys have green bubbles and that bad guys have purple bubbles. When a character is damaged the bubbles turn red and then shrink to represent the remaining health.

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2015/05/damage-264x300.png" alt="damage" width="264" height="300" class="alignnone size-medium wp-image-2114" />
</div>

#### Character Turn</strong>

All of the living characters appear on the left hand side of the screen in order of character turn. Good guys are in green and bad guys are in purple. The active character is at the bottom and appears larger than the characters awaiting their turn. I may show character attributes like health, strength, mana, etc, down the road, but I’m going to work on gameplay before deciding which character information needs to be shown.

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2015/05/character-turn-123x300.png" alt="character turn" width="123" height="300" class="alignnone size-medium wp-image-2116" />
</div>

#### Character Actions

By default a character will have attack, defend, and move icons, which can be triggered by clicking the appropriate icon.

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2015/05/defaultactions-300x220.png" alt="defaultactions" width="300" height="220" class="alignnone size-medium wp-image-2129" />
</div>

The move and defend actions are pretty self explanatory and while the attack icon is just a single attack option right now, it&#8217;ll get more complicated with multiple attack options in the future.

#### Movement Range

The tiles that are in a character’s movement range appear as green rhombus shapes.

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2015/05/movement-range-300x173.png" alt="movement range" width="300" height="173" class="alignnone size-medium wp-image-2113" />
</div>

I’m pretty proud of that artwork because it’s one of the only assets that I created myself. And by create I mean cut, paste, hack, and colorize other various pieces of artwork that Scott provided into something that looks acceptable.

#### Attack Range

The attack range is displayed by a series of purple rhombus shapes (also designed by yours truly). If an enemy falls in that range then the shape is twice as dark as a position with no enemy inside of it.

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2015/05/attack-range-300x250.png" alt="attack range" width="300" height="250" class="alignnone size-medium wp-image-2119" />
</div>

#### Confirmation Check Mark

I didn’t have any type of confirmation for events the character actions at first, but I felt that too many mis-clicks were happening. For example, if I accidentally clicked on the defend icon instead of the attack icon then the character would defend themselves and essentially lose a turn. A mis-click could be the difference between winning and losing a battle, so I added a check box icon that confirms a user’s action.

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2015/05/checkbox-300x185.png" alt="checkbox" width="300" height="185" class="alignnone size-medium wp-image-2115" />
</div>

#### Victory Screen

When you win a battle the victory screen and then a continue button appear. The continue button is another artistic hack on my part, and the font might have to change, but it’s serviceable for now.

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2015/05/victory-300x168.png" alt="victory" width="300" height="168" class="alignnone size-medium wp-image-2118" />
</div>

Pro Tip &#8211; When the victory screen pops up, you should read it in [Johnny Drama&#8217;s voice][3].

#### Next Time

There are a bunch of minor fixes for the UI, but I also plan to start adding music and sounds to this first battlefield. I’m still a few months off from my immediate goal of completing the first 4 boards and having a playable alpha, but the remaining work is all on my end now that all of the art assets are in.

 [1]: http://appylon.weebly.com
 [2]: http://appylon.weebly.com/battle-of-brothers.html
 [3]: https://www.youtube.com/watch?v=GIeWjLC_SB0