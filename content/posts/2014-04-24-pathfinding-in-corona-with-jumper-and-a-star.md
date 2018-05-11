---
title: Pathfinding in Corona with Jumper and A Star
author: chris
type: post
date: 2014-04-24T15:57:28+00:00
url: /2014/04/24/pathfinding-in-corona-with-jumper-and-a-star/
categories:
  - sirchris
  - Uncategorized
tags:
  - code
  - corona
  - learning

---
If you&#8217;re making a grid based game and you need a character to move from point A to point B while avoiding obstacles, then you&#8217;re going to need some type of pathfinding. Luckily for us, Roland Yonaba utilized the power of A Star, a popular pathfinding algorithm, and made it even better with his open source Jumper library. Visually, what we&#8217;re trying to accomplish looks a little something like:

<!--more-->

<div class="inlineimg">
  <img class="alignnone size-full wp-image-371" src="http://localhost:8888/wp-content/uploads/2014/04/Jumper-Grid1-1.png" alt="Jumper Grid" width="500" height="499" srcset="http://localhost:8888/wp-content/uploads/2014/04/Jumper-Grid1-1.png 500w, http://localhost:8888/wp-content/uploads/2014/04/Jumper-Grid1-1-150x150.png 150w, http://localhost:8888/wp-content/uploads/2014/04/Jumper-Grid1-1-300x300.png 300w, http://localhost:8888/wp-content/uploads/2014/04/Jumper-Grid1-1-100x100.png 100w" sizes="(max-width: 500px) 100vw, 500px" />
</div>

The first thing you&#8217;ll want to do is download and install [Jumper][1]. I&#8217;m using the latest development version in this example. After that, let&#8217;s do some basic setup by declaring local variables and drawing a background to the screen.

https://gist.github.com/codepaladin/11145485

And now that all the basics are set up, we&#8217;ll draw a grid, make a map, and set our start and end positions with the following function:

https://gist.github.com/codepaladin/11145629

This function is responsible for a few things. First, it draws a square grid made up of 100 tiles with each tile being 48 pixels wide.

You&#8217;ll see that some tiles have gridRow[col] set to either a 1 or a 0, and that is how we create obstacles, or un-walkable tiles for the Jumper library. When we declared local variables, walkable was set to 0, which means any value other than 0 makes a tile un-walkable.

Secondly, the function populates the local map {} table with those 1 and 0 values. When the function is finished running, the map table will contain 10 nested tables, with each nested table consisting of 10 values. The map is a direct representation of the grid drawn to the screen and this table is what Jumper needs in order to know how many rows and columns make up the grid and which positions are walkable or un-walkable. For example, if you were to print out the contents of map[4], you&#8217;d see a table like {0,0,1,1,1,1,1,1,0,0}.

Finally, the function calls the drawStart and drawEnd functions, which look like:

https://gist.github.com/codepaladin/11145921

These two functions draw the A and B values on the screen, but they also set the start and end grid coordinates, which the Jumper library will need in order to create a path.

So now that we have our grid, obstacles, and start/end positions, we can figure out the correct path by running the getPath function.

https://gist.github.com/codepaladin/11145940

The Jumper library utilizes the map, obstacle, start and finish variables to figure out the optimal grid path to get way to get form point A to point B. To take things further, you could store the grid path and then use it to move a sprite from A to B one grid position at a time. Doing that would require a little more work to do things like translate grid coordinates to pixel coordinates, and I recommend the [Pathfinding with Jumper][2] tutorial if you need some more help.

The source code to this tutorial can be [found on GitHub][3]

 [1]: https://github.com/Yonaba/Jumper
 [2]: http://masteringcoronasdk.com/jumper-pathfinding-tutorial-a/
 [3]: https://github.com/codepaladin/Jumper-Tutorial