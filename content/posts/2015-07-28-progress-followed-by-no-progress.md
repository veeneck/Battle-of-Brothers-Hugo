---
title: Progress Followed By No Progress
author: Ryan
type: post
date: 2015-07-28T17:05:55+00:00
url: /2015/07/28/progress-followed-by-no-progress/
featured_image: /wp-content/uploads/2015/07/Screen-Shot-2015-07-27-at-2.11.42-PM-e1438020988234-2.png
number:
  - 23
  - 23
keyevent:
  - Finished soundtrack.
  - Fundamental menu controls.
  - Pathfinding in iOS9
  - Finished soundtrack.
  - Fundamental menu controls.
  - Pathfinding in iOS9
categories:
  - sirryan
tags:
  - status

---
It&#8217;s been nearly two months since my last status update. To quickly sum up those two months, June was extremely productive while July was almost a waste. June consisted of implementing reusable menus, music, sound effects, button effects, volume controls, unit management and more. Basically, a lot of foundation type elements needed for a game. Unfortunately, I started playing with iOS9 in July, which happened to be both a necessity and a time sink. Finally, just last Friday, I finished the contract with the composer, so all of the music for the game has been completed.

<!--more-->

<div class="inlineimg">
  [youtube=https://www.youtube.com/watch?v=z44JcViQG9U&w=740&theme=light]
</div>

#### Fundamental Menu Controls

Sorry for the vague subheading, but it&#8217;s the best way I could describe the many small, mundane tasks that were completed. This list may be more helpful.

  * Shiny new UI. Not final, but good enough for a Beta.
  * Up to 3 saves files, that can be resumed and deleted from the main menu.
  * Redesign menus, and refactor slide out menus to reusable code.
  * Music transitions throughout.
  * Level selection and ability to replay the cutscene for a level.
  * Volume control for music and sound from settings.
  * Unit management in Camp screen: purchase, heal, and reform units.

<div class="inlineimg">
  [gfycat data_id=&#8221;PastSmartHaddock&#8221; data_autoplay=true data_controls=false]
</div>

That&#8217;s the gist of the changes. Behind the scenes, there were also plenty of refactors. For example, all sound code had to be touched to get volume to work correctly. But most importantly, any new screens, buttons or menus now pull from reusable code.

#### iOS9, Pathfinding and Refactoring

I&#8217;ve known all along that I would have to take a 3 month chunk to work on pathfinding at some point. I&#8217;ve dreaded it, but it looks like now is the time. With the release of iOS9, pathfinding agents and dynamic navmeshes will be available to SpriteKit via GameplayKit. The great news here is that tasks like static pathfinding, ECS implementation, improved state machine and other goodies is much easier. Since all of these game development essentials are supported by Apple, they will most likely receive performance optimizations as well.

<div class="inlineimg">
  [gfycat data_id=&#8221;BackFluffyBrontosaurus&#8221; data_autoplay=true data_controls=false]
</div>

So, I&#8217;m about 3 weeks into working with iOS9, and beta software always comes with complications. I&#8217;ve worked through most of them and have a proof of concept up and running. There are still plenty of obstacles to solve though.

  * Determine when a wheeling formation would hit a wall during the wheel, and instead just flip direction.
  * Curving a unit around corners. Current implementation has them walk to waypoint and turn.
  * Performance is still a big issue with physics and separation turned on for 150-200 units.
  * If one unit gets stuck on a physics object, give it individual pathfinding abilities.
  * Dynamic movement. All sorts of challenges avoiding other units and moving obstacles while balancing performance.

That&#8217;s just a sampling of what I&#8217;m working on. Ideally, I will have a decently solid pathfinding implementation by the end of August. It&#8217;s the last key piece before I will feel like I have all of the tech worked out, and then can just implement game components at a much quicker pace.

#### Music

The soundtrack is complete! We&#8217;re working with about 30 minutes of custom music made possible by <a href="http://www.manfredoniamusic.com" target="_blank">Tony Manfredonia</a>. He has been professional, responsive, and open to iteration. I highly recommend him to anyone looking for music.

A note to anyone new to working on a soundtrack for their game. Even though I didn&#8217;t make the music, it still took quite a bit of my time. Particularly, the story cutscenes. Temporary voice acting had to be created to get a feel for timing. The story video had to be adjusted with that voice. Finally, as each scene was completed by the composer, the music had to be tested and iterated upon.