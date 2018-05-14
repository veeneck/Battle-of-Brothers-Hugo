---
title: 'Charge, Flee, Economy & Scene Management'
author: Ryan
type: post
date: 2016-02-08T20:53:48+00:00
url: /sirryan/charge-flee-economy-scene-management/
featured_image: /wp-content/uploads/2016/02/Screen-Shot-2016-01-29-at-11.53.54-AM.png
number:
  - 27
keyevent:
  - Final Scene Management
  - 'Charge & Flee'
  - Basic Economy
categories:
  - sirryan
tags:
  - status

---
January 2016. Getting close to that two year mark. This month marks the first full month of iteration on an existing &#8220;platform&#8221;. I&#8217;m rapidly iterating through smaller features instead of spending months implementing core code. Because of that, I&#8217;m also going to change these status updates slightly. I&#8217;ll have my videos go through all the incremental changes, while the posts look through the bigger picture of what&#8217;s left. This should allow for easier tracking of overall progress. Additionally, I can save thoughts, ideas, and other general topics for the blog posts.
<!--more-->

<div class="inlineimg">
  [youtube=https://www.youtube.com/watch?v=bEUbAE7cLH4&w=740&theme=light]
</div>

Changelogs:

[Jan 1st &#8211; 15th][1]
  
[Jan 16th &#8211; 31st][2]

#### Quick Note on Workflow

I&#8217;m fully embracing a release every other week. Even if there is only one change, it keeps me accountable and so far is helping with momentum. This may change slightly with travel and my daughters arrival, but generally I&#8217;ll stick to it. Likewise, I set out goals in Github at the beginning of the two weeks to keep me focused.

#### The Big Picture

Let&#8217;s start with the road to alpha. I&#8217;m targeting September because that is when I think iOS10 will be released, and I have a feeling I&#8217;ll be using some of the SpriteKit features in the release. I expect them implementing quad trees among other things. I&#8217;m also trying to factor in a 2 month slow period between March and April for new baby. So, below is a ~5 and a half month estimate of specific tasks. I imagine there will be much more than listed, but it provides a general outline of my roadmap. I&#8217;ll keep track of this and see how it goes.

**Squads (~1 month)**

  * Get Squads their own pathfinding agent, and have each unit follow that. Eliminate idea of squad leader.
  * Provide more data to followers. Who is in front of them, behind them, etc. Allows for smarter wheeling, taking over for dying units, etc.
  * Refactor Flee, Charge, Engage, and other states based off changes above.
  * Implement concept of friendly fire for archers.
  * Improve appearance of melee combat. Knock backs, other ideas, etc.

**Camp (~1 week)**

  * Camp should change as you advance through game. Artwork finished, but need to implement logic.
  * Ambiance for camp (people walking, flag moving, noise, etc)
  * Change unit column count
  * Min / max for recruiting units, healing units, columns

**Abilities (~1 month)**

  * Spreadsheet of proposed abilities, DPS and balance
  * Select and save ability for Leader in Training Scene.
  * Select and save ability for squad in Camp Scene.
  * Select and save ability for Heroes in Heroes Scene.
  * Allow abilities to dynamically stack on action bar. (i.e: Attack turns to Charge which then turns to Flee once engaged).
  * Implement proposed abilities in gameplay up to level 3.

**Cutscenes (~1 week)**

  * All movie scenes finished, and ready to send off to voice over and sound effects.
  * In battle cutscene script finished, and features of those scenes tied to abilities being revealed.

**Heroes (~1 month)**

  * Unlock a hero from Heroes Scene.
  * Assign hero to a squad. Implement and figure out UI.
  * Implement heroes throughout gameplay layer. Extensive work here.
  * Refactor abilities to target individual unit (hero) or squad.

**Pathfinding (~1 month)**

  * Figure out absolute final approach to pathfinding. Either something new in iOS10, or continue with heavily modified GKObstacleGraph to work out all edge cases.
  * Have squads avoid other squads instead of walking directly through them.
  * Allow units to temporarily walk through obstacles. For example, walking through castle gate when fleeing, or spawning on a wall during a cutscene.

**Scaling & Performance (~1 month)**

  * Quad trees for larger maps to keep CPU in a decent range.
  * Object pools and other tricks for improving rendering performance.
  * Bug fixing for all of the above.
  * Test levels and test cases in the code to easily validate some of the more complex features above.

 [1]: https://gist.github.com/veeneck/4d0795f8139bef223052
 [2]: https://gist.github.com/veeneck/1c18139181f5bb1942fb