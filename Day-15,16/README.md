<h2>Respository for day 15,16 about Matplotlib with Datacamp</h2>

1. Basic plots with Matplotlib
   Hi! My name is Hugo, and I'm a data scientist and educator at DataCamp. I'm also the host of the weekly podcast DataFramed, which you need to check out to stay up to date with everything that's happening in data science. In this intermediate Python course, you're going to take your Python skills to the next level, specifically for data science.

2. Basic plots with Matplotlib
   You will learn how to visualize data and to store data in new data structures. Along the way, you will master control structures, which you will need to customize the flow of your scripts and algorithms. These are the types of things data scientists use every day. We'll finish this chapter with a case study, where you'll blend together everything you've learned to solve an exciting challenge.

3. Data visualization
   This first chapter is about data visualization, which is a very important part of data analysis. First of all, you will use it to explore your dataset. The better you understand your data, the better you'll be able to extract insights. And once you've found those insights, again, you'll need visualization to be able to share your valuable insights with other people.

4. Beautiful plot
   As an example, have a look at this beautiful plot. It's made by the late, the great Swedish professor Hans Rosling. His talks about global development have been viewed millions of times. And what makes them so intriguing, is that by making beautiful plots, he allows the data to tell their own story. Here we see a bubble chart, where each bubble represents a country. The bigger the bubble, the bigger the country's population, so the two biggest bubbles here are China and India. There are 2 axes.

1 Source: GapMinder, Wealth and Health of Nations 5. Beautiful plot
The horizontal axis shows the GDP per capita, in US dollars.

1 Source: GapMinder, Wealth and Health of Nations 6. Beautiful plot
The vertical axis shows life expectancy. We clearly see that people live longer in countries with a higher GDP per capita. Still, there is a huge difference in life expectancy between countries on the same income level. Now why am I telling you this? Well, because by the end of this chapter, you'll be able to build this beautiful plot yourself!

1 Source: GapMinder, Wealth and Health of Nations 7. Matplotlib
There are many visualization packages in python, but the mother of them all, is matplotlib. You will need its subpackage pyplot. By convention, this subpackage is imported as plt, like this. For our first example, let's try to gain some insights in the evolution of the world population. I have a list with years here, year, and a list with corresponding populations, expressed in billions, pop. In the year 1970, for example, 3.7 billion people lived on planet Earth. To plot this data as a line chart, we call plt-dot-plot and use our two lists as arguments. The first argument corresponds to the horizontal axis, and the second one to the vertical axis. You might think that a plot will pop up right now, but Python's pretty lazy. It will wait for the show function to actually display the plot. This is because you might want to add some extra ingredients to your plot before actually displaying it, such as titles and label customizations. I'll talk about that some more later on. Just remember this: the plot function tells Python what to plot and how to plot it. show actually displays the plot.

8. Matplotlib
   When we look at our plot, we see that the years are indeed shown on the horizontal axis, and the populations on the vertical axis.

9. Matplotlib
   There are four data points, and Python draws a line between them. In 1950, the world population was around 2 point 5 billion. In 2010, it was around 7 billion. So the world population has almost tripled in sixty years. What if the population keeps on growing like that? Will the world become over populated? You'll find out in the exercises.

10. Scatter plot
    Let me first introduce you to another type of plot: the scatter plot. To create it, we can start from the code from before. This time, though, you change the plot function to scatter.

11. Scatter plot
    The resulting scatter plot simply plots all the individual data points; Python doesn't connect the dots with a line. For many applications, the scatter plot is often a better choice than the line plot, so remember this scatter function well. You could also say that this is a more -honest- way of plotting your data, because you can clearly see that the plot is based on just four data points.

---

1. Histogram
   Oh you are killing it! Now in this video, I'll introduce the histogram.

2. Histogram
   The histogram is a type of visualization that's very useful to explore your data. It can help you to get an idea about the distribution of your variables. To see how it works, imagine 12 values between 0 and 6.

3. Histogram
   I've put them along a number line here. To build a histogram for these values, you can divide the line into equal chunks, called bins.

4. Histogram
   Suppose you go for 3 bins, that each have a width of 2. Next, you count how many data points sit inside each bin.

5. Histogram
   There's 4 data points in the first bin,

6. Histogram
   6 in the second bin

7. Histogram
   and 2 in the third bin.

8. Histogram
   Finally, you draw a bar for each bin. The height of the bar corresponds to the number of data points that fall in this bin. The result is a histogram, which gives us a nice overview on how the 12 values are distributed. Most values are in the middle, but there are more values below 2 than there are above 4. Of course, we can use matplotlib to build histograms as well.

9. Matplotlib
   As before, you should start by importing the pyplot package that's inside matplotlib. Next, you can use the hist function. Let's open up its documentation. There's a bunch of arguments you can specify, but the first two here are the most important ones. x should be a list of values you want to build a histogram for. You can use the second argument, bins, to tell Python into how many bins the data should be divided. Based on this number, hist will automatically find appropriate boundaries for all bins, and calculate how may values are in each one. If you don't specify the bins argument, it will by 10 by default.

10. Matplotlib example
    So to generate the histogram that you've seen before, let's start by building a list with the 12 values. Next, you simply call hist and pass this list as an input, so it's matched to the argument x. I also specified the bins argument to be 3, so that the values are divided in three bins. If you finally call the show function, you get a histogram. Histograms are really useful to give a bigger picture.

11. Population pyramid
    As an example, have a look at this so-called population pyramid. The age distribution is shown, for both males and females, in the European Union. Notice that the histograms are flipped 90 degrees; the bins are horizontal now. The bins are largest for the ages 40 to 44, where there are 20 million males and 20 million females. They are the so called baby boomers. These are figures of the year 2010. What do you think will have changed in 2050?

12. Population pyramid
    Let's have a look. The distribution is flatter, and the baby boom generation has gotten older. With the blink of an eye, you can easily see how demographics will be changing over time. That's the true power of histograms at work here!

---

1. Customization
   Wow, now you've got histograms under your datavis belt, let's figure out how to customize our plots. Creating a plot is one thing. Making the correct plot, that makes the message very clear -- that's the real challenge.

2. Data visualization
   For each visualization, you have many options. First of all, there are the different plot types. And for each plot, you can do an infinite number of customizations. You can change colors, shapes, labels, axes, and so on. The choice depends on: one, the data, and two, the story you want to tell with this data. Since there are so many possible customizations, the best way to learn this is by example.

3. Basic plot
   Let's start with the code in this script to build a simple line plot. It's similar to the line plot we've created in the first video, but this time the year and pop lists contain more data, including projections until the year 2100, forecasted by the United Nations. If we run this script, we already get a pretty nice plot: it shows that the population explosion that's going on will have slowed down by the end of the century. But some things can be improved. First, it should be clearer which data we are displaying, especially to people who are seeing the graph for the first time. And second, the plot really needs to draw the attention to the population explosion.

4. Axis labels
   The first thing you always need to do is label your axes. Let's do this by adding the xlabel and ylabel functions. As inputs, we pass strings that should be placed alongside the axes. Make sure to call these functions before calling the show function, otherwise your customizations will not be displayed. If we run the script again,

5. Axis labels
   this time the axes are annotated. Fantastic!

6. Title
   We're also going to add a title to our plot, with the title function. We pass the actual title, 'World Population Projections', as an argument.

7. Title
   And there's the title! So, using xlabel, ylabel and title, we can give the reader more information about the data on the plot: now they can at least tell what the plot is about. To put the population growth in perspective, I want to have the y-axis start from zero.

8. Ticks
   You can do this with the yticks function. The first input is a list, in this example with the numbers zero up to ten, with intervals of 2.

9. Ticks
   If we run this, the plot will change: the curve shifts up. Now it's clear that already in 1950, there were already about 2.5 billion people on this planet.

10. Ticks (2)
    Next, to make it clear we're talking about billions, we can add a second argument to the yticks function, which is a list with the display names of the ticks. This list should have the same length as the first list. The tick 0 gets the name 0, the tick 2 gets the name 2B, the tick 4 gets the name 4B and so on. By the way, B stands for Billions here. If we run this version of the script,

11. Ticks (2)
    the labels will change accordingly. Awesome!

12. Add historical data
    Finally, let's add some more historical data to accentuate the population explosion in the last 60 years. On wikipedia, I found the world population data for the years 1800, 1850 and 1900. I can write them in list form and append them to the pop and year lists with the plus sign. If I now run the script once more,

13. Add historical data
    three data points are added to the graph, giving a more complete picture.

14. Before vs. after
    Now that's how you turn an average line plot into a visual that has a clear story to tell! Over to you now.
