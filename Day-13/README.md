<h1> Functions </h1>

I'm going to introduce you to functions. Once you learn about them you won't be able to stop using them. I sure can't.

2. Functions
Functions aren't entirely new for you actually: you've already used them. type, for example, is a function that returns the type of a value. But what is a function? Simply put, a function is a piece of reusable code, aimed at solving a particular task. You can call functions instead of having to write code yourself. Maybe an example can clarify things here.

3. Example
Suppose you have the list containing only the heights of your family, fam: Say that you want to get the maximum value in this list. Instead of writing your own piece of Python code that goes through the list and finds the highest value, you can also use Python's max function. This is one of Python's built-in functions, just like type. We simply pass fam to max inside parentheses. The output makes sense: 1-point-89, the highest number in the list. max worked kind of like a black box here:

4. Example
you passed it a list, then the implementation of max, that you don't know, did its magic,

5. Example
and produced an output. How max actually did this, is not important to you, it just does what it's supposed to, and you didn't have to write your own code, which made your life easier.

6. Example
Of course, it's possible to also assign the result of a function call to a new variable, like here. Now tallest is just like any other variable; you can use it to continue your fancy calculations.

7. round()
Another one of these built-in functions is round. It takes two inputs: first, a number you want to round, and second, the precision with which to round, which is how many digits after the decimal point you want to keep. Say you want to round 1-point-68 to one decimal place. The first input is 1-point-68, the second input is 1. You separate the inputs with a comma. But there's more. It's perfectly possible to call the round function with only one input, like this. This time, Python figured out that you didn't specify the second input, and automatically chooses to round the number to the closest integer. To understand why both approaches work, let's open up the documentation. You can do this with yet another function, help, like this. It appears that round takes two inputs.

8. round()
In Python, these inputs, also called arguments, have names: number and ndigits. When you call the function round,

9. round()
with these two inputs, Python matches the inputs to the arguments:

10. round()
number is set to 1-point-68 and

11. round()
ndigits is set to 1. Next,

12. round()
The round function does its calculations with number and ndigits as if they are Python variables in a script. We don't know exactly what code Python executes. What is important, though, is that the function produces an output,

13. round()
namely the number 1-point-68 rounded to 1 decimal place.

14. round()
If you call the function round with only one input,

15. round()
Python again tries to

16. round()
match the inputs to

17. round()
the arguments. There's no input to match to the ndigits argument though. Luckily,

18. round()
the internal machinery of the round function knows how to handle this. When ndigits is not specified, the function simply rounds to the closest integer and

19. round()
returns that integer. That's why we got the number 2.

20. round()
In other words, ndigits is an optional argument. This tells us that you can call round in this form, as well as in this one.

21. Find functions
By now, you have an idea about how to use max and round, but how could you know that a function such as round exists in Python in the first place? Well, this is something you will learn with time. Whenever you are doing a rather standard task in Python, you can be pretty sure that there's already a function that can do this for you. In that case, you should definitely use it! Just do a quick internet search and you'll find the function you need with a nice usage example. And there is of course DataCamp, where you'll also learn about powerful functions and how to use them.

-----------------------------------------------------------

1. Methods
Built-in functions are only

2. Built-in Functions
one part of the Python story. You already know about functions such as max, to get the maximum of a list, len, to get the length of a list or a string, and so on. But what about other basic things, such getting the index of a specific element in the list, or reversing a list? You can look very hard for built-in functions that do this, but you won't find them.

3. Back 2 Basics
In the past exercises, you've already created a bunch of variables. Among other Python types, you've created strings, floats and lists, like the ones you see here. Each one of these values or data structures are so-called Python objects. This string is an object, this float is an object, but this list is also, you got it, an object. These objects have a specific type, that you already know:

4. Back 2 Basics
string, float, and list, and of course they represent the values you gave them, such as "liz", 1-point-73 and an entire list. But in addition to this, Python objects also come with a bunch of so-called "methods". You can think of methods as functions that "belong to" Python objects. A Python object of type string has methods,

5. Back 2 Basics
such as capitalize and replace, but also objects of type float and list have specific methods depending on the type. Enough for the theory now; let's try to use a method!

6. list methods
Suppose you want to get the index of the string "mom" in the fam list. fam is an Python object with the type list, and has a method named index. To call the method, you use the dot notation, like this. The only input is the string "mom", the element you want to get the index for. Python returns 4, which indeed is the index of the string "mom". I called the index method "on" the fam list here, and the output was 4. Similarly, I can use the count method on the fam list to count the number of times 1-point-73 occurs in the list. Python gives me 1, which makes sense, because only liz is 1-point-73 meters tall. But lists are not the only Python objects that have methods associated. Also floats, integers, booleans and strings

7. str methods
are Python objects that have specific methods associated with them. Take the variable sister for example, that represents a string. You can call the method capitalize on sister, without any inputs. It returns a string where the first letter is capitalized now. Or what if you want to replace some parts of the string with other parts? Not a problem. Just call the method replace on sister, with two appropriate inputs. In the output, "z" is replaced with "sa".

8. Methods
To be absolutely clear: in Python, everything is an object, and each object has specific methods associated. Depending on the type of the object, list, string, float, whatever, the available methods are different. A string object like sister has a replace method, but a list like fam doesn't have this, as you can see from this error.

9. Methods
Objects of different types can have methods with the same name: Take the index method. It's available for both strings and lists. If you call it on a string, you get the index of the letters in the string; If you call it on a list, you get the index of the element in the list. This means that, depending on the type of the object, the methods behave differently. Before I unleash you on some exercises on methods,

10. Methods (2)
there's one more thing I want to tell you. Some methods can change the objects they are called on. Let's retake the fam list, and call the append method on it. As the input, we pass a string we want to add to the list. Python doesn't generate an output, but if we check the fam list again, we see that it has been extended with the string "me". Let's do this again, this time to add my height to the list. Again, the fam list was extended. This is pretty cool, because you can write very concise code to update your data structures on the fly, but it can also be pretty dangerous. Some method calls don't change the object they're called on, while others do, so watch out.

11. Summary
Let's take a step back here and summarize this. you have Python functions, like type, max and round, that you can call like this. There's also methods, which are functions that are specific to Python objects. Depending on the type of the Python object you're dealing with, you'll be able to use different methods and they behave differently. You can call methods on the objects with the dot notation, like this, for example. There's much more to tell about Python objects, methods and how Python works internally,

----------------------------------------------------------

1. Packages
By now, I hope you're convinced

2. Motivation
that python functions and methods are extremely powerful: you can basically use other people's code to solve your own problems. That's amazing! However, adding all functions and methods that have been written up to now to the same Python distribution would be a mess. There would be tons and tons of code in there, that you'll never use. Also, maintaining all of this code would be a real pain.

3. Packages
This is where packages come into play. You can think of packages as a directory of Python scripts. Each such script is a so-called module. These modules specify functions, methods and new Python types aimed at solving particular problems. There are thousands of Python packages available from the internet. Among them are packages for data science: there's NumPy to efficiently work with arrays, Matplotlib for data visualization, and scikit-learn for machine learning. Not all these packages are available in Python by default.

4. Install package
To use Python packages, you'll first have to install them on your own system, and then put code in your script to tell Python that you want to use these packages. Datacamp already has all necessary packages installed for you, but if you want to install them on your own system, you'll want to use pip, a package maintenance system for Python. If you go to this URL, you can download the file get-pip-dot-py. Next, you go to the terminal, and execute python3 get-pip-dot-py. Now you can use pip to actually install a Python package of your choosing. Suppose we want to install the numpy package, which you'll learn about in the next chapter. You type pip3 install numpy. You have to use the commands python3 and pip3 here to tell our system that we're working with Python version 3. Now that the package is installed, you can actually start using it in one of your Python scripts.

5. Import package
Before you can do this, you should import the package, or a specific module of the package. You can do this with the import statement. To import the entire numpy package, you can do import numpy, like this. A commonly used function in NumPy is array. It takes a list as input. Simply calling the array function like this, will generate an error. To refer to the array function from the numpy package, you'll need this. This time it works. The NumPy array is very useful to do data science, but more on that later. Using this numpy dot prefix all the time can become pretty tiring, so you can also import the package and refer to it with a different name. You can do this by extending your import statement with as, like this. Now, instead of numpy-dot-array, you'll have to use np-dot-array to use NumPy's array function. There are cases in which you only need one specific function of a package. Python allows you to make this explicit in your code. Suppose that we only want to use the array function from the NumPy package. Instead of doing import numpy, you can instead do from numpy import array, like this. This time, you can simply call the array function like this, no need to use numpy dot here. This from import version to use specific parts of a package can be useful to limit the amount of coding, but you're also loosing some of the context.

6. from numpy import array
Suppose you're working in a long Python script. You import the array function from numpy at the very top, and way later, you actually use this array function. Somebody else who's reading your code might have forgotten that this array function is a specific NumPy function; it's not clear from the function call.

7. import numpy
In that respect, the more standard import numpy call is preferred: In this case, your function call is numpy-dot-array, making it very clear that you're working with NumPy.

