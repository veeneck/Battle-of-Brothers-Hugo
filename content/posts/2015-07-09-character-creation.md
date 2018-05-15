---
title: Character Creation
author: chris
type: post
date: 2015-07-09T19:08:47+00:00
url: /sirchris/character-creation/
featured_image: /wp-content/uploads/2015/07/Screen-Shot-2015-07-09-at-2.43.39-PM-2.png
keyevent:
  - First Crack at Character Creation
number:
  - 27
categories:
  - sirchris
tags:
  - status

---
After working on the intro, world map, and combat layer, it was time to work on the character selection screen. My short-term goal is to have 4 playable levels and the only major missing piece is the functionality to manage your heroes. Everything is still in a bit of a rough state, but here’s a look at what I have so far.
<!--more-->

<div class="inlineimg">
  [youtube=https://www.youtube.com/watch?v=jJ3nX9PMOiE&w=740&theme=light]
</div>

There&#8217;s still a lot to be done in terms of making the interface usable to an actual player, but there were four main areas I addressed during this first attempt:

**View Available & Unavailable Characters**

You can see that there are two characters shown in color and 8 characters shown as silhouettes. The colored characters have been unlocked and are available to play and the silhouettes are yet to be unlocked. I’m not exactly sure how I’m going to price the game so it’s possible some of the unlocked characters are purchasable and it’s possible that they’re all unlocked by progressing through the game.

**About**
  
The about screen just has some basic info for now, but in the future it may handle things like setting a squad leader, adding and removing characters from a group, purchasing characters etc.

**Assign Base/Skill Points**
  
I plan on making a fairly traditional RPG where you can customize a character’s base (i.e. strength, stamina, etc.) and attack attributes. I don’t know exactly what the stats will be but

**Inventory**
  
Like all good RPG’s, there will be weapons, necklaces, magic items, etc. that a character can equip to increase their stats. This part isn’t just finished yet, but it’s almost to a playable state.

#### Behind the Scenes

All in all this doesn’t looks like too much but looks can be deceiving. Here are a few of the things that had to be re-worked behind the scenes for any curious devs out there.

**Saved Games**
  
Right now, I’m using JSON to store game data and I previously had JSON files for each character and a JSON file containing basic game information &#8211; like what level the player is at. Now that characters can be customized and there are multiple games/states, I have to customize things that different characters with different stats are associated with different games.

**Base Character Stats**
  
When a new game is made a new character file has to be created based off of a base character template for that class.

**Character Creation**
  
Since I had to re-write how the file system works, the character creation scripts that run at the beginning of each level had to be re-worked. I also had to add some calculations to adjust a character’s stats based on if they have any stat altering factors, like magical items.

**Multi-Language**
  
I don’t know if this will be an english only game, but just in case I added multi language support just in case it isn’t. This isn’t a big technical problem, but it is pretty tedious.

#### Conclusion

I’m getting pretty excited where things are at right now because I’m so so close to being able to interact with a rough version of the game. So much of this process has been grunt work, and I’m sure there’s still a lot of that a head, but I feel I’m about to turn a corner.