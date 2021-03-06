---
title: More Difficult Than When I Thought Things Were Difficult
author: Ryan
type: post
date: 2014-11-03T21:45:01+00:00
url: /sirryan/more-difficult-than-when-i-thought-things-were-difficult/
featured_image: /wp-content/uploads/2014/11/B1X2Ni5CMAAZg0v.png
status_number:
  - 13
keyevent:
  - Navmesh proof of concept.
  - Line of sight proof of concept.
  - Started work on story art.
  - Entered contract with animator.
categories:
  - sirryan
tags:
  - status

---
Alright, so that title is sort of doom and gloom. Really though, my mood is pretty good. I&#8217;m a married man now! On the work front, the difficulty I&#8217;m encountering is programming difficulty, which I feel is in my control. That&#8217;s always better than art, story, music, sound or gameplay difficulty. Current pain points? Pathfinding, and moving units as a formation.
<!--more-->

That said, I have made progress on both fronts. I have a basic navmesh implemented, and formation walking and rotating. Not bad, right? Problem is that it doesn&#8217;t look or feel right. There are so many edge case left to fix. Have a watch of my status video to see what I&#8217;m talking about.

{{< youtube l4wT2B4chdc >}}

In short, people can walk, sometimes. Have a look at this navmesh:

<div class="inlineimg">
  <img class="alignnone size-full wp-image-1415" src="/wp-content/uploads/2014/11/B0zmh0LIEAAWw1v.png-large.png" alt="B0zmh0LIEAAWw1v.png-large" width="650" />
</div>

Everything appears to work except when:

  * You move into a space that has 3 polygons sharing the same point, and then try to come back out.
  * You click anywhere outside of the navmesh.
  * Clicking inside of a concave polygon, and then outside, will trigger line of sight to break. This may or may not be an issue with `SKPhysicsWorld.bodyAlongRayStart()`

And there are plenty more examples where things will break. However, what you see is still a huge accomplishment. I know have a full featured debug system underneath the code, which I can turn on and off with different flags. That&#8217;s the overlay you see in the image above. Also, my first attempt at implementing a navmesh results in 30% CPU usage (mainly due to internal SKShapeNode bugs). I was able to bring that down to just using 1% more CPU. I also have a working understanding of A* now, which is huge. So, I&#8217;m a better game developer now &#8212; it&#8217;s just a tough process. Sometimes, it feels like I imagine walking through mud would feel.

#### Illustrations

Art is moving along nicely. During the first few weeks, things went slow because we were trying to figure out how to make art for an unknown game. Now that things are more defined, art is flying. Have a look at this story scene:

<div class="inlineimg">
  <img class="alignnone size-full wp-image-1420" src="/wp-content/uploads/2014/11/B1Iql1NCIAEGtKo.png-large.png" alt="B1Iql1NCIAEGtKo.png-large" width="662" height="654"  />
</div>

There is plenty more where that came from too. Overall, here is where the illustrations are at:

  * 6/15 levels
  * 15/26 characters
  * 5/15 cutscenes
  * 0 / 1 world map
  * 0 / 1 start screen
  * 0 / 1 camp screen
  * 0 / 1 interface
  * 0 / 1 polish like rivers, birds, flags, etc
  * 0 / 1 marketing materials

<div>
  And at this point, I&#8217;m just over half way through my first illustrator contract.
</div>

#### Animations

I just entered into a new contract with an animator. She lives in Israel, and so far has been amazing to work with. I&#8217;m excited to see the results, and hope that this marks the end of <a href="http://battleofbrothers.com/sirryan/my-experiences-hiring-an-artist-part-2" target="_blank">my search for artists</a>. Here is a sample of her work:

<div class="inlineimg">
  <img class="alignnone size-full wp-image-1395" src="/wp-content/uploads/2014/11/Archer-1-Walk-Front.gif" alt="Archer-1-Walk-Front" width="128" height="128" s />
</div>

She&#8217;ll be working on ~26 characters, each with 4 to 6 8 frame animations.

#### Goals for November

Walking. Sounds simple, but I want it perfect. Every pathfinding bug, and units moving naturally throughout the map. The units won&#8217;t flock or avoid each other just yet. But, I&#8217;d like to see controlled movement. On the art front, the story will probably be finished, and the first animation contract will be nearly complete by the end of the month.