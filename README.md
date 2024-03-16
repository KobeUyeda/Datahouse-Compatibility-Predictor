# Datahouse-Compatibility-Predictor

## Overview

We are designing a program that can help determine if an applicant is compatible with a team. We will have to determine if an applicant is compatible based on the attributes that are given for each user. Based on this we have to give them a score ranging from 0 to 1.

This project will be completed in `python`

## Thoughts Before Coding

1. We must first standardize the data so that it is on a range from 0 to 1
    - If we look at the practice data we can see that the attributes are all working on a scale range from 0 to 10
    - Based on this we can just divide all of the attributes by 10.

2. Now that the data is standardized to the scale that we are suppose to have we now have to figure out how we are to determine if someone is compatible
    - Compatibility is subjective some attributes may be viewed more favorably than others
        - This could lead to us creating a weighted system where certain attributes are weighted more in determining someones compatibility than others

    - We can also find the average in the team for all the attributes and from their have that as a vector and anything in that vector range we can then say they are compatible.
        - The main way we can do this is by using the dot product to see if the vectors are going the same way

## Second Thoughts After Coding

1. If we use a vector system then we don't have to scale the data by dividing by 10. We can just set the weight to the value and then we can make that a vector. From their we can make it a unit vector by dividing each component by the magnitude.

## Final Route Taken

1. We then want to add a weight to the attribute so if a certain attribute is more important than another it can be adjusted
2. The next step is to get the average of each attribute for the team and store that
3. Now that we have the data mostly standardized we now can put all the data into a vector. Since we are using python we can use numpy
4. Once they are in a vector we can make it a unit vector which can be done by dividing each component by the magnitude
5. Once this is done we can use the dot product to find out if the vectors are headed in the same direction

## Final Thoughts

The route we took allows us to make sure we account for if certain fields may hold more weight than others. We were then able to also make sure that based on that we calculated the compatibility of a applicant by checking the average team member and seeing if they were going in the same direction as a vector. Some notes while we could have also checked to see how similar in magnitude they were, but that didn't seem right since if we did this what if a applicant had a bigger spicy food tolerance than the teams average and that made them more compatible and not less. Then the magnitude would ruin the compatibility score.