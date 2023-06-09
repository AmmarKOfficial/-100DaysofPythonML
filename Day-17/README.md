Weeeeeelcome back. Now do I have a treat for you. In this video, I'll be talking about a new Python type: the dictionary. Dictionaries are sooooo useful in the data world and to see this, imagine the following: you work for the World Bank and want to keep track of the population in each country.

2. List
You can put the populations in a list. You start with Afghanistan, 30.55 million, Albania, 2.77 million, Algeria, around 40 million, and so on. To keep track about which population belongs to which country, you can create a second list, with the names of the countries in the same order as the populations. Now suppose that want to get the population of Albania. First, you have to figure out where in the list Albania is, so that you can use this position to get the correct population. Remember about the method index(), a list method you learned about in the Intro to Python course? Let's use it to get the index of Albania in countries, like this. Now, we can use this index to subset the pop list, to get the population corresponding to Albania. As expected, we get 2.77, the population of Albania in millions. So we built two lists, and used the index to connect corresponding elements in both lists. It worked, but it's a pretty terrible approach: it's not convenient and not intuitive. Wouldn't it be easier if we had a way to connect each country directly to its population, without using an index? This is where the dictionary comes into play.

3. Dictionary
Let's convert this population data to a dictionary. I included the lists to start from on the top here, so you can see what's going on. To create the dictionary, you need curly brackets. Next, inside the curly brackets, you have a bunch of what are called key:value pairs. In our case, the keys are the country names, and the values are the corresponding populations.

4. Dictionary
The first key is Afghanistan, and its corresponding value is 30.55. Notice the colon that separates the key and value here. Let's do the same thing for the two other key-value pairs, and store the dictionary under the name world.

5. Dictionary
If you know want to find the population for Albania, you simply type world, and then the string Albania inside square brackets. In other words, you pass the key in square brackets, and you get the corresponding value. The key opens the door to the value: pretty poetic, isn't it? This approach is not only intuitive, it's also very efficient, because Python can make the lookup of these keys very fast, even for huge dictionaries.

____________________________________________________________________

2. Recap
we created the dictionary "world", which basically is a set of key value pairs. You could easily access the population of Albania, by passing the key in square brackets, like this. For this lookup to work properly, the keys in a dictionary should be unique. If you try to add another key:value pair to world with the same key, Albania, for example, you'll see that the resulting world dictionary still contains three pairs. The last pair that you specified in the curly brackets was kept in the resulting dictionary.

3. Recap
Also, these unique keys in a dictionary should be so-called immutable objects. Basically, the content of immutable objects cannot be changed after they're created. Strings, booleans, integers and floats are immutable objects, but the list for example is mutable, because you can change its contents after it's created. That's why this dictionary, that has all immutable objects as keys, is perfectly valid. This one, however, that uses a list as a key, is not valid, so we get an error. So now that you have an idea of how to build a valid dictionary and how to access it using square brackets, let's see how we can add more data to a dictionary that already exists.

4. Principality of Sealand
Say for example that you, an employee of the World Bank, decide to acknowledge the Principality of Sealand. Sealand is an unrecognized micronation, on an offshore platform located in the North Sea. At the moment, it has 27 inhabitants.

1 Source: Wikipedia
5. Dictionary
To add this information, simply write the key sealand in square brackets and assign 27 expressed in millions to it with the equals sign. If you check out "world" again, indeed, sealand is in there. To check this with code, you can also write "sealand in world", which gives you True if the key sealand is in there.

6. Dictionary
With the same syntax, you can also change values, for example, to update the population of sealand to 28. Because each key in a dictionary is unique, Python knows that you're not trying to create a new pair, but want to update the pair that's already in there. You can see this from the printout here. Suppose now that your boss didn't see the humour of adding Sealand to the list, and asks you to remove it again. You can do this with del, again pointing to sealand inside square brackets. If you print world again, Sealand is no longer in there. Good riddance!

7. List vs. Dictionary
If you remember the discussion of lists from the intro course, you'll notice that using lists

8. List vs. Dictionary
and dictionaries is pretty similar. You can

9. List vs. Dictionary
select, update and remove elements with square brackets.

10. List vs. Dictionary
There are some big differences though. The list is a sequence of values

11. List vs. Dictionary
that are indexed by a range of numbers. The dictionary, on the other hand,

12. List vs. Dictionary
is indexed by unique keys, that can be any immutable type. When to use which one, I hear you ask? Well, if you have a collection of values

13. List vs. Dictionary
where the order matters, and you want to easily select entire subsets of data, you'll want to go with a list. If, on the other hand, you need some sort of

14. List vs. Dictionary
look up table, where looking for data should be fast and where you can specify unique keys, a dictionary is the preferred option.

__________________________________________________________________

<h2>Pandas</h2>

1. Pandas, Part 1
As a data scientist, you'll often be working with tons of data. The form of this data can vary greatly, but pretty often, you can boil it down to a tabular structure, that is, in the form of a table like in a spreadsheet. Let's have a look at some examples.

2. Tabular dataset examples
Suppose you're working in a chemical plant and have a ton of temperature measurements to analyze. This data can come in the following form:

3. Tabular dataset examples
every row is a measurement, or an observation, and for each observation, there are different variables. For each measurement, there's of course the temperature, but also the date and time of the measurement, and the location. Another example: you have collected information on the so-called BRICS countries, Brazil, Russia, India, China and South Africa. You can again build a table with this data,

4. Tabular dataset examples
like this. Each row is an observation and represents a country. Each observation has the same variables: the country name, the capital, the area in millions of square kilometers and the population in millions.

5. Datasets in Python
To start working on this data in Python, you'll need some kind of rectangular data structure. That's easy, we already know one! The 2D NumPy array, right? Well, it's an option, but not necessarily the best one. In the two examples we covered, there are different data types and NumPy arrays are not great at handling these. In the BRICS example,

6. Datasets in Python
the area and population are floats, while

7. Datasets in Python
the country and capital are strings, for example. Your datasets will typically comprise different data types, so we need a tool that's better suited for the job. To easily and efficiently handle this data, there's the Pandas package. Pandas is a high level data manipulation tool developed by Wes McKinney, built on the NumPy package. Compared to NumPy, it's more high level, making it very interesting for data scientists all over the world. In pandas, we store the tabular data like the brics table here in an object called a DataFrame. Have a look at the Pandas DataFrame version of the BRICS data I showed you before:

8. DataFrame
You see a similar structure: the rows represent the observations, and the columns represent the variables. Also notice that each row has a unique row label: BR for Brazil, RU for Russia, and so on. The columns, or variables, also have labels: country, population, and so on. Notice that the values in the different columns have different types. This is all great news, but how can we create this DataFrame in the first place? Well, there are different ways.

9. DataFrame from Dictionary
First of all, you can build it manually, starting from a dictionary. Using the distinctive curly brackets, we create key value pairs. The keys are the column labels, and the values are the corresponding columns, in list form. After importing the pandas package as pd, you can create a DataFrame from the dictionary using pd (dot) DataFrame.

10. DataFrame from Dictionary (2)
If you check out brics now, we're almost there. Pandas assigned some automatic row labels, 0 up to 4. To specify them manually, you can set the index attribute of brics to a list with the correct labels. The resulting brics DataFrame is the same one as you saw before. Using a dictionary approach is fine, but what if you're working with tons of data, which is typically the case as a data scientist? Well, you won't build the DataFrame manually. Instead, you import data from an external file that contains all this data.

11. DataFrame from CSV file
Suppose the brics data that I showed you before comes in the form of a CSV file called brics.csv. By the way, CSV is short for comma separated values.

12. DataFrame from CSV file
Let's try to import this data into Python using Pandas read_csv function. You pass the path to the csv file as an argument. If you now print brics, there's still something wrong. The row labels are seen as a column in their own right. To solve this, we'll have to tell the read_csv function that the first column contains the row indexes. You do this by setting the index_col argument, like this.

13. DataFrame from CSV file
This time brics contains the DataFrame we started with in this video. It nicely contains the row and column labels. The read_csv function features many more arguments that allow you to customize your data import, make sure to check out its documentation

we created the DataFrame brics, containing basic data on the BRICS countries. Here it is again. The code here makes sure that the rows and columns are given appropriate labels. This is important to make accessing columns, rows and single elements in your DataFrame easy. Now that's exactly what I'll show you in this video, what a coincidence!

3. Index and select data
There are numerous ways in which you can index and select data from DataFrames, so we'll take this step by step. First, I'm going to talk about how to use square brackets; next, I'm going to tell you about advanced data access methods, loc and iloc, that make Pandas extra powerful.

4. Column Access [ ]
Suppose that you only want to select the country column from brics. How to do this with square brackets? Well, you type brics, and then the column label inside square brackets. Python prints out the entire column, together with the row labels. But there's something strange here. The last line says Name: country, dtype: object. We're clearly not dealing with a regular DataFrame here. Let's find out about the type of the object that gets returned, with the type function,

5. Column Access [ ]
with the type function, as follows. Okay, so we're dealing with a Pandas Series here. In a simplified sense, you can think of the Series as a 1-dimensional array that can be labeled, just like the DataFrame. Otherwise put, if you paste together a bunch of Series, you can create a DataFrame.

6. Column Access [ ]
If you want to select the country column but keep the data in a DataFrame, you'll need double square brackets, like this. If you check out the type of this fellow,

7. Column Access [ ]
it's a good old DataFrame, this time with only one column though.

8. Column Access [ ]
You can perfectly extend this call to select two columns, country and capital, for example. If you look at it from a different angle, you're actually putting a list with column labels inside another set of square brackets, and end up with a 'sub DataFrame', containing only the country and capital columns. You can also use the same square brackets to select rows from a DataFrame.

9. Row Access [ ]
The way to do it is by specifying a slice. To get the second, third and fourth rows of brics, we use the slice 1 colon 4. Remember that the end of the slice is exclusive and that the index starts at zero.

10. Row Access [ ]
Here are the row indexes so that you see what's happening.

11. Discussion [ ]
These square brackets work, but it only offers limited functionality. Ideally, we'd want something similar to 2D NumPy arrays. There, you also used square brackets, the index or slice before the comma referred to the rows, the index or slice after the comma referred to the columns. If we want to do a similar thing with Pandas, we have to extend our toolbox with the loc and iloc functions. loc is a technique to select parts of your data based on labels, iloc is position based. Let's start with loc first.

12. Row Access loc
Let's have another look at the brics DataFrame, and try to get the row for Russia. This is how it's done. You put the label of the row of interest in square brackets after loc. Again, we get a Pandas Series, containing all the row's information, rather inconveniently shown on different lines.

13. Row Access loc
To get a DataFrame, we have to put the "RU" string inside another pair of brackets.

14. Row Access loc
We can also select multiple rows at the same time. Suppose you want to also include India and China. This will do the trick; simply add some more row labels to the list. This was only selecting entire rows, that's something you could also do with the basic square brackets. The difference here is that you can extend your selection with a comma and a specification of the columns of interest.

15. Row & Column loc
Let's extend the previous call to only include the country and capital columns. We add a comma, and a list of column labels we want to keep. The intersection gets returned. Of course, you can also use loc to select all rows but only a specific number of columns.

16. Row & Column loc
Simply replace the first list that specifies the row labels with a colon, a slice going from beginning to end. This time, the intersection spans all rows, but only two columns.

17. Recap
So, let's take a step back: simple square brackets work fine if you want to get columns; to get rows, you can use slicing. The loc function is more versatile: you can select rows, columns, but also rows and columns at the same time. When you use loc, subsetting becomes remarkable similar to how you subsetted 2D NumPy arrays. The only difference is that you use row labels with loc, not the positions of the elements. If you want to subset Pandas DataFrames based on their position, or index, you'll need the iloc function.

18. Row Access iloc
Let's cover the same examples as with loc, and start with getting the row for Russia. In loc, you use the "RU" string in double square brackets, to get a DataFrame, like here. In iloc, you use the index 1 instead of RU. The results are exactly the same.

19. Row Access iloc
To get the rows for Russia, India and China, which was coded like this when using loc, you can now use

20. Row Access iloc
a list with the index 1 to 3. Again, the same result.

21. Row & Column iloc
To in addition only keep the country and capital column, which we did as follows with loc,

22. Row & Column iloc
we put the indexes 0 and 1 in a list after the comma, referring to the country and capital column.

23. Row & Column iloc
Finally, you can keep all rows and keep only the country and capital column in a similar fashion. With loc, this is how it's done.

24. Row & Column iloc
For iloc, it's like this. loc and iloc are pretty similar, the only difference is how you refer to columns and rows. I know all of this could be a lot to take in, so lets get you coding yourself to master indexing and selecting data. Keep learning by doing!

