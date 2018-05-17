---
title: Memory Usage in Sprite Kit
author: Ryan
type: post
date: 2014-08-25T14:58:39+00:00
url: /sirryan/memory-usage-in-sprite-kit/
categories:
  - sirryan
tags:
  - code
  - learning
  - sprite kit

---
Now that I&#8217;m <a href="http://battleofbrothers.com/sirryan/0-to-art-in-two-weeks" target="_blank">receiving real art</a> for my game, I thought it would be a good time to learn about memory usage and limits. This was also prompted by my current level running at 55-60MB before any gameplay action or characters loaded on screen. That memory usage seemed a bit high, so I decided this was an issue that I needed to <a href="https://www.youtube.com/watch?v=2o1U2pWcR34" target="_blank">delve into</a>. In hindsight, most of this is basic to an experienced game developer, but I found the process to be quite fun. You can just read my lessons learned below if you don&#8217;t want to follow my detective work.
<!--more-->

  * Product -> Clean in Xcode between each test.
  * <a href="http://stackoverflow.com/a/15200855/3519461" target="_blank">Upper limits on memory usage</a>.
  * Compress png&#8217;s to improve download size, not memory management.
  * PVR is a commonly recommend format.
  * Change <a href="http://stackoverflow.com/questions/21625654/sprite-kit-texture-atlas-define-image-format-rgba4444-rgb565" target="_blank">build settings to </a><span style="color: #000000"><a href="http://stackoverflow.com/questions/21625654/sprite-kit-texture-atlas-define-image-format-rgba4444-rgb565" target="_blank">RGBA4444</a> if your images still look good at that setting. I&#8217;m not sure if it is my art style, but I couldn&#8217;t get them to look right (even with dithering).</span>
  * RGB565 seems to hold up quality, but does not support transparency. This would work well for my base background.
  * Breaking apart large images into tiles, and removing tiles that would be covered by other gameplay elements, shows minor gains.
  * Create a smaller file for smaller resolution devices as fallback.
  * Group files in texture atlases according to use.
  * Read<a href="https://developer.apple.com/library/ios/documentation/3ddrawing/conceptual/opengles_programmingguide/TechniquesForWorkingWithTextureData/TechniquesForWorkingWithTextureData.html" target="_blank"> official advice</a>.

Of course, nothing is ever easy. Here are my unanswered questions:

  * Sprite Kit seems to convert atlases at build time, so setting one image to be RGB565 won&#8217;t work. It&#8217;s all or nothing. I tried adding my one image to images.xcassets, but memory usage increases since the benefits of atlases aren&#8217;t being used. I&#8217;m trying to find a way to set different compressions for different atlases.
  * I am not having any luck getting PVR files to work with Sprite Kit. Any tips?

#### Test 1: Remove GUI

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1088" src="/wp-content/uploads/2014/08/Test-2.png" alt="Test 2" width="625" height="467"  />
</div>

I began my tests by removing things piece by piece. The goal was to get down to 1 node and observe what happened along the way.

Memory: **52MB**    CPU: **17%**

#### Test 2: Remove Layers

<div class="inlineimg">
  <img class="alignnone size-full wp-image-1091" src="/wp-content/uploads/2014/08/foothills_base_01-compressor.jpg" alt="foothills_base_01-compressor" width="625" />
</div>

My game is isometric, so there are a ton of layers to give depth and allow units to walk behind objects. I went ahead and removed all of those, which leaves a basic full size background image. This had hugely successful results mainly because anywhere a layer is sitting gone top of the background, the memory usage for that part of the screen is essentially doubled.

Memory: **25.5MB**    CPU: **14%**

#### Test 3: Compress Images

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1092" src="/wp-content/uploads/2014/08/Test-4.png" alt="Test 4" width="625" height="507"  />
</div>

Using <a href="https://compressor.io" target="_blank">compressor.io</a>, I shrunk my background image from 1.93MB to 390KB. That&#8217;s a huge difference, and I was expecting huge results. But, I didn&#8217;t get the results I was looking for. Hmmm. At a minimum, this at least helps with the <a href="http://stackoverflow.com/questions/4753100/max-size-of-an-ios-application" target="_blank">over-the-air download limit</a>.

Memory: **25.5MB**    CPU: **12%    **Verdict: **Helps download size, but not in game memory.**

#### Test 4: Clean Up Atlas Folder

I was using my `.atlas` folders to hold generic items instead of specific collections. I removed everything not necessary to the scene, and noticed good results. It appears that if you touch anything inside of an atlas, the entire contents of the atlas are accessed in some fashion.

Memory: **20.9MB**    CPU: **12%    **Verdict:** Important.**

#### Test 5: New Swift / Sprite Kit Project

Making progress now, so a benchmark is needed. What does a brand new, empty project run at?

Memory: **8.1MB**    CPU: **9%**

#### Test 6: Clean Up images.xcassets

Since cleaning up the texture atlases helped, I decided to see if cleaning up images.xcassets would have a similar effect. No luck.

Memory: **20.9MB**    CPU: **12%    **Verdict: **Not related.**

#### Test 7: Stop All Code

I made sure that all of my code was no longer executing. The scene is unpacked, and then nothing else happens. No change.

Memory: **20.9MB**    CPU: **12%**

#### Test 8: Try A Smaller Background Image

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1093" src="/wp-content/uploads/2014/08/Screen-Shot-2014-08-23-at-12.01.36-PM.png" alt="Screen Shot 2014-08-23 at 12.01.36 PM" width="625" height="468" />
</div>

At this point, it became clear that file size alone is not the only indicator of memory. So, I tried an image of 1/4 the size. 75% savings, which proved that the remaining ~12MB between a base project and mine was due to the texture size of the background image. Turns out textures use memory based on their <a href="http://stackoverflow.com/questions/20377859/high-memory-usage-in-spritekit-when-using-texture-atlas" target="_blank">resolution and color depth</a>.

Memory: **11.8MB**    CPU: **11%    **Verdict:  **Huge. Memory is related to texture size.**

#### Test 9: RGBA4444

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1110" src="/wp-content/uploads/2014/08/foothills_bad.png" alt="foothills_bad" width="625" height="481" />
</div>

Using RGBA444 instead of RGBA8888 cuts the memory used in half. The problem is that it leaves artifacts all over the artwork, and in my case they are quite noticeable. I pointed out the water and snow as examples above.

Memory: **14.9MB**    CPU: **11%    **Verdict: **Huge. But, image quality suffers.**

#### Test 10: Break Apart Into Tiles

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1116" src="/wp-content/uploads/2014/08/Screen-Shot-2014-08-24-at-10.45.14-AM.png" alt="Screen Shot 2014-08-24 at 10.45.14 AM" width="625" height="468" />
</div>

I wanted to see what would happen if the background was tiled instead of one giant image. Then, I could remove tiles that would be hidden behind a z-index overlay. I thought this would be significant, but I only saw minor gains.

Memory: **Saved 1.8MB**    CPU: **11%    **Verdict: **Minimal gains. Last resort.**