## **Task 1**


    It's pretty straightforward. Your goal is to create a function that removes the first and last characters >of a string. You're given one parameter, the original string. You don't have to worry with strings with >less than two characters.

---


## **Task 2**


     Simple, remove the spaces from the string, then return the resultant string.

---
## **Task 3**


##### Task

- Given three integers `a` ,`b` ,`c`, return the largest number obtained after inserting the following operators and brackets: `+`, `*`, `()`
- In other words , try every combination of `a`,`b`,`c` with `[*+()]` , and return the Maximum Obtained (Read the notes for more detail about it)

#### Example

*__With the numbers are 1, 2 and 3__, here are some ways of placing signs and brackets:*

- `1 * (2 + 3) = 5`
- `1 * 2 * 3 = 6`
- `1 + 2 * 3 = 7`
- `(1 + 2) * 3 = 9`

So _**the maximum value**_ that you can obtain is **_9_**.
#### Notes

- The numbers are always positive.
- The numbers are in the range (1? ?? a,?b,?c? ?? 10).
- You can use the same operation more than once.
- It's not necessary to place all the signs and brackets.
- Repetition in numbers may occur .
- You cannot swap the operands. For instance, in the given example you cannot get expression (1 + 3) * 2 = 8.


--- 


#### **Input >> Output Examples:**

```python
expressionsMatter(1,2,3)  ==>  return 9
```
#### **_Explanation:_**

_After placing signs and brackets, the **Maximum value** obtained from the expression_ `(1+2) * 3 = 9`.


```python
expressionsMatter(1,1,1)  ==>  return 3
```

---

#### **_Explanation:_**

_After placing signs, the **Maximum value** obtained from the expression is `1 + 1 + 1 = 3`._

```python
expressionsMatter(9,1,1)  ==>  return 18
```
---

## **Task 4**


**Terminal game move function**

In this game, the hero moves from left to right. The player rolls the dice and moves the number of spaces indicated by the dice two times.


Create a function for the terminal game that takes the current position of the hero and the roll (1-6) and return the new position.


**Example:**

```python
move(3, 6) should equal 15
```

---

## **Task 5**

##### Introduction

The first century spans from the **year 1** up to and _including_ the year 100, the second century - from the year 101 up to and _including_ the year 200, etc.

##### Task

Given a year, return the century it is in.

##### Examples


```
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
```

___

## **Task 6**

Complete the solution so that it reverses all of the words within the string passed in.

**Example(Input --> Output):**

```
"The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"
```

___

## **Task 7**

#### **Subtract the sum**


_NOTE! This kata can be more difficult than regular 8-kyu katas (lets say 7 or 6 kyu)_

Complete the function which get an input number n such that n >= 10 and n < 10000, then:

1. Sum all the digits of `n`.
2. Subtract the sum from `n`, and it is your new `n`.
3. If the new `n` is in the list below return the associated fruit, otherwise return back to task 1.

**Example**

n = `325`
sum = `3+2+5` = `10`
n = `325-10` = `315` (not in the list)
sum = `3+1+5` = `9`
n = `315-9` = `306` (not in the list)
sum = `3+0+6` = `9`
n = `306-9` = `297` (not in the list)
.
.
.
...until you find the first `n` in the list below.

There is no preloaded code to help you. _This is not about coding skills; think before you code_
```
1-kiwi
2-pear
3-kiwi
4-banana
5-melon
6-banana
7-melon
8-pineapple
9-apple
10-pineapple
11-cucumber
12-pineapple
13-cucumber
14-orange
15-grape
16-orange
17-grape
18-apple
19-grape
20-cherry
21-pear
22-cherry
23-pear
24-kiwi
25-banana
26-kiwi
27-apple
28-melon
29-banana
30-melon
31-pineapple
32-melon
33-pineapple
34-cucumber
35-orange
36-apple
37-orange
38-grape
39-orange
40-grape
41-cherry
42-pear
43-cherry
44-pear
45-apple
46-pear
47-kiwi
48-banana
49-kiwi
50-banana
51-melon
52-pineapple
53-melon
54-apple
55-cucumber
56-pineapple
57-cucumber
58-orange
59-cucumber
60-orange
61-grape
62-cherry
63-apple
64-cherry
65-pear
66-cherry
67-pear
68-kiwi
69-pear
70-kiwi
71-banana
72-apple
73-banana
74-melon
75-pineapple
76-melon
77-pineapple
78-cucumber
79-pineapple
80-cucumber
81-apple
82-grape
83-orange
84-grape
85-cherry
86-grape
87-cherry
88-pear
89-cherry
90-apple
91-kiwi
92-banana
93-kiwi
94-banana
95-melon
96-banana
97-melon
98-pineapple
99-apple
100-pineapple
```






