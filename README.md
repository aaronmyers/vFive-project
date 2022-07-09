# vFive project repository

## Project prompt:

Here's the work sample question statement:

We have built an AI assistant that helps users find a place to live based on data from this New York Times article: https://www.nytimes.com/interactive/2021/11/23/opinion/sunday/best-places-live-usa-quiz.html.

The assistant can ask questions or make statements like “I want to live in a big city with good schools” and get recommendations of the cities with high score on schools and air quality from the AI assistant.

We want you to add a new feature to the assistant so that it can give insight about the responses by making comments like: “There is generally more crime in cities with high population density”

Your job is to write a function that takes one or more criteria ("Region", “How Expensive”, “price_score”, or any other score columns in attached CSV) and returns a text description of the other criteria that is likely to appear with a high score in the returned results.

Please work out of a git repository and when you have finished, submit a link to the repository, documentation on how to run your code (if required), write up a description of your approach, how much you implemented and what else you could do to improve, along with instructions on how we can test your function.


## My plan outline:

I'm going to repeat the prompt in my own words to ensure I've got it correct:

The end result is a function `f(x)`, where `x` is an array of criteria (e.g. `["How Expensive", "price_score", ...]`) where the criteria are limited to the column titles of the csv file sent; `length(x)` must be greater than or equal to one. The function should return text that describes other criteria (i.e. not in `x`) that would be likely to have a "high score". 

### Time Plan:

3 hours total

1. 1 hour: read prompt, think through assumptions and questions, identify potential solutions
2. milestone (1 hour): decide on solution
3. 1 hour: attempt MVP of first idea
4. milestone(2 hours): if solution not working, decide to pivot to another solution or keep going
5. 45 mins: continue work on solution
6. 15 mins: pause to push code, write what I would have done with more time and any other documentation



### Assumptions/Clarity:

1. The input criteria contains actual search data, not just column titles. e.g. `x` would be `["West", "low", ...]` and not `["Region", "price_score", ...]`
2. I'm going to exclude any columns that do not have a clear "high" and "low" from being in any returned text
3. Some criteria are likley to be filtered on and some will be sorts. e.g. filter on Region, but sort on price_score. 
4. Create all code to run locally, not worrying about pushing to the cloud or any security concerns.
5. This is a problem with variable length input, 3-hours short for thinking through a complete AI solution. 
6. Skip the AI solution given the time constraints. This is risky given the role is AI based, but hopefully I can show critical thinking skills and my deep AI background is enough.  
7. Spend less time cleaning data. e.g. pick a simple normalization since this step could get complicated quickly and burn a lot of time.


### Questions:

1. I do not know the definition of "high score" as it relates to criteria that do not have obvious "high" and "low". e.g. Region, Location, Logitude.


### Potential solutions:

1. [brute force, no AI] identify certain elements in `x` as filters and some as sorts. Apply the appropriate filters and sorts to the data we have and for each remaining row, pick the column (not in `x`) that has the highest score. The top 5 column headings will be returned.
2. [PCA] put all of the data into a PCA. This would give us the ability to better understand correlation since the principle components are really the eigenvectors of the correlation matrix. We could then take the inputs and find the most correlated other columns
3. [AI] Random forest. Think of this as a clasification problem. What is the probability of each column being high given the columns you have. e.g. predict which column is the max given the data and then remove the columns you have from the final result. 

Run each output (likley a column title) through a static text output.

### Solution choice:

3 hours is very little time. I'd love to build some AI but my guess is that it would be sloppy and incomplete within 3 hours considering I also have to do data ingestion and cleaning and ensure the code can run on another machine. All while knowing I'm quite unfamiliar with this specific dataset.

I'm going with choice 2 above.

This is risky given the role is AI based, but creating an AI MVP here that I'm confident in would likely take me a day or two.

### Details on solution implementation:

1. The singular values of the decomposition drop fairly precipitously so I think the first few vectors will largely describe whats going on.



### What I would do with more time:

1. Pursue a more AI-focused path to see if that would improve results.
2. Be more thoughtful about data cleaning, inputs, and outputs.
3. Whiteboard some solution options with my network of talented engineers over some drinks :)
4. I largely used only the correlation matrix given the time constraints, would be nice to investigate using the singular values and vectors more.
5. I reversed the assumption number 1 in the assmption list above after a clarification email from Siamak.
6. Text generation model for the output
7. Save the covariance matrix sparsely and load it when needed instead of doing the full analysis with each call.


## How to run this:

1. run pip install for requirements
2. ensure the local data file is stores as 'nytdata.csv'
3. run the `return_text.py` file

The `return_text.py` file can be imported or run directly (import `function_to_run`. 
