# Two-speaker presentation notes with animation cues

Target: approximately 9–10 minutes including short pauses. Francisco presents slides 1–9; Lilian presents slides 10–18; both share slide 19. Rehearse with the builds enabled.

Controls: use a single click, Space, or Right Arrow for each numbered reveal. After the last reveal, the NEXT SLIDE click changes slides. Wait about half a second for each fade/dissolve; avoid double-clicks. Slide changes are manual. The PDF is static and shows all content.

## 1. Poker Hand Classification

SPEAKER: Francisco
REHEARSAL TARGET: 20 seconds plus brief reveal pauses
REVEALS: 0; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[NO CONTENT BUILDS — keep this slide visible while speaking.]
Hello, we are Francisco Gutierrez and Lilian Kim. Our project asks how well classification models recognize five-card poker hands, especially when some categories are much more common than others. I will cover the data and modeling setup, and Lilian will explain the results and what they mean.

[NEXT SLIDE — after the final sentence, pause 1 second. Click once to advance. Let the next dissolve finish before triggering a reveal.]

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs

## 2. Table of Contents

SPEAKER: Francisco
REHEARSAL TARGET: 15 seconds plus brief reveal pauses
REVEALS: 0; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[NO CONTENT BUILDS — keep this slide visible while speaking.]
We will follow the analysis from the research question through data preparation, exploration, model selection, and evaluation. We will show short code excerpts along the way, then close with limitations and recommendations.

[NEXT SLIDE — after the final sentence, pause 1 second. Click once to advance. Let the next dissolve finish before triggering a reveal.]

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs

## 3. Introduction

SPEAKER: Francisco
REHEARSAL TARGET: 35 seconds plus brief reveal pauses
REVEALS: 3; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[CLICK 1 — fade in Goal: classify five-card hands into ten categories. Wait 0.5 seconds, then speak.]
Our goal is to classify a supplied five-card hand into one of ten categories. We are not predicting future cards or an opponent's hidden cards.

[CLICK 2 — fade in Motivation: explore applications of statistics beyond our work in medical research. Wait 0.5 seconds, then speak.]
Our experience with statistics has often centered on medical research. Poker gives us a different setting in which to apply the same ideas.

[CLICK 3 — fade in Why UCI Poker Hand? Clear labels and common / rare categories let us study class imbalance. Wait 0.5 seconds, then speak.]
We chose the UCI dataset because its known labels and mix of common and rare hands let us study class imbalance. Our main question is how performance differs between these categories. Because rules determine the correct category, we can also ask what a statistical model actually learns.

[NEXT SLIDE — after the final sentence and all 3 reveals, pause 1 second. Click once to advance. Let the next dissolve finish before triggering a reveal.]

EVIDENCE: poker_hand_analysis.ipynb, saved descriptive outputs

## 4. What does one record contain?

SPEAKER: Francisco
REHEARSAL TARGET: 30 seconds plus brief reveal pauses
REVEALS: 1; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[CLICK 1 — fade in the five-card record example. Wait 0.5 seconds; pause 1 second before explaining.]
Each hand has ten inputs: a suit and a rank for each of five cards. The target is a separate category code. In this example, two cards have rank ten, so the correct category is one pair. Suit numbers identify categories, not strength. We keep the target out of the inputs. The raw representation also gives each card a position, which matters later when we discuss limitations.

[NEXT SLIDE — after the final sentence and all 1 reveals, pause 1 second. Click once to advance. Let the next dissolve finish before triggering a reveal.]

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs

## 5. Data Loading and Preparation

SPEAKER: Francisco
REHEARSAL TARGET: 40 seconds plus brief reveal pauses
REVEALS: 4; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[CLICK 1 — fade in 25,010 training records; 1,000,000 supplied test records. Wait 0.5 seconds, then speak.]
The supplied files contain twenty-five thousand and ten training records and one million test records. Training records pass checks for missing values, valid codes, and repeated cards within a hand.

[CLICK 2 — fade in Remove 112 repeated unordered hands. Wait 0.5 seconds, then speak.]
We identify the same five cards even when their order changes. Removing one hundred and twelve repeated hands leaves twenty-four thousand eight hundred and ninety-eight distinct development hands.

[CLICK 3 — fade in Split 24,898 distinct hands: 19,918 training / 4,980 validation. Wait 0.5 seconds, then speak.]
We split these into nineteen thousand nine hundred and eighteen training hands and four thousand nine hundred and eighty validation hands. The supplied test file stays separate from fitting and model selection.

[CLICK 4 — fade in One-hot encode suits and ranks. Wait 0.5 seconds, then speak.]
We one-hot encode suits and ranks so their codes are treated as discrete values. The encoder learns only from the training split.

[NEXT SLIDE — after the final sentence and all 4 reveals, pause 1 second. Click once to advance. Let the next dissolve finish before triggering a reveal.]

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs

## 6. Code: prevent the same hand crossing the split

SPEAKER: Francisco
REHEARSAL TARGET: 35 seconds plus brief reveal pauses
REVEALS: 1; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[CLICK 1 — fade in the preparation code. Wait 0.5 seconds; pause 1 second before explaining.]
This excerpt shows the essential preparation steps. The helper creates a key for the five-card set, ignoring order. We keep the first occurrence, separate the inputs from the target, and make an eighty-twenty stratified split with a fixed random seed. Stratification approximately preserves the category proportions. The full notebook also checks label conflicts and verifies that training and validation keys do not overlap. This prevents identical-card-set leakage, although it does not group hands related by renaming suits.

[NEXT SLIDE — after the final sentence and all 1 reveals, pause 1 second. Click once to advance. Let the next dissolve finish before triggering a reveal.]

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs

## 7. Exploratory Data Analysis

SPEAKER: Francisco
REHEARSAL TARGET: 25 seconds plus brief reveal pauses
REVEALS: 4; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[CLICK 1 — fade in High card: 50.12%; one pair: 42.25%. Wait 0.5 seconds, then speak.]
The main exploratory finding is severe class imbalance. High card represents about fifty percent of the combined files, and one pair represents about forty-two percent.

[CLICK 2 — fade in Together: 92.37% of combined records. Wait 0.5 seconds, then speak.]
Together, they account for more than ninety-two percent of records.

[CLICK 3 — fade in Only 8 royal flush records. Wait 0.5 seconds, then speak.]
There are only eight royal-flush records. These are descriptive frequencies across both supplied files, not held-out model results. We disclose that the test file was included in that earlier descriptive exploration.

[CLICK 4 — fade in Accuracy alone can hide rare-hand failures. Wait 0.5 seconds, then speak.]
A model can score reasonably well on accuracy while missing uncommon hands. That is why we need metrics that examine all ten categories.

[NEXT SLIDE — after the final sentence and all 4 reveals, pause 1 second. Click once to advance. Let the next dissolve finish before triggering a reveal.]

EVIDENCE: poker_hand_analysis.ipynb, saved descriptive outputs

## 8. Most records belong to just two categories

SPEAKER: Francisco
REHEARSAL TARGET: 30 seconds plus brief reveal pauses
REVEALS: 1; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[CLICK 1 — fade in the class-distribution chart. Wait 0.5 seconds; allow 2 seconds for the audience to inspect the chart.]
The logarithmic axis makes the rare categories visible. It changes the spacing, not the counts. There are over five hundred thousand high-card records but only eight royal-flush records in the combined files. This means a model can score reasonably well on accuracy while missing uncommon hands. We therefore need a measure that gives each category equal weight, and we need to inspect how many examples support each score.

[NEXT SLIDE — after the final sentence and all 1 reveals, pause 1 second. Click once to advance. Let the next dissolve finish before triggering a reveal.]

EVIDENCE: poker_hand_analysis.ipynb, saved descriptive outputs

## 9. Model Selection

SPEAKER: Francisco
REHEARSAL TARGET: 40 seconds plus brief reveal pauses
REVEALS: 4; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[CLICK 1 — fade in Majority baseline: always predict high card. Wait 0.5 seconds, then speak.]
We compare three candidates on the same validation split. Our reference is a majority baseline that always predicts high card.

[CLICK 2 — fade in Decision tree: a simple learned comparison. Wait 0.5 seconds, then speak.]
The decision tree is a depth-limited learned comparison.

[CLICK 3 — fade in Random forest: 200 trees. Wait 0.5 seconds, then speak.]
The random forest combines two hundred trees. Class weighting increases the influence of uncommon categories but does not create examples. Both learned models use one-hot encoding fitted on training data.

[CLICK 4 — fade in Select by validation macro F1; inspect accuracy and class-level metrics. Wait 0.5 seconds, then speak.]
We select using macro F1, which averages F1 across all ten categories, and also report accuracy and class-level results. Lilian will now explain the implementation and findings.

[HANDOFF — look toward Lilian and pause 1 second. Advance once; Lilian triggers the next slide's code reveal.]

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs

## 10. Code: fit the encoder and classifier together

SPEAKER: Lilian
REHEARSAL TARGET: 35 seconds plus brief reveal pauses
REVEALS: 1; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[CLICK 1 — fade in the model pipeline code. Wait 0.5 seconds; pause 1 second before explaining.]
Thank you, Francisco. This pipeline keeps preprocessing and the classifier together. Calling fit on the training split learns both the encoder and the forest. We then predict the separate validation inputs. The macro F1 calculation includes all ten labels, so categories with no successful predictions still count. These are the forest settings used in the saved notebook. The other candidates use the same split and evaluation procedure, allowing a consistent comparison.

[NEXT SLIDE — after the final sentence and all 1 reveals, pause 1 second. Click once to advance. Let the next dissolve finish before triggering a reveal.]

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs

## 11. Model Analysis

SPEAKER: Lilian
REHEARSAL TARGET: 30 seconds plus brief reveal pauses
REVEALS: 4; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[CLICK 1 — fade in Random forest selected by macro F1. Wait 0.5 seconds, then speak.]
The random forest has the highest validation macro F1 among these candidates, so the notebook selects it.

[CLICK 2 — fade in Validation accuracy: 60.56%. Wait 0.5 seconds, then speak.]
Its validation accuracy is sixty point five six percent.

[CLICK 3 — fade in Validation macro F1: 0.1194. Wait 0.5 seconds, then speak.]
However, macro F1 is only zero point one one nine four. That is a warning that performance is uneven across categories.

[CLICK 4 — fade in 100% training accuracy suggests overfitting. Wait 0.5 seconds, then speak.]
Training accuracy is one hundred percent. The large training-to-validation gap suggests overfitting. Selection means the strongest of these three candidates on this one split, not an established reliable classifier across all categories.

[NEXT SLIDE — after the final sentence and all 4 reveals, pause 1 second. Click once to advance. Let the next dissolve finish before triggering a reveal.]

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs

## 12. Validation Results

SPEAKER: Lilian
REHEARSAL TARGET: 25 seconds plus brief reveal pauses
REVEALS: 4; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[CLICK 1 — fade in the majority-baseline row Wait 0.5 seconds, then speak.]
The majority baseline reaches forty-nine point nine six percent accuracy, with macro F1 of zero point zero six six six.

[CLICK 2 — fade in the decision-tree row Wait 0.5 seconds, then speak.]
The decision tree has lower accuracy, twenty-two point five seven percent, but higher macro F1 of zero point zero eight three seven. This shows why the two metrics can rank models differently.

[CLICK 3 — fade in the random-forest row Wait 0.5 seconds, then speak.]
The forest leads on both measures: sixty point five six percent accuracy and macro F1 of zero point one one nine four.

[CLICK 4 — fade in the +10.60 percentage-point takeaway Wait 0.5 seconds, then speak.]
Its accuracy exceeds the baseline by ten point six percentage points. All these numbers come from the four thousand nine hundred and eighty validation hands. The optional final test evaluation has not been run.

[NEXT SLIDE — after the final sentence and all 4 reveals, pause 1 second. Click once to advance. Let the next dissolve finish before triggering a reveal.]

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs

## 13. The forest improves accuracy, but macro F1 stays low

SPEAKER: Lilian
REHEARSAL TARGET: 25 seconds plus brief reveal pauses
REVEALS: 1; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[CLICK 1 — fade in the two-metric comparison chart. Wait 0.5 seconds; allow 2 seconds for the audience to inspect the chart.]
The two panels summarize the same comparison with different metrics. The accuracy panel uses a zero-to-one-hundred-percent scale. Macro F1 is on a separate zero-to-one scale, with the axis zoomed to zero point one five so the differences are readable. The forest improves over the baseline, but its low macro F1 indicates that the improvement does not extend evenly across the ten categories. A higher overall score is only part of the story.

[NEXT SLIDE — after the final sentence and all 1 reveals, pause 1 second. Click once to advance. Let the next dissolve finish before triggering a reveal.]

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs

## 14. Where the Model Struggles

SPEAKER: Lilian
REHEARSAL TARGET: 25 seconds plus brief reveal pauses
REVEALS: 4; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[CLICK 1 — fade in High-card recall: 87.7%. Wait 0.5 seconds, then speak.]
The class-level results explain the weak macro F1. The forest correctly identifies about eighty-eight percent of actual high-card hands.

[CLICK 2 — fade in One-pair recall: 39.5%. Wait 0.5 seconds, then speak.]
It identifies only about forty percent of actual one-pair hands. Even the notebook's example pair of tens is predicted as high card.

[CLICK 3 — fade in Eight other categories: 0% recall on this split. Wait 0.5 seconds, then speak.]
The other eight categories have zero recall on this validation split.

[CLICK 4 — fade in Rare-class scores have very little support. Wait 0.5 seconds, then speak.]
A single example illustrates an error, but the class-level evaluation is the broader evidence. We also need support, the number of examples behind each score.

[NEXT SLIDE — after the final sentence and all 4 reveals, pause 1 second. Click once to advance. Let the next dissolve finish before triggering a reveal.]

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs

## 15. Recall reveals which hands are missed

SPEAKER: Lilian
REHEARSAL TARGET: 30 seconds plus brief reveal pauses
REVEALS: 1; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[CLICK 1 — fade in the class-recall chart. Wait 0.5 seconds; allow 2 seconds for the audience to inspect the chart.]
Recall asks what fraction of actual hands in a category the model finds. The labels also show support, the number of validation examples. Two pairs has two hundred and forty-one examples with zero recalled, so the failures extend beyond just the rarest hands. In contrast, each of the three rarest categories has only one validation example. Their observed zero recall is real for this split, but one example cannot tell us their population performance reliably.

[NEXT SLIDE — after the final sentence and all 1 reveals, pause 1 second. Click once to advance. Let the next dissolve finish before triggering a reveal.]

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs

## 16. Limitations

SPEAKER: Lilian
REHEARSAL TARGET: 35 seconds plus brief reveal pauses
REVEALS: 4; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[CLICK 1 — fade in One validation example for each of the three rarest categories. Wait 0.5 seconds, then speak.]
Each of the three rarest categories has only one validation example. This cannot establish reliable population performance.

[CLICK 2 — fade in One split; no repeated evaluation. Wait 0.5 seconds, then speak.]
The comparison uses one validation split, which also guides selection. We have not measured variability across repeated evaluations.

[CLICK 3 — fade in Card order may change predictions. Wait 0.5 seconds, then speak.]
Inputs retain card positions, so changing card order may change a prediction. Deduplication removes identical card sets but does not group suit-renamed equivalents.

[CLICK 4 — fade in Final test evaluation remains pending. Wait 0.5 seconds, then speak.]
Final testing and development-to-test overlap reporting remain pending. We also disclose the earlier descriptive exploration of both supplied files.

[NEXT SLIDE — after the final sentence and all 4 reveals, pause 1 second. Click once to advance. Let the next dissolve finish before triggering a reveal.]

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs

## 17. Recommendations

SPEAKER: Lilian
REHEARSAL TARGET: 30 seconds plus brief reveal pauses
REVEALS: 4; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[CLICK 1 — fade in Compare consistent card ordering and order-independent features. Wait 0.5 seconds, then speak.]
Our next experiments should improve representation. We can compare consistent card ordering with order-independent features.

[CLICK 2 — fade in Use a rule-based evaluator as a reference. Wait 0.5 seconds, then speak.]
A correct rule-based evaluator provides a useful reference. We should explain when engineered features encode poker rules directly.

[CLICK 3 — fade in Repeat validation where feasible. Wait 0.5 seconds, then speak.]
We should repeat validation where rare-class counts allow it.

[CLICK 4 — fade in Lock the model, then run final testing. Wait 0.5 seconds, then speak.]
Then we should lock the model and procedure before final testing. Report results on the supplied test file and separately on hands absent from development. These are proposed next steps, not completed results.

[NEXT SLIDE — after the final sentence and all 4 reveals, pause 1 second. Click once to advance. Let the next dissolve finish before triggering a reveal.]

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs

## 18. Conclusion

SPEAKER: Lilian
REHEARSAL TARGET: 25 seconds plus brief reveal pauses
REVEALS: 3; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[CLICK 1 — fade in Random forest beats the baseline on validation accuracy. Wait 0.5 seconds, then speak.]
Our answer is qualified: the random forest improves validation accuracy over a majority baseline.

[CLICK 2 — fade in Low macro F1 shows weak performance across all ten categories. Wait 0.5 seconds, then speak.]
Low macro F1, zero recall outside the two most common classes, and the training-to-validation gap limit that result.

[CLICK 3 — fade in Reliable hand recognition needs better features and further evaluation. Wait 0.5 seconds, then speak.]
The current representation does not support reliable classification across all ten categories. The project shows why careful preparation and class-level interpretation matter as much as one headline accuracy.

[PAUSE 1 second after the conclusion. Advance once to the shared closing slide.]

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs

## 19. Sources, speaking roles, and contribution record

SPEAKER: Both
REHEARSAL TARGET: 10 seconds plus brief reveal pauses
REVEALS: 0; then one separate click to advance.

[ON ARRIVAL — let the 0.45-second dissolve finish; pause 0.5 seconds. Title and context are visible. Do not advance again yet.]

[NO CONTENT BUILDS — keep this slide visible while speaking.]
Francisco: Our code and saved outputs are documented in the two project notebooks.
Lilian: Before submission, we will confirm the contribution record and complete the required AI attribution. Thank you.

[FINISH — pause 2 seconds after “Thank you.” Leave the closing slide visible; do not advance.]

EVIDENCE: Local notebooks and README course-requirement summary; speaking roles are assigned here, actual coding/review roles remain to be confirmed.
