---
title: Learning Sprite Kit by Example
author: Ryan
type: post
date: 2014-05-15T14:13:33+00:00
url: /2014/05/15/learning-sprite-kit-by-example/
categories:
  - sirryan
tags:
  - code
  - learning

---
I hated school. I hate technical books. Generally, I feel like I can learn faster with the unstoppable trio of myself, Google and wonderful online communities. The trouble with game development is I don&#8217;t know what questions to ask. In web development, I can search how to make two elements sit next to each other and find what I&#8217;m looking for. In game development, I wouldn&#8217;t have looked for a finite state machine, much less double dispatch for physics. I may be late to the party compared to other developers, but I&#8217;m finding myself humbled by both books and open source projects that are extremely well crafted.
<!--more-->

I thought it would be interesting to look at the 5 week path I took to becoming comfortable enough with Sprite Kit to have the confidence to make a game.

#### Intro to Objective-C / Sprite Kit Project

CartoonSmart provides a wonderful <a href="http://www.cartoonsmartcode.com/sprite_kit_video_tutorials.php5" target="_blank">introduction to Sprite Kit</a>. Coming from web development, the main goal at this point was to understand the syntax of Objective-C and the terminology of Sprite Kit.

#### How to Make an RPG

Sticking with CartoonSmart, I decided to purchase their tutorial on <a href="http://www.cartoonsmartcode.com/sprite_kit_rpg_tutorials1.php5" target="_blank">Role Playing Games with Sprite Kit</a>. It helped that my game would be having role-playing elements, but this series also covered broad, important concepts like animation, attacking, movement, physics, and loading data through a property list.

#### Apple Adventure Game

About two thirds into the role-playing tutorial, I felt comfortable with the scope of that session. At this point, questions were popping into my mind. Should I preload assets? Should I use @property instead of an instance variable? I&#8217;ve only followed one teacher, but do they know everything or should I expand?

While I fully appreciate and recommend the CartoonSmart series, branching out and reading through the source of <a href="https://developer.apple.com/library/ios/documentation/GraphicsAnimation/Conceptual/CodeExplainedAdventure/AQuickTouroftheProject/AQuickTouroftheProject.html" target="_blank">Apple&#8217;s Adventure project</a> did reveal things like preloading, parallax, and more. It also allowed me to see how someone else might organize classes in their code.

#### Double Dispatch

At this point, I was happily working on my own project with both the CartoonSmart and Apple projects open. As I would implement a feature, I would reference both projects and decide on my preferred way of implementing it. Had I not referenced the Adventure Game, I would not have noticed Double Dispatch in the <a href="https://developer.apple.com/library/ios/documentation/GraphicsAnimation/Conceptual/SpriteKit_PG/Physics/Physics.html#//apple_ref/doc/uid/TP40013043-CH6-SW17" target="_blank">Apple Docs</a>. And if I had not heard the term Double Dispatch, I would not have stumbled across this amazing open source project showing perfect example code: <a href="https://github.com/kouky/iOS-SpriteKit-Pong" target="_blank">iOS-SpriteKit-Pong</a>. Finding this project was a huge turning point for me. Prior to this, I did not believe reading through a random project on Github would be an effective use of my time. My general impression was that each project would be too specific, or too bloated to be of use. Turns out I was wrong, and there are plenty of gems out there.

#### Timer Class

With my new-found love of open source projects, I was on the lookout for what I could study next. I was trying to implement a timer for my tower defense game, and stumbled across the wonderful [TCProgressTimer][1] by Tony Chamblee. His code was clean and easy to read. It took less than an hour to modify it for my code base and having a working timer. It also introduced me to SKCropNode, which I was&#8217;t familiar with at the time.

#### Web Resources

Two extremely useful resources that have made their way around the web are <a href="http://gameprogrammingpatterns.com" target="_blank">Game Programming Patterns</a> and <a href="http://gamemechanicexplorer.com" target="_blank">Game Mechanic Explorer</a>. Just reading through these two makes me feel smarter, and it opens up my vocabulary on what to look out for. It turns out I was using proper techniques semi-successfully but I didn&#8217;t know what they were called. After reading these resources, I began to recognize patterns and know how to search for more information on them.

#### Cocoapods

My growing confidence and love for other people&#8217;s code finally gave me the courage to install <a href="http://cocoapods.org" target="_blank">Cocoapods</a>. This immediately paid off as I found a state machine for Sprite Kit called <a href="https://github.com/blakewatters/TransitionKit" target="_blank">TransitionKit</a>. I am not using TransitionKit in my project, but I did read every line of it thoroughly. State machines are complicated, and this process took almost a dedicated week of coding. I came out with a better understanding of Objective-C, coding patterns and my own home grown state machine.

I also found <a href="https://github.com/warrenm/AHEasing" target="_blank">AHEasing</a> and <a href="https://github.com/buddingmonkey/SpriteKit-Easing" target="_blank">SpriteKit-Easing</a> through this same process. It is tempting to move forward and implement the next visual feature, but just taking the time to slowly read through projects like these really does accelerate the learning curve.

<hr class="dots" />

&nbsp;

As you can see, each great resource leads to another great resource. The amount of information and quality code out there is both inspiring and intimidating. I think there is a benefit in realizing how inadequate my code is for a task as long as I act on the realization. While it may be depressing to see 5 hours of work go down the drain, the payoff and education is worth it. If you&#8217;re in the same boat as me and learning Sprite Kit as a beginner, diving into other developer&#8217;s code is a hugely beneficial tool. My thanks to everyone in the open source community.

 [1]: http://tonychamblee.com/2013/11/18/tcprogresstimer-a-spritekit-progress-timer/