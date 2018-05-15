---
title: We Have a Story
author: Ryan
type: post
date: 2015-02-16T13:46:52+00:00
url: /sirryan/we-have-a-story/
featured_image: /wp-content/uploads/2015/02/Trebuchet-Drive-Front_01-e1424094538475.png
number:
  - 17
keyevent:
  - First pass of story complete.
  - Formations of all sizes.
  - Third contract with animator.
categories:
  - sirryan
tags:
  - status

---
Story, story, story. 8 of the 10 days over the past two weeks have been spent preparing story assets, implementing them into the game engine, revising dialogue, and getting the cutscenes to work. It has been extremely tedious, but it feels great to have finished a first pass.
<!--more-->

In between story work, I was able to coordinate with Scott (illustrator) over the next drawing, start a third contract with Liron (animator), and <a href="http://battleofbrothers.com/sirryan/300-for-script-editor" target="_blank">start a contract with Mike Waterston for script editing</a>. See video for details.

<div class="inlineimg">
  [youtube=https://www.youtube.com/watch?v=OavYEl_Lfu4&list=PLU-00W724Flc4vr1yH95AL_NcLykWi9P7&w=740&theme=light]
</div>

#### Story

Story is a vague term. In order to implement the story, here is what had to happen:

  * Different scene objects (decision, level, story, travel)
  * <a href="http://battleofbrothers.com/sirryan/saving-game-data-in-spritekit" target="_blank">Save game</a>
  * <a href="http://battleofbrothers.com/sirryan/create-skippable-cutscenes-in-spritekit-with-timing-functions" target="_blank">Skippable cutscenes</a>
  * Contract with Mike
  * Progress between levels (footsteps)
  * Animate the world map
  * Revise script
  * Implement art (months of Scott&#8217;s work)
  * &#8220;Scene Switchboard&#8221; to handle navigation between game scenes.

<div class="inlineimg">
  {{< gfycat data_id="FineFarBichonfrise" >}}
</div>

For example, what happens if someone finishes the first level, but turns their iPad off before the &nbsp;cutscene finishes immediately after the level? I tried to handle as many edge cases like this as I could.

Next steps&nbsp;for this are to continue to revise the script, and to try to really polish each scene. I&#8217;ll do whatever cheap tricks I can to bring animation and life to each scene.

#### Camp

Another item we started work on this week is the camp screen. The camp screen is where the player can manage their army, buy heroes, upgrade their abilities, etc. Here is an example of the merchant.

<div style="margin-left: 130px !important">
  <blockquote class="twitter-tweet" width="550">
    <p>
      A colorful merchant (designed by <a href="https://twitter.com/Appylon">@appylon</a>, of course). Want to buy something? <a href="https://twitter.com/hashtag/screenshotsaturday?src=hash">#screenshotsaturday</a> <a href="https://twitter.com/hashtag/gameart?src=hash">#gameart</a> <a href="https://twitter.com/themeatly">@themeatly</a> <a href="http://t.co/pGvUDWKb25">pic.twitter.com/pGvUDWKb25</a>
    </p>
    
    <p>
      &mdash; Ryan Campbell (@veeneck) <a href="https://twitter.com/veeneck/status/564072270956855298">February 7, 2015</a>
    </p>
  </blockquote>
  
  <p>
    </div> 
    
    <p>
      This is quite a large scene, so it was not completely finished in time for this update. Once the scene is done, the individual menus will have to be designed. For example, if you click on the merchant cart above, what does the screen look like that it takes you to?
    </p>
    
    <h4>
      Formations and AI
    </h4>
    
    <p>
      With my remaining time, I tried to implement a few features for the battle scenes. First up, formations have been rewritten to support different layouts. The columns, max units, and spacing between units are all variables, and the code determines the proper layout. Prior to this, everything was hard coded.
    </p>
    
    <div style="margin-left: 130px !important">
      <blockquote class="twitter-tweet" width="550">
        <p>
          Formations can now have different shapes, sizes, and spacing. Also, hello to trebuchet. <a href="https://twitter.com/hashtag/screenshotsaturday?src=hash">#screenshotsaturday</a> <a href="https://twitter.com/hashtag/indiedev?src=hash">#indiedev</a> <a href="http://t.co/rva4TLerEJ">pic.twitter.com/rva4TLerEJ</a>
        </p>
        
        <p>
          &mdash; Ryan Campbell (@veeneck) <a href="https://twitter.com/veeneck/status/566658237983117312">February 14, 2015</a>
        </p>
      </blockquote>
      
      <p>
        </div> 
        
        <p>
          After that, I began work on enemy AI. My goal is to be able to finish a battle in its most basic form. So, that&#8217;s what I&#8217;ll continue working on in between cutscene work over the upcoming two weeks. Things that have to happen:
        </p>
        
        <ul>
          <li>
            Enemy AI is smart enough to attack.
          </li>
          <li>
            Game sends enemies in waves.
          </li>
          <li>
            After last wave, and last enemy killed, game knows to tell the player they won or lost.
          </li>
          <li>
            Integrate that with the cutscene project.
          </li>
        </ul>