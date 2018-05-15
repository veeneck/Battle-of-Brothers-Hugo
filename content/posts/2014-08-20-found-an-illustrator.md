---
title: Found an Illustrator
author: chris
type: post
date: 2014-08-20T14:40:56+00:00
url: /sirchris/found-an-illustrator/
featured_image: /wp-content/uploads/2014/08/castle-1.jpg
number:
  - 10
keyevent:
  - Contracted an Illustrator
  - Started "Engagement" Game Mechanic
  - Tested Resolution Sizes
categories:
  - sirchris
tags:
  - status

---
When I left off last time, I was working with an illustrator to see if he could create the style of art I hope to use in my game. I&#8217;m happy to say that he exceeded my expectations and will be playing a large role in the game&#8217;s development. In addition to formally contracting the artist, I spent a little time playing with game mechanics and a lot of time preparing for the art that&#8217;s about to come rolling in.
<!--more-->

I wrote about what I was [looking for in an illustrator][1], and that person ended up being [Scott Pellico][2] ([@appylon][3]). Not only is Scott great artist, but he has innovative ideas, a great work ethic, experience in game design, and he&#8217;s a excellent communicator. I don&#8217;t want to show all of the art that I receive, because something needs to be saved for the eventual promotion of the game, but here&#8217;s another little teaser.

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/08/Jungle-1.jpg" alt="Jungle" width="425" height="412" class="alignnone size-full wp-image-983" srcset="http://localhost:8888/wp-content/uploads/2014/08/Jungle-1.jpg 850w, http://localhost:8888/wp-content/uploads/2014/08/Jungle-1-300x291.jpg 300w, http://localhost:8888/wp-content/uploads/2014/08/Jungle-1-768x745.jpg 768w" sizes="(max-width: 425px) 100vw, 425px" />
</div>

Scott is so good that Ryan and I are actually going to both be using him as our illustrator. Scott assured us that he has the time to work on both of our projects over the next 5 months, and we&#8217;ve signed a contract to have him illustrate both of the games. It is a little weird to have the same illustrator for what is a competition, but I&#8217;m sure he&#8217;ll provide me with better work since I&#8217;m the one who found him. For the record, Ryan tried out a number of other artists, which isn&#8217;t a cheap task, but was in awe when he saw the trial illustration Scott did for me. We would have preferred to have separate artists, but the right person is the right person.

To allow Scott to work efficiently, he rotates between our two games on a weekly basis. He worked on Ryan&#8217;s game last week and he will be working on my game this week. I spent a solid week in preparation for working with Scott this next by creating a few design documents for the three categories of art that will be in my game: level art, cut scene art, and character art.

In addition to the design documents, I spent a few days trying to figure out exactly how Corona handles displaying images to different devices. It&#8217;s important that I fully understood how Corona dynamically resizes images so my game is playable on anything from an iPhone, to an iPad Retina, to a Ouya. Some image cropping will happen on every device, but because different devices have different dimensions, the cropping happens in different places. I need to make sure that important parts of the game are not cropped. In case you&#8217;re curious, I&#8217;ll be asking Scott to draw on a canvas size of 4275 x 2700, which I&#8217;ll scale down to 2850 x 1800 and 1425 x 900 for the actual build. Those sizes should account for all the major mobile devices and even desktop screens if I make a PC/Mac version of the game later on.

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/08/level1-guide-1-1024x604.png" alt="level1-guide" width="625" height="368" class="alignnone size-large wp-image-985" />
</div>

As far as programming goes, the main game mechanic that I&#8217;ve been playing around with is what I call engagement. My game is a turn based game, and the idea is that if a character fights another character, then they should be engaged. And if you&#8217;re engaged, then you should be encouraged to stay engaged with the character you&#8217;re fighting. I don&#8217;t like that in most turn based games you can simply walk anywhere at anytime without any type of penalty. If you were to fight in real life and simply turn your back, then you&#8217;d get hit in the back. I haven&#8217;t figured out exactly what the penalty will be, or if it will be different for different characters, but I have the groundwork done so that the characters &#8220;know&#8221; if they&#8217;re engaged or when they disengage. I hope to build on that the concept to see if it makes the game more or less fun.

The next couple of weeks are really exciting for me because I get to work with Scott. This will be our first week working together, so I expect things to go a little slower than they will in the future. It&#8217;s important that we figure out an art style for level design, a style for cut scenes, and a style for characters. What we do now will influence the entire game, so it&#8217;s important to take our time and lay the foundation to a solid game.

 [1]: http://battleofbrothers.com/sirchris/what-im-looking-for-in-an-illustrator
 [2]: http://appylon.weebly.com
 [3]: https://twitter.com/Appylon