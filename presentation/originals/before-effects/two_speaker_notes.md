# Two-speaker presentation notes

Target: 9 minutes 0 seconds, including chart-reading pauses and handoff. Rehearse to stay within 8–10 minutes.

The charts and model metrics use local data and saved notebook outputs. No model was retrained and final testing was not run. Actual coding/review contributions must be confirmed by the team.

## 1. Poker Hand Classification

**Speaker:** Francisco · **Time:** 20 seconds

Hello, we are Francisco Gutierrez and Lilian Kim. Our project asks how well classification models recognize five-card poker hands, especially when some categories are much more common than others. I will cover the data and modeling setup, and Lilian will explain the results and what they mean.

**Evidence:** poker_hand_model_training.ipynb, saved code and validation outputs

## 2. Table of Contents

**Speaker:** Francisco · **Time:** 15 seconds

We will follow the analysis from the research question through data preparation, exploration, model selection, and evaluation. We will show short code excerpts along the way, then close with limitations and recommendations.

**Evidence:** poker_hand_model_training.ipynb, saved code and validation outputs

## 3. Introduction

**Speaker:** Francisco · **Time:** 35 seconds

Our experience with statistics has often centered on medical research. Poker gives us a different setting with clear rules and known labels. The task is to classify a supplied hand into one of ten categories. We are not predicting future cards or an opponent's hidden cards. Because rules determine the correct category, this is also a useful way to examine what a statistical model actually learns. Our main question is how performance differs between common and rare hands.

**Evidence:** poker_hand_analysis.ipynb, saved descriptive outputs

## 4. What does one record contain?

**Speaker:** Francisco · **Time:** 30 seconds

Each hand has ten inputs: a suit and a rank for each of five cards. The target is a separate category code. In this example, two cards have rank ten, so the correct category is one pair. Suit numbers identify categories, not strength. We keep the target out of the inputs. The raw representation also gives each card a position, which matters later when we discuss limitations.

**Evidence:** poker_hand_model_training.ipynb, saved code and validation outputs

## 5. Data Loading and Preparation

**Speaker:** Francisco · **Time:** 40 seconds

The supplied files contain twenty-five thousand and ten training records and one million test records. Training records pass checks for missing values, valid codes, and repeated cards within a hand. We also identify the same five cards even when their order changes. Removing one hundred and twelve repeated hands leaves twenty-four thousand eight hundred and ninety-eight distinct development hands. We split these into nineteen thousand nine hundred and eighteen training hands and four thousand nine hundred and eighty validation hands. The supplied test file stays separate from fitting and model selection.

**Evidence:** poker_hand_model_training.ipynb, saved code and validation outputs

## 6. Code: prevent the same hand crossing the split

**Speaker:** Francisco · **Time:** 35 seconds

This excerpt shows the essential preparation steps. The helper creates a key for the five-card set, ignoring order. We keep the first occurrence, separate the inputs from the target, and make an eighty-twenty stratified split with a fixed random seed. Stratification approximately preserves the category proportions. The full notebook also checks label conflicts and verifies that training and validation keys do not overlap. This prevents identical-card-set leakage, although it does not group hands related by renaming suits.

**Evidence:** poker_hand_model_training.ipynb, saved code and validation outputs

## 7. Exploratory Data Analysis

**Speaker:** Francisco · **Time:** 25 seconds

The main exploratory finding is severe class imbalance. High card represents about fifty percent of the combined files, and one pair represents about forty-two percent. Together, they account for more than ninety-two percent of records. These are descriptive frequencies across both supplied files, not held-out model results. We disclose that the test file was included in that earlier descriptive exploration.

**Evidence:** poker_hand_analysis.ipynb, saved descriptive outputs

## 8. Most records belong to just two categories

**Speaker:** Francisco · **Time:** 30 seconds

The logarithmic axis makes the rare categories visible. It changes the spacing, not the counts. There are over five hundred thousand high-card records but only eight royal-flush records in the combined files. This means a model can score reasonably well on accuracy while missing uncommon hands. We therefore need a measure that gives each category equal weight, and we need to inspect how many examples support each score.

**Evidence:** poker_hand_analysis.ipynb, saved descriptive outputs

## 9. Model Selection

**Speaker:** Francisco · **Time:** 40 seconds

We compare three candidates on the same validation split: a majority baseline, a depth-limited decision tree, and a random forest with two hundred trees. The baseline always predicts high card. The learned models use one-hot encoded suits and ranks, with the encoder fitted only on training data. Class weighting increases the influence of uncommon categories but does not create more examples. We select using macro F1, the average F1 across all ten categories, and also report accuracy and class-level results. Lilian will now explain the implementation and findings.

**Evidence:** poker_hand_model_training.ipynb, saved code and validation outputs

## 10. Code: fit the encoder and classifier together

**Speaker:** Lilian · **Time:** 35 seconds

Thank you, Francisco. This pipeline keeps preprocessing and the classifier together. Calling fit on the training split learns both the encoder and the forest. We then predict the separate validation inputs. The macro F1 calculation includes all ten labels, so categories with no successful predictions still count. These are the forest settings used in the saved notebook. The other candidates use the same split and evaluation procedure, allowing a consistent comparison.

**Evidence:** poker_hand_model_training.ipynb, saved code and validation outputs

## 11. Model Analysis

**Speaker:** Lilian · **Time:** 30 seconds

The random forest has the highest validation macro F1 among these candidates, so the notebook selects it. Its validation accuracy is sixty point five six percent, while macro F1 is only zero point one one nine four. Training accuracy is one hundred percent. That large training-to-validation gap suggests overfitting. Selection here means the strongest of these three candidates on this one split; it does not establish a reliable classifier across all categories.

**Evidence:** poker_hand_model_training.ipynb, saved code and validation outputs

## 12. Validation Results

**Speaker:** Lilian · **Time:** 25 seconds

The table shows why both metrics matter. The decision tree has lower accuracy than the majority baseline but a higher macro F1. The forest leads on both measures. Its accuracy exceeds the baseline by ten point six percentage points. All of these numbers come from the four thousand nine hundred and eighty validation hands. The notebook has not run the optional final test evaluation.

**Evidence:** poker_hand_model_training.ipynb, saved code and validation outputs

## 13. The forest improves accuracy, but macro F1 stays low

**Speaker:** Lilian · **Time:** 25 seconds

The two panels summarize the same comparison with different metrics. The accuracy panel uses a zero-to-one-hundred-percent scale. Macro F1 is on a separate zero-to-one scale, with the axis zoomed to zero point one five so the differences are readable. The forest improves over the baseline, but its low macro F1 indicates that the improvement does not extend evenly across the ten categories. A higher overall score is only part of the story.

**Evidence:** poker_hand_model_training.ipynb, saved code and validation outputs

## 14. Where the Model Struggles

**Speaker:** Lilian · **Time:** 25 seconds

The class-level results explain the weak macro F1. The forest correctly identifies about eighty-eight percent of high-card hands, but only about forty percent of one-pair hands. It has zero recall for the eight remaining categories on this validation split. Even the notebook's example pair of tens is predicted as high card. That example illustrates an error; the class-level evaluation provides the broader evidence.

**Evidence:** poker_hand_model_training.ipynb, saved code and validation outputs

## 15. Recall reveals which hands are missed

**Speaker:** Lilian · **Time:** 30 seconds

Recall asks what fraction of actual hands in a category the model finds. The labels also show support, the number of validation examples. Two pairs has two hundred and forty-one examples with zero recalled, so the failures extend beyond just the rarest hands. In contrast, each of the three rarest categories has only one validation example. Their observed zero recall is real for this split, but one example cannot tell us their population performance reliably.

**Evidence:** poker_hand_model_training.ipynb, saved code and validation outputs

## 16. Limitations

**Speaker:** Lilian · **Time:** 35 seconds

There are several limits to the claim. This is one validation split, and we have not quantified variability across repeated evaluations. The same split guides selection and supplies the reported comparison. The rarest categories have tiny support. Inputs retain card positions, so changing card order may change a prediction. Deduplication removes identical card sets, but does not group suit-renamed equivalents. We also disclose the earlier descriptive exploration of both supplied files. Final testing and development-to-test overlap reporting remain pending.

**Evidence:** poker_hand_model_training.ipynb, saved code and validation outputs

## 17. Recommendations

**Speaker:** Lilian · **Time:** 30 seconds

Our next experiments should improve representation and evaluation. We can compare consistent card ordering with order-independent features, while explaining when those features encode poker rules directly. A correct rule-based evaluator is a useful reference. We should repeat validation where rare-class counts allow it, then lock the model and procedure before final testing. The final evaluation should report performance on the supplied test file and separately on hands absent from development. These are proposed next steps, not completed results.

**Evidence:** poker_hand_model_training.ipynb, saved code and validation outputs

## 18. Conclusion

**Speaker:** Lilian · **Time:** 25 seconds

Our answer is qualified: the random forest improves validation accuracy over a majority baseline, but the current representation does not support reliable classification across all ten categories. Low macro F1, zero recall outside the two most common classes, and the training-to-validation gap all limit the result. The project demonstrates why preparing data carefully and interpreting class-level metrics matter as much as reporting a single headline accuracy.

**Evidence:** poker_hand_model_training.ipynb, saved code and validation outputs

## 19. Sources, speaking roles, and contribution record

**Speaker:** Both · **Time:** 10 seconds

Francisco: Our code and saved outputs are documented in the two project notebooks.
Lilian: Before submission, we will confirm the contribution record and complete the required AI attribution. Thank you.

**Evidence:** Local notebooks and README course-requirement summary; speaking roles are assigned here, actual coding/review roles remain to be confirmed.
