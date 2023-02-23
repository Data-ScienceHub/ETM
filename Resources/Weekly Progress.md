# Weekly Progress

### 1/22/2023
- Finalized the initial data features to use for the initial model.
- The initial features to be used are: event type and event timestamp. The time gaps will be used to predict which users will return.
- Finalized the [budget proposal](https://github.com/Data-ScienceHub/ETM/blob/main/Resources/Budget%20Proposal.pdf) using AWS and Snowflake calculators. 

### 1/29/2023
- Created an initial model proposal.
- Leverage idle time interval as special event to denote period of disengagement
    - Mark as idle if greater than 95% of users' event gaps​
    - Preliminary value of ~73 hours of idle time between event cycles per user (~280 hours as initial benchmark for churned out based on 90% quantile of users' maximum event gaps)​
- If an event sequence is not idle, predict the rest of the events until idle period is expected​
    - Then, use most recent completed sequence to predict whether the user will return​
- Sequence length of interest appears to be 16-48 events​
- Next steps would be to encode sequences of the desired lengths and to perform training for both sequence prediction and classification

### 2/5/2023
- Created a mockup proposal deck with the purpose of being able to explain the model to marketing/sales departments.
- Run initial classification and prediction model using the proposed model.
- The initial classification model was able to achieve an accuracy of ~58%.

### 2/13/2023
- Completed data processing and cleaning of entire 2022 dataset
- Successfully built, trained, and evaluated a baseline sequence classifier model for the most recent period of user engagement
- The model produced an accuracy of ~67% on the testing set, but the model's room for improvement seems capped by the quality and content of the available data
- Given the nature of collection and the way events are triggered, patterns in the sequence proved to be more difficult more the model to discern than expected
- Having discovered this, we were prompted to reevaluate the feature selection process and consider how the model could be adapted
- We proceeded to perform an enhanced feature EDA and identified at least 4 new attributes which could be incorporated into our model
- We also with our sponsor, laid out the current situation, and discussed ways in which we could steer the current project path towards clearer success
- Ultimately, we determined to pursue a new, slightly modified approach which will be able to build off the the work previously accomplished and hopefully yield more tangible results for our client
- The pivoted proposal is to now construct an MLP which will identify users likely to solidify their engagement through subscription and not simply be short-term binge consumers of journal content

### 2/20/2023
- Revisited all of the tables in our database to explore what other features we might engineer to reconfigure our model
- Focused primarily on the tables such as Event, Content, Profile, and Organization
- Reimagined the goal and scope of our data's predictive capabilities
- Established a new definition for good user engagement and determined how to extract that from our data
- Opted to base user quality on number of interactions rather than duration or subscriptions tendencies
- Crystallized our vision for a new model which will take 6 numeric inputs and output a binary prediction regarding their propensity to continue consuming content
- Drafted our Progress Report 1
