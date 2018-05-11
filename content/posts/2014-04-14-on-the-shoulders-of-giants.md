---
title: On the Shoulders of Giants
author: Ryan
type: post
date: 2014-04-14T13:44:21+00:00
url: /2014/04/14/on-the-shoulders-of-giants/
featured_image: /wp-content/uploads/2014/04/Screen-Shot-2014-04-14-at-8.06.58-AM-1.png
number:
  - 2
  - 2
keyevent:
  - Finished video tutorials
  - Proof of concept completed
  - Double dispatch working for physics
  - Finished video tutorials
  - Proof of concept completed
  - Double dispatch working for physics
categories:
  - sirryan
tags:
  - status

---
Game development has always been intimidating to me. There have always been so many unknowns that learning how make a game, let alone write in C, seemed unachievable. The past two weeks have been shocking to me because the tools and libraries available have come so far that game development is now accessible. I feel like I did when developing for the web and <a href="http://jquery.com" target="_blank">jQuery</a>/<a href="http://prototypejs.org" target="_blank">Prototype.js</a> came out. It&#8217;s an amazing time and indie games will only become easier to produce.

<!--more-->

Now, don&#8217;t get me wrong. There is still a ton of work ahead. Fortunately, most of my work will be adding polish, levels and enemies to my world instead of struggling to draw something to the screen. There will also be a learning curve organizing a code base that needs to be so flexible and always changing. But enough about my concerns &#8212; let&#8217;s celebrate what I&#8217;ve accomplished in the first two weeks by watching the video below.

{{< youtube VdbZIZB8gjU >}}

In my demo, I&#8217;ve got music, text, video, particle effects, collision detection, a HUD, animation and combat. That&#8217;s crazy! I thought I would have a couple of circles. It&#8217;s been an extremely rewarding two weeks. Aside from a few Objective C growing pains, I&#8217;ve had a great time working with Sprite Kit. I&#8217;m also starting to gain confidence that I can actually finish a game.

#### What Surprised me the Most?

There is more logic than I could have ever expected, and the code needs to be flexible enough to accomodate everything. To give an example, let&#8217;s walk through a ranged unit determining what to shoot.

  * Drop a new circular physics object sized by the archers range.
  * Once an enemy collides with that object, shoot the enemy and remove the ranged physics object.
  * Once the enemy dies, drop the range physics object again and wait for another enemy to collide.

By that point, I thought I had the foundation of archers working. As I developed more, the code had to be adjusted in some way. What happens when a unit walks out of range? If multiple units are in range, how will you decide which unit to attack? Should arrows collide with only their intended target, or hit other obstacles in the way? What if a unit has a min range in addition to a max range like a catapult? Are two different projectile types need to handle splash damage and normal damage separately? What about special effects like poison on an arrow?

As you can see, each feature touches the code in some way, so organization will be critical.

#### Onwards

You&#8217;ll notice my demo is of the tower defense variety. Tower Defense games like <a href="http://www.defenderchronicles.com" target="_blank">Defender Chronicles</a> and <a href="http://www.kingdomrush.com" target="_blank">Kingdom Rush</a> have always been among my favorite mobile games, so it is natural that I&#8217;m pulled towards that direction. In terms of scope, I&#8217;m a bit concerned but I won&#8217;t turn back just yet. Most importantly, I&#8217;d like to add enough interesting, new concepts to move the genre forward a bit.

Over the next two weeks my focus will be movement and melee combat. I&#8217;d like movement to feel organic for skirmishers, and I&#8217;d also like to add a formation option to group units together. For combat, make the units smarter and visually make things look more interesting. For example, have units pick up their speed as they get closer to engaging someone. Check back in two weeks to see how it goes!