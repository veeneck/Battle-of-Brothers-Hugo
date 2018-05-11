---
title: How To Implement Squads and Formations, Part 1
author: Ryan
type: post
date: 2014-09-08T18:38:01+00:00
url: /2014/09/08/how-to-implement-squads-and-formations-part-1/
categories:
  - sirryan
tags:
  - code
  - learning

---
There is an awesome article on Gamasutra about <a href="http://www.gamasutra.com/view/feature/131720/coordinated_unit_movement.php?page=1" target="_blank">Coordinated Unit Movement</a>. They also have a companion post about <a href="http://www.gamasutra.com/view/feature/131721/implementing_coordinated_movement.php?page=1" target="_blank">implementing said movement</a>. However, the posts are from 1999, and they deal mainly in pseudocode. Also, I&#8217;m convinced there is absolutely nothing else on the entire internet explaining the topic. So, an experienced developer may be able to read the ideas and know how to implement them, but it has been a bit of a struggle for me as a new developer. I&#8217;m going to try to document a step by step implementation of formations, squads, and movement for someone who hasn&#8217;t done it before. I&#8217;ll be writing in Swift / Sprite Kit, but the code should be easy enough for anyone to follow. I also welcome corrections / improvements from experts.

<!--more-->

#### Arrange Units in Rows and Columns

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1201" src="http://localhost:8888/wp-content/uploads/2014/09/Screen-Shot-2014-09-06-at-2.42.07-PM-1024x789.png" alt="Screen Shot 2014-09-06 at 2.42.07 PM" width="625" height="481" />
</div>

Before reading anything, I started out by trying to make a Formation class that would be smart enough to handle any size or shape. Wrong approach. Instead, we&#8217;ll start with a `Squad` class that contains all of the units, and a `Formation` <a href="http://en.wikipedia.org/wiki/Strategy_pattern" target="_blank">strategy</a> that describes the layout of those units. It&#8217;s important to note that each arrangement (4&#215;3, 5&#215;2, wedge, etc) would be a new strategy, but for simplicity in this article I&#8217;m only going to use one class.



So, that&#8217;s the empty `Squad` container class. Here is the `Formation` class.

https://gist.github.com/d7386c8f4752b64ef349

Interestingly, a formation is just an array of vectors. Each vector is an offset from `0,0`, which is the center of our formation. I place the center row first in the array so that those spots are filled first. As of now, I&#8217;m matching the `units` array and the `positions` array.

The last step is to take the units and form them up into the appropriate positions. For that, we&#8217;ll add a `moveIntoFormation()` function to the `Squad` class.



And that&#8217;s it. With this code, we&#8217;ve recreated the screenshot at the top of this section.

#### Rotating the Formation

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1212" src="http://localhost:8888/wp-content/uploads/2014/09/Screen-Shot-2014-09-06-at-3.21.27-PM-1-1024x789.png" alt="Screen Shot 2014-09-06 at 3.21.27 PM" width="625" height="481" />
</div>

Next up, rotation. I won&#8217;t cover wheeling just yet, but the first step to wheeling is finding out what the final position should look like. This seems like it should be difficult. How can you rotate the vector `0,64` by 13 degrees and convert it to new coordinates? Well, thanks to a little bit of linear algebra and a lotta bit of internet help, we can apply a simple equation on each vector to adjust it to the new coordinate space. Here is what our new `moveIntoFormation()` function looks like.

https://gist.github.com/e6d881884efdc7077c8b

In particular, look at our `newX` and `newY` variables. They&#8217;ve been modified by a hard coded radian. We could easily make that a parameter in the function, and control the units rotation. And, to give credit where it&#8217;s due, I pulled the code from this <a href="http://stackoverflow.com/questions/22818531/how-to-rotate-2d-vector" target="_blank">Stack Overflow post</a>.

#### Improving Unit&#8217;s Position Selection

Up until now, each unit has been taking the vector that corresponds to their position in the `units` array. That causes people to overlap when they move into formation, as shown in the gif below.

<div class="inlineimg">
  <img class="alignnone size-full wp-image-1218" src="http://localhost:8888/wp-content/uploads/2014/09/http___makeagif.com__media_9-08-2014_ag03kX-1.gif" alt="http___makeagif.com__media_9-08-2014_ag03kX" width="400" height="300" />
</div>

This overlap looks a bit chunky, so let&#8217;s add some logic to the `moveIntoFormation()` function.



Two import changes to point out:

  * We&#8217;re looping over a count now instead of the \`units\` array.
  * The unit that gets moved is now determined by \`findClosestUnitToPosition()\`

Let&#8217;s have a look at our new function to determine the closest unit.

https://gist.github.com/a87b942a30a74a6bbef4

With all of that applied, the gif below shows our new `moveIntoFormation()` code executing. Notice that the units walk in a smarter fashion now.

<div class="inlineimg">
  <img class="alignnone wp-image-1226 size-full" src="http://localhost:8888/wp-content/uploads/2014/09/http___makeagif.com__media_9-08-2014_xyPv_m-1.gif" alt="" width="400" height="300" />
</div>

&nbsp;

#### Further Polish

We&#8217;ve got a lot of the core formation working, so all that is left is polish. Here are a few ideas:

  * The \`findClosestUnitToPosition()\` function is just one of the many modifiers you could run. For example, if we wanted the healer to always be in the middle, we could make a function that moves him first, and then surrounds him. There are a ton of possibilities.
  * We could store a vector called \`direction\` on the \`Formation\` class. That way, units can face the correct direction once they reach their final position.
  * To take direction a step further, we could have an array of directional vectors. Each wall of the formation could face outwards instead of everyone facing the same direction.
  * When people assemble, place a random delay between each iteration of the loop. That way, it won&#8217;t look like \*snap\*, everyone moved. It&#8217;ll feel more natural.

I&#8217;ve implemented a couple of those in the gif below. One note I would leave with is to be careful of doing too much at this step. For example, in my gif, one guy travels a bit too far to get to his spot. I could optimize that, but it would take more loops. I&#8217;d prefer to get everything acceptably functional, and then see what room is left for even more polish.

<div class="inlineimg">
  <img class="alignnone size-full wp-image-1224" src="http://localhost:8888/wp-content/uploads/2014/09/http___makeagif.com__media_9-08-2014_7krXMl-1.gif" alt="http___makeagif.com__media_9-08-2014_7krXMl" width="400" height="300" />
</div>