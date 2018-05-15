---
title: 'Music & Memory'
author: chris
type: post
date: 2015-03-31T17:17:38+00:00
url: /sirchris/music-memory/
featured_image: /wp-content/uploads/2015/03/Unknown-1.png
number:
  - 23
keyevent:
  - First music scored.
  - Help with intro video.
categories:
  - sirchris
tags:
  - status

---
I’m happy to report that I’ve received the first 30 seconds of game music and that my ears are happy with what they&#8217;re hearing. It’s amazing what a little sound can do to the intro video and I can’t wait to see how the future music adds more depth to the game. I’ve also continued to experiment with some memory concerns and making scene transitions as smooth as possible. That’s required a bit of a re-write, but the game is heavy on texture memory usage, so it’s important to tackle this issue sooner than later.
<!--more-->

Let’s start off with the most interesting part of this update &#8211; music. As a quick recap, I’ve contracted [Brendon Williams][1], a talented composer, to create the game’s music. He’ll be scoring original pieces for the intro video, start screen, world map, and battles. He’s starting with the intro video because that will set the tone for the rest of the game. The first piece of music marks the transition from a series of evil scenes to scenes featuring the heroes, so I asked Brendon to kind of make something to transition from what will be a slow evil drum sound to a more defiant and vibrant heroic sound. Something like [The Gael from The last of the Mohicans Theme][2]. There’s only about 25 seconds of music so far, but I think Brendon is off to a fantastic start.

<div class="inlineimg">
  [youtube=https://www.youtube.com/watch?v=oChbnCv1H1k&w=740&theme=light]
</div>

#### Intro Video

A friend of mine who runs a creative studio, [Secret Powers][3], was in town recently and I had him take a look at the intro. He said things weren’t bad, but there was a lot that could be done to make things better. When you take a look at his [demo reel][4], it’s obvious that while my work is alright, his is really great. I asked him to help me make things better and once we got talking, we decided that it might be a good idea for him to handle some of my video needs. Things like this intro, the ending video, game trailers, etc.

We haven’t finalized anything yet, but I believe he’ll be on board soon to help out with these videos. That would be a big win for me not only because it’s going to make all of my marketing materials 10x more awesome, but it’s going to save me a ton of time. I also think it’s going to be possible to directly embed video into the game and not worry about manually coding all of the video animations. In theory that should make the loading time a lot shorter and improve quality.

#### Battlefield Animations

I plan on adding movement to the battlefield scenes where possible and I set up the code to handle how that’s going to work. Things like moving water, floating rocks, and pulsing magic will help the world feel a little more alive. I’ll need a little help from the illustrator or the first two items, but here’s a look at some of the land’s magic pulsing.

<div class="inlineimg">
  {{< gfycat data_id="ElegantEmbarrassedGardensnake" >}}
</div>

<div class="inlineimg">
  {{< gfycat data_id="BewitchedTautAlleycat" >}}
</div>

#### Scene Management

I wrote about scene management a little bit last time and how scene transitions can be a little slow without multi threading. I’ve re-written each game scene to correctly run off of Corona’s composer library, and while that helps with code organization, it doesn’t really help with making transitions any faster. In order to do that there are a few things that I’ve been experimenting with:

**Efficient Animations**
  
I’ve been working on the world map recently and when I load the scene without any animations, the texture memory usage comes in at about 20MB. That number jumps to about 75MB when the animations are loaded. That’s just way too much memory and the main reason why is because I have 4 high quality 90 frame water animations going on. Here’s a look at the world map with waterfalls, rapids, and waves.

<div class="inlineimg">
  {{< gfycat data_id="ClassicDependableChanticleer" >}}
</div>

The first thing I’m going to play around with is using fewer frames. Each waterfall cycle is 2-3 seconds, so I should be able to cut the number of frames needed in half. The other thing I’m going to try is shrinking the size of each frame and then scaling it up to the appropriate size on the world map. I’m usually hesitant to scale images up, but I think it might work out with the water animations just because there is generally more flexibly with how water works.

One thing to note is that I have a few battle maps with water, and there is absolutely no way I’ll be able to animate that water with a high number of frames. I’m probably going to have to resort to a 3 frame cycle animation, some masking tricks, or a combo of both.

**Loading More at Once**
  
While play testing the game, I noticed that I’d rather wait 20 seconds one time than 10 seconds two times. There are also times when waiting feels natural and times when waiting feels like it interrupts the flow of the game. What I’ve been trying to do is load more assets at opportunistic times to make the game feel smoother and to have fewer, but longer breaks in the action.

**Keeping Scenes in Memory**
  
Some scenes, like the world map and character management scenes, are re-used throughout the game. Other scenes, like battle scenes, are only played one time. The time spent transitioning between scenes can be dramatically lowered by keeping reusable scenes in memory, so I’d like to keep those scenes in memory as much as possible. The key here is to reduce the memory allocated to the re-usable scenes, because everything takes a hit if they’re too memory intensive. Right now the world map takes up a lot of memory, so I have some adjustments to make.

**Keeping Textures in Memory**
  
Character sprite animations are the game’s biggest memory hogs, so any efficiencies I can find with those animations will have big impacts on overall memory management. Some characters are commonly seen throughout the game, so it probably makes sense to keep them, or at least their sprite textures, in memory. My initial test show that this can work out, but I’ll need to program something that knows when to dynamically load and un-load character sprites as needed. I don’t want to keep a character in memory if they won’t be around for a while, and I’ll also need a way to un-load any non-essential assets if I’m nearing max memory usage limits.

#### Next Time

I can feel a little bit of burnout coming on and that’s going to work out nicely considering that I’m taking a few days off in a couple of weeks. Right now I&#8217;m trying to complete as many tedious tasks as possible so that I have something clean and fun to work on when I return.

 [1]: http://www.brendonwilliams.com
 [2]: https://youtu.be/mGkNHG64O-8
 [3]: http://secretpowers.com
 [4]: http://secretpowers.com/portfolio/secret-powers-2014-showreel/