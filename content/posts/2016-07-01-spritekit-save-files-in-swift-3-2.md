---
title: SpriteKit Save Files in Swift 3
author: Ryan
type: post
date: 2016-07-01T21:07:39+00:00
url: /2016/07/01/spritekit-save-files-in-swift-3-2/
categories:
  - sirryan
tags:
  - code

---
Last year I wrote about [saving game data in SpriteKit][1], and that code is now completely out of date. Swift 3 has brought about all sorts of fun changes, so it&#8217;s time for me to provided some updated code.

<!--more-->

The general approach remains the same &#8212; conform save data to NSCoding and write to a plist file. The main changes / improvements are:

  * You have to manually create an empty DefaultFile.plist in your project directory
  * Uses new singleton implementation
  * You have to use encodeInteger / Double / Bool instead of just encodeObject
  * Swift 3 syntax changes

You can read my last post for more context, or jump straight to the gist below. First, code calling the GameData class.

https://gist.github.com/veeneck/1d988af6e20e67b131c9cf775f546f16

Then, you can look at the GameData and Level class here:

  * [GameData][2]
  * [LevelData][3]

 [1]: http://battleofbrothers.com/sirryan/saving-game-data-in-spritekit
 [2]: https://gist.github.com/veeneck/5521e0b6381051b8387f48ba792ba888
 [3]: https://gist.github.com/veeneck/96306731570687e76d1190fa6ccacf0c