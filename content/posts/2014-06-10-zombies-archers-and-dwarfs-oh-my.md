---
title: Zombies, Archers, and Dwarfs! Oh My!
author: chris
type: post
date: 2014-06-10T16:19:33+00:00
url: /sirchris/zombies-archers-and-dwarfs-oh-my/
keyevent:
  - New Character Animations
  - Added Sound Effects
  - Basic Prototype is Playable
number:
  - 6
categories:
  - sirchris
tags:
  - status

---
I&#8217;ve added a lot of pretty cool changes to my prototype in the last two weeks, including new characters, attack animations, directional movement, death animations, and sound effects. The game is still a very rough prototype, but as you can see in the video below, I&#8217;m now able to actually play a complete level from start to finish.
<!--more-->

https://www.youtube.com/watch?v=dX6BCnXXZ7U

Figuring out what to develop has been pretty easy up to this point because I&#8217;ve been able to continuously add code and core functionality that will absolutely be part of my finished game. The artwork will change and additional functionality will be added, but the these new core features should be flexible enough work for any type of turn based game I eventually develop.

**New Zombie, Mage, Archer & Dwarf Sprites**
  
The old Knight, Zealot and Ogre images weren&#8217;t working out for a number of reasons, so I went to [spritedatabase.net][1] for some new images. Once I found some acceptable art, I cut it up at <http://imagesplitter.net> and then made sprite sheets using [TexturePacker][2]. These characters can&#8217;t be used for commercial works, and they&#8217;ll all have to be thrown out, but I need functional artwork to develop a prototype.

**Direction Logic**
  
My game&#8217;s characters are now able to move in four directions, so I added the logic to have them face the appropriate direction when moving, attacking, and being attacked. This was easy for the melee characters, but trickier for the ranged characters who don&#8217;t always attack at 90 degree angles.

**Death Animations**
  
I didn&#8217;t really like the death animations that came with my character images, so I went rogue on this one and made it so that characters fade up and away then they die. The most important thing is that I now have isolated sections in my code to handle death.

**Game, Movement, Attack, Hit, and Death Sound Effects**
  
Like the death animations, I have isolated sections in my code that now load and play sounds at the appropriate times. The free sound effects I&#8217;m using can be found at <opengameart.org> and <freesound.org>.

 **Start and End Screens**
  
Placeholder code for the start of a scene and the end of the scene, including logic to know whether a game was won or lost.

**Subtle Effects**
  
I added some subtle effects, like the highlight squares fading in and out, just to make the demo look a little more polished. These may or not be part of the final game, and the code may not be reusable, but sometimes it&#8217;s important do just do things that make you happy.

#### Two Steps Forward

I feel that I took two steps forward in the last two weeks, so that means it&#8217;s probably time for me to take a step back. I recently took a look at how my game works across multiple devices, and what looks great on an iPad looks not so great on pretty much every other device. I think it&#8217;s time to make my game work on multiple devices before I add more assets and code to the project.

 [1]: http://spritedatabase.net
 [2]: http://www.codeandweb.com/texturepacker