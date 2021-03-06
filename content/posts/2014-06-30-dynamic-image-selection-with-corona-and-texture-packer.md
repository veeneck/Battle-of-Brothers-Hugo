---
title: Dynamic Image Selection with Corona and Texture Packer
author: chris
type: post
date: 2014-06-30T15:26:31+00:00
url: /sirchris/dynamic-image-selection-with-corona-and-texture-packer/
categories:
  - sirchris
tags:
  - code
  - corona
  - learning

---
Most mobile apps are developed to run across multiple devices, which means developers have to account for multiple screen resolutions. Image scaling is an important part of multi-device support because you want to use higher resolution images on modern, high-res devices, while using lower resolution images on low-res devices. That saves memory on the low-res devices while maximizing all of the pixel density goodness on the high-res devices. Lucky for Corona SDK developers, Corona makes image scaling a breeze with their [dynamic image selection][1] feature.
<!--more-->

In this tutorial I&#8217;m going to go over how to implement dynamic image selection using [Texture Packer][2] and Corona to easily scale your images across multiple devices. If you haven&#8217;t already downloaded Texture Packer, go and [download the free trial][3]. Texture Packer easily creates sprite sheets for multiple game engines and they also automatically scale sprite sheets for Corona SDK.

#### Drag your Images into Texture Packer

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/Screen-Shot-2014-06-24-at-2.19.59-PM-1024x590.png" alt="Screen Shot 2014-06-24 at 2.19.59 PM" width="625" height="360" class="alignnone size-large wp-image-708" />
</div>

I&#8217;m using a [Tuscan Knight image][4] that I found at open game art, so you can download that to follow along.

In this first step we find our knight images, which are in the /Isometric/Idle folder and drag them over into Texture Packer. Also make sure that the Texture Packer data format setting at the top left of the screen is set to Corona SDK.

#### Configure Auto-SD Settings

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/Screen-Shot-2014-06-24-at-2.20.19-PM.png" alt="Screen Shot 2014-06-24 at 2.20.19 PM" width="851" height="679" class="alignnone size-full wp-image-709" />
</div>

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/Screen-Shot-2014-06-24-at-2.20.28-PM.png" alt="Screen Shot 2014-06-24 at 2.20.28 PM" width="836" height="678" class="alignnone size-full wp-image-710" />
</div>

Click the AutoSD cog in the left hand panel to bring up the Auto-SD Settings panel. Once that pops up, click on corona@2x and hit Apply. This is done so that Texture Packer will create two sprite sheets. One at full size and one at half-size.

#### Name your Files

You need to include {v} in your file names as a placeholder for the variant identifier, which is 2x in this case.

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/Screen-Shot-2014-06-24-at-2.21.24-PM.png" alt="Screen Shot 2014-06-24 at 2.21.24 PM" width="387" height="376" class="alignnone size-full wp-image-711" />
</div>

#### Export the Sprite Sheet

Click the Publish button and export your sprite sheets and corresponding .lua files. There should be 4 total files which in this example are knight.lua, knight.png, knight@2x.lua and knight@2x.png.

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/Screen-Shot-2014-06-24-at-2.21.50-PM-1024x857.png" alt="Screen Shot 2014-06-24 at 2.21.50 PM" width="625" height="523" class="alignnone size-large wp-image-707" />
</div>

#### Create a Corona Project

Create a new project in Corona and add the two .png files and two .lua files that were generated by Texture Packer. You&#8217;ll also want to create a main.lua file and config.lua file.

#### The Config File

https://gist.github.com/codepaladin/f17194932197ea3aa91e

They key to image scaling is the .config file, and you can read more about what a config file handles over on the [official Corona site][5]. The config file that I&#8217;m using was taken from Corona&#8217;s [tutorial on modernizing the config.lua file][6]:

What the config file does here is tell Corona to use the larger sprite sheet, or the &#8220;@2x&#8221; .png file on devices that have a screen width greater than 1040 pixels. The smaller base .png file will be used on any devices that have a screen width less than 1040 pixels.

#### Displaying Images

https://gist.github.com/codepaladin/b202d45864ba6a886cc6

Here we draw an animated knight sprite to the screen based off of the sprite sheets that Texture Packer created. Corona automatically handles which sprite sheet to use based on the device you&#8217;re using.

So if you&#8217;re on an iPhone 5, the display will look like:

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/Screen-Shot-2014-06-24-at-4.08.47-PM.png" alt="Screen Shot 2014-06-24 at 4.08.47 PM" width="369" height="770" class="alignnone size-full wp-image-714" />
</div>

And if you&#8217;re on an iPad Retina, the display will look like:

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/Screen-Shot-2014-06-24-at-4.09.02-PM.png" alt="Screen Shot 2014-06-24 at 4.09.02 PM" width="828" height="1080" class="alignnone size-full wp-image-715" />
</div>

The images look similar, but they&#8217;re actually taken from different sprite sheets as you can see by the image with the 2x on it. The iPhone will use less memory since it loads in a smaller image. The iPad uses more memory, but it has more clarity due to the greater pixel density.

Files for this tutorial can be [downloaded on GitHub][7].

 [1]: http://docs.coronalabs.com/guide/basics/configSettings/#dynamic-image-selection
 [2]: http://www.codeandweb.com/texturepacker
 [3]: http://www.codeandweb.com/texturepacker/download
 [4]: http://opengameart.org/content/tuscan-knight-bleeds-game-art-hd
 [5]: http://docs.coronalabs.com/guide/basics/configSettings/index.html
 [6]: http://coronalabs.com/blog/2013/09/10/modernizing-the-config-lua/
 [7]: https://github.com/codepaladin/Image-Scaling