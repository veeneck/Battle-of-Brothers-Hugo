---
title: The Shaping of a Game
author: Ryan
type: post
date: 2014-06-09T16:11:47+00:00
url: /sirryan/the-shaping-of-a-game/
status_number:
  - 6
keyevent:
  - Evolving map.
  - Arrow slits and castle gate.
  - First attempt at UI.
categories:
  - sirryan
tags:
  - status

---
If last week was a <a href="http://battleofbrothers.com/sirryan/feature-rush" target="_blank">feature rush</a>, this week was a feature overload. I&#8217;ve slowly been breaking out of the learning phase and into the implementation phase. I definitely know what needs to happen now &#8212; it&#8217;s just a matter of doing it. Exciting times are ahead because I can now begin testing features that will make my game unique. My update this week introduces a lot of those features, including a defendable castle and dynamic spawn points.
<!--more-->

Video may do this weeks update the most justice since the UI and map have gotten a complete overhaul (thanks again <a href="http://www.kenney.nl/assets" target="_blank">Kenney&#8217;s assets</a>). Have a look below:

{{< youtube awgofqGLrLY >}}

I really enjoyed worked on the project this week because I was able to think about design and function instead of just focusing on technical implementation. This can be seen in a few areas:

#### Evolving Map

By spending a large amount of time working on a real map, it became clear that I would have to thoroughly plan out the design and flow before sending specs to an artist. In particular, I envision a map that changes as you progress throughout the level. The map may start out in the foothills of a mountain, but as you buy different units the map will slowly change. Campfires, weapon racks, broken carts, caves, footprints in snow, fences and more will be introduced. The concept of gradually revealing a piece of art is one of the scalable ways I hope to make my game engaging.

By working through a dry run of an evolving map, I learned a few things:

  * The art needs to be layered at an object level.
  * My pList file needs to be much more flexible to dynamically load all of this data.
  * Spawn flags may not be where the unit stands because the scenery and action is blocked.
  * The castle needs to be of a certain size to host the catapults, arrow slits and other planned features. At the same time, it can&#8217;t dominate the map as it only accounts for 1/3 of the strategy I have in mind.

#### Spawn Points

How do you balance a level? I don&#8217;t know the answer to that yet, but I started to think about it this week. Should spawn points be evenly spaced from where the enemy units walk? Or, should each spawn point have a base range so that the map can look more organic and still be balanced? The downside to the latter approach is that it is not as intuitive to the end user. However, my game will only accept certain units per spawn, so that eliminates some of the confusing choices that the user would have been presented with.

I constantly think about issues like the above as I&#8217;m trying to sleep, when I&#8217;m running, and when I&#8217;m eating. It&#8217;s fun. I did implement the ability to show the user range this week, so I hope to have a decision on this problem in the coming weeks. The good part is that I&#8217;m allowed to start thinking of this, which I could not do previously due to the technical learning curve.

#### Heads Up Display

As you can see, the user interface has changed and this is my first serious attempt at thinking it through. Changes of note:

  * Larger surface area to tap. Previous versions had trouble accurately getting a tap. The menus work better now, but the flags are still having trouble.
  * Wave count, health and money all bounce when your attention is needed. I don&#8217;t think this will be the final iteration, but I do like the simplicity of the UI at this point.
  * There is now a start game button. You can add units and decide on your strategy before the enemy waves come out.
  * A progress bar arrow is placed on the map shortly before enemies come out. Allows the user time to adapt to an incoming wave. This was technically impressive for me as well because I had to implement a moving crop node based on vectors and radians. I&#8217;m becoming more comfortable with my math.

#### What&#8217;s Next

Swift. It&#8217;s both a blessing and a curse, but I&#8217;ll be spending a lot of time with Swift over the next two weeks. My code has been getting worse and worse, and the idea of a refactor seems dreadful. With Swift, I&#8217;ll at least get to learn a new language that is easier to work with while taking on the boring tasks of rewriting large portions of my code.