---
title: And Then There was a Playable Game
author: Ryan
type: post
date: 2014-05-12T15:49:28+00:00
url: /sirryan/and-then-there-was-a-playable-game/
featured_image: /wp-content/uploads/2014/05/Screen-Shot-2014-05-12-at-11.49.52-AM-1.png
keyevent:
  - Behaviors for units.
  - pList driven spawn points.
  - Gold and health.
  - Understand easing.
number:
  - 4
categories:
  - sirryan
tags:
  - status

---
Don&#8217;t look now, but I think my Xcode project just turned into a playable game. That&#8217;s right, you heard me correctly. User input, gold and a game over state. I would almost say it&#8217;s time to wrap things up and call it a win for team Ryan.
<!--more-->

As you can see, I&#8217;ve come a long way since my <a href="http://battleofbrothers.com/sirryan/its-not-all-sunshine-and-rainbows" target="_blank">last status update</a>. I spent a lot of time trying to understand AI and state machines in previous weeks, and now I am able to see some of the rewards.

Let&#8217;s jump to the video to do this status update justice:

{{< youtube Dcb_2ysh5r8 >}}

Reaching this point also makes work easier to handle. I&#8217;m starting to feel like I know where things should go in my code, and am transitioning out of the super beginner phase in some regards. An example of this would be clearer separation of code responsibilities:

  * My Character class is responsible for modifying local variables or providing convenience methods to be used elsewhere.
  * My state machine deals specifically with behavior that a non programmer could understand. Just a collection of calls to readable helper functions exposed by the character or AI system. The code would read as &#8220;If this character is currently waiting, scan for an ideal target. If a target is found, switch to engage that target.&#8221;
  * The AI code handles the logic associated with &#8220;scanning for ideal target.&#8221; This includes looping over all targets in range, finding out which one is the biggest threat, and so on.

While I&#8217;m much happier with the code, there are still two catches that I&#8217;m not thrilled about. The entire combat system only works if two specific things occur:

  * When one character engages another, it must notify the target by calling an exposed method.
  * When one character disengages another, it must notify its target.

The reason for this coupling is because each character keeps an array of targetsInRange and of unitsCurrentlyAttacking. The AI functions under the assumption that these two arrays are always accurate.

#### The Update Loop

Another huge break through for me was to finally embrace the update loop. For some reason, I thought I could get by using the built in tools provided by Sprite Kit. The best example to illustrate this is moving to engage a target. Pretend you want to characters to charge each other to attack. Originally, I tried to have each communicate to agree on meeting coordinates, and then call the moveTo:coords SKAction on each. This breaks easily. Imagine one character decides mid move that there is something more important to do. He will walk on while the other guy aimlessly walks to the meeting point.

By using the update loop, each character can walk towards another incrementally. That way, if one character changes directions or goes somewhere else, the other can adjust their course to still engage them properly. I resisted going this approach because I was hesitant to learn vectors, but it opened up significant opportunities. By running update methods on each character I can:

  * Heal, poison, freeze the character over time
  * Run AI on the character each frame
  * Update local data (i.e: current walking vector)
  * Easing

It turns out that it is much easier to make a coding decision based on accurate real time variables instead of trying to coordinate SKActions and completion blocks.

#### Other Progress

Accomplishments of note this week:

  * Gold, health, game over state
  * Working AI for skirmishers
  * Partially working AI for formations
  * Partially working AI for archers
  * Spawn points, read from a plist file, that allow you to select a unit type
  * Understand easing to add &#8220;juice&#8221; &#8212; notice health bar or unit menu coming into view.

#### Where I&#8217;m Headed

My primary focus is to implement basic functionality of each feature so I can understand the scope of the project. For example, small environmental effects like  squirrel running around requires plist data, code in the engine to load and display that data, and an environmental animated node that could possibly require basic state behavior. It sounds easy to say &#8220;let&#8217;s add a moving squirrel to the game,&#8221; and while it isn&#8217;t too difficult it is still worth going through the motions to understand how flexible your code needs to be. I still have at least 2-4 weeks of features I know I want, so I&#8217;ll just try to knock those out.

A secondary goal of mine is to incrementally refactor. I thought I would like to keep working quickly for a few more weeks and then do an entire rewrite. Instead, I&#8217;m going to challenge myself to refactor a class every other day and see if I can gradually improve the code base.