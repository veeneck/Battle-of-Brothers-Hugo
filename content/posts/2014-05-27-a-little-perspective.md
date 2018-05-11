---
title: A Little Perspective
author: chris
type: post
date: 2014-05-27T15:40:58+00:00
url: /2014/05/27/a-little-perspective/
featured_image: /wp-content/uploads/2014/05/Screen-Shot-2014-05-23-at-9.21.30-AM-1.png
keyevent:
  - Added Obstacles
  - Switched to Isometric Perspective
  - Added Isometric Artwork
  - Added Obstacles
  - Switched to Isometric Perspective
  - Added Isometric Artwork
number:
  - 5
  - 5
categories:
  - sirchris
tags:
  - status

---
I was really excited after the last update because I felt like the foundation of my code was relatively solid and the core game mechanics were working. With that core work out of the way, I was free to focus on polishing what I had built and thinking about what type of game I ultimately want to build. In the last 2 weeks I was able to fix a bunch of bugs, add obstacles, add art, and switch the camera point of view. Add all of those together and you get a game that&#8217;s starting to look pretty sweet in my unbiased opinion.

<!--more-->

I&#8217;m going to start out with the most exciting part of this update and that is my decision to switch from an orthographic point of view to an isometric point of view. What that basically means is the game will look less flat and more 3D because of how the tiles and artwork are drawn. Visually, what that means is that my game went from this

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-21-at-2.39.51-PM-1.png" alt="Screen Shot 2014-05-21 at 2.39.51 PM" width="764" height="574" class="alignnone size-full wp-image-569" />
</div>

to this

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-21-at-2.38.07-PM-1.png" alt="Screen Shot 2014-05-21 at 2.38.07 PM" width="768" height="574" class="alignnone size-full wp-image-570" srcset="http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-21-at-2.38.07-PM-1.png 1025w, http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-21-at-2.38.07-PM-1-300x224.png 300w, http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-21-at-2.38.07-PM-1-768x573.png 768w, http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-21-at-2.38.07-PM-1-1024x764.png 1024w" sizes="(max-width: 768px) 100vw, 768px" />
</div>

Successful games have been [made from both viewpoints][1], but I like the isometric viewpoint a lot more. After I switched to the new viewpoint, I found some cheap artwork over at the Unity asset store and added some ground tiles, trees, rocks, and a couple of buildings. So now the game in its current state looks like:

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-23-at-9.21.30-AM-1.png" alt="Screen Shot 2014-05-23 at 9.21.30 AM" width="769" height="502" class="alignnone size-full wp-image-571" srcset="http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-23-at-9.21.30-AM-1.png 961w, http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-23-at-9.21.30-AM-1-300x196.png 300w, http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-23-at-9.21.30-AM-1-768x502.png 768w" sizes="(max-width: 769px) 100vw, 769px" />
</div>

The switch really wasn&#8217;t as difficult as I thought it would be and the only real programmatic hurdle was in calculating pixel location-based on grid location and vice versa. Once that was fixed, then object placement, pathfinding, and movement all fell into place.

In addition to the point of view switch, some noteworthy fixes were:

**Objects Take up Space**
  
Image objects, like trees, houses, rocks, and characters themselves now &#8220;take up space&#8221;. This is important because now when characters move, they cannot walk over areas that are occupied. The pathfinding algorithm now recognizes which spaces are occupied and characters are routed around occupied spaces when they move.

**Objects are Indexed for Depth**
  
In Corona, images do not have a Z-index variable and they are drawn to the screen in the order that they&#8217;re called. So if I drew a square to the screen and then a circle to the same location, the square would appear to be beneath the circle. This is a problem because if I have a Knight originally behind a tree and that Knight then moves in front of the tree, he will still appear to be behind the tree. What I have to do is re-draw every image on every frame. On each frame, the images are sorted by their Y position so that the image highest on the screen is drawn first and the image lowest on the screen is drawn last.

**Maps are Loaded Programmatically**
  
I previously drew map tiles by hard coding a fixed number of columns. That was fine when all the tiles were exactly the same, but it was time to get more efficient with the addition of obstacles. I now load the maps in from a JSON file that represents terrain obstacles as numeric values.

**Added Custom Event Handlers**
  
This last point gets a little nerdy, but it&#8217;s a critical part of game development. Basically, when some events, like the death of a character happen, specific pieces of code need to be executed. By setting up [custom events][2], code objects that are &#8220;listening&#8221; for certain events then handle any necessary code.

#### Next 2 Weeks

Besides cleaning up my code, which seems to be a very common task in game development, some of the tasks which I hope to accomplish are adding multiple directions for characters (so they face where they&#8217;re walking), cleaning up movement and attack animations, adding death animations, and testing some new game mechanics I&#8217;ve been brainstorming. I&#8217;m pumped about getting back to work after a long Memorial Day weekend, because I think this thing is really starting to take shape.

 [1]: http://battleofbrothers.com/sirchris/common-turn-based-game-projection-techniques
 [2]: http://coronalabs.com/blog/2012/06/26/how-to-use-custom-events-in-corona/