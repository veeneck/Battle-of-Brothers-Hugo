---
title: It’s Not All Sunshine and Rainbows
author: Ryan
type: post
date: 2014-04-28T15:09:18+00:00
url: /sirryan/its-not-all-sunshine-and-rainbows/
featured_image: /wp-content/uploads/2014/04/FSM7-1.png
number:
  - 3
keyevent:
  - Varied enemy movement.
  - Progress timer implemented.
  - Groundwork for finite state machine.
categories:
  - sirryan
tags:
  - status

---
With update #3, I bring you my most challenging two weeks so far. As you can see from the featured image, working with Finite State Machines, and AI in general, plays a big part in my frustrations. When this cycle began, I was hoping to have wave movement, group formations and melee combat working. Since only one of those three goals was accomplished, let&#8217;s take a look at what went right and what went wrong.
<!--more-->

As always, the status update is available in video format. Check it out below:

{{< youtube QfCRQUN3gMk >}}

#### Enemy Waves and Movement

The good news is that I&#8217;m happy with the code that spawns enemies and tells them where to move. Specifically, a few cool things are happening now:

  * Subpaths are now supported. When a wave is assigned a path (i.e: enter from top of screen or right side of screen) they will now randomly choose between an array of subpaths within that main path.
  * A 16px variance in any direction for skirmishers at each waypoint. This ensures that enemies on the same subpath still won&#8217;t walk along the same exact line.
  * Arc to path for mid points. Instead of connecting each waypoint with a straight line, each one is connected with a curved line. This makes the movement less rigid, and is achieved by using `CGPathAddArcToPoint(pathing, NULL, end.x, end.y, next.x, next.y, 50);`
  * Enemies start walking on a random delay so that they aren&#8217;t all on the same animation cycle.

<div class="inlineimg">
  <img class="alignnone size-large wp-image-403" src="http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-28-at-8.56.58-AM-1-1024x793.png" alt="Screen Shot 2014-04-28 at 8.56.58 AM" width="625" height="484" srcset="http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-28-at-8.56.58-AM-1-1024x793.png 1024w, http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-28-at-8.56.58-AM-1-300x232.png 300w, http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-28-at-8.56.58-AM-1-768x595.png 768w, http://localhost:8888/wp-content/uploads/2014/04/Screen-Shot-2014-04-28-at-8.56.58-AM-1.png 1136w" sizes="(max-width: 625px) 100vw, 625px" />
</div>

The other gem I found was a tutorial by Tony Chamblee on <a href="http://tonychamblee.com/2013/11/18/tcprogresstimer-a-spritekit-progress-timer/" target="_blank">progress timers with Sprite Kit</a>. I love when someone shares a concept openly on Github with well documented or easy to follow code. Seeing how other people approach problems helps newbies learn. In this case, I was introduced to SKCropNode and tracking time.

#### Formations

Implementing formations (or group based movements) was the start of a downhill slope for me these past two weeks. As is becoming the norm, everything seems easy but I&#8217;m oversimplifying it. In the case of formations, what should happen if someone dies? Does the person behind them move up? What if everyone behind is dead? Can a formation be attacked on the side &#8212; if so, how does that affect reforming after a death. When marching, each unit must reach the front of the formation before turning towards the desired destination. Is the code flexible enough to handle that? These are just a few of the thoughts to consider.

In addition to the logical problems, implementing formations is pushing me to try to become a better programmer. For example, this code is acceptable, but is it the best approach? Have a look at this pseudocode:



In an ideal world, I would think that one object should have no knowledge of its containing object. So, a soldier should not know he is in a formation, which means he should not store a pointer to his formation. Then, if the soldier dies, he can&#8217;t just call a method directly on his container like `self.formation.removeSoldier(self)`. Instead, the soldier should trigger an event of his death and the formation listens to it, finds out if the soldier belongs to said formation, and acts accordingly.

That small example illustrates what I&#8217;m spending a lot of my time on lately. Should I add overhead and complexity or take shortcuts. What do other game developers do? What do forums say? This process is time-consuming, and often results in setting up sample projects to see the flow of the code.

#### Artificial Intelligence

Take my frustrations with formations and add 6x the amount of work and you&#8217;ll be left with Artificial Intelligence. The problems and solutions are easy to say verbally. If I&#8217;m being attacked, I should face my target and attack him. But if I&#8217;m already fighting someone else, stay engaged with that person until he dies. Most importantly, if my friend goes below 20% health, stop attacking and heal him. Then, resume combat. In terms of code, it is easy to write a bunch of if statements to handle that. Once the if&#8217;s get out of control, every developer will find themselves researching <a href="http://gameprogrammingpatterns.com/state.html" target="_blank">finite state machines</a>.

State machines in general are not a problem for me. They just led me down a path of questions that open all sorts of holes in my code. Let&#8217;s start with the concept of attacking. An enemy intersects with my range object, so I store it in an array of pointers named targetsInRange. Once I decide to attack, do I directly communicate with the target like `[target handleEnemyEngagement:self];`? Or do I trigger a custom event that the enemy listens to? Either way, combat depends on me broadcasting my intentions (see my <a href="http://stackoverflow.com/questions/23302509/finite-state-machine-communicating-state-between-objects" target="_blank">Stack Overflow question regarding this</a>).

I struggle with the example above is because one object requires another to call its method in order for it to function properly. In every other state, the object behaves correctly using its own data / intelligence. When patrolling, scan for enemies. When an enemy found, engage. When health is low, flee. The only thing an object can&#8217;t recognize is when it is being attacked, so it relies on a handshake mechanic. So I ask myself, is a handshake acceptable as an exception, and where do I draw the line on using it? Preferably, all code follows a predictable pattern that is easy to follow and debug.

#### Next Two Weeks

I would really love to have a handle on formations, movements and melee behaviors by the next update. More importantly, I want the code to be a foundation that any character type can build on. The past two weeks turned out to be more of an education than actual progress on the game, so I hope to convert that knowledge into something I can show off.