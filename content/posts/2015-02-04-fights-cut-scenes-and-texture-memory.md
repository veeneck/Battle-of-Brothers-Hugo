---
title: Fights, cut scenes, and texture memory
author: chris
type: post
date: 2015-02-04T16:15:28+00:00
url: /sirchris/fights-cut-scenes-and-texture-memory/
featured_image: /wp-content/uploads/2015/01/SC01_011-e1423929268304.jpg
number:
  - 19
keyevent:
  - Experimenting with texture memory
  - Add sprite sheets
categories:
  - sirchris
tags:
  - status

---
The good news is that I’ve received a ton of artwork over the last two weeks. The bad news is that I can only demo a small portion of it because there just isn’t enough time to get it all into the game. That’s a good problem to have, though, and what I can show you is some pretty cool cut scenes, some character animations, and this sweet footage of a knight putting the beat down on an evil ogre.
<!--more-->

<div class="inlineimg" style="clear:both">
  {{< gfycat data_id="CoarseWeakKagu" >}}
</div>

You can’t see all of the animations in that .png sequence, but you can see 3 of the knight’s 4 attack moves, the ogre’s hit animation and the ogre’s death animation. For debugging purposes, I built a tool to display all of a character’s animations at once, and here are those two characters going through all of their moves.

<div class="inlineimg">
  {{< gfycat data_id="ShamelessSecondBlackpanther" >}}
</div>

<div class="inlineimg">
  {{< gfycat data_id="EmbellishedSpitefulCuttlefish" >}}
</div>

#### Memory Considerations

The animations are looking great, but one thing I noticed during the game demo was that each new character took up too much texture memory. Each character has 8 animations, each animation is ~45 frames, and each animation is shot from 2 angles. That gives me a total of 720 sprites per character. I use [Texture Packer][1] to condense those sprites into sprite sheets, but many of the sprite sheets took up 4 &#8211; 16MB of memory. When you consider that I&#8217;ll have up to 12 characters on-screen at the same time, I had a potential problem on my hand. The good news is that I have some options to deal with this issue.

  * One option is to use fewer frames per animation. This is promising, especially for some of the animations that run at higher frame rates.</p> 
  * Another option is to load/unload sprite sheets as needed, but I’m worried that will make the animations unreliable and clunky.

  * A third option is to shrink the individual sprites and then scale them up in-game.

Based on my initial tests, I think I’m going to try the third option. I get some good memory savings by shrinking sprites by about 20%, and it’s hardly noticeable when those sprites are scaled-up in-game. Having fewer frames per animation would be my second choice and possibly something I still utilize in certain situations, but I felt that having fewer sprites per animation was more noticeable to the eye than slightly scaling up sprites.

Most of my time in the last week has been experimenting with animations and creating testing tools to figure out the memory issue before adding any new characters to the game. Creating sprite sheets is a boring and time intensive process, so I’ll save in the long run by figuring out a strategy now.

#### Illustrations

I have all of the battlefield maps, world map, and character concepts illustrated, but I still have some cut scene and marketing work to be illustrated. The first contract that I had with [Scott Pellico][2], the game’s illustrator, was completed and I’ve entered into a second contract to hopefully finish the remaining work. This is going to put me over budget, but I think the investment will be worth it. Scott started on the cut scenes and story this week, and here’s one of the images that will help me provide the player with a bit of background story before getting into the game.

<div class="inlineimg">
  <img src="/wp-content/uploads/2015/01/SC01_01-2.jpg" alt="SC01_01" width="800" height="269" class="alignnone size-full wp-image-1762" srcset="/wp-content/uploads/2015/01/SC01_01-2.jpg 800w, /wp-content/uploads/2015/01/SC01_01-2-300x101.jpg 300w, /wp-content/uploads/2015/01/SC01_01-2-768x258.jpg 768w" sizes="(max-width: 800px) 100vw, 800px" />
</div>

#### What&#8217;s Next

Now that I have more artwork than I now what to do with, I have a couple of options. I can either add some more characters into the game or I can start playing with the cut scenes and story part of the game. My gut says I&#8217;ll want to go with the cut scenes only because I&#8217;ve been playing with sprites for the last few weeks and a change of pace is good for the soul.

 [1]: https://www.codeandweb.com/texturepacker
 [2]: http://appylon.weebly.com