---
title: First Look at SKLightNode in iOS8
author: Ryan
type: post
date: 2014-06-03T17:24:14+00:00
url: /sirryan/first-look-at-sklightnode-in-ios8/
categories:
  - sirryan
tags:
  - code
  - learning

---
Lighting effects were curiously missing from SpriteKit in iOS7, so I&#8217;m happy to see them appear in iOS8. Here&#8217;s a quick look at what you can expect from the light source / raycasting implementation.
<!--more-->

[SKLightNode][1] is the API object of interest today, and we can initialize one with some defaults.



The settings are fairly self explanatory. The important one to note is `categoryBitMask`, which you would likely make more involved. For example, if you had multiple light sources, they could each have different categories. Additionally, each light source will only affect nodes that accept that category of light. To configure a node to light up, configure one of the three bitmasks:



Have a look at some screenshots showing the different types of lighting. Focus on the flags throughout the scene. First, `shadowCastBitMask`.

<img class="alignnone size-large wp-image-607" src="http://battleofbrothers.com/wp-content/uploads/2014/06/shadowcast-1024x813.png" alt="shadowcast" width="625" height="496" />

Next up, `lightingBitMask`.

<img class="alignnone size-large wp-image-608" src="http://battleofbrothers.com/wp-content/uploads/2014/06/lightcast-1024x813.png" alt="lightcast" width="625" height="496" />

Lastly, note that you can toggle a few additional parameters like `falloff` &#8212; the decay of the light over distance. However, as of the time of this post, I&#8217;m having trouble getting `falloff` or `shadowedBitMask` to show any change in the lighting. (working with first beta preview).

 [1]: https://developer.apple.com/library/prerelease/ios/documentation/SpriteKit/Reference/SKLightNode_Ref/index.html#//apple_ref/occ/instp/SKLightNode/