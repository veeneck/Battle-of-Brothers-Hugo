---
title: The Beginning of a Game
author: chris
type: post
date: 2014-05-12T18:55:50+00:00
url: /2014/05/12/the-beginning-of-a-game/
featured_image: /wp-content/uploads/2014/05/Update-4-1.png
keyevent:
  - AI Foundation Written
  - Archer and Mage Classes Added
  - Initial Combat System Developed
number:
  - 4
categories:
  - sirchris
tags:
  - status

---
I&#8217;m a little over a month into my game now and I feel like I finally have something that resembles what will one day be a playable game. When I left off last time, I was hoping to add some AI to the game, and I&#8217;m happy to report that the AI system wasn&#8217;t as hard as I had originally feared. In the last two weeks, I was able to add archer and mage characters to the game and also give the enemy characters some intelligence.

To see where I&#8217;m out, check out the following video.
<!--more-->

https://www.youtube.com/watch?v=7GqLByw3_2A&feature=youtu.be

Here you can see that the player is able to control both melee and ranged classes and the computer can also play both ranged and melee classes. I was lucky to find an article over at Gamasutra on how to [design AI for turn based games][1], and it was exactly what I needed.

If you&#8217;re curious about how the AI system works, here is a screenshot to illustrate what happens when it is an enemy player&#8217;s turn.

<div class="inlineimg">
  <p>
    <img class="alignnone size-full wp-image-489" src="http://localhost:8888/wp-content/uploads/2014/05/Scoring-e1399920168875-1.png" alt="Scoring" width="600" height="416" srcset="http://localhost:8888/wp-content/uploads/2014/05/Scoring-e1399920168875-1.png 600w, http://localhost:8888/wp-content/uploads/2014/05/Scoring-e1399920168875-1-300x208.png 300w" sizes="(max-width: 600px) 100vw, 600px" /></div> 
    
    <p>
      Here you can see that there are numbers above each of the good guy&#8217;s heads. What happens is that at the beginning of an NPC&#8217;s turn, a calculation runs and generate scores for each opposing character. The NPC will perform the action associated with the highest score returned. In the screenshot above, the mage ran scores against the three PC characters and attacked the archer, who had the highest score.
    </p>
    
    <p>
      The scoring system is pretty rudimentary right now, only caring about things like character type, distance, and weakness to attack type. The system is pretty flexible, though, and I look forward to making the NPC&#8217;s smarter as my game matures. The core mechanics of my combat system depend on the scoring framework that I developed, so it&#8217;s a big win to get this done.
    </p>
    
    <h4>
      Next 2 weeks
    </h4>
    
    <p>
      The first thing I need to focus on is polishing some of the little things that I&#8217;ve skipped over. Things like adding obstacles to the game, cleaning up code (again), fixing animations, and other housekeeping items.
    </p>
    
    <p>
      After that, I need to start designing the game that I ultimately want to produce. 6 characters fighting on a battlefield is a great start, but it&#8217;s not a game anybody wants to play. I feel I have a good grasp on Corona and LUA, and I&#8217;m comfortable with the mechanics of game development, so now it&#8217;s time for me to work on a game worth playing.
    </p></div>

 [1]: http://www.gamasutra.com/view/feature/1535/designing_ai_algorithms_for_.php