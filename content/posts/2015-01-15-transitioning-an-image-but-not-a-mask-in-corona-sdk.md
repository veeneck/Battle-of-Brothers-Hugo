---
title: Transitioning an Image but Not a Mask in Corona SDK
author: chris
type: post
date: 2015-01-15T14:09:10+00:00
url: /sirchris/transitioning-an-image-but-not-a-mask-in-corona-sdk/
categories:
  - sirchris
tags:
  - corona
  - learning

---
I was recently playing around with image masking, and I wanted to transition the mask so that the image behind it gradually appeared on screen. Unfortunately, Corona doesn&#8217;t allow you to transition masks, but after [doing a little research][1] I learned that you can use groups to transition the image behind the mask. Here&#8217;s an example to see what I&#8217;m talking about.
<!--more-->

https://www.youtube.com/watch?v=8DhcjrqaqO0&feature=youtu.be

In this example, I have a base image that looks like:

<div class="inlineimg">
  <img src="/wp-content/uploads/2015/01/base-image-3.png" alt="base-image" width="600" height="300" class="alignnone size-full wp-image-1629" />
</div>

and a mask that looks like:

<div class="inlineimg">
  <img src="/wp-content/uploads/2015/01/example-mask-3.png" alt="example-mask" width="600" height="300" class="alignnone size-full wp-image-1630" />
</div>

In order to move the base image and not the mask over the image, I created a [new display group][2], placed the image inside of the group, and then masked the group instead of the image. I was then able to move the image inside of the group without moving the mask in order to achieve my desired effect. Here&#8217;s the code that I used for anybody who&#8217;s interested.

https://gist.github.com/codepaladin/2ba72935cd2d26b4361b

 [1]: http://forums.coronalabs.com/topic/34774-moving-image-but-not-mask/
 [2]: http://docs.coronalabs.com/api/library/display/newGroup.html