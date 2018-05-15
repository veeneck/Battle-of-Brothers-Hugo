---
title: Handling zPosition in a 2.5d World
author: Ryan
type: post
date: 2014-04-21T15:28:10+00:00
url: /2014/04/21/handling-zposition-in-a-2-5d-world/
categories:
  - sirryan
tags:
  - code
  - learning

---
Not surprisingly, dealing with zPosition in a 2.5d game is about as complicated as everything else in game development &#8212; it will be harder to handle than you think it should be. For example, how should you handle moving a sprite from behind a tree to in front of a tree in perceived depth. While the initial drawing of objects is straightforward, things become tricky once they start moving around. Let&#8217;s take a look at how I&#8217;m approaching zPosition in my Sprite Kit game.
<!--more-->

#### An Enum for World Layers

The most common thing to start out with is an [enum that handles general world layers][1]. Using this approach, the UI, background, characters and foreground are all children of a layer node. In my project, I took inspiration from Apple&#8217;s adventure game and ended up with this.



This sort of setup is good for organization, but it didn&#8217;t answer all of my needs. Mainly, what happens when objects start moving. To give the illusion of depth, we need moving objects to change zPosition when they move in front of another object. I&#8217;ve altered the enum approach in a couple of ways.

#### Give the Enum a Wider Range

The first change to make is to give each layer of the enum more zPosition to work with. For starters, I&#8217;ve just modified the loop above to be multiples of 5000.

    layer.zPosition = (i - kWorldLayerCount)*5000

The main reason for this is because when nodes are added to a parent layer they will still have individual zPositions that take priority. For example, a world layer with a zPosition of 3 contains a node with a zPosition of 100. The 100 will be the zPosition used, which means we could place a character on top of our HUD even though the character layer is lower than the HUD layer.

#### Initialize a zPosition on Object Creation

Whenever I created a character, or SKSpriteNode, I provide a zPosition in the initialization method. For example, if my character layer takes up the range of 5000-10000, I might initialize a character like this:

    self.zPosition = 10000 - self.position.y

Because anything with a larger y position will be further back in depth, we want it to have a lower zPosition. At this point, everything will be correctly positioned when first drawn.

#### Update Nodes When They Move

The next step is to update the zPosition of a node as it moves throughout the world. Currently, I&#8217;m just handling this in the global update method. A simplified version of the code would look like:



My only concern here is that this runs every frame, but it seems to have a low enough overhead that it won&#8217;t be an issue. At this point, we have nodes drawing correctly on initialization and when they move.

#### Unknowns and Improvements

Depending on the features for your particular game, there will be a couple of edge cases or improvements that need to be made. For example, if we have a character that shoots arrows on an arc path. Those arrows may rise, which means their y position will rise. However, we don&#8217;t want the zPosition to change even though the y position is changing. If you can picture in your head, the arrow would still be in front of the background targets.

To accommodate for this, make sure everything is subclassed accurately. Basically, custom logic statements are needed for certain cases. In the arrow example, I just hard coded an offset of the average character height. Since my arrows don&#8217;t arch too high, this visually looks right most of the time.

It&#8217;s easy to think of how zPosition will get more complicated. For example, something that arcs high will have to only account for change in perceived depth and not just look at x and y movement. I haven&#8217;t gotten to that point yet, but I&#8217;m happy to have a framework to begin working with.

 [1]: https://www.makegameswith.us/gamernews/368/control-the-drawing-order-in-cocos2d-and-sprite-ki