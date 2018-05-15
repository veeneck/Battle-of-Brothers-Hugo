---
title: 'Joy of Debugging: Command swiftc failed with exit code 1'
author: Ryan
type: post
date: 2014-12-21T17:51:14+00:00
url: /sirryan/joy-of-debugging-command-swiftc-failed-with-exit-code-1/
categories:
  - sirryan
tags:
  - code
  - sprite kit
  - swift

---
I&#8217;ve been working through a particularly nasty issue, so it feels right to document it for anyone else who encounters it. Also, just to serve as a note and reminder that game development is full of unexpected, time consuming tasks on a near weekly basis. This most recent problem &#8212; releasing a build to an iOS device fails to compile, but it works on the simulator. Specifically, this occurs when I try to change the Swift compiler optimization level.
<!--more-->

<pre>Command /Applications/...../XcodeDefault.xctoolchain/usr/bin/swiftc failed with exit code 1</pre>

Unfortunately, no line number accompanies this issue. Stack Overflow is full of potential causes like <a href="http://stackoverflow.com/questions/10373016/command-xcode-app-contents-developer-toolchains-xcodedefault-xctoolchain-usr-bi" target="_blank">missing resource</a>, <a href="http://stackoverflow.com/questions/27219115/random-error-with-exit-code-1-xcode-6-1-swift" target="_blank">deleting derived data</a>, or <a href="http://stackoverflow.com/questions/24223210/xcode-6-beta-toolchain-error" target="_blank">codesign issues</a>. Unfortunately, none of those worked for me. (Side note: two of those links are not swiftc errors. They are clang, and swift-stdlib-tool commands. In my frustration I overlooked that.) However, I did stumble across this <a href="http://stackoverflow.com/a/26848000/3519461" target="_blank">wonderful post explaining how to get more information from the build</a>. Going forward with the command line approach, a helpful error message is visible at the bottom of the output:

<pre>** BUILD FAILED **

The following build commands failed:

    CompileSwift normal arm64 /Users/veeneck/Documents/Games/Xcode/Fort/Fort/PinchGesture.swift

    CompileSwiftSources normal arm64 com.apple.xcode.tools.swift.compiler</pre>

That shows me that `PinchGesture.swift` is the culprit. You can get similar help from Xcode, but it is not as clear. You have to scan each individual file in the output for errors instead of just jumping to the bottom. In any case, if you&#8217;re interested in that approach, show all messages in the output <a href="http://stackoverflow.com/a/27271734/3519461" target="_blank">like so</a>. Notice the error in the same file, but this time it may read:

<pre>LLVM ERROR: Broken function found, compilation aborted!</pre>

Now that the error has been isolated, let&#8217;s fix the code. I was able to fix this by trial and error, and I still don&#8217;t fully understand the differences, but here goes. My original function:

{{< gist veenecke1875c65a9d4b5161783 >}}

And now the new function. Notice that I changed the variable to not be editable, and to return within the if statements.

{{< gist veeneck7af997b8e02a1d2bcc6d >}}

Definitely an interesting bug, and anything you encounter will most likely be a different sort of issue. But, now we know how to track something like this down.