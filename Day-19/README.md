
<h2>While loop</h2>

In the previous chapter, you've discovered the if-elif-else construct, a way to alter the flow of your scripts. As soon as Python encounters an if statement, it checks the condition.

2. if-elif-else
When this condition is True, the corresponding code is executed. If the conditions evaluates to False, and if there are elif and else statements, Python continues the search. Anyways, Python goes through this piece of code only once. After that, Python heads over to the next command in the script. The while loop is somewhat similar to an if statement: it executes the code inside if the condition is True. However, as opposed to the if statement, the while loop will continue to execute this code over and over again as long as the condition is true.

3. While
The syntax of a while loop is very similar to the if statement, as you can see here. The while loop is not that common, but in some cases it can be very useful. As example, suppose you're numerically calculating a model based on your data. This typically involves taking the same steps over and over again, until the error between your model and your data is below some boundary. When you can reformulate the problem as 'repeating an action until a particular condition is met', a while loop is often the way to go. Say that we start with an error of fifty and that our fancy algorithm divides the error by four on each run. We want to keep going until the error is no longer above 1.

4. While
Now heading over to the script, we start by adding the error we start with, 50. Next, we write a while loop. In the condition part, we write error > 1, so that the while loop executes again as long as the error is above 1. Inside the code, we divide the error by four and update the error variable. This kind of simulates our fancy algorithm that divides the error by four on every run. Next, we also print this error. Let's go through what happens if you actually run this script, step by step.

5. While
On the first run, the error is 50, so the while condition is True and the corresponding code is executed. The error is divided by four and printed out: 12.5.

6. While
Now, Python heads back to the condition of the while loop, with error equal to 12.5. Again, the condition is True, and the code is executed. The Error is divided by 4 and printed out. Now the error is 3.125 and Python heads back to the while condition.

7. While
3.125 is still greater than 1 so the corresponding code is executed again. Now, the error is only zero point seven eight so on, as you can see from the printout.

8. While
Once more, Python heads over to the while condition, but this time, the condition is False. The code in the while loop is not executed anymore, and Python moves on. Notice that inside this while loop, this update of error is crucial: the error had to go down to become lower than 1 at some point.

9. While
Suppose that we comment out these updates of the error value, and run the script again. The error isn't updated, so the condition is always True and the while loop will go on forever. On DataCamp, this will cause your session to be disconnected. If you're making this mistake on your own system, you will have to interrupt the python program by pressing the control and C keys.

____________________________________________________________

<h2>For Loop</h2>

Next to the while loop, Python features another type of loop as well: You've seen the while loop and now it's time for another loop: the for loop! Have a look at the for loop's recipe here:

2. for loop
This can be read as: for each var, a variable, in seq, a sequence, execute the expressions. Makes sense?

3. fam
Let's see how this actually works with an example. Remember about the fam list, containing the heights of your family? Here it is again, in the family (dot) py script. Suppose that instead of a single printout of the entire list, like this, we want to print out each element in the list separately.

4. fam
You could do this by doing 4 print calls with the correct subsetting operations. Instead of this repetitive and tedious approach, you can use a for loop.

5. for loop
Let's wipe the print calls, and start a for loop: for height in fam, followed by a colon. This means that I want to execute some code for each height in the fam list. Height is an arbitrary name here, I could just as well call it h or something else. Inside the for loop, on every iteration, I print out the value of height. When you run this script, Python encounters the for loop and evaluates the seq element, fam in this case. It sees that it's a list containing 4 elements. Then the actual iteration starts.

6. for loop
In the first run, Python stores the first element, so the float 1 point 73, in the variable height. Next, the expression, print(height), is executed, printing out 1 point 73.

7. for loop
In the second iteration, Python stores the second value of fam in height, being 1 point 68 now, and prints out height again.

8. for loop
This process continues until all heights in fam have been iterated over, and we end up with 4 separate printouts, great! In this solution, you don't have access to the index of the elements you're iterating over.

9. for loop
Say that, together with printing out the height, you also want to display the index in the list, so that the printouts are converted to this. How should the for loop be built in this case?

10. enumerate
To achieve this, you can use enumerate(). Let's update the for loop definition like this. Now, enumerate(fam) produces two values on each iteration: the index of the value, and the value itself. Instead of a single variable height, you now write index, height. Now, on each iteration, index will contain the index, and height will contain the float. This means that we can now also update the statement inside the for loop with a more complicated print() call. Notice that I had to convert the floats to strings with str() so that you can add everything together. The printouts are exactly what we wanted, nice.

11. Loop over string
The for loop doesn't only work with lists. You can also create a for loop that iterates over every character a string, "family" for example, and stores it in c, one after the other. Inside the loop, the string c is capitalized and printed out. This time, 7 different printouts occur. That's enough on the for loop for now.
________________________________________________________

<h2>Loop Data Structures Part 1 </h2>

So you already saw how looping over lists and strings works, but what about those other data structures, such as dictionaries and NumPy arrays? Well, in both cases, you can use a similar for loop construct, but the way you define the "sequence" over which you're iterating will differ depending on the data structure.

2. Dictionary
Let's go back to our "world" dictionary, containing country names as keys and corresponding populations as values, shown here. How should we approach this if we want to print out the key and corresponding value for each key:value pair on a new line? Maybe like this, simply hoping that the key and value are correctly set? Unfortunately, we get an error. Python sees that you expect two values in every iteration, like enumerate did before when you wanted the index and value from a list element, but in this case, Python has no idea how to go about this.

3. Dictionary
We can fix this by calling the method items() on world. This will generate a key and value in each iteration. If you have a look at the printout, there's something strange: afghanistan comes first in world, but not in the printout. That's because dictionaries are inherently unordered: the order in which they're iterated over is not fixed, at least in Python 3.5.

4. Dictionary
The names key and value are totally arbitrary by the way, I can also call these k and v, like here. The order does matter though. The first variable gets the key, the second one the value.

5. NumPy Arrays
Now for the NumPy array, that "data science equivalent" of the Python list I've been talking about quite a bit. Let's start from the bmi array that you already know -- here it is. It's pretty straightforward: the most basic for loop you can imagine already does the trick.

6. 2D NumPy Arrays
Let's see if this also works with a 2D NumPy array. Here, I created meas, by combining the np_height and np_weight arrays. If we want to print out each element in this 2D array separately, the same basic for loop won't do the trick though. The 2D array is actually built up from an array of 1D arrays. The for loop simply prints out an entire array on each iteration.

7. 2D NumPy Arrays
To get every element of an array, you can use a NumPy function called nditer(). The input is the array you want to iterate over, meas in our case. This time, we get 10 printouts, first all the heights, then all the weights. Nice!

8. Recap
To recap: if you want to iterate over key-value pairs in a dictionary, use the items() method on the dictionary to define the sequence in the for loop. If you want to iterate over all elements in a NumPy array, you should use the nditer() function to specify the sequence. Pay attention here: dictionaries require a method, NumPy arrays use a function.

_______________________________________________________

<h1> Loop Data Structures Part 2 </h2>

There's one killer data structure out there that we haven't covered up to now when it comes to looping: the Pandas DataFrame.

2. brics
Let's go over the data on the brics countries one last time. These lines of code import it from the CSV file brics.csv. You can see its contents on the top right here, so you can follow along.

3. for, first try
If a Pandas DataFrame were to function the same way as a 2D NumPy array, then maybe a basic for loop like this, to print out each row, could work. Let's see what the output is. Well, this was rather unexpected. We simply got the column names. Also interesting, but not exactly what we want. In Pandas, you have to mention explicitly that you want to iterate over the rows.

4. iterrows
You do this by calling the iterrows method on the brics country, thus specifying another "sequence": The iterrows method looks at the DataFrame, and on each iteration generates two pieces of data: the label of the row and then the actual data in the row as a Pandas Series. Let's change the rest of the for loop to reflect this change: we store the row label as lab, and the row data as row. To understand what's happening, let's print lab and row seperately. In the first iteration, lab is BR, and row is this entire Pandas Series. Because this row variable on each iteration is a Series, you can easily select additional information from it using the subsetting techniques you learned about earlier.

5. Selective print
Suppose you only want to print out the capital on each iteration: let's change the print statement as follows, printing the label and the capital together. You can take things further than simple printouts, though.

6. Add column
Let's add a new column to the brics DataFrame, named name_length, containing the number of characters in the country's name. To do this, we'll need to blend together a lot of the things we've learned. It's pretty advanced stuff, so try to stay with me here. The specification of the for loop can be the same, because we'll need both the row label and the row data. Next, we can calculate the length of each country name by selecting the country column from row, and then passing it to the len() function, that determines the number of characters in a string. Finally, we'll have to add this new information to a new column, name_length, at the appropriate location. I used loc here, which is label-based. To see whether we coded things correctly, I'm adding a printout of brics after the for loop, so without indentation. Running this scripts shows that it worked: there's a new column in there with the length of the country names. Nice, but not especially efficient, because you're creating a Series object on every iteration. For this small DataFrame that doesn't matter, but if you're doing funky stuff on a ginormous dataset, this loss in efficiency can become problematic.

7. apply
A way better approach if you want to calculate an entire DataFrame column by applying a function on a particular column in an element-wise fashion, is apply(). In this case, you don't even need a for loop. This is how it's done. Basically, you're selecting the country column from the brics DataFrame, and then, on this column, you apply the len function. Apply calls the len function with each country name as input and produces a new array, that you can easily store as a new column, "name_length". This is way more efficient, and also easier to read, if you ask me. So, I've told you how to iterate DataFrames with a for loop, and how to do vectorized operations with the apply function. These skills will become very useful once you start transforming your own datasets!

__________________________________________________________
