---
title: Animating a Path Using Image Masking
author: chris
type: post
date: 2015-04-06T18:40:23+00:00
url: /sirchris/animating-a-path-using-image-masking/
categories:
  - sirchris
tags:
  - corona
  - learning

---
I recently found myself wanting to animate a character&#8217;s progress path and initially I thought I would do this by creating multiple animation frames, much like a sprite. After a bit of frustration, trial and error, I realized that creating an image mask was a more efficient and effective method.

To give you an example of what I was trying to accomplish, here is a picture of a portion of my game&#8217;s world map. The yellow and line is the path that my character takes.
<!--more-->

<div class="inlineimg">
  <img src="/wp-content/uploads/2015/04/Screen-Shot-2015-04-06-at-2.05.01-PM.png" alt="Screen Shot 2015-04-06 at 2.05.01 PM" width="625" height="371" class="alignnone size-large wp-image-2022" />
</div>

I wanted to animate the yellow path that shows the character progressing from point A to point B, kind of like this:

<div class="inlineimg">
  {{< gfycat data_id="EmptyScaryAbalone" >}}
</div>

At first, I thought I could accomplish my goal by cutting the path up into 50 or so tiny .png files and then placing them onto the screen. While this is technically possible, it became extremely time-consuming. Because each individual .png file was a different size and had to be placed on a pixel perfect location, animating it became an extremely tedious process. Changing the world map or the path itself would have been an excruciating process.

Next, I thought I would make something like an animation sequence, where the 50.png files were exactly the same size. This would remove the problem with pixel perfect location for each individual image, and I started to go in this direction. The problem with this technique is that the game&#8217;s artwork tends to evolve and if I were to change the color or texture of the path, I would have to re-cut everything from scratch.

Lucky for me, [Ryan][1] told me to take a look at masking, which proved to be much easier. If you&#8217;re not familiar with how masking works in Corona, check out their [basic tutorial][2]. What I did is instead of cutting up the path .png image into a bunch of files, I made a bunch of mask images that could be overlaid on top of the path.

To illustrate this, take a look at the image below:

<div class="inlineimg">
  <img src="/wp-content/uploads/2015/04/masking-path.png" alt="masking path" width="554" height="1024" class="alignnone size-large wp-image-2027" />
</div>

The base image is what the path looks like when it&#8217;s fully drawn. If you use the first mask image, labeled &#8220;Nothing Shows&#8221;, as a mask over the base image, then none of the base image shows. If you lay the second image, labeled &#8220;Path 1&#8221;, as a mask image, then a tiny part of the base image shows. What is in white on the mask images is what will show when laid on top of the base image.

I created about 40 of the mask images, each with a little more of the path shown in white, and labeled the files mask1, mask2, mask3, etc. Then I was able write a loop that sequentially applies each mask image over the base image.

https://gist.github.com/codepaladin/c2d7921dd50d23898683

What&#8217;s great about masking is that the mask image is always drawn exactly over the base image. I only need to worry about pixel precision when placing the base image and the mask images will automatically be displayed in the right location. And it&#8217;s no problem if I change or alter of the yellow path, because the mask stays exactly the same. As a bonus, I can do other cool things with masking like add gradients, brush strokes and other effects by simply changing the shades of grey in the mask. [Here&#8217;s an example][3] of what I&#8217;m talking about.

 [1]: http://battleofbrothers.com/sirryan
 [2]: http://docs.coronalabs.com/guide/media/imageMask/index.html
 [3]: http://www.gamasutra.com/blogs/OwenCanavan/20150106/233616/Creating_the_Scribble_Effect_in_Guild_of_Dungeoneering.php?utm_campaign=iOS_GameDev_Weekly_17&utm_medium=email&utm_source=iOS%2BGameDev%2BWeekly