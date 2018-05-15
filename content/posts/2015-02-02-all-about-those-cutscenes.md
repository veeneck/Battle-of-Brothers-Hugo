---
title: All About Those Cutscenes
author: Ryan
type: post
date: 2015-02-02T13:41:07+00:00
url: /sirryan/all-about-those-cutscenes/
featured_image: /wp-content/uploads/2015/01/Screen-Shot-2015-01-30-at-1.26.23-PM.png
number:
  - 16
keyevent:
  - Started melee combat.
  - Hired a composer.
  - Skippable cutscene engine.
  - Scene management.
categories:
  - sirryan
tags:
  - status

---
I&#8217;ve done quite a lot over the past two weeks. Work has started on melee combat. I&#8217;ve hired a composer! But most of all, I&#8217;ve been consumed with cutscenes. When I started this process, I didn&#8217;t realize that the decision to add a story to my game would end up costing me ~30% of my budget and an equal amount of programming time. Now that I&#8217;m actually implementing the story, I&#8217;m starting to understand all of the implications.
<!--more-->

As always, I cover all of this in the video update, so follow along there if you prefer.

{{< youtube 4IzAr7jXEDs >}}

Let&#8217;s break down each of the tasks I took on over the past two weeks.

#### Melee Combat

I left off last update working on ranged combat, so I carried that into the first week by working on melee combat. The good news is that the code to process combat works just fine, so no refactoring was needed. The bad news is that combat doesn&#8217;t look perfect just yet. See for yourself.

<div class="inlineimg">
  {{< gfycat data_id="MildNecessaryGoitered" >}}
</div>

I have to play around with making combat look more natural. For example, have soldiers feet moved when they are pushed. Or, when processing allows, have a soldier walk around someone rather than through them. Finally, if it&#8217;s 4 on 1, have the 4 properly surround the target. Right now, they just walk in a straight line directly to the closest target.

I would have continued working on this, but I received an unexpected email.

#### Hired a Composer

I&#8217;ve received a few emails about music needs for my game, and I&#8217;ve told everyone that I&#8217;m not ready to think about that yet. The other day, I was contacted by <a href="https://soundcloud.com/tony-manfredonia" target="_blank">Tony Manfredonia</a> and felt the urge to do a trial with him. Something about the tone of his email showed me he cared about his work, and was genuinely interested in my project.

So, I ran through a trial with him (samples in the video above), and everything checked out. At first, he gave me a sample title song. Then, followed up with a battle song. I plan to write more about this in depth, but we went through 8 revisions on the battle song. He was cool with the entire process, and open to feedback. That&#8217;s the kind of person I like to work with, so I&#8217;m excited to start with him in May.

#### Cutscenes

Because a composer needs a story to compose, I immediately switched gears to cutscenes. As far as timing goes, I should be finished with them by the end of February, so that they are ready for voice overs. Then, with voice added, send them off to the composer.

Cutscenes are hard. Here&#8217;s why:

  * Dialogue is hard. I keep iterating to try to stay away from the cheese.
  * Timing is hard without sound and music. Sometimes, a pause is just too long. Other times, with the right music, it is the perfect touch.
  * They have to be skippable / skimmable, which requires a lot of flexibility in the code.
  * Effects and animations are time consuming, and will stand out if they aren&#8217;t polished enough.
  * Camera work / placement is a skill in itself. Basically, I find myself having to research basic director skills.

Given all of that, I&#8217;m both excited and nervous about the end product. But, I&#8217;m committed. For now, I&#8217;ve got a <a href="http://battleofbrothers.com/sirryan/create-skippable-cutscenes-in-spritekit-with-timing-functions" target="_blank">basic, skippable engine in place</a> and roughly 1/4 of the content in there. I&#8217;ll keep working towards a finished product over the next month.

<div class="inlineimg">
  {{< gfycat data_id="WearyEverlastingBee" >}}
</div>

#### Scene Management

While working on cutscenes, I received quite the education in scene management. There are both technical and logical challenges.

On the technical side, scenes have to transition into one another gracefully. This is easier said than done when working with large assets. So, to implement transitions, I have had to start a preloading system. Each scene has a tree of next scenes, and based on the state of the game will being a background thread that preloads the upcoming scene. This system allows for graceful transitions like this:

<div class="inlineimg">
  {{< gfycat data_id="EntireImaginativeIndianrockpython" >}}
</div>

On the logic side, there are a bunch of edge cases with players quitting the game or turning off their device. Some scenes, like story dialogue, can be marked as complete if they get shown. Other scenes, like player decisions, must have a decision made in order to not be shown again. That decision must be stored somewhere. I&#8217;ve started the process of implementing that. Another example would be the world map. If revealing a new level, zoom in and show it. Otherwise, show the entire map in its normal state.

<div class="inlineimg">
  {{< gfycat data_id="WhirlwindMeekLacewing" >}}
</div>

<hr class="dots" />

&nbsp;

Next week, I plan to really flesh out the two scene management concepts I talked about above. Once that foundation is solid, I can go on an implement the next 1/4 or so of the story.