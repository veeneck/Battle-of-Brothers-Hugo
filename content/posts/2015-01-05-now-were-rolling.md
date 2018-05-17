---
title: Now We’re Rolling
author: Ryan
type: post
date: 2015-01-05T13:43:10+00:00
url: /sirryan/now-were-rolling/
featured_image: /wp-content/uploads/2014/12/B4wQf2AIIAA8hjZ.png-large.png
number:
  - 14
keyevent:
  - 90 Units at 50% CPU
  - Basics attacks
  - Story fully illustrated
  - Started world map
categories:
  - sirryan
tags:
  - status

---
Things are moving along much better now. I wouldn&#8217;t say moving quickly just yet, but they&#8217;re at least moving. I&#8217;ve overcome a lot of technical hurdles and learning curves in the past 3 months. The latest of those was how to support 100-150 units on the screen at once. Serious progress has been made in that department. And, as always, I&#8217;ve received amazing illustrations and animations from Scott and Liron. Lastly, I&#8217;ve dabbled a bit in icon making.
<!--more-->

Let&#8217;s jump to the video for more.

{{< youtube _t7P1VBBOYk >}}

#### Supporting an Army

How many units can I fit on the screen at once? I hate to optimize code this early in the process, but the answer to that determines a lot about how my game will flow. After a week of focusing on this, <a href="http://battleofbrothers.com/sirryan/joy-of-debugging-command-swiftc-failed-with-exit-code-1" target="_blank">optimizing the compiler</a>, <a href="https://www.youtube.com/watch?v=vdMYn8GShkg" target="_blank">testing different approaches</a>, and going through the code piece by piece, I can support ~90 units at 50% CPU.

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1485" src="/wp-content/uploads/2014/12/Screen-Shot-2014-12-23-at-1.53.30-PM.png" alt="Screen Shot 2014-12-23 at 1.53.30 PM" width="625" height="469" />
</div>

The good news is that I still have plenty of reasonable ideas to increase performance. For the first time, I&#8217;m confident I can support 125-150 units at under 50% CPU. That would allow for all of the game design ideas in my head, and plenty of additional CPU for art, sound, effects, etc.

It would be too much to explain everything I&#8217;ve tried in this post, but I hope to go over it later in a blog post. It&#8217;s just important to note 5-7 full work days were spent just tweaking code.

#### Icons

I&#8217;m learning that I have to develop some basic art skills in order to get this game to work out with a reasonable budget. First example: Icons. My game may have 50+ icons. I could have Scott think on, design, iterate and finalize all of them. I would love to do that, but it would become to expensive. So, instead, my approach for icons and the HUD in general is to do as much of a first take as I can. If I can think of every icon and give it a starting point, then hopefully Scott can make minor changes / filters to bring them in line with his style.

Anyway, that said, here is my first take on icons. Love the progress I have made, but they aren&#8217;t quite there yet. Need them to look more like they belong with the maps / characters.

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1474" src="/wp-content/uploads/2014/12/B4hDHA2IUAAABya.png-large.png" alt="B4hDHA2IUAAABya.png-large" width="625" height="876"  />
</div>

#### World Map

Designing the world map took more time than I thought. The story illustrations and level illustrations have to be considered so that it makes logical sense. If the story has a river in the background, the world map should show that. Obviously, it doesn&#8217;t have to be 100% exact, but some consistency is desired. On that same note, the path that the character takes throughout the map should make sense with the story. For example, you would&#8217;t cross 75% of the map for resources if that same resource could be found much closer. So, I thought through that, and came up with a rough illustration for Scott. I have a separate blog post in mind for this process, so for now, I&#8217;m just going to leave a teaser.

<div class="inlineimg">
  <img class="alignnone size-large wp-image-1479" src="/wp-content/uploads/2014/12/WorldMap_lineart_02.jpg" alt="WorldMap_lineart_02" width="625" height="420"  />
</div>

#### What&#8217;s Left and What&#8217;s Next

Rough break down:

  * 6/15 levels
  * 21/26 characters
  * 14/15 cutscenes
  * 0.7 / 1 world map
  * 0 / 1 start screen
  * 1 / 1 camp screen
  * 0 / 1 interface
  * 0 / 1 polish like rivers, birds, flags, etc
  * 0 / 1 marketing materials

There will be more screens in the end, but that doesn&#8217;t matter for now. The main focus is the levels, characters, cutscenes and world maps. I&#8217;m excited that the story mode / cutscenes are nearly complete. The camp screen and credits screen are also finished, but I&#8217;ll reveal those later.

Next week, I plan to focus more on getting level 1 in game working. Units should die, and there should be a game over state. After that, enemy AI, followed by enemy waves.