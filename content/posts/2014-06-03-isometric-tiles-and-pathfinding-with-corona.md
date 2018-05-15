---
title: Isometric Tiles and Pathfinding with Corona
author: chris
type: post
date: 2014-06-03T17:43:32+00:00
url: /sirchris/isometric-tiles-and-pathfinding-with-corona/
categories:
  - sirchris
tags:
  - code
  - corona
  - learning

---
I previously wrote a tutorial on how to create a square grid and [implement pathfinding with Corona SDK][1] and the Jumper library, but now we&#8217;re going to take things up a notch and do the same thing on an isometric grid. Isometric grids use rhombus, or diamond shaped tiles, as opposed to square tiles. The introduction of angled tiles adds the perception of depth and can dramatically change the visuals of your game without adding much complexity to your code.
<!--more-->

For a comparison, here is what a simple map looks like in isometric (2.5D) vs orthographic (flat) projection.

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-26-at-2.45.39-PM-1.png" alt="Screen Shot 2014-05-26 at 2.45.39 PM" width="787" height="388" class="alignnone size-full wp-image-583" srcset="http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-26-at-2.45.39-PM-1.png 787w, http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-26-at-2.45.39-PM-1-300x148.png 300w, http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-26-at-2.45.39-PM-1-768x379.png 768w" sizes="(max-width: 787px) 100vw, 787px" />
</div>

<div class="inlineimg">
  <img src="http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-26-at-2.52.23-PM-1.png" alt="Screen Shot 2014-05-26 at 2.52.23 PM" width="787" height="415" class="alignnone size-full wp-image-584" srcset="http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-26-at-2.52.23-PM-1.png 787w, http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-26-at-2.52.23-PM-1-300x158.png 300w, http://localhost:8888/wp-content/uploads/2014/05/Screen-Shot-2014-05-26-at-2.52.23-PM-1-768x405.png 768w" sizes="(max-width: 787px) 100vw, 787px" />
</div>

And to get a greater feel for the difference between the projection techniques, [take a look at my current game&#8217;s status](), where I add a little artwork to the equation.

But enough talk for now, let&#8217;s get to the nuts and bolts of how to make the switch. You&#8217;ll first want to [download and install Jumper][2], the open source pathfinding library used for this project. Once you have that downloaded, lets&#8217;s do some basic setup by declaring local variables and drawing a background to the screen.

https://gist.github.com/codepaladin/8dc3511c2c5b6b4044ad

Once the basics are set up, we&#8217;ll draw a grid to the screen and populate the map table with information about the grid.

https://gist.github.com/codepaladin/04e7c8ed2fa73fcb8a65

This function is responsible for a couple things. The first is to 6 rows and 6 columns in order to give us our grid. Since the isometric look depends on the tiles being diamond shaped, we create 36 polygons, each with a width of 128 pixels and a height of 64 pixels. It&#8217;s important to note that compared to a square grid, a little extra math needs to be performed when calculating grid and pixel coordinates. This is because moving an x or y position on the cartesian grid also affects both the x and y pixel coordinates. I don&#8217;t want to get into that too much in this tutorial, but I recommend reading [Isometric Tiles Math][3] if you want to learn more about the mathematics behind plotting isometric tiles.

The second responsibility of the drawGrid() function is to populate the local map {} table with 1 and 0 values. When the function is finished running, the map table will contain 6 nested tables, with each nested table consisting of 6 values. The map is a direct representation of the grid drawn to the screen and this table is what Jumper needs in order to know how many rows and columns make up the grid and which positions are walkable or un-walkable.

Next, we create our start and end positions:

https://gist.github.com/codepaladin/4035d4415e2f1cec82b5

These two functions draw the A and B values onto the screen by using the start and end coordinates declared earlier. These points are also what the Jumper library will use to create the most efficient path.

https://gist.github.com/codepaladin/d85a5d7f9f0244b774fd

The Jumper library utilizes the map, obstacle, and start and finish variables to figure out the optimal grid path to get way to get form point A to point B. To take things further, you could store the grid path and then use it to move a sprite from A to B one grid position at a time. Doing that would require a little more work to do things like translate grid coordinates to pixel coordinates, and I recommend the [Pathfinding with Jumper][4] tutorial if you need some more help.

The source code to this tutorial can be [found on GitHub][5].

 [1]: http://battleofbrothers.com/sirchris/pathfinding-in-corona-with-jumper-and-a-star
 [2]: https://github.com/Yonaba/Jumper
 [3]: http://clintbellanger.net/articles/isometric_math/
 [4]: http://masteringcoronasdk.com/jumper-pathfinding-tutorial-a/
 [5]: https://github.com/codepaladin/Jumper-Isometric