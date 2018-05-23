---
title: A Bit of Story and a Sprinkle of AI
author: Ryan
type: post
date: 2015-03-05T20:31:58+00:00
url: /sirryan/a-bit-of-story-and-a-sprinkle-of-ai/
featured_image: /wp-content/uploads/2015/03/Screen-Shot-2015-03-05-at-1.18.57-PM-e1425579863658.png
keyevent:
  - New chat system.
  - Enemy waves and basic AI
  - Round 1 of story polish
number:
  - 18
categories:
  - sirryan
tags:
  - status

---
The past two weeks have been 75% story and 25% in game work. That trend will continue for the next few updates as I prepare to send the story of to voice and sound. The encouraging news on the story front is that the first round of polish has resulted in noticeable improvements. Most importantly, the new chat bubbles add animation and interest while also allowing me to add dialogue to travel and battle scenes. As far as battle goes, enemies now have a basic spawn service and will attack the closest target they can find.
<!--more-->

<div class="inlineimg">
  {{< youtube HfiGmCYnwcQ >}}
</div>

#### Battle Improvements

The biggest change to battle is that enemies now spawn and attack. This seems simple, but required some significant improvements.

  * Open up pathfinding code to enemies.
  * Encapsulate UI button functionality (i.e.: walk) so that enemy AI can call them.
  * A separate &#8220;brain&#8221; in the state machine for enemies.
  * A service to handle spawning enemies at certain points with certain delays.
  * Modify the navmesh to create off screen polygons that are valid to walk out of but not in to.

After that was in place, I wanted to give some love to the shields that control the units. They have a long way to go, but the first step is to make sure they always remain on screen. This came with it&#8217;s own set of problems. Here it is in a broken state:

<div class="inlineimg">
  {{< gfycat data_id="CloudyIllustriousCuttlefish" >}}
</div>

As you can see, the shield disappears in the corner. It took a few hours to eventually get this right, but it is all working now as shown in the video.

The next issue I wanted to look at was the size of the battle maps. The forest level I have been showing is the first map, so the size won&#8217;t be as much of an issue. But, for later maps, size will allow for anticipation and flexibility. So, I asked Scott to expand one of the maps. Here is the result:

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1971" src="/wp-content/uploads/2015/03/bigger_map.jpg" alt="bigger_map" width="625" height="420" />
</div>

This is the first time I&#8217;ve shown a new map, and I&#8217;m really happy with the result. You can already see the extra room will allow for more drama as the catapults fire. I plan to make every 3rd map grow by 50% as the game progresses.

Finally, Scott finished the camp screen, which will change as your army grows. It doesn&#8217;t have any functionality yet in the code base, so I can only give a peak of the initial state.

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1972" src="/wp-content/uploads/2015/03/Camp_phase_0_a.jpg" alt="Camp_phase_0_a" width="625" height="396" />
</div>

#### Decision Screen

The decision screen makes multiple appearances throughout the game, so I figured that it would be a good place to start working on UI. The timing for this was a bit odd, but I wanted to start thinking of general UI so that I could give accurate instructions to Scott on future game screens. I asked Twitter what they thought of these two screens.

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1973" src="/wp-content/uploads/2015/03/decision1.png" alt="decision1" width="625" height="838" />
</div>

Unfortunately, most people preferred the banner. I&#8217;m not a huge fan of textured or realistic UI&#8217;s, so I have to keep iterating. That said, I did love the circle with a head in it. That staple could work for in battle icons, dialogue icons, skill trees, etc. So, I decided to solidify that as a UI element. For example, here is a round move icon in the same format.

<div class="inlineimg">
  <img class="alignnone size-full wp-image-1974" src="/wp-content/uploads/2015/03/icon-progress.png" alt="icon progress" width="300" height="101" />
</div>

#### Story Improvements

Taking those icons a step further, I came up with a new chat system. It had to meet the follow criteria:

  * Work on any screen.
  * Clear text at expected locations.
  * Work for up to 3 speakers on any device.
  * Change amount of speakers midway through conversation.

You can see it in action here:

<div class="inlineimg">
  {{< gfycat data_id="ShimmeringHarshGnatcatcher" >}}
</div>

The neat part about these chat bubbles is that they can be used anywhere. Here is what they look like during travel.

<div class="inlineimg">
  {{< youtube iFpZbheBEO0 >}}
</div>

Now, I may make subtle changes to the animations, but the general framework will remain the same.

Lastly, Scott and I spent a day adding polish to the story. Every cheap animation we could do was added. Blinking eyes, moving clouds, one frame animations, and changing arm or head positions. You name it, we added it. The plan is to do a couple of rounds of polish like this to bring the story from a B to an A.