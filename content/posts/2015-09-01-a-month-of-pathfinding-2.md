---
title: A Month of Pathfinding
author: Ryan
type: post
date: 2015-09-01T13:58:46+00:00
url: /2015/09/01/a-month-of-pathfinding-2/
featured_image: /wp-content/uploads/2015/09/1.png-3.jpeg
number:
  - 24
keyevent:
  - New pathfinding
  - Added steering behaviors
  - Tools to create navmesh
categories:
  - sirryan
tags:
  - status

---
At the beginning of August I challenged myself to get pathfinding under control. In truth, if I couldn&#8217;t figure it out I would be forced to consider making the game turn based instead. So, I set out with a giant todo list containing many edge cases to solve. Fortunately, the main branch was merged in yesterday, so I&#8217;m in an infinitely better position than I was. It&#8217;s been an exhausting month, so I&#8217;m ready to move on. Let&#8217;s have a look at what&#8217;s been completed, and what issues still remain.

<!--more-->

<div class="inlineimg">
  [youtube=https://www.youtube.com/watch?v=GVu4rrOWFDM&w=740&theme=light]
</div>

#### A Sampling of Pathfinding Issues

How hard can walking be, right? Well, finding the best path is only one of the many issues. But there are many more like managing state, performance and user input. Here is a list of the main issues tackled:

  * Port navmesh to use iOS9&#8217;s new GKObstacleGraph
  * Port code to use iOS9&#8217;s entity component system with steering agents
  * Write tool to import data from <a href="https://www.codeandweb.com/physicseditor" target="_blank">PhysicsEditor</a>
  * Manage multiple GKObstacleGraphs so that wider formations take a larger turn radius
  * If destination is more than 2 radians of a turn, reform squad instead of wheeling
  * When Idle, check every so often to see if a unit has been bumped, and attempt to move back into position
  * If destination is invalid (off of a cliff), stop as close to destination as possible
  * If leader is still moving but destination is invalid, leave formation and just attempt to stay nearby other followers
  * If stuck on a physics object, leave formation and use pathfinding to figure a way back to the squad.
  * Multiple performance issues with units overlapping, updating their direction, etc
  * Figure out a way to preview a move
  * Figure out a way to allow the user to rotate a squad
  * Decouple UI actions from squad commands
  * Define a completed move so that sound, state and other callbacks / listeners are always accurate

The list continues on with each item getting more specific. The point is that this has been a ton of work. During the first year of game development, I learned a lot about movement so I chalk that time up to education. Now that I know what to look for, I&#8217;m still amazed at how complex everything becomes. According to RescueTime, I&#8217;ve put in 116 programming hours this month, which resulted in ~2,500 lines of code.

For those of you interested, let&#8217;s break down a few of the issues.

#### Stuck on an Object

This is something that should rarely happen because the navmesh should have a proper turn radius set for each unit. That said, there will be edge cases. For example, catapult knocks one unit aside but doesn&#8217;t kill it. The unit will have to figure out how to catch up to his friends. I hard coded walking into a corner, and how it would be solved. Check out the gif.

<div class="inlineimg">
  [gfycat data_id=&#8221;IllinformedSpanishBuffalo&#8221; data_autoplay=true data_controls=false]
</div>

As you can see, their pathfinding eventually kicks in and they round the corner.

#### Invalid Positions

There are multiple types of invalid positions. First, we can have the user tapping on water or a cliff. That should be detected, and provide visual feedback. Second, we have a leader who has stopped in a valid position, but tells some of his followers that their desired position is off of a cliff. Third, we have a leader who is moving, and is temporarily telling is followers to walk off of a cliff. The gif below shows how the third case was solved.

<div class="inlineimg">
  [gfycat data_id=&#8221;PrestigiousUnfortunateFalcon&#8221; data_autoplay=true data_controls=false]
</div>

The blue dots represent the leaders orders. Whenever the dot is in an invalid position, each follower is instructed to stay close by, but favor moving towards the dot. If the follower hits a physics edge, ignore the dot, and just try to stay close by while avoiding obstacles. That&#8217;s easy enough to type out in english, but you can imagine the math and constant checks per frame to make sure they&#8217;re doing the right thing.

#### Previewing and Rotating a Move

I was trying to think of an elegant way to allow previewing rotating. I didn&#8217;t want a separate button for rotate, and I still wanted moving to be easy. So, the solution is: Tap to move, hold your finger down to preview, and move your finger while holding to rotate. Surprisingly, it feels quite natural, so I&#8217;m happy with the outcome.

<div class="inlineimg">
  [gfycat data_id=&#8221;TiredRepulsiveGaur&#8221; data_autoplay=true data_controls=false]
</div>

The code isn&#8217;t quite perfect yet as you can see. Units don&#8217;t face the proper direction at the end, for example. But the idea and code is there. Speaking of the code, this took quite a refactor. Tap and hold should only be registered  when a move command is active. So basically, each icon is now a full component that updates each frame. Each icon is responsible for registering its own events, updating UI with icons like the move marker, disabling itself, etc. This was a necessary refactor that feels good to have finished as well.

#### Problems with the Actual Mesh

Getting the GKObstacleGraph to work took up quite a bit of time. First, I need a tool to help make the outline of the map. Adding each coordinate by hand wouldn&#8217;t cut it. So, I wrote an importer from PhysicsEditor. That was super cool until I noticed random imperfections. To investigate, I wrote a tool that tries to move to every 20 pixels on the map, and placed a red X if it was in the buffer region and inaccessible.

<div class="inlineimg">
  <img class="alignnone size-large wp-image-2296" src="http://localhost:8888/wp-content/uploads/2015/08/IMG_0223-2-1024x768.jpg" alt="IMG_0223" width="625" height="469" />
</div>

As you can see, there are pockets that look like they are in a valid position but can&#8217;t be walked to. It turns out that the triangles exported by Physics Editor (remember, no concave objects allowed) are sometimes sharp angles. When you stroke the path of a sharp angle, the resulting path points out quite a bit further. So, as a temporary fix, I had to manually adjust the individual triangles to try to have 30 degrees or larger angles.

#### Bumped out of Position

Contact with a physics object could cause some followers of an idle squad to be bumped out of position. When that happens, they should attempt to move back into position. See the problem in the yellow squad:

<div class="inlineimg">
  <img class="alignnone size-large wp-image-2299" src="http://localhost:8888/wp-content/uploads/2015/08/IMG_0224-3-1024x768.jpg" alt="IMG_0224" width="625" height="469" />
</div>

There are two ways to solve this. First, on physics contact, change state to find a way back to the desired position. Second, check if you are out of position during certain intervals. The first is more accurate, but requires more CPU. The second has a noticeable delay, but works and is not intensive. Currently, I&#8217;ve implemented the second, but I do plan to experiment with quad trees at some point. If I can get the performance where it needs to be, I can switch to more accurate options.

#### Where Does This Leave Us?

We&#8217;re now in a cautiously optimistic spot. Most importantly, everything is flexible now. I can easily scale up and down the accuracy. What you see now is balanced for performance, so I may even do different things for different platforms. Additionally, my state machine now makes sense and does not have a ton of redundant code. So, the logic for certain conditions is clean and easy to modify. All of this is good, and it will make the next steps easier.

What are the next steps? Combat and avoidance. Building on this foundation, make combat look more natural. While the combat code is ready to go, the pathfinding for it is horrible. I need to work on charging, surrounding units, and fleeing with everything appearing believable. As for avoidance, I&#8217;m putting it on the future list for now. Ideally, units would try to avoid each other instead of walking through one another.