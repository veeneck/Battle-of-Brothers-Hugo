---
title: Isometric Projectile Trajectory in Swift and SpriteKit
author: Ryan
type: post
date: 2016-07-12T18:08:19+00:00
url: /sirryan/isometric-projectile-trajectory-in-swift-and-spritekit/
categories:
  - sirryan
tags:
  - code
  - spritekit

---
How do you launch a catapult, grenade, arrow, or any other projectile in an isometric world? I had to joy of figuring that out over these past two days, and I thought I would share. Before jumping in, let me point out that the code below is for my specific use case, and is not a full featured framework. So, you&#8217;ll still have to understand the concepts, but if you&#8217;re Googling for help this will hopefully get you on the right track.
<!--more-->

<div class="inlineimg">
  [gfycat data_id=&#8221;FrayedEvenCardinal&#8221; data_autoplay=true data_controls=false]
</div>

To accomplish the above, here is what has to happen:

  * Load up your high school math brain.
  * Bookmark [HyperPhysics Trajectories][1]. This tool will be your math checker and teacher.
  * Figure out a meters to pixels conversion that works for your game. 50px / meter works for mine.
  * Supply a start point, end point, and launch angle. The example above is 60 degrees.
  * Note that my `degreesToRadians` and `distanceTo` functions below come from [SKTUtils][2].
  * Call the function below, and run the returned SKAction on your projectile.

https://gist.github.com/veeneck/8a12a23f673d410359ca96b8978a913f

 [1]: http://hyperphysics.phy-astr.gsu.edu/hbase/traj.html#tra6
 [2]: https://github.com/raywenderlich/SKTUtils