---
title: Spawns, Heraldry and UI
author: Ryan
type: post
date: 2015-05-26T18:07:51+00:00
url: /sirryan/spawns-heraldry-and-ui/
number:
  - 22
keyevent:
  - Added unit placement.
  - Refactored heraldry.
  - Progress on UI elements.
categories:
  - sirryan
tags:
  - status

---
This update is broken into three main events. First, I created spawn zones for the player to place their troops before battle. Second, I fixed off screen heraldry, and refactored the code to make it more flexible. Lastly, I played with consistent UI classes that will work for every screen. And in between all of that, I fixed bugs and worked with the composer (<a href="http://www.manfredoniamusic.com" target="_blank">Tony Manfredonia</a>).
<!--more-->

One interesting side note about developing games. It is nice to be able to switch gears. When I&#8217;m bored with combat work, I can play with UI. When I don&#8217;t feel like coding, I can try to implement and learn about music or sound effects. There is a huge variety of things to work on. Of course, that comes with a downside. There is a mountain of work to be done that is quite intimidating, and I really have to stop myself from focusing on that aspect.

{{< youtube NIWS48fUkXY >}}

#### Placing Units

The task here was to create a region that allows troop placement. If the user taps outside of that region, it won&#8217;t work. The code had to be flexible for every map, and also allow a limit to the amount of units that could be placed in a particular region. Here is a working draft.

<div class="inlineimg">
  {{< gfycat data_id="TightDamagedGull" >}}
</div>

Once all units are placed, the game begins. In the future, there may be a button to being battle if it is optional to use every unit. Another cool thing to note is the direction the archers are facing when placed. I have a few hidden nodes with rotation sitting inside of the placement zone. When a unit is placed, the code finds the closest node. Whatever the rotation of that node is, the unit is set to that heading. I will allow the player to rotate units, but this is a nice touch for convenience.

#### Heraldry

I refer to the shields that identify the squads as Heraldry. They are ket to the UI because they act as unique identifiers, show life, standing, spells and are the item you click to interact with a unit.  They also perform two other functions that I implemented:

  * When a unit is spawning under delay, the Heraldry will gradually appear.
  * When a unit is offscreen, the Heraldry shrinks but still indicates the location of the unit.

<div class="inlineimg">
  {{< gfycat data_id="SpiritedAgitatedBarbet" >}}
</div>

Technically, the offscreen placement has been a pain. Weeks ago, I was able to get the location of the intersection with the edge of the screen. Everything worked until there were a bunch of units. The Heraldry started to overlap, and I have to avoid this as much as possible. So, we now have a grid of dots that sit at the edge of the screen. Each Heraldry can only be on one unique dot. If that dot is occupied, the next dot is selected. Now, we no long have off screen overlapping. On screen overlapping still does occur, but that&#8217;s a challenge for another week.

#### UI

This weeks work on the interface was more about usability and less about appearance. I had to tackle a few problems.

  * Keep the settings icon in the same place on all screens.
  * Keep the navigation in the bottom right on all screens.
  * Figure out the &#8220;Slide&#8221; system. What does 1 pane look like? How about 2?
  * What does a confirm dialogue look like?
  * What about controls, like plus and minus to toggle volume?
  * If the UI is transparent, what happens when the heraldry goes partially behind it?

I don&#8217;t have the answers to all of these questions, but I am fairly confident in the functionality on the &#8220;Slide&#8221; system. You&#8217;ve already seen <a href="http://battleofbrothers.com/sirryan/a-wobbly-foundation" target="_blank">how it would look on the main menu and world map</a>. Here is an idea of how it would apply to the Camp screen.

<div class="inlineimg">
  <img class="alignnone size-large wp-image-2145" src="/wp-content/uploads/2015/05/Screen-Shot-2015-05-23-at-10.35.05-AM.png" alt="Screen Shot 2015-05-23 at 10.35.05 AM" width="625" height="479" />
</div>

Functionally, it works. In the future I&#8217;ll spend time on appearance. I&#8217;m also imagining the iPhone version will have a slight variation where the second pane takes up the entire width of the remaining screen.

Another UI task that was accomplished this week was settings and pausing. I thought pausing would take me forever, but I was lucky that everything &#8220;just worked.&#8221; All of my game nodes were already in a separate World layer, so pausing just that layer stops the game while the UI layer is still active. See it in action below.

<div class="inlineimg">
  {{< gfycat data_id="UnsteadyUnlinedFlicker" >}}
</div>

#### Music

Progress is being made on the soundtrack as well. Here is what we have completed.

  * Main menu
  * World map
  * Unit placement
  * Player decisions
  * Battles 1-3
  * Boss 1

One other interesting thing to bring up &#8212; when you&#8217;re about 75% complete with a level, the music cross fades into a rock / electric version of the same track. It&#8217;s an interesting effect that you can hear in the video status update. I&#8217;m interested in more ways to add value through the music.