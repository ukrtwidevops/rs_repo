## **Task 1**


Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata `y` isn't considered a vowel.


---

## **Task 2**

A **balanced number** is a number where the sum of digits to the left of the middle digit(s) and the sum of digits to the right of the middle digit(s) are equal.

If the number has an odd number of digits, then there is only one middle digit. (For example, `92645` has one middle digit, `6`.) Otherwise, there are two middle digits. (For example, the middle digits of `1301` are `3` and `0`.)

The middle digit(s) should not be considered when determining whether a number is balanced or not, e.g. 413023 is a balanced number because the left sum and right sum are both 5.


#### **The task**

Given a number, find if it is balanced, and return the string `"Balanced"` or `"Not Balanced"` accordingly. The passed number will always be positive.


#### **Examples**

1. ```7 ==> return "Balanced"```

    Explanation:

- middle digit(s): 7
- sum of all digits to the left of the middle digit(s) -> 0
- sum of all digits to the right of the middle digit(s) -> 0
- 0 and 0 are equal, so it's balanced.

2. ```295591 ==> return "Not Balanced"```

    Explanation:

- middle digit(s): 55
- sum of all digits to the left of the middle digit(s) -> 11
- sum of all digits to the right of the middle digit(s) -> 10
- 11 and 10 are not equal, so it's not balanced.

3. ```959 ==> return "Balanced"```

    Explanation:

- middle digit(s): 5
- sum of all digits to the left of the middle digit(s) -> 9
- sum of all digits to the right of the middle digit(s) -> 9
- 9 and 9 are equal, so it's balanced.

4. ```27102983 ==> return "Not Balanced"```

    Explanation:

- middle digit(s): 02
- sum of all digits to the left of the middle digit(s) -> 10
- sum of all digits to the right of the middle digit(s) -> 20
- 10 and 20 are not equal, so it's not balanced.

---

## **Task 3**


Complete the function/method so that it returns the url with anything after the anchor (`#`) removed.

#### **Examples**

```
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"
```

---

## **Task 4**


In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from `a to m`.

The colors used by the printer are recorded in a control string. For example a "good" control string would be `aaabbbbhaijjjm` meaning that the printer used three times color a, four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. `aaaxbbbbyyhwawiwjjjwwm` with letters not from `a to m`.

You have to write a function `printer_error` which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from `a` to `z`.

**Examples:**
```
s="aaabbbbhaijjjm"
printer_error(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s) => "8/22"
```



---

## **Task 5**

In John's car the GPS records every `s` seconds the distance travelled from an origin (distances are measured in an arbitrary but consistent unit). For example, below is part of a record with `s = 15`:
```
x = [0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]
```

The sections are:
```
0.0-0.19, 0.19-0.5, 0.5-0.75, 0.75-1.0, 1.0-1.25, 1.25-1.50, 1.5-1.75, 1.75-2.0, 2.0-2.25
```
We can calculate John's average hourly speed on every section and we get:
```
[45.6, 74.4, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0, 60.0]
```
Given `s` and `x` the task is to return as an integer the `*floor*` of the maximum average speed per hour obtained on the sections of `x`. If `x` length is less than or equal to 1 return `0` since the car didn't move.

**Example:**
with the above data your function `gps(s, x)` should return `74`

Note
With floats it can happen that results depends on the operations order. To calculate hourly speed you can use:
 `(3600 * delta_distance) / s`.

___

## **Task 6**


- Input : an array of integers.

- Output : this array, but sorted in such a way that there are two wings:

- the left wing with numbers decreasing,

- the right wing with numbers increasing.

- the two wings have the same length. If the length of the array is odd the wings are around the bottom, if the length is even the bottom is considered to be part of the right wing.

- each integer `l` of the left wing must be greater or equal to its counterpart `r` in the right wing, the difference `l - r` being as small as possible. In other words the right wing must be nearly as steep as the left wing.

The function is `make_valley or makeValley or make-valley`.
```
a = [79, 35, 54, 19, 35, 25]
make_valley(a) --> [79, 35, 25, *19*, 35, 54]
The bottom is 19, left wing is [79, 35, 25], right wing is [*19*, 35, 54].
79..................54
    35..........35
        25. 
          ..19

a = [67, 93, 100, -16, 65, 97, 92]
make_valley(a) --> [100, 93, 67, *-16*, 65, 92, 97]
The bottom is -16, left wing [100, 93, 67] and right wing [65, 92, 97] have same length.
100.........................97
    93..........
               .........92
        67......
               .....65
            -16     

a = [66, 55, 100, 68, 46, -82, 12, 72, 12, 38]
make_valley(a) --> [100, 68, 55, 38, 12, *-82*, 12, 46, 66, 72]
The bottom is -82, left wing is [100, 68, 55, 38, 12]], right wing is [*-82*, 12, 46, 66, 72].

a = [14,14,14,14,7,14]
make_valley(a) => [14, 14, 14, *7*, 14, 14]

a = [14,14,14,14,14]
make_valley(a) => [14, 14, *14*, 14, 14]
```
**A counter-example:**
```
a = [17, 17, 15, 14, 8, 7, 7, 5, 4, 4, 1]
A solution could be [17, 17, 15, 14, 8, 1, 4, 4, 5, 7, 7]
but the right wing [4, 4, 5, 7, 7] is much flatter than the left one 
[17, 17, 15, 14, 8].

Summing the differences between left and right wing:
(17-7)+(17-7)+(15-5)+(14-4)+(8-4) = 44

Consider the following solution:
[17, 15, 8, 7, 4, 1, 4, 5, 7, 14, 17]
Summing the differences between left and right wing:
(17-17)+(15-14)+(8-7)+(7-5)+(4-4) = 4
The right wing is nearly as steep as the right one.
```
