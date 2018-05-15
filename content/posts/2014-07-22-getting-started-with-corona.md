---
title: Getting Started with Corona
author: chris
type: post
date: 2014-07-22T17:37:32+00:00
url: /2014/07/22/getting-started-with-corona/
categories:
  - sirchris
tags:
  - corona
  - learning

---
I&#8217;ve been working on my game for about three months now and I feel like I&#8217;m in a pretty good spot. I have a good grasp of LUA and the Corona SDK and my problems are more focused on what type of game to make and not how to make a game. I&#8217;ve spent a lot of time reading documentation and taking tutorials and I want to share the resources that helped me get started with any fellow beginners out there.
<!--more-->

#### Coronalabs.com

If you have a question about Corona, then there is a good chance you can find the answer in Corona&#8217;s [resource documentation][1]. I&#8217;ve spent a a lot of time going through their [university][2], [API docs][3], [forums][4], and [blog][5]. I also recommend taking a look at the [Corona Geek Videos][6] and subscribing to the [Corona Labs Digest][7], which both keep you up to date with Corona&#8217;s features and enhancements.

#### Masteringcoronasdk.com

After poring over Corona&#8217;s official website, I took the [free beginner&#8217;s game development crash course][8]. The free tutorial was done well, so I sprung for the [beginning mobile game development][9] video tutorial series. If I could go back in time, then I think I would have started out by taking these video tutorials before reading so much of Corona&#8217;s official documentation.

#### Scene Management

Scene management is a core concept in Corona and [develephant.net][10], a wonderful Corona resource, has a [great storyboarding tutorial][11] explaining how it all works. Corona has since moved from the storyboard API to the new composer API, but the tutorial is still good at explaining the concepts of scene management. Corona has since published a tutorial on their [composer API][12], which is what you&#8217;ll want to use now.

#### Classes & Inheritance

My original code got unwieldy very quickly and I&#8217;ve refactored my code to use objects and inheritance in an effort to tame the beast. Two of the tutorials that helped me understand how OOP works in Corona are [RPG Themed OOP Design Pattern for Corona][13] and [Form Zero to OO &#8211; ArdentKids guide to OOP with LUA and Corona][14].

#### Game Assets

I found most of my game assets at [opengameart.org][15] and [spritedatabase.net][16]. I use [imagesplitter.net][17] to split up the single images into multiple frames and then use [TexturePacker][18] to create sprite sheets ready to use with Corona. I recently wrote a [couple of tutorials][19] demonstrating how I&#8217;ve used the various services for my sprite needs.

 [1]: http://coronalabs.com/resources/
 [2]: http://coronalabs.com/resources/tutorials/getting-started-with-corona/
 [3]: http://docs.coronalabs.com
 [4]: http://forums.coronalabs.com
 [5]: http://coronalabs.com/blog/
 [6]: http://coronageek.com
 [7]: http://coronalabs.com/resources/corona-labs-digest/
 [8]: http://masteringcoronasdk.com/game-development-crash-course/
 [9]: http://masteringcoronasdk.com/beginning-mobile-game-development/
 [10]: http://www.develephant.net
 [11]: http://www.develephant.net/a-simple-storyboard-framework-for-corona-sdk-part-1/
 [12]: http://coronalabs.com/blog/2014/01/21/introducing-the-composer-api-plus-tutorial/
 [13]: http://www.develephant.net/an-rpg-themed-oop-design-pattern-for-corona-sdk-part-1/
 [14]: http://www.omidahourai.com/from-zero-to-oo-ardentkids-guide-to-object-oriented-lua-with-corona-sdk
 [15]: http://opengameart.org
 [16]: http://spritedatabase.net
 [17]: http://imagesplitter.net
 [18]: https://www.codeandweb.com/texturepacker
 [19]: http://battleofbrothers.com/tag/learning?k=sirchris