# python learning journal

---
## the setup

+ setup Windows Powershell(the Terminal) & Atom(the editor).

### how to RUN THE FILE

+ save the file as xxxx.py by Atom, use "cd" to the **locate** the file in Terminal, use "python" to open it.
example code:

```
cd mystuff;python ex1.py
```

### how to use the "cd" command in Powershell   
*  
```cd C:\xxxx\xxx\xxx``` let you go straight to the directory you want.
* 
``` cd xxxx ```
let you go to child folder xxxx.  
* ``` cd .. ``` let you go to parent directory, which is the upper class directory.

[reference](https://technet.microsoft.com/en-us/library/ee176962.aspx)

### question:how to return to the default/start location/directory?


## ex4
+ variables & names.  
done.

## ex5
+ about string & "formatters" （格式符？）   
done.

## ex6

+ compare formatter %r & %s
+ 
```
x = "abcdef" 

print x 
```
means same as 
```
print "%s" % x
```
```print "%r" % x ```
means it will put out something like 'abcdef'

### question
Why adding the two strings w and e with + makes a longer string?

use "x" on strings to a make longer string, but why does it work?

## ex7

+ comma
if a sentence is two long(over 80 char), then use a comma:
```
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
```

### note  
> Why are you using the variable named 'snow'?

> That's actually not a variable: it is just a string with the word snow in it. A variable wouldn't have the single-quotes around it.

## ex8

> Why do I have to put quotes around "one" but not around True or False?


> Python recognizes True and False as keywords representing the concept of true and false. If you put quotes around them then they are turned into strings and won't work. You'll learn more about how these work in Exercise 27.
```
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
```

+ single-quotes and double-quotes

> Why does %r sometimes print things with single-quotes when I wrote them with double-quotes?

> Python is going to print the strings in the most efficient way it can, not replicate exactly the way you wrote them. This is perfectly fine since %r is used for debugging and inspection, so it's not necessary that it be pretty.

## ex9
### question
```
print "Here are the days: ", days
```
output:
> **Here are the days:  Mon Tue Wed Thu Fri Sat Sun**

+ why ? how does Mon Tue... print out?

+ use three quotes like: """ abcd """ to print as much as we like.
**you can print dot "." by using """**
## ex10

\# \t does the same as Tab  
```tabby_cat = "\tI'm tabbed in."```  
\# \n to jump to a new line  
```persian_cat = "I'm split\non a line."```  
\# \\ print out "\"  
```backslash_cat = "I'm \\ a \\ cat."```

\# you can directly print out punctuations like " : * . in """ """ syntax
```fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
""" ```

## ex11
### question
> Related to escape sequences, try to find out why the last line has '6\'2"' with that \' sequence. See how the single-quote needs to be escaped because otherwise it would end the string?

my Terminal actually print out this:
> So, you're '24' old, "6'2''" tall and '60kg' heavy.  
with no \ in it.

## ex12 

+ raw_input must be assigned to a variable:  
```
height = raw_input("How tall are you? ")
```  
> Why can't I do print "How old are you?" , raw_input()?
> You'd think that'd work, but Python doesn't recognize that as valid. The only answer I can really give is, you just can't.

## ex13

+ introduce Module "argv"

## ex14
```
from sys import argv
```  
\# you'll need to assign a name to this script,   
\# and it must be the same name that you saved this script as  
```script, user_name = argv
```

## ex15

+ **don't know how to open file from Terminal?**

## ex16

### error?
```
PS C:\Users\Family\mystuff> python ex16.py   test.txt  
We're going to erase 'test.txt'.  
If you don't want that, hit CRTL-C(^C).
If you do want that, hit RETURN.
?Traceback (most recent call last):
  File "ex16.py", line 9, in <module>
    raw_input("?")
EOFError
```
## ex17
### todo
+  **read Appendix A**

## 感想

+ 用代码试错的方式了解代码的用法
+ 写练习的同时也写笔记
+ 搜索能力还是不够好，经常搜不到想要的答案