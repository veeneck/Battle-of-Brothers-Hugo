---
title: Multi-Device Support and HUD Elements
author: chris
type: post
date: 2014-06-30T15:25:12+00:00
url: /sirchris/multi-device-support-and-hud-elements/
keyevent:
  - Added Multi-Device Support
  - Added Basic HUD
  - Tested Dynamic Image Scaling
number:
  - 7
categories:
  - sirchris
tags:
  - status

---
This update was delayed by a week because I took a &#8220;[vacation][1]&#8220;, but I&#8217;m back in action and hard at work again. After the last update I had some concerns about making my game work across multiple devices, but I&#8217;m happy to say that Corona makes multi-device support pretty easy. It was actually so easy that I was not only able to make my prototype work across multiple devices, but I also had time to start adding some basic HUD elements to the game.
<!--more-->

#### Multi Device Support

I plan on releasing my game to phone and tablet users running both the Android and iOS operating systems, so that means I&#8217;ll need to support a lot of mobile devices. iPads, iPhones, iTouches, Droids, Galaxy Phones and Tablets, Kindles, and even the Ouya all have different screen sizes and resolutions. I knew that Corona handles the porting of the game logic, but I didn&#8217;t know what type of work I&#8217;d have to do to the display elements.

My background is in web development and because of my experience with developing cross browser applications, I absolutely dreaded making my game prototype work across multiple platforms. Up to this point, I had been developing the game for the 1024 x 768 iPad and all of the design elements were displayed properly. Unfortunately, the design elements were not displayed properly in just about every other device.

**iPad**

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/iPad.png" alt="iPad" width="625" height="471" class="alignnone size-large wp-image-727" />
</div>

**iPad Retina**

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/iPad-Retina.png" alt="iPad-Retina" width="625" height="468" class="alignnone size-large wp-image-728" />
</div>

**iPhone 5**

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/iPhone5.png" alt="iPhone5" width="625" height="314" class="alignnone size-large wp-image-729" />
</div>

**Galaxy S3**

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/GalaxyS3.png" alt="GalaxyS3" width="625" height="338" class="alignnone size-large wp-image-730" />
</div>

**Nook-Color**

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/Nook-Color.png" alt="Nook-Color" width="625" height="346" class="alignnone size-large wp-image-731" />
</div>

**Ouya**

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/Ouya.png" alt="Ouya" width="625" height="359" class="alignnone size-large wp-image-732" />
</div>

As you can see, each device displays a different version of the game and most of them weren&#8217;t very playable. So I headed over to the [Corona Docs][2] expecting to find guidance on how to build some sort of master conversion file that would allow me to specify how things needed to look on each device. To my surprise, I didn&#8217;t need to do anything like that because Corona once again knew this would be an issue and made my life as a developer easier. As it turned out, the only code I needed to add to make my demo work on multiple devices was to add these lines:

https://gist.github.com/codepaladin/f17194932197ea3aa91e

Now when I view my updated demo in multiple devices, it looks like:

**iPad**

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/iPad1.png" alt="iPad" width="625" height="471" class="alignnone size-large wp-image-750" />
</div>

**iPad Retina**

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/iPad-Retina1.png" alt="iPad-Retina" width="625" height="471" class="alignnone size-large wp-image-751" />
</div>

**iPhone 5**

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/iPhone51.png" alt="iPhone5" width="665" height="331" class="alignnone size-full wp-image-752" />
</div>

**Galaxy S3**

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/GalaxyS31.png" alt="GalaxyS3" width="625" height="351" class="alignnone size-large wp-image-753" />
</div>

**Nook-Color**

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/Nook-Color1.png" alt="Nook-Color" width="625" height="346" class="alignnone size-large wp-image-757" />
</div>

**Ouya**

<div class="inlineimg">
  <img src="http://battleofbrothers.com/wp-content/uploads/2014/06/Ouya1.png" alt="Ouya" width="625" height="360" class="alignnone size-large wp-image-759" />
</div>

Not too bad! The game doesn&#8217;t look exactly the same, because the dimensions differ across devices, but the game is playable on all of the devices and the differences can be cleaned up by using expandable backgrounds and other device-specific artwork.

Corona also helps developers optimize their games through [dynamic image scaling][3], which allows you to use hi-res images on hi-res devices and low-res images on low-res devices. During this update I did make sure that dynamic image scaling works for my game, but I didn&#8217;t fully implement it because of the tedious work involved with rebuilding all of my sprite assets. I&#8217;ll be replacing all of the artwork with custom art specific to my game, so there is no need to rebuild all of the prototype art.

#### Heads up Display (HUD)

Since I had some extra time after fooling around with multi-device support, I started working on the [heads up display (HUD)][4]. I still don&#8217;t know exactly how my game is going to be played, but I do know that there will be some key HUD elements including indicating player turn, player actions, and a settings icon. With this general framework in mind, here is what I&#8217;ve come up with so far.

https://www.youtube.com/watch?v=rwKX0LrdTZs&feature=youtu.be

**Player Turn**
  
At the bottom-left of the screen you can whose turn it is and which characters are coming up in future turns. This can be expanded upon to show character health, abilities, defense, etc. I think [Banner Saga][5] did a good job with this type of functionality and I&#8217;d like to put my own spin on it.

**Player Actions**
  
Player actions can be seen at the bottom-right of the screen and this is where character specific actions will be located. I only added attack and next-turn actions for this update, but I expect this area to expand significantly as the game develops. The next turn icon does work, but the attack actions don&#8217;t actually do anything just yet.

#### What&#8217;s Next

I plan on building out the HUD a little bit more over the next couple of weeks. I&#8217;ll be adding functionality to the settings and attack icons and also adding some new action icons to the characters. Each character only has a base attack, but as any turn based rpg fan knows, any game worth buying has characters with super and even super duper attacks.

 [1]: http://www.ragnartrail.com/locations/appalachians-wv
 [2]: http://docs.coronalabs.com/guide/basics/configSettings/
 [3]: http://battleofbrothers.com/sirchris/dynamic-image-selection-with-corona-and-texture-packer
 [4]: http://en.wikipedia.org/wiki/HUD_(video_gaming)
 [5]: http://mmohuts.com/wp-content/gallery/the-banner-saga-factions-preview/c-users-guillaume-pictures-screenshots-2013-04-07-14_22_05-the-banner-saga-factions-1-6-57.jpg?f096f9