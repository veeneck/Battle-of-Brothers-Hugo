---
title: One Year Later – Late and Over Budget
author: chris
type: post
date: 2015-04-08T17:37:55+00:00
url: /sirchris/one-year-later-late-and-over-budget/
categories:
  - sirchris
tags:
  - learning

---
Today marks the one year anniversary of our [game development competition][1], so I can now safely say that the game will be late. Not only will the game be late, but I&#8217;m also about [2k over budget][2]. If you had asked me a year ago if I would be disappointed about being late and over budget, I would have absolutely said yes.
<!--more-->

In my former career as a web developer I prided myself meeting budget and time deadlines. I rarely missed any type of programming deadline (unless management screwed things up, of course) and could fairly accurately predict how long any coding task would take. Now that I have a year of game development under my belt, I can confidently say that I can in no way estimate how long it takes to develop a game.

I would have been upset if my being late was due to a lack of effort, but it&#8217;s more due to the fact that there is so much more to game development than game programming. I have been off on pretty much every meaningful estimate and the game will be at least 6 months late and possibly a year late (hopefully?). The fact that [my opponent][3] is also late helps soften the blow, and while I can&#8217;t speak for him, here are some aspects of game development that took more time than I expected.

#### Game Design

I don&#8217;t know what I was originally thinking here, but coming up with an original game idea, making an art design document, working with multiple contractors, researching music styles, writing dialogue, testing interfaces, and all of the other tasks associated with game design has taken a ton of time. If you take a look at just my last 3 months of development time, you can see that 40% was spent on actual software development.

<div class="inlineimg">
  <img src="/wp-content/uploads/2015/04/Screen-Shot-2015-04-06-at-2.50.58-PM-1024x357.png" alt="Screen Shot 2015-04-06 at 2.50.58 PM" width="625" height="218" class="alignnone size-large wp-image-2030" />
</div>

At least sixty percent of my time was spent on doing things other than development. I say at least because I spend a lot of time at home and not logged into [RescueTime][4] that isn&#8217;t represented in this chart. Some of that sixty percent of time is doing tedious and repetitive development tasks outside of code, like cutting up sprites, but a lot of it is spent researching, thinking, planning, and testing the game. Somehow I didn&#8217;t think about the fact that a game has hundreds of sound effects and somebody has to think of what effects to use and then create an excel spreadsheet detailing those effects. I honestly didn&#8217;t understand how game design was a real job before I started making a game by myself, but I definitely get it now. Somebody has to do the mountain of planning work that isn&#8217;t programming and art, and when you&#8217;re alone that somebody is you.

#### New Tools

I knew I&#8217;d have to learn the how the [Corona SDK][1] worked, but I never really gave much thought to the other tools I&#8217;d need to learn and understand. Some of the applications that I have had to learn are [iDraw][5] and [PixelMator][6] for image editing,[Texture Packer][7] for sprite sheets, [Batch Crop][8] for batch image cropping, [Particle Designer][9] for particle effects, and [Garage Band][10] for music editing. Like learning game development API calls, none of these tools have caused major headaches, but getting an understanding of them all has taken up a solid chunk of time.

I can also understand how game studios end up building custom tools, because as I&#8217;ll talk about in the next section, game development can be very tedious even when you have tools at your disposal.

#### Tediousness

I wish I could think of a better title for the section, but so much about game development has just been a tedious process. Don&#8217;t get me wrong, I&#8217;m enjoying the process, but sometimes I feel like I&#8217;m basically doing manual labor on a computer.

A recent example to illustrate what I&#8217;m talking about is what I&#8217;ve gone through to add a hero&#8217;s path to the world map. Here I have a world map that looks like:

<div class="inlineimg">
  <img src="/wp-content/uploads/2015/04/Screen-Shot-2015-04-06-at-2.05.01-PM-1024x608.png" alt="Screen Shot 2015-04-06 at 2.05.01 PM" width="625" height="371" class="alignnone size-large wp-image-2022" />
</div>

What I want to do is animate a yellow and green line that goes from point A to point B in order to indicate the path that the heroes take. The end result looks a little something like this:

<div class="inlineimg">
  {{< gfycat data_id="EmptyScaryAbalone" >}}
</div>

That small path looks easy enough, but implementing it requires going into Pixelmator, creating 20 or 30 mask images, and then sequentially animating the path with those mask images. The game has 22 of these paths, so that&#8217;s 22 path animations that have to be cut up, animated, tested, usually fixed in some way, and then tested again.

This same scenario happens in some way with pretty much every visual element that goes on-screen. Consider the fact that I have something like 10,000 images making up character sprites and all of those need to made into sprite sheets, tested, resized for multiple devices, etc. and it&#8217;s easy to understand how time flies. The devil is in the details, but man, those details sure do take a lot of time.

#### Game Programming

I would say that I beat my expectations as to how long it would take to learn and be comfortable with a new programming language and development platform. I thought it would take me a few months to become comfortable with a new programming language, but making the switch from PHP to LUA wasn&#8217;t all that difficult. On top of that, the [Corona SDK][11] has been very easy to use and was easier than I expected. Where I didn&#8217;t beat my estimate is how long it would take to learn all of the new functionality associated with game programming.

To understand what I&#8217;m talking about, take a look at [Corona&#8217;s API reference chart][12]. None of that functionality is particularly hard to learn individually, but learning how and when to utilize different techniques has taken a lot of time in aggregate.

As I went over in the last section, [masking images][13] is a widely used gaming technique in which I had no experience. Like I did with so many techniques, I took the tutorials, built out a test separate project for experimentation, and then eventually added the technique into my game. Unfortunately, things never seem to work out quite right the first time, so it usually takes two or three attempts to get a new technique to work out just right. What I initially think will take a day can easily end up taking a week to perfect.

This same scenario has played out with scene management, sprite sheets, animations, character pathing, event listeners, display groups, audio management, memory management, multiple device support, and the list goes on. I&#8217;m getting very comfortable with the techniques used to make a game, but it&#8217;s taken me a year to get here.

#### Conclusion

So the bad news is that the game is going to be late and over budget. The good news is that I&#8217;ve learned a ton, am having having a blast making this game, and have every intention of seeing it through. If I could go back in time I probably would have chosen a simpler game with less story and less complicated artwork, but there was no way for me to know how much is involved with all of this. I see games and game developers in an entire new light now and have a new respect for aspects of games that I never knew existed. It&#8217;s been a good year and hopefully I&#8217;m writing about a successfully launched game a year from now.

 [1]: http://battleofbrothers.com
 [2]: http://battleofbrothers.com/sirchris/budget
 [3]: http://battleofbrothers.com/sirryan
 [4]: https://www.rescuetime.com/
 [5]: http://www.indeeo.com/idraw/
 [6]: http://www.pixelmator.com/mac/
 [7]: https://www.codeandweb.com/texturepacker
 [8]: http://www.batchcrop.com
 [9]: https://71squared.com/particledesigner
 [10]: https://www.apple.com/mac/garageband/
 [11]: https://coronalabs.com/products/corona-sdk/
 [12]: http://docs.coronalabs.com/api/
 [13]: http://battleofbrothers.com/sirchris/animating-a-path-using-image-masking