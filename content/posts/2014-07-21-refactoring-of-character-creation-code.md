---
title: Refactoring of Character Creation Code
author: chris
type: post
date: 2014-07-21T16:37:29+00:00
url: /sirchris/refactoring-of-character-creation-code/
featured_image: /wp-content/uploads/2014/07/refactoring-1.jpg
keyevent:
  - Added Settings to HUD
  - Added Action Item to HUD
  - Refactored Character Creation Code
number:
  - 8
categories:
  - sirchris
tags:
  - status

---
After the last update, I had plans to build out the HUD and add new attack actions to my characters. I added a new attack action to the archer and was feeling excited about all the new awesomeness about to go into my game. Unfortunately, my excitement was short-lived because I quickly realized that my code needed to be refactored before adding new action functionality to all my characters. Warning: This article gets technical.
<!--more-->

The code was originally written to extend a parent character class with sub-classes like dwarf, mage, archer, etc. Things were going great until I saw that when new attack actions and functionality were added to the sub-classes, a lot of the code amongst the sub-classes was too similar. For example, all of the sub classes had similar functions setting sprite animation, sound, and attack options. Those functions weren&#8217;t in the parent class because the animation, sound, and attack variables were all different and specific to the sub-class. Each sub-class had these values hard-coded into them, and if you were to consider that my final game may have dozens of sub-classes, it&#8217;s easy to realize that there would be way too much duplicate code.

I decided that instead of having individual .lua files for each sub-classe, I would have a base character class that creates a character object by loading in data from a JSON file. So instead of having a `dwarf.lua` file that has all of a dwarf&#8217;s attributes hard-coded into it, now a universal `character.lua` file reads in a dwarf&#8217;s data from a JSON file. That data looks something like

https://gist.github.com/codepaladin/5feeb738ac9764157360

That same base character reads in data from archers, mages, zombies, and any other characters I create in the future. This will theoretically allow me to eliminate every sub-class and only have a single base character class.

While that&#8217;s great for the sub-class code that is similar, it doesn&#8217;t solve all of my problems. The next issue is that some sub-class functions are similar to only some sub-classes and not others. For example, ranged characters have functions to set the speed, angle, and end point to the projectile they fired. Melee characters do not need those functions. And to confuse things a little more, NPC ranged characters and PC ranged characters also have some separate functions specific to their player character type. To solve this issue, I&#8217;ve created a `characterFactory.lua` file that is responsible for reading in the JSON, creating the character, and then adding any character-specific functionality to the character created. To give you a visual, here is how the character creation process works now.

<div class="inlineimg">
  <img src="/wp-content/uploads/2014/07/characterCreation-1.png" alt="characterCreation" width="485" height="690" class="alignnone size-full wp-image-859" srcset="/wp-content/uploads/2014/07/characterCreation-1.png 485w, /wp-content/uploads/2014/07/characterCreation-1-211x300.png 211w" sizes="(max-width: 485px) 100vw, 485px" />
</div>

So the bad news is that I lost a couple of weeks of development. The good news is that I&#8217;ve probably removed a third of my code and made the character creation process much more efficient. I&#8217;m almost back to where I was at a couple of weeks ago, so I should be able to get back to adding functionality to my game in the near future.