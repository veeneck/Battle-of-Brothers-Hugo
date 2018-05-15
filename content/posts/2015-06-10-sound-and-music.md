---
title: Sound and Music
author: chris
type: post
date: 2015-06-10T13:19:19+00:00
url: /2015/06/10/sound-and-music/
featured_image: /wp-content/uploads/2015/06/Screen-Shot-2015-06-09-at-11.55.26-AM-2.png
number:
  - 26
keyevent:
  - Added first sound effects.
  - Level 1 Music Take 1
categories:
  - sirchris
tags:
  - status

---
In the last update I demoed the [latest version of the game’s battle layer][1] and I&#8217;m comfortable with how that part of the game is progressing. There are still bugs to squish and polish to add, but now that I’m confident in the game’s art, animation, and general flow, it’s time to give audio some love. I’ve contracted the pros to help me out in this area, and with their help the game has gotten some fantastic ear candy. Here’s a look at the latest build with the new audio enhancements.
<!--more-->

<div class="inlineimg">
  [youtube=https://www.youtube.com/watch?v=j4beFuH_3Ho&w=740&theme=light]
</div>

#### Music

[Brendon Williams][2] already [created a great piece for the game&#8217;s intro][3] and this was his first attempt at battle music.

This piece is going to be used in the 4 battles that take place in the “sky world”, which is where the player begins the game. We’re going to try changing a few things, like how the song begins and ends, but I’m very pleased with his first attempt.

I’ve asked Brendon to consider a few things while making the battle music including:

  * Creating unique sounds for all of the 5 different &#8220;lands&#8221;.
  * Making the music unique and interesting but not overpowering at the same time. Battles could take upwards of 15 minutes and the same songs are used in multiple battles, so the challenge is to create something new and exciting while not annoying when looped for 15 minutes.
  * Adding the ability to increase the song’s intensity. When a battle is nearing its final phases I’d like the intensity to grow. For example, if there is one enemy or hero left, the song should sound more dramatic.
  * Mesh with the game’s future music. Each of the 5 lands will have their own unique sound, but the world map’s music will be a mesh of those unique sounds into one coherent song. Brendon’s challenge is to think ahead and create those unique yet complementary sounds.

#### Sound

[Wesley Slover][4] is the guy in charge of making the game sound amazing and I think he’s off to a great start. Wes started experimenting with sound effects after receiving a demo of the first battle begin played to Brendon&#8217;s music. Wes first created this demo with a couple different types off effects including Japanese RPG/Arcade sounds and a metal click/lever/switch types of sounds.

<div class="inlineimg">
  [youtube=https://www.youtube.com/watch?v=Hw10MA0CNBg&w=740&theme=light]
</div>

I really like the sound of metal tech control board sounds, so he remade the final demo using those types of sounds. There are only a handful of sounds in the game so far, but it’s amazing how much a difference they make. I love the fact that Wes didn’t just go straight for the generic medieval, realistic type of sound that I would have gone for had I been in charge. I think what he’s done has already added a ton of personality to the game and I can’t wait to see what he comes up with down the road.

#### Melee Combat

In addition to sound, music, and squashing a lot of bugs, I spent a good amount adding flexibility to the combat layer. If you take a look at this attack sequence, you’ll notice that the sound effects, text effects, damage effects, and flinch all happen at the (relatively) appropriate times.

<div class="inlineimg">
  {{< gfycat data_id="GroundedCloudyGar" >}}
</div>

Those actions all used to be hard-coded, but that&#8217;s not scalable when the game has a variety of unique melee attacks requiring custom sequences and timing. For example, here’s a look at the knight on the receiving end of a double attack.

<div class="inlineimg">
  {{< gfycat data_id="GoldenSilverHusky" >}}
</div>

I can tweak the timing of all the attack variables in JSON, which saves me a ton of time making the melee sequences look and sound right.

#### Ranged Combat

Wizards don’t swing words, so I also had to work on how ranged combat works. Here’s a look at a couple of wizards going at it.

<div class="inlineimg">
  {{< gfycat data_id="FeistyRawAlpineroadguidetigerbeetle" >}}
</div>

There are a three major parts to the ranged combat.

  * The first is the beginning phase, which is where the projectile is drawn to the screen. In this example, that is where the fireball is growing in the wizards hand. The beginning phase may be slow for a complicated and slow building spell or lightning fast for an archer’s triple attack.
  * The second phase is when the projectile is released and this phase gave me a little bit of trouble. Speed is one variable which I had to account for, and that was pretty easy. I just need to specify how many pixels per second the projectile travels and everything just works.
  
      
    What was tricky was handling the projectile’s z-index. I don’t want to get too far into that problem in this post, but basically the problem is that I can’t handle a projectile’s z-index in the same way I handle a fixed object’s z-index. The projectile has to be offset due to varying release and impact points and I had to dust off my old math skills to get that working. I’ll try to write-up a more detailed tutorial once I get all the kinks out.
  * The last phase is the projectile’s impact phase. Right now I just have the projectile disappear on impact, but this is where I could have the projectile explode, hit multiple characters, trigger custom events, etc.

Like the melee combat system, I can now customize the ranged variables in JSON.

#### Next Time

Besides a few nagging bugs, I’m pretty happy with this initial version of the combat layer. I’ll eventually add a lot of flavor through custom attacks and more complicated AI, but this will probably be about it for my goal of creating the first 4 levels. Up next is revisiting the world map and adding some of the other game components like hero management, item management, and game settings.

 [1]: http://battleofbrothers.com/sirchris/the-battlefield-ui
 [2]: http://www.brendonwilliams.com
 [3]: http://battleofbrothers.com/sirchris/music-memory
 [4]: http://www.sonosanctus.com