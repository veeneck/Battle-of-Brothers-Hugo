---
title: Feature Rush
author: Ryan
type: post
date: 2014-05-27T16:50:37+00:00
url: /2014/05/27/feature-rush/
featured_image: /wp-content/uploads/2014/05/Screen-Shot-2014-05-27-at-12.48.56-PM-1.png
keyevent:
  - Catapult implemented.
  - "Combat system for DoT's and resistances."
  - 'Limitations & upgrades on spawn flags.'
number:
  - 5
categories:
  - sirryan
tags:
  - status

---
Last update I had a [playable game][1]. This update has been spent trying to add as many features to the game as possible, which has been an enlightening process that has revealed two lessons. First, I [need to prototype][2] since you don&#8217;t know what&#8217;s fun until you try it. Second, while my code is getting better, it still isn&#8217;t ready to scale to an entire project. Each time I add a new asset or feature, I&#8217;m finding myself copying a lot of code. By going through the motions, it&#8217;s becoming clear what needs to be fixed up.
<!--more-->

Have a look at my accomplishments now that we&#8217;re 8 weeks in.

{{< youtube fIli2uh6hYY >}}

New features:

  * Catapult
  * Castle wall that blocks enemies from passing until they destroy it
  * Upgrades available to units
  * Flags limit what can be built on them
  * Damage over time
  * Resistances
  * Multiple spawns per wave
  * Adding sound back in

#### Prototyping

Earlier this week, I wrote about my [first encounter with prototyping][3]. I naievly thought that the ideas in my head would instantly transform into fun gameplay elements, but I&#8217;ve quickly learned that I&#8217;ll need to test out my ideas. This will directly influence what I work on next week. I think I understand the technical aspects of 2d game development enough to get over the gratifiction of seeing characters animate. Now it&#8217;s time to get dirty with balance and level design. Hopefully, I&#8217;ll be able to quickly work out a level that other people can play, so that I can focus on what makes a tower defense game fun.

#### Thoughts on Refactoring

I keep going back and forth over incremental refactoring versus a full overhaul. On one hand, it is nice to spend 2 hours with a piece of code just focusing on making that piece better. On the other hand, some code is tightly coupled with other code, and the changes spread too far. For now, I have a few pieces of code that are isolated enough that they can be fixed up over the next couple of updates. Eventually, I think it is inevitable that I will have to spend almost an entire two week cycle just making my code more efficient. I&#8217;m delaying that step as I&#8217;m still learning what the game requirements will be. It&#8217;s just worth noting that this is a constant battle that is faced with game development (at least with me).

#### Time for Polish

Polish will help with both code requirements and prototyping. For code, adding hooks for all details you think you may need shows just how flexible the code needs to be. For example, I coupled death with the `doDamageWithAmount` method and had the enemy fade out. When I implemented catapults, I wanted the enemy to fly. That required me to separate out death into a specific method that can be overriden. Of course, that&#8217;s just good code practice as well, but implementing the details ensures your code is on the right path.

On the prototyping side, I think sound, effects, and even simple animations like changing the amount of gold or health you currently have will add to the perceived fun. I&#8217;d like to combine the balance I mentioned before with tons of little details and bug fixes. I&#8217;ll actually be visiting relatives in two weeks, so it would be interesting to see them interact with a demo.

 [1]: http://battleofbrothers.com/sirryan/and-then-there-was-a-playable-game
 [2]: http://www.gamasutra.com/view/feature/179501/rapid_prototyping_tips_for_.php
 [3]: http://battleofbrothers.com/sirryan/trial-and-error-is-a-necessity-for-game-development