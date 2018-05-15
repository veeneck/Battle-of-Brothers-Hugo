---
title: Detecting and Managing Memory Leaks Between SKScenes
author: Ryan
type: post
date: 2016-01-08T20:46:40+00:00
url: /sirryan/detecting-and-managing-memory-leaks-between-skscenes/
categories:
  - sirryan
tags:
  - code
  - spritekit

---
Memory leaks suck. You know they exist, and you dread the day you have to track them down. In SpriteKit, I&#8217;ve encountered two main types of leaks. One is where the entire scene is not deallocated after transitioning to a new scene. The other is where memory is constantly being used up while interacting with a scene. For the latter, you have to use Instruments in XCode, or comb over your code, to get a handle on what is happening. But, for cleaning up scenes after you&#8217;re finished with them, here are a few tips that simplified the process for me.
<!--more-->

#### Identify The Leak

Figuring out a leak exists is pretty easy. You can either watch the memory usage while navigating between scenes, or you can place this small snippet in your parent `GameScene : SKScene`:

    deinit {
        print("\n THIS SCENE WAS REMOVED FROM MEMORY (DEINIT) \n")
    }

This will print a debug line if your scene is properly torn down. If you don&#8217;t see this line when transitioning to a new scene then you can assume your scene has a strong reference to it somewhere.

#### Fix The Leak

Now that you know you have a leak, here are a couple of tips on fixing it. First, you can start by cleaning up all nodes and actions when the scene is removed from view.

    override public func willMoveFromView(view: SKView) {
        self.removeAllChildren()
        self.removeAllActions()
    }

I&#8217;ve seen this tip a few times across the web, and it seems like a safe practice. No performance issues yet, so it doesn&#8217;t hurt to have that catch all. But, more specifically, using `weak` references to `scene` and `self` are the true fix to removing strong references to scenes.

Let&#8217;s say you&#8217;re using a closure as a callback. Here is the proper way to set that:

    object.callback = { [weak self] in
        self?.doSomething()
    }

Notice the `[weak self]` at the top, and the conditional `self?` in the code. Without that, a strong reference would have been created and the scene would have been retained. It&#8217;s important to note that this is an issue even if you aren&#8217;t using the `self` keyword. For example, take this function:

    func userTouchedSomething(scene:GameScene) {
        object.callback = { [weak scene] in
            scene?.doSomething()
        }
    }

In the example above, scene was passed as a parameter to a function, and then used in the closure. We must use the `weak` reference in the exact same way.

Another variation of this issues can be seen with protocols and delegates. If you have a protocol, and set it as a `weak` delegate, you will see this error:

> weak cannot be applied to non-class type MyProtocol

As seen in this <a href="http://stackoverflow.com/questions/24066304/how-can-i-make-a-weak-protocol-reference-in-pure-swift-w-o-objc" target="_blank">Stack Overflow answer</a>, we can fix this by adding `: class` to the protocol definition.

    public protocol MyProtocol : class {
        /// protocol code
    }

#### Follow Up

I&#8217;ll add to this if I come across anything specific. If you&#8217;re interested, you can also check out the <a href="https://github.com/veeneck/SwitchBoard" target="_blank">SwitchBoard</a> project that I am working on. The goal is to make scene management easy across all SpriteKit projects. It is not ready for primetime, but it does show you how to handle asset loading, caching, and scene transitions from one place.