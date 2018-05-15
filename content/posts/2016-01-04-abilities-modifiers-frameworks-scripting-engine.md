---
title: 'Abilities, Modifiers, Frameworks & Scripting Engine'
author: Ryan
type: post
date: 2016-01-04T16:06:23+00:00
url: /sirryan/abilities-modifiers-frameworks-scripting-engine/
featured_image: /wp-content/uploads/2016/01/Screen-Shot-2016-01-04-at-11.04.37-AM-e1451923520630-2.png
number:
  - 26
keyevent:
  - 'Abilities & Modifiers'
  - Split code into frameworks
  - In battle cutscene engine
categories:
  - sirryan
tags:
  - status

---
It&#8217;s been quite the 2 months. In anticipation of becoming a father, I&#8217;ve significantly picked up my work efforts. It&#8217;s not that I wasn&#8217;t trying before &#8212; it&#8217;s just that deadlines have a way of motivating me further. I&#8217;ve tackled a few major rewrites / problems with the foundation of my code, and I now have a working &#8220;game&#8221; that is actually installed on 3 devices via Testflight! With all of this in place, I can iterate on the platform and slowly work towards a rough alpha and then polished beta.
<!--more-->

<div class="inlineimg">
  [youtube=https://www.youtube.com/watch?v=j5stQgL6IjE&w=740&theme=light]
</div>

#### Abilities & Modifiers

It&#8217;s easy to get caught in the trap of thinking of combat as damage vs hit points. As of last update, that is what I had working, and I focused most of my time on the visual aspects of combat. With this update, I&#8217;ve now thought it through and I&#8217;ve settled on Abilities, Modifiers, and Attributes to be the three things representing combat. Here are a two use cases that should illustrate how complex a combat system is, and how flexible the code must be:

  * Ability that can be used once per 5 minutes, lasts for 10 seconds, and increases walking speed by 10. Can only be used if walking.
  * Ability that can be used if a target is in range and the unit is not engaged in combat. Has a 30% chance to hit. On hit, trigger a secondary AoE ability that does 10 damage to target hit points and -5 to moral.

The possibilities are infinite, and they touch every portion of the code. For example, walking speed is handled by steering behaviors using goals. You can&#8217;t change the goal every frame for performance reasons, so any change to a units walking speed attribute will not have an immediate impact unless the proper portions of the code are listening for a change.

Things start to get more technical quickly, so the important part to note is that all abilities from walking to combat are now text files that the code reads in. Units are assigned abilities based on another test file, and their experience level. Lastly, all parts of the code know how to process abilities, so characters, walls, rocks, and the AI are much more dynamic.

#### Frameworks & Docs

Up until now I have been writing code in one large project so that I can quickly iterate and learn. Now that I halfway know what I&#8217;m doing, I feel comfortable making reusable frameworks that I can use in any game I wish to make. The main benefit of frameworks is that they force you to think of code as an API that anyone can use, and this often leads to testable, flexible, focused code. Additionally, it forces you to think about documenting your code.

<div class="inlineimg">
  <img class="alignnone size-full wp-image-2349" src="http://localhost:8888/wp-content/uploads/2015/12/RyanDocs-e1451413833718-3.png" alt="RyanDocs" width="800" height="514" srcset="http://localhost:8888/wp-content/uploads/2015/12/RyanDocs-e1451413833718-3.png 800w, http://localhost:8888/wp-content/uploads/2015/12/RyanDocs-e1451413833718-3-300x193.png 300w, http://localhost:8888/wp-content/uploads/2015/12/RyanDocs-e1451413833718-3-768x493.png 768w" sizes="(max-width: 800px) 100vw, 800px" />
</div>

So, I&#8217;ve begun this process. Here is what I have so far:

  * <a href="https://github.com/veeneck/WavePool" target="_blank">WavePool </a>&#8211; Manage waves of enemies units over time.
  * <a href="https://github.com/veeneck/Particleboard" target="_blank">Particleboard </a>&#8211; Useful tools for any Swift / SpriteKit project. Sound / music / math. An extension of <a href="https://github.com/raywenderlich/SKTUtils" target="_blank">SKTUtils</a>.
  * <a href="https://github.com/veeneck/CutsceneKit" target="_blank">CutsceneKit </a>&#8211; Ability to run SKActions as groups, and fast forward them. Also useful extensions to SKVideoNode.
  * <a href="https://github.com/veeneck/SpeakerBox" target="_blank">SpeakerBox </a>&#8211; Somewhat specific to my game, but isolates code to add talking chat heads for in game story.
  * <a href="https://github.com/veeneck/SwitchBoard" target="_blank">SwitchBoard </a>&#8211; Still in progress and I hope to have it finished for next update. Complete scene management for SpriteKit with ability to preload, load by tag, cache, etc.

#### Scripting Engine

<div class="inlineimg">
  {{< gfycat data_id="AccomplishedIndolentKusimanse" >}}
</div>

Cutscenes seem simple, but like everything they have their quirks and challenges. Here are a few to show you what I mean:

  * Needed the ability for NPC units
  * Needed the ability to pause waves
  * Conditional checking for when story should progress
  * Complications with camera movements versus screen edges.
  * Conditionally disabling parts of the UI
  * Which portions you&#8217;re able to skip and&nbsp;others to&nbsp;only show once.

So, through state machines, delegates and my new ability system, I&#8217;ve been able to address most of the issues above. I may find some edge cases still, but I have a decent in game dialogue and scripting system in place.

#### Adding New Units

<div class="inlineimg">
  <img class="alignnone size-full wp-image-2357" src="http://localhost:8888/wp-content/uploads/2016/01/xEe9StP5lOTkWmBuO6p2jMS-hDbFAiv3Kelf6EbJtdg-e1451923146393-3.png" alt="xEe9StP5lOTkWmBuO6p2jMS-hDbFAiv3Kelf6EbJtdg" width="600" height="679" />
</div>

I&#8217;ve added another unit to the game. For now, we&#8217;ll call them the Ice Guard. Two major positives came out of this.

First, adding units is getting easier. With my new abilities system, I just add a text file for the unit, and list what abilities they should have. Next, chop of the assets and save them with the correct file names. Last, make the heraldry with their shield icon. It takes about 15 minutes, and is getting easier and more flexible with each iteration.

Second, it caused me to give Heraldry a second look. I&#8217;m using a SKCropNode to render the shields. I knew performance was rough for cropping, but it turns out it&#8217;s really rough. By turning the SKCropNode into a texture, and only updating it when an event like a soldier dying occurs, I&#8217;ve saved about 20% CPU.

#### Progression of Story

Slowly but surely, the story is coming together. About 3 of 15 minutes has been through the video editing process. Here is a recent still image:

<div class="inlineimg">
  {{< gfycat data_id="DefensiveBothAppaloosa" >}}
</div>

Late in the alpha process we would like to have everything completed so that it can be sent to voice and sound. That will also give us an idea of any art is missing, and we can follow up with our illustrator.