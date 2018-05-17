---
title: Saving Game Data in SpriteKit
author: Ryan
type: post
date: 2015-02-03T13:22:40+00:00
url: /sirryan/saving-game-data-in-spritekit/
categories:
  - sirryan
tags:
  - code
  - spritekit
  - swift

---
When searching for tips on how to save game data in SpriteKit, most posts explain how to save one variable (high score, for example). In that regard, this <a href="http://www.thinkingswiftly.com/saving-spritekit-game-data-swift-easy-nscoder/" target="_blank">Thinking Swiftly post</a> was extremely helpful, and is where a majority of the code below comes from. I just wanted to extend that post, and look at how an entire object could be saved in a self contained way.
<!--more-->

**NOTE: This article has been updated. Refer to [SpriteKit Saving with Swift 3][1]**

A class will hold a singleton which will automatically load the first time it is called. No initialization from the outside needed.

    // Access a variable. Will lazy load the first time.
    
    GameData.sharedInstance.variableA

Likewise, to save, we simply call save. Below, we&#8217;ll change a value, and save it out.

    // Change a variable, and then save.
    
    GameData.sharedInstance.variableA = 2
    GameData.sharedInstance.save()

The only major difference from other posts I&#8217;ve seen is in the actual save method. Instead of encoding each variable, I am just encoding the entire object. Note: This only works with standard variable types &#8212; if you need to save out a custom class, you have to make the class extend NSCoding.

    let saveData = NSKeyedArchiver.archivedDataWithRootObject(self.scores);
    
    // Becomes
    
    let saveData = NSKeyedArchiver.archivedDataWithRootObject(GameData.sharedInstance);

Have a look at the entire `GameData` class below, which should act as a self contained, lazy loading class to hold game data of standard variable types.

{{< gist veeneck 98c0c46e70ba533c0c08 >}}

&nbsp;

 [1]: http://battleofbrothers.com/sirryan/spritekit-save-files-in-swift-3