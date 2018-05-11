---
title: Health Bars and Taking Damage in Corona SDK
author: chris
type: post
date: 2014-06-24T17:30:09+00:00
url: /2014/06/24/health-bars-and-taking-damage-in-corona-sdk/
categories:
  - sirchris
tags:
  - code
  - corona
  - learning
  - lua

---
It&#8217;s common to see [health bars attached to a characters][1] in video games, and in this tutorial I explain how that can easily be accomplished in Corona SDK. And as an added bonus, the health bar also updates as the character takes damage.

<!--more-->

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/dwarf-healthbar.jpg" alt="dwarf-healthbar" width="547" height="249" class="alignnone size-full wp-image-632" />
</div>

https://gist.github.com/codepaladin/7d7afd56df17468abd24

The first thing we do is create a new display group called characterGroup. Think of display groups as containers that hold different objects, like images, shapes, and text. The reason we need a display group in this example is because we will have three objects, a character, a health bar, and a damage bar, all which need to move in unison as the character moves across the screen.

After we have the character group created and centered on the screen, a dwarf image is added to the group. You&#8217;ll also see maxHealth and currentHealth variables, which will be used for our health bars.

https://gist.github.com/codepaladin/72b438209eebe018511d

Here we draw the health bar to the screen as a green rectangle. The width is set to maxHealth, which conveniently makes the health bar 100 pixels wide. Then we draw a red rectangle called damageBar directly on top of the green health bar. The damage bar is 0 pixels wide to start, because our character is at full health. Note that it&#8217;s important to draw the damage bar second, because Corona z-indexes images to the screen in the order they&#8217;re drawn.

The health bar and the damage bar are added to the characterGroup so that they are in the same container as the dwarf image.

https://gist.github.com/codepaladin/3d554c91ee65fbd27fdb

The moveLeft and moveRight functions move the character, health bar, and damage bar 100 pixels to the left and then to the right. Notice that in the transition.to() function, the characterGroup is what&#8217;s being moved. We move the group and not the individual objects, because moving a group also moves the objects inside of a group.

If you look at the moveRight() function, you&#8217;ll see that damageCharacter() is called, which then subtracts the damage taken from the character&#8217;s maxHealth. The updateDamageBar() function is then called so that the red damage bar&#8217;s width is increased in order to show how much health remains.

The complete source code to this tutorial can be found on [GitHub][2]

 [1]: http://battleofbrothers.com/sirchris/health-display-roundup
 [2]: https://github.com/codepaladin/Health-Bar-Tutorial