tell application "/Volumes/formac2/Applications/Keynote Creator Studio.app"
tell front document
set presenter notes of slide 1 to "SPEAKER: Francisco
TARGET: 20 seconds

Hello, we are Francisco Gutierrez and Lilian Kim. Our project asks how well classification models recognize five-card poker hands, especially when some categories are much more common than others. I will cover the data and modeling setup, and Lilian will explain the results and what they mean.

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs"
set presenter notes of slide 2 to "SPEAKER: Francisco
TARGET: 15 seconds

We will follow the analysis from the research question through data preparation, exploration, model selection, and evaluation. We will show short code excerpts along the way, then close with limitations and recommendations.

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs"
set presenter notes of slide 3 to "SPEAKER: Francisco
TARGET: 35 seconds

Our experience with statistics has often centered on medical research. Poker gives us a different setting with clear rules and known labels. The task is to classify a supplied hand into one of ten categories. We are not predicting future cards or an opponent's hidden cards. Because rules determine the correct category, this is also a useful way to examine what a statistical model actually learns. Our main question is how performance differs between common and rare hands.

EVIDENCE: poker_hand_analysis.ipynb, saved descriptive outputs"
set presenter notes of slide 4 to "SPEAKER: Francisco
TARGET: 40 seconds

The supplied files contain twenty-five thousand and ten training records and one million test records. Training records pass checks for missing values, valid codes, and repeated cards within a hand. We also identify the same five cards even when their order changes. Removing one hundred and twelve repeated hands leaves twenty-four thousand eight hundred and ninety-eight distinct development hands. We split these into nineteen thousand nine hundred and eighteen training hands and four thousand nine hundred and eighty validation hands. The supplied test file stays separate from fitting and model selection.

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs"
set presenter notes of slide 5 to "SPEAKER: Francisco
TARGET: 25 seconds

The main exploratory finding is severe class imbalance. High card represents about fifty percent of the combined files, and one pair represents about forty-two percent. Together, they account for more than ninety-two percent of records. These are descriptive frequencies across both supplied files, not held-out model results. We disclose that the test file was included in that earlier descriptive exploration.

EVIDENCE: poker_hand_analysis.ipynb, saved descriptive outputs"
set presenter notes of slide 6 to "SPEAKER: Francisco
TARGET: 40 seconds

We compare three candidates on the same validation split: a majority baseline, a depth-limited decision tree, and a random forest with two hundred trees. The baseline always predicts high card. The learned models use one-hot encoded suits and ranks, with the encoder fitted only on training data. Class weighting increases the influence of uncommon categories but does not create more examples. We select using macro F1, the average F1 across all ten categories, and also report accuracy and class-level results. Lilian will now explain the implementation and findings.

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs"
set presenter notes of slide 7 to "SPEAKER: Lilian
TARGET: 30 seconds

The random forest has the highest validation macro F1 among these candidates, so the notebook selects it. Its validation accuracy is sixty point five six percent, while macro F1 is only zero point one one nine four. Training accuracy is one hundred percent. That large training-to-validation gap suggests overfitting. Selection here means the strongest of these three candidates on this one split; it does not establish a reliable classifier across all categories.

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs"
set presenter notes of slide 8 to "SPEAKER: Lilian
TARGET: 25 seconds

The table shows why both metrics matter. The decision tree has lower accuracy than the majority baseline but a higher macro F1. The forest leads on both measures. Its accuracy exceeds the baseline by ten point six percentage points. All of these numbers come from the four thousand nine hundred and eighty validation hands. The notebook has not run the optional final test evaluation.

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs"
set presenter notes of slide 9 to "SPEAKER: Lilian
TARGET: 25 seconds

The class-level results explain the weak macro F1. The forest correctly identifies about eighty-eight percent of high-card hands, but only about forty percent of one-pair hands. It has zero recall for the eight remaining categories on this validation split. Even the notebook's example pair of tens is predicted as high card. That example illustrates an error; the class-level evaluation provides the broader evidence.

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs"
set presenter notes of slide 10 to "SPEAKER: Lilian
TARGET: 35 seconds

There are several limits to the claim. This is one validation split, and we have not quantified variability across repeated evaluations. The same split guides selection and supplies the reported comparison. The rarest categories have tiny support. Inputs retain card positions, so changing card order may change a prediction. Deduplication removes identical card sets, but does not group suit-renamed equivalents. We also disclose the earlier descriptive exploration of both supplied files. Final testing and development-to-test overlap reporting remain pending.

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs"
set presenter notes of slide 11 to "SPEAKER: Lilian
TARGET: 30 seconds

Our next experiments should improve representation and evaluation. We can compare consistent card ordering with order-independent features, while explaining when those features encode poker rules directly. A correct rule-based evaluator is a useful reference. We should repeat validation where rare-class counts allow it, then lock the model and procedure before final testing. The final evaluation should report performance on the supplied test file and separately on hands absent from development. These are proposed next steps, not completed results.

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs"
set presenter notes of slide 12 to "SPEAKER: Lilian
TARGET: 25 seconds

Our answer is qualified: the random forest improves validation accuracy over a majority baseline, but the current representation does not support reliable classification across all ten categories. Low macro F1, zero recall outside the two most common classes, and the training-to-validation gap all limit the result. The project demonstrates why preparing data carefully and interpreting class-level metrics matter as much as reporting a single headline accuracy.

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs"
set newSlide to make new slide at end of slides with properties {base layout:slide layout "Blank"}
tell newSlide
set box to make new text item with properties {object text:"Sources, speaking roles, and contribution record", position:{100, 70}, width:1720, height:160}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 60
set color of object text of box to {29000, 5000, 2000}
set box to make new text item with properties {object text:"Speaking allocation is set; actual coding and review contributions need team confirmation.", position:{105, 225}, width:1710, height:85}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 28
set color of object text of box to {25000, 25000, 25000}
set box to make new text item with properties {object text:"Francisco Gutierrez: research question, data, preparation, EDA, model selection
Lilian Kim: implementation, validation results, errors, limitations, conclusions

Coding / code review: add verified contributions and commit or review links.

Data: Cattral & Oppacher (2002), UCI Poker Hand. DOI: 10.24432/C5KW38
Evidence: poker_hand_analysis.ipynb; poker_hand_model_training.ipynb
AI disclosure: OpenAI Codex assisted with slide additions and speaker notes.
Review and explain the content; complete the course-required attribution.", position:{120, 350}, width:1680, height:580}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 29
set color of object text of box to {9000, 9000, 9000}
set box to make new text item with properties {object text:"AAI 500  |  Evidence: saved project notebooks  |  19", position:{105, 1015}, width:1710, height:40}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 21
set color of object text of box to {35000, 24000, 14000}
set presenter notes to "SPEAKER: Both
TARGET: 10 seconds

Francisco: Our code and saved outputs are documented in the two project notebooks.
Lilian: Before submission, we will confirm the contribution record and complete the required AI attribution. Thank you.

EVIDENCE: Local notebooks and README course-requirement summary; speaking roles are assigned here, actual coding/review roles remain to be confirmed."
end tell
set newSlide to make new slide at end of slides with properties {base layout:slide layout "Blank"}
tell newSlide
set box to make new text item with properties {object text:"Recall reveals which hands are missed", position:{100, 70}, width:1720, height:160}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 60
set color of object text of box to {29000, 5000, 2000}
set box to make new text item with properties {object text:"Selected random forest • normalized within each true category • support shown as n", position:{105, 225}, width:1710, height:85}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 28
set color of object text of box to {25000, 25000, 25000}
make new image with properties {file:POSIX file "/Volumes/formac2/_SchoolWork/FinalProject/presentation/support/validation_recall.png", position:{110, 325}, width:1700, height:646}
set box to make new text item with properties {object text:"AAI 500  |  Evidence: saved project notebooks  |  15", position:{105, 1015}, width:1710, height:40}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 21
set color of object text of box to {35000, 24000, 14000}
set presenter notes to "SPEAKER: Lilian
TARGET: 30 seconds

Recall asks what fraction of actual hands in a category the model finds. The labels also show support, the number of validation examples. Two pairs has two hundred and forty-one examples with zero recalled, so the failures extend beyond just the rarest hands. In contrast, each of the three rarest categories has only one validation example. Their observed zero recall is real for this split, but one example cannot tell us their population performance reliably.

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs"
end tell
move newSlide to before slide 10
set newSlide to make new slide at end of slides with properties {base layout:slide layout "Blank"}
tell newSlide
set box to make new text item with properties {object text:"The forest improves accuracy, but macro F1 stays low", position:{100, 70}, width:1720, height:160}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 60
set color of object text of box to {29000, 5000, 2000}
set box to make new text item with properties {object text:"Same validation split • n=4,980 • separate metric scales • no final test results", position:{105, 225}, width:1710, height:85}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 28
set color of object text of box to {25000, 25000, 25000}
make new image with properties {file:POSIX file "/Volumes/formac2/_SchoolWork/FinalProject/presentation/support/validation_comparison.png", position:{110, 325}, width:1700, height:646}
set box to make new text item with properties {object text:"AAI 500  |  Evidence: saved project notebooks  |  13", position:{105, 1015}, width:1710, height:40}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 21
set color of object text of box to {35000, 24000, 14000}
set presenter notes to "SPEAKER: Lilian
TARGET: 25 seconds

The two panels summarize the same comparison with different metrics. The accuracy panel uses a zero-to-one-hundred-percent scale. Macro F1 is on a separate zero-to-one scale, with the axis zoomed to zero point one five so the differences are readable. The forest improves over the baseline, but its low macro F1 indicates that the improvement does not extend evenly across the ten categories. A higher overall score is only part of the story.

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs"
end tell
move newSlide to before slide 9
set newSlide to make new slide at end of slides with properties {base layout:slide layout "Blank"}
tell newSlide
set box to make new text item with properties {object text:"Code: fit the encoder and classifier together", position:{100, 70}, width:1720, height:160}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 60
set color of object text of box to {29000, 5000, 2000}
set box to make new text item with properties {object text:"Notebook excerpt • 200 trees • fixed seed • preprocessing fitted on training only", position:{105, 225}, width:1710, height:85}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 28
set color of object text of box to {25000, 25000, 25000}
set box to make new text item with properties {object text:"model = make_pipeline(
    OneHotEncoder(handle_unknown=\"ignore\"),
    RandomForestClassifier(n_estimators=200,
        class_weight=\"balanced_subsample\", random_state=42, n_jobs=-1),
)
model.fit(X_train, y_train)
prediction = model.predict(X_validation)
score = f1_score(y_validation, prediction, labels=list(range(10)),
                 average=\"macro\", zero_division=0)", position:{120, 350}, width:1680, height:580}
set font of object text of box to "Menlo"
set size of object text of box to 32
set color of object text of box to {9000, 9000, 9000}
set box to make new text item with properties {object text:"AAI 500  |  Evidence: saved project notebooks  |  10", position:{105, 1015}, width:1710, height:40}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 21
set color of object text of box to {35000, 24000, 14000}
set presenter notes to "SPEAKER: Lilian
TARGET: 35 seconds

Thank you, Francisco. This pipeline keeps preprocessing and the classifier together. Calling fit on the training split learns both the encoder and the forest. We then predict the separate validation inputs. The macro F1 calculation includes all ten labels, so categories with no successful predictions still count. These are the forest settings used in the saved notebook. The other candidates use the same split and evaluation procedure, allowing a consistent comparison.

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs"
end tell
move newSlide to before slide 7
set newSlide to make new slide at end of slides with properties {base layout:slide layout "Blank"}
tell newSlide
set box to make new text item with properties {object text:"Most records belong to just two categories", position:{100, 70}, width:1720, height:160}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 60
set color of object text of box to {29000, 5000, 2000}
set box to make new text item with properties {object text:"Combined supplied files • 1,025,010 records • descriptive analysis only", position:{105, 225}, width:1710, height:85}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 28
set color of object text of box to {25000, 25000, 25000}
make new image with properties {file:POSIX file "/Volumes/formac2/_SchoolWork/FinalProject/presentation/support/class_distribution.png", position:{110, 325}, width:1700, height:646}
set box to make new text item with properties {object text:"AAI 500  |  Descriptive counts: local UCI files  |  8", position:{105, 1015}, width:1710, height:40}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 21
set color of object text of box to {35000, 24000, 14000}
set presenter notes to "SPEAKER: Francisco
TARGET: 30 seconds

The logarithmic axis makes the rare categories visible. It changes the spacing, not the counts. There are over five hundred thousand high-card records but only eight royal-flush records in the combined files. This means a model can score reasonably well on accuracy while missing uncommon hands. We therefore need a measure that gives each category equal weight, and we need to inspect how many examples support each score.

EVIDENCE: poker_hand_analysis.ipynb, saved descriptive outputs"
end tell
move newSlide to before slide 6
set newSlide to make new slide at end of slides with properties {base layout:slide layout "Blank"}
tell newSlide
set box to make new text item with properties {object text:"Code: prevent the same hand crossing the split", position:{100, 70}, width:1720, height:160}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 60
set color of object text of box to {29000, 5000, 2000}
set box to make new text item with properties {object text:"Excerpt from the training notebook; validation helpers are defined there.", position:{105, 225}, width:1710, height:85}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 28
set color of object text of box to {25000, 25000, 25000}
set box to make new text item with properties {object text:"train_keys = unordered_hand_keys(train_data)
keep = ~train_keys.duplicated()
development = train_data.loc[keep].copy()
X_development = development[FEATURE_COLUMNS]
y_development = development[\"CLASS\"]

X_train, X_validation, y_train, y_validation = train_test_split(
    X_development, y_development,
    test_size=0.20, stratify=y_development, random_state=42,
)", position:{120, 350}, width:1680, height:580}
set font of object text of box to "Menlo"
set size of object text of box to 32
set color of object text of box to {9000, 9000, 9000}
set box to make new text item with properties {object text:"AAI 500  |  Evidence: saved project notebooks  |  6", position:{105, 1015}, width:1710, height:40}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 21
set color of object text of box to {35000, 24000, 14000}
set presenter notes to "SPEAKER: Francisco
TARGET: 35 seconds

This excerpt shows the essential preparation steps. The helper creates a key for the five-card set, ignoring order. We keep the first occurrence, separate the inputs from the target, and make an eighty-twenty stratified split with a fixed random seed. Stratification approximately preserves the category proportions. The full notebook also checks label conflicts and verifies that training and validation keys do not overlap. This prevents identical-card-set leakage, although it does not group hands related by renaming suits.

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs"
end tell
move newSlide to before slide 5
set newSlide to make new slide at end of slides with properties {base layout:slide layout "Blank"}
tell newSlide
set box to make new text item with properties {object text:"What does one record contain?", position:{100, 70}, width:1720, height:160}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 60
set color of object text of box to {29000, 5000, 2000}
set box to make new text item with properties {object text:"Five cards → ten input values → one category label", position:{105, 225}, width:1710, height:85}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 28
set color of object text of box to {25000, 25000, 25000}
set box to make new text item with properties {object text:"Card          1        2        3        4        5
Suit          1        2        3        4        1
Rank         10       10        2        7       13

CLASS = 1  →  One pair (two tens)

Suits: 1=hearts, 2=spades, 3=diamonds, 4=clubs
Ranks: Ace=1, Jack=11, Queen=12, King=13", position:{120, 350}, width:1680, height:580}
set font of object text of box to "Menlo"
set size of object text of box to 34
set color of object text of box to {9000, 9000, 9000}
set box to make new text item with properties {object text:"AAI 500  |  Evidence: saved project notebooks  |  4", position:{105, 1015}, width:1710, height:40}
set font of object text of box to "Helvetica Neue"
set size of object text of box to 21
set color of object text of box to {35000, 24000, 14000}
set presenter notes to "SPEAKER: Francisco
TARGET: 30 seconds

Each hand has ten inputs: a suit and a rank for each of five cards. The target is a separate category code. In this example, two cards have rank ten, so the correct category is one pair. Suit numbers identify categories, not strength. We keep the target out of the inputs. The raw representation also gives each card a position, which matters later when we discuss limitations.

EVIDENCE: poker_hand_model_training.ipynb, saved code and validation outputs"
end tell
move newSlide to before slide 4
save
end tell
end tell