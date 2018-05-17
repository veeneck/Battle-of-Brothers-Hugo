---
title: Designing Backgrounds for Multiple Aspect Ratios and Corona’s Config.lua
author: chris
type: post
date: 2014-08-26T13:50:19+00:00
url: /sirchris/designing-backgrounds-for-multiple-aspect-ratios-and-coronas-config-lua/
categories:
  - sirchris
tags:
  - art
  - corona
  - design
  - learning

---
One of the reasons I chose Corona SDK as my development platform was because they support many devices across many platforms. But mo&#8217; devices means mo&#8217; problems, and one of those problems is creating artwork that scales across all devices.
<!--more-->

Artwork isn&#8217;t cheap, especially when you&#8217;re working with contractors, so you&#8217;d like to reuse a single piece of art on all of the devices you&#8217;re targeting. One problem with supporting multiple devices is that [different devices have different aspect ratios][1], so an image that fills the screen in one device may look bad in another device. For example, here is how an image that&#8217;s specifically created for an iPad 3 looks on an iPhone 5.

<div class="inlineimg">
  <img src="/wp-content/uploads/2014/08/bridge-iphone.png" alt="bridge-iphone" width="532" height="270" class="alignnone size-full wp-image-1054"  />
</div>

You can see that the iPad adds spacing to the left and right of the image. This is because the iPhone has an aspect ratio of 16:9, while the iPad has an aspect ratio of 4:3. This gives the iPad more screen real estate vertically, but it gives the iPhone more space horizontally. If you were to create an image specifically for an iPhone, then the top and bottom of the iPad would end up with added spacing.

<div class="inlineimg">
  <img src="/wp-content/uploads/2014/08/bridge-ipad.png" alt="bridge-ipad" width="625" height="483" class="alignnone size-large wp-image-1056"  />
</div>

Corona has a clever way of dealing with resolution related issues with their [config.lua file][2] and [dynamic content scaling][3], which take resolution out of the equation and allow you to use a common set of screen coordinates and graphics across all devices. This is great because if you were to position a graphic at screen position (0,0), it will always appear at the top-left corner of the screen. It&#8217;s also great because images are also automatically scaled to almost look the same in devices.

I say almost look the same, because we still run into problems when screens have different aspect ratios. Corona will make an image on an iPad and an iPad Retina look exactly the same, because even though they have different resolutions, they have the same aspect ratios. But even with image scaling, there is no way to fit the exact same image into an iPad and an iPhone without distorting the image. The solution to this problem is to create a background image that caters to all aspect ratios . It needs to be as tall as the tallest resolution and as wide as the widest resolution. The magic number currently appears to be 2850 x 1800. An image that size allows us to do a few things:

  * Support 4:3 and 16:9 aspect ratios
  * Support high res devices like the iPad 3
  * Create 1x and 2x size images, with 1x at 1450 x 900 and 2x at 2850 x 1800. The 1x sizes are used for devices with a smaller screen width to preserve memory.

An image created at the &#8220;magic&#8221; resolution will need a little bit of cropping because it doesn&#8217;t exactly fit either aspect ratio. The solution to that is to add some good looking yet non-critical additions to the area that could potentially be cropped out. If you take my previous example and add a little extra fluff content around the top and bottom of the image, here&#8217;s a picture of what would be seen in the iPad and iPhone.

<div class="inlineimg">
  <img src="/wp-content/uploads/2014/08/bridgetest.jpg" alt="bridgetest" width="625" height="394" class="alignnone size-large wp-image-1049" />
</div>

The iPad still has more vertical room and the iPhone still has more horizontal room, but I&#8217;m able to use a single illustration for both screens by only adding non essential artwork to the areas that are cropped. That same image would work across a variety of mobile devices and even desktops.

 [1]: http://mediag.com/news/popular-screen-resolutions-designing-for-all/
 [2]: http://coronalabs.com/blog/2013/09/10/modernizing-the-config-lua/
 [3]: http://docs.coronalabs.com/guide/basics/configSettings/#dynamicscaling