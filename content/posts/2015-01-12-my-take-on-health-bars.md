---
title: My Take on Health Bars
author: Ryan
type: post
date: 2015-01-12T16:35:41+00:00
url: /2015/01/12/my-take-on-health-bars/
categories:
  - sirryan
tags:
  - art
  - thoughts

---
Health indicators are found in almost every game. As Chris pointed out, they come in a <a href="http://battleofbrothers.com/sirchris/health-display-roundup" target="_blank">variety of shapes and sizes</a>. When it became time to think about them in my game, I wanted to add something that was functional, but also unique or interesting in some way.
<!--more-->

Here are the conditions that my health bars had to meet:

  * Too cluttered to exist on an individual unit, so they had to represent the entire group.
  * At a glance, clear what total health would be, and when health has been removed.
  * Ability to be different colors.
  * Not too demanding technically.
  * Compliment, and not distract, from the units icon.
  * Also, must work with icons of different shapes.
  * And, must work for units of different sizes.
  * Work together visually with a units selected state.

Here&#8217;s what I came up with:

<div class="inlineimg">
  <img class="alignnone size-full wp-image-1527" src="http://localhost:8888/wp-content/uploads/2015/01/final-2.png" alt="final" width="444" height="150" srcset="http://localhost:8888/wp-content/uploads/2015/01/final-2.png 444w, http://localhost:8888/wp-content/uploads/2015/01/final-2-300x101.png 300w" sizes="(max-width: 444px) 100vw, 444px" />
</div>

Surprisingly, this was a 2 day process, which shows how hard it can be to estimate for the &#8220;little things.&#8221; Let&#8217;s talk about a few of the considerations.

#### Health Removed

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1532" src="http://localhost:8888/wp-content/uploads/2015/01/health-removed-2.png" alt="health removed" width="573" height="167" srcset="http://localhost:8888/wp-content/uploads/2015/01/health-removed-2.png 573w, http://localhost:8888/wp-content/uploads/2015/01/health-removed-2-300x87.png 300w" sizes="(max-width: 573px) 100vw, 573px" />
</div>

How does the image above look when health is removed? There is definitely enough contrast for missing health, and it is easy to check if something is ~50% health, or some other large mark. However, one criticism I have is that it is tough to tell, at a glance, the starting health of a squad. That&#8217;s an acceptable compromise for me, as the player will also see the actual units on screen, and be able to visually tell, for example, if there are 4 or 9.

#### Selecting a Unit

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1537" src="http://localhost:8888/wp-content/uploads/2015/01/selected-2.png" alt="selected" width="625" height="298" />
</div>

Next, how would this implementation handle units that have been selected by the player? At first, I tried toggling the actual color of the health bars. In the image above, notice the shields with black bars indicating that they are missing. That idea just added too much confusion, so I went with a white background, and missing bars, for a selected state.

The second thing I tried is a blur. The main problem with the blur is that it lowers the contrast of the health bars. So, while it achieves the effect of making something look selected, it comes at a cost. I will keep iterating to find a balance that satisfies both requirements.

The main knock at this step is that a separate sprite is required for the selected state, and I was hoping to achieve it with color changing only.

#### Enemy Units

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1533" src="http://localhost:8888/wp-content/uploads/2015/01/enemy-2.png" alt="enemy" width="625" height="174" srcset="http://localhost:8888/wp-content/uploads/2015/01/enemy-2.png 660w, http://localhost:8888/wp-content/uploads/2015/01/enemy-2-300x84.png 300w" sizes="(max-width: 625px) 100vw, 625px" />
</div>

Once I was happy with friendly units, I made sure this would work for enemy units. The pleasant surprise here is that it works, and it actually aids the user in quickly recognizing good versus bad. Also add bonus points for it being fairly easy to implement.

        if self.squad.friendly {
            self.pictureToMask.color = UIColor(red:0.533, green:0.769, blue:0.639, alpha:1) /*#88c4a3*/
        }
        else {
            self.pictureToMask.color = UIColor(red:0.929, green:0.455, blue:0.318, alpha:1) /*#ed7451*/
        }

I can expand this further into NPC&#8217;s, damage over time indicators, and so on. Just set up a pList file of color options, and we&#8217;re good to go.

#### Notifications

<div class="inlineimg">
  <img class="alignnone size-full wp-image-1531" src="http://localhost:8888/wp-content/uploads/2015/01/notifications-1.png" alt="notifications" width="670" height="217" srcset="http://localhost:8888/wp-content/uploads/2015/01/notifications-1.png 670w, http://localhost:8888/wp-content/uploads/2015/01/notifications-1-300x97.png 300w" sizes="(max-width: 670px) 100vw, 670px" />
</div>

This part was tricky because I don&#8217;t know what notifications, if any, my game will have. In fact, this is a challenge with game development overall &#8212; trying to plan for everything because it is impossible to know what will and won&#8217;t work. Anyway, I ran a quick test to see how cluttered this would look with other information in the area. I&#8217;m not fully satisfied, but confident I can find a working solution. Moving on!

#### Implementation

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1534" src="http://localhost:8888/wp-content/uploads/2015/01/implementation-3.png" alt="implementation" width="625" height="234" />
</div>

Implementation is a bit tricky, and a bit resource intensive. Here&#8217;s what is happening:

  * Shield is an image, with an outer border 10px away. Transparency in between.
  * Dark background in shape of first image is added underneath.
  * Grid, or sunburst added in between the two above. Same dark background set as the mask for the grid.

So, 3 images to achieve this. The middle layer could be done dynamically, but <a href="http://sartak.org/2014/03/skshapenode-you-are-dead-to-me.html" target="_blank">SKShapeNode is horrible</a> in SpriteKit. I may have to spend some time trying this with CGPath&#8217;s, as that would save the majority of the resource usage.

One other note &#8212; regardless of if you use sunburst or squares, there will be discrepancies in each health bar size. You can see the sunburst example above on the right. Some gaps are larger than others. For a grid implementation that isn&#8217;t divisible by 4, the bars will be different lengths (see above for that as well).

While I still have a few things to tighten up, I love the end result.

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1535" src="http://localhost:8888/wp-content/uploads/2015/01/B7Ac8MDIUAEXT1m-3.png-large-3.png" alt="B7Ac8MDIUAEXT1m.png-large" width="625" height="482" />
</div>