---
title: Challenges You May Encounter While Porting Your SpriteKit Game to Swift
author: Ryan
type: post
date: 2014-06-18T16:20:02+00:00
url: /2014/06/18/challenges-you-may-encounter-while-porting-your-spritekit-game-to-swift/
categories:
  - sirryan
tags:
  - code
  - learning
  - sprite kit
  - swift

---
The introduction of [Swift][1] comes at a perfect time for me. I’ve been working on a SpriteKit game in Objective-C for 10 weeks now, and some of the code is definitely in need of refactoring. Refactoring is known to be tedious, so being able to learn a new language during the process is a plus. I’ve been taking notes of any challenge I’ve come across during the conversion.

<!--more-->

#### Preloading Assets

Apple&#8217;s own adventure game <a href="https://developer.apple.com/library/mac/documentation/GraphicsAnimation/Conceptual/CodeExplainedAdventure/BuildingtheWorld/BuildingtheWorld.html#//apple_ref/doc/uid/TP40013140-CH3-SW2" target="_blank">loads assets asynchronously</a> while showing a loading screen. I used a similar setup in my game, so went ahead and changed it over. In your `ViewController`, wrap the loading of the scene into a callback function.



Notice the call to `loadSceneAssetsWithCompletionHandler` &#8212; we&#8217;ll have to implement that function on our scene (`Foothills.swift` in my case).



The odd part to me was the syntax for the callback function. Aside from that, the setup is similar to its Objective-C counterpart.

#### Static Variables in a Class

While the previous section, Preloading Assets, handles the setup code to show a loading screen, we still have actually have to store the loaded textures somewhere. In the example above, notice the call to `MySprite.loadSharedAssets()`. In Objective-C, a method like this would usually load data into a static class variable. It appears static variables are only allowed in enums or structs in Swift, which leads to this code that populates an array of textures to be shared across each instance of the class:



Keep an eye on <a href="http://stackoverflow.com/questions/24024549/dispatch-once-singleton-model-in-swift" target="_blank">this Stack Overflow thread</a> because the preferred solution to this problem appears to be changing as developers learn more.

#### Closures

<a href="https://developer.apple.com/library/prerelease/ios/documentation/swift/conceptual/swift_programming_language/Closures.html" target="_blank">Closures</a> can be as simple as `{ // your code }` when passing a parameter. The interesting part is with the function definition. Have a look at this code:

https://gist.github.com/a3b35bbc51f0f82c5afb

If you’re like me, the syntax will be foreign. The parameter definition states that a closure with no parameters and no return value should be passed in. But what happens when we want a closure to accept parameters? The syntax changes to `{ (param1, param2) in }`. For example, let’s look at `enumerateChildNodesWithName`:

https://gist.github.com/f95625ecc77bced84caf

And thanks to this <a href="http://stackoverflow.com/questions/24213436/how-to-use-enumeratechildnodeswithname-with-swift-in-spritekit" target="_blank">Stack Overflow post</a>, the code can be simplified even more:

https://gist.github.com/af6f2525af76f13c513c

I did find a thorough read of Swift&#8217;s <a href="https://developer.apple.com/library/prerelease/ios/documentation/swift/conceptual/swift_programming_language/Closures.html#//apple_ref/doc/uid/TP40014097-CH11-XID_117" target="_blank">Closure Documentation</a> to be helpful once I understood the basic concepts.

#### Casting

In the example above, the first parameter of the closure is of the type `SKNode`. How would we change the code if we know what type of object will be returned?



We can use the `as` keyword to cast to a subclass of `SKNode`. The annoying part here is the addition of an extra line of code. I thought it would be nice if we could cast directly in the parameter definition, but it turns out <a href="http://stackoverflow.com/questions/24272642/cast-callback-parameter-in-swift" target="_blank">down casting in a closure is not possible</a> &#8212; you can only upcast.

#### pList Files and Data Types

An extension of my problems with casting can be found when working with pList files. In the example below, we’ll load a pList file with an array of dictionaries.

https://gist.github.com/f0c0753cde8fc7ddd4c2

Notice that the array is cast as a `NSArray` (line 3 above). If you try to cast it to a Swift Array object without knowing the types of data contained within,  you will get this error:

> Cannot convert the expression&#8217;s type &#8216;Array<$T7>&#8217; to type &#8216;$T8&#8217;

In Swift, each collection should have the same data type contained inside. Since that’s what we have at the Dictionary level (line 4 above), we can do a direct conversion to a Swift friendly object:

    Dictionary<String,String>[]

This will create a Swift Dictionary that has keys and values that are Strings. Once we’re working with a Swift object, all loops and other features will behave as expected. In some cases, you will have to loop over pList data that does not have the same data type for each element. In those cases, the loop may look like this:

https://gist.github.com/c5732e746a5f55c9f42e

Notice that the item is set to `NSDictionary` instead of `Dictionary`, but we can still access the data inside with the shorthand syntax.

#### Subclass & Initializers

When subclassing an object like SKSpriteNode, you may encounter this error at runtime even though the build succeeds:

> fatal error: use of unimplemented initializer &#8216;init(texture:color:size:)&#8217; for class

The reason for this error is that Swift <a href="http://www.codeproject.com/Articles/783584/Subclassing-Objective-C-classes-in-Swift-and-the-p" target="_blank">does not inherit initializers from a parent class</a> by default. One way to solve this is to define each initializer. For example, extending `SKSpriteNode` could result in:



An alternate solution is to call the initializer that we know will definitely be used:



This is nice because we don&#8217;t have to define each initializer, but it is still frustrating to have to call the verbose `init` that requires all parameters.

From the Swift Docs &#8211; <a href="https://developer.apple.com/library/prerelease/ios/documentation/swift/conceptual/swift_programming_language/Initialization.html#//apple_ref/doc/uid/TP40014097-CH18-XID_284" target="_blank">Class Inheritance and Initialization</a>

#### More Reading

A few problems or noteworthy items that other developers have encountered:

  * <a href="https://medium.com/swift-programming/swift-gotchas-cfe0182a58af" target="_blank">Swift Gotchas</a>
  * <a href="https://medium.com/swift-programming/initial-trip-ups-with-swift-cc111b6ef012" target="_blank">Initial Trip-Ups With Swift</a>
  * <a href="https://blog.codecentric.de/en/2014/06/10-early-thoughts-swift-programming-language/" target="_blank">10 Early Thoughts on the Swift Programming Language</a>
  * <a href="https://blog.codecentric.de/en/2014/06/10-early-thoughts-swift-programming-language/" target="_blank">Thoughts on the Swift Language</a>
  * <a href="http://graydon2.dreamwidth.org/5785.html" target="_blank">Swift (From Rust designer)</a>
  * [Swift Impressions][2]

 [1]: https://developer.apple.com/swift/
 [2]: http://www.evanmiller.org/swift-impressions.html