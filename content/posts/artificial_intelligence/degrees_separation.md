---
title: "Determining the Degrees of Separation Apart two Actors"
description: "As a project from CS50's Introduction to Artificial Intelligence with Python"
date: 2022-10-02T13:49:09+08:00
draft: false
math: true
tags: ["AI", "DFS/ BFS", "Searching Algorithms"]
---

[CS50's Original Page](https://cs50.harvard.edu/ai/2020/projects/0/degrees/)

[Source Code](https://github.com/spcccomputerclub/spcccomputerclub.github.io/src/ai/cs50_aipy/degrees)

## Problem Statement

Determine the degrees of separation apart two actors, for example:

```
Loading data...
Data loaded.
Name: Morgan Freeman
Name: Denzel Washington
1 degrees of separation.
1: Morgan Freeman and Denzel Washington starred in Glory
```

```
Loading data...
Data loaded.
Name: Elvis Presley
Name: Kevin Bacon
Which 'Kevin Bacon'?
ID: 9323132, Name: Kevin Bacon, Birth: 
ID: 102, Name: Kevin Bacon, Birth: 1958
Intended Person ID: 102
4 degrees of separation.
1: Elvis Presley and James Burton starred in Elvis on Tour
2: James Burton and Jackson Browne starred in Roy Orbison: Black and White Night 30
3: Jackson Browne and Pete Seeger starred in The Power of Their Song: The Untold Story of Latin America's New Song Movement
4: Pete Seeger and Kevin Bacon starred in Songs to Keep: Treasures of an Adirondack Folk Collector
```

```
Loading data...
Data loaded.
Name: Tom Holland
Which 'Tom Holland'?
ID: 276169, Name: Tom Holland, Birth: 1943
ID: 4043618, Name: Tom Holland, Birth: 1996
Intended Person ID: 4043618
Name: Asa Butterfield
2 degrees of separation.
1: Tom Holland and Samuel L. Jackson starred in Spider-Man: Far from Home
2: Samuel L. Jackson and Asa Butterfield starred in Miss Peregrine's Home for Peculiar Children
```

We define the degrees of separation apart two actors as the cost of the shortest path linking the two nodes, where the cost of each action is constant. For instance, according to the [IMDb database](https://www.imdb.com/interfaces/), Morgan Freeman and Denzel Washington have a degree of separation of 1, as they appeared in the same movie, but Elvis Presley and Kevin Bacon have a degree of separation of 4, that is they are connected by a chain of 4 acquaintances.

This problem originated from a 1929 short story by [Frigyes Karinthy](https://en.wikipedia.org/wiki/Frigyes_Karinthy), which found the theory that 'a chain of "friend of a friend" statements can be made to connect to any two people in a maximum of six steps', which is the six handshakes rule. This is popularized by the game 'Six Degrees of Kevin Bacon', which goal is to find the 'Bacon Number': the degree of separation between an actor and Kevin Bacon.
