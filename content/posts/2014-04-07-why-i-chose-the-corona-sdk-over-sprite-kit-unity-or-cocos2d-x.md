---
title: Why I Chose the Corona SDK over Sprite Kit, Unity, or Cocos2d-x
author: chris
type: post
date: 2014-04-07T15:17:57+00:00
url: /2014/04/07/why-i-chose-the-corona-sdk-over-sprite-kit-unity-or-cocos2d-x/
categories:
  - sirchris
tags:
  - thoughts

---
I&#8217;ve spent the last couple of weeks testing out different 2d game development frameworks, and I&#8217;ve decided that the [Corona SDK][1] is the tool for me. I was hoping there would be a standout framework that could make basic 2d games much better than the others, but I feel they each have pros and cons and they can all make games just fine. What it really comes down to is what makes me comfortable and excited about game development. I&#8217;m not qualified to list out the [pros and cons of each environment][2], since I&#8217;ve been developing games for all of two weeks, but I can tell you why Corona won my business.

<!--more-->

**Ease of Use**
  
Corona utilizes the [Lua programming language][3], which I find intuitive and extremely easy to learn. There is plenty of documentation and support behind Lua, and I&#8217;ve yet to encounter a problem that wasn&#8217;t already answered by either Corona or a member of the Lua community.

Like Lua, Corona is beginner friendly, and I was able to immediately jump into playing around with games. Their API&#8217;s are [well documented][4] and they provide plenty of examples on getting started. Corona also allows me to use my preferred text editor, [Sublime Text][5], which won them some bonus points.

The knock on Lua is that it&#8217;s an underpowered and unstructured scripting language, but that doesn&#8217;t worry me too much. I&#8217;m the sole developer on my game, so I should be able to keep the code organized. And while Corona and Lua may not have the flexibility and power compared to the other frameworks/languages, I&#8217;m confident it will pack enough power to create my 2d game.

**Community**
  
I&#8217;m new to game development and Lua, so it&#8217;s important that there is a community to fall back on when times get tough. I&#8217;ve already been able to quickly find not only official documentation, but a slew of blog posts explaining how various parts of Corona and Lua work. For example, I didn&#8217;t understand how Lua and Corona managed [event listeners][6], [variable scope][7], [classes and inheritance][8], or [storyboarding][9], but basic Google searches resulted in quality and well written examples by the community.

When I visit the Corona forums I&#8217;m impressed with not only how much knowledge is readily available, but in the activity of [Corona&#8217;s moderators and experts][10]. They quickly answer questions from both absolute beginners and advanced programmers, and I feel that I&#8217;ll have somebody to lean on when I do eventually get snagged.

**Active Development**
  
Corona does cost money if you&#8217;re serious about making games, but I&#8217;m ok with that because they&#8217;re actively building and supporting their product. A glance their [blog][11] and [daily builds][12] shows that the product is actively being built upon and thoroughly tested. I&#8217;m confident that as the gaming landscape continues to change, Corona will quickly work towards supporting whatever the future may bring.

**My Gut**
  
I developed web applications in a LAMP environment and I&#8217;m used to hearing debates about this language vs. that language, which database is best, and why one framework is better than another. What I&#8217;ve seen is people build absolutely amazing applications in any environment and also produce awful code in every language.

While there was nothing really wrong with Unity, Sprite Kit or Cocos2d-x, they didn&#8217;t feel right, either. I wasn&#8217;t exited about working in Unity&#8217;s GUI, Sprite Kit&#8217;s use of Objective-C and Xcode, and Cocos2d-x&#8217;s less beginner friendly environment. I&#8217;m new to building games, and momentum and excitement are important to me right now. I am excited about Corona and that&#8217;s why I ultimately choose them.

 [1]: http://coronalabs.com/products/corona-sdk/
 [2]: http://www.raywenderlich.com/67585/cocos2d-vs-sprite-kit-vs-unity-2d-tech-talk-video
 [3]: http://www.lua.org/docs.html
 [4]: http://docs.coronalabs.com/api/
 [5]: http://www.sublimetext.com
 [6]: http://www.omidahourai.com/2013-06-27/improve-runtime-event-listeners-by-using-closures-lua-corona-sdk
 [7]: http://www.develephant.net/how-to-use-global-variables-in-corona-sdk/
 [8]: http://www.omidahourai.com/from-zero-to-oo-ardentkids-guide-to-object-oriented-lua-with-corona-sdk
 [9]: http://www.develephant.net/a-simple-storyboard-framework-for-corona-sdk-part-1/
 [10]: http://forums.coronalabs.com/user/414323-rob-miracle/
 [11]: http://coronalabs.com/blog/
 [12]: http://developer.coronalabs.com/corona-daily-builds/summary