---
title: Animating Sprites from a Texture Packer Image
author: chris
type: post
date: 2014-04-10T16:58:48+00:00
url: /2014/04/10/animating-sprites-from-a-texture-packer-image/
categories:
  - sirchris
tags:
  - code
  - corona
  - learning

---
I&#8217;ve been experimenting with animation and recently ran into a little trouble with spritesheets, [TexturePacker][1], [Corona SDK][2] and animation. The problem started when I wanted to animate [some sprites][3] from opengameart.org. The download included 89 animation sequences and each animation contained 8 individual character sprites, which looked like:
<!--more-->

<div class="inlineimg">
  <img class="wp-image-266 alignnone" alt="amg1" src="http://localhost:8888/wp-content/uploads/2014/04/amg1-1.png" width="256" height="32" />
</div>

Instead of including 89 .png files into my project, I used TexturePacker to condense them into one .png file. That made the spritesheet look something like:

<div class="inlineimg">
  <img class="alignnone size-full wp-image-268" alt="test1_Corona SDK-0" src="http://localhost:8888/wp-content/uploads/2014/04/test1_Corona-SDK-01-1.png" width="256" height="100" />
</div>

I ran into trouble because I was able load an animation sequence as a single image, but I had trouble splitting that sequence into the individual 8 frames required for animation. Here&#8217;s what I came up with to solve the issue.

https://gist.github.com/codepaladin/10392771

What we&#8217;re doing here is loading the spritesheet.lua file, which references the spritesheet.png file. Once we have the spritesheet information, we create an options table associated with one specific animation sequence, which is called amg1 in our example.

We then add width and numFrames variables to the options table so that Corona knows that the animation sequence contains 8 single frames, and each sprite frame is of equal size.

Finally, we generate an [imageSheet object][4] by passing in the spritesheet.png file and the options table.



Here we create a [sequenceData][5] table to store information on our animation&#8217;s name, which frame it should start on, how many frames should run, and how long each frame should run.

We then build the [sprite object][6] by passing the imageSheet and sequenceData info. Finally, we run the animation, which results in something like:

<div class="inlineimg">
  <img class="alignnone size-full wp-image-276" alt="825wp" src="http://localhost:8888/wp-content/uploads/2014/04/825wp-1.gif" width="32" height="32" />
</div>

You can [download the files][7] that I used for this on Github.

 [1]: http://www.codeandweb.com/texturepacker
 [2]: http://coronalabs.com/products/corona-sdk/
 [3]: http://opengameart.org/content/700-sprites
 [4]: http://docs.coronalabs.com/api/library/graphics/newImageSheet.html
 [5]: https://docs.coronalabs.com/api/library/display/newSprite.html#sequence-data
 [6]: https://docs.coronalabs.com/api/library/display/newSprite.html
 [7]: https://github.com/codepaladin/SpriteSheet