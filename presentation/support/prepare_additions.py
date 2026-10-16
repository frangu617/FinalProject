"""Build chart assets, two-speaker rehearsal notes, and the Keynote edit script.
Run with Python plus matplotlib. Charts use local records / saved notebook outputs.
AI assistance: OpenAI Codex helped prepare these presentation materials.
"""
from pathlib import Path
import csv, collections, json, re, zipfile
from PIL import Image, ImageDraw, ImageFont
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'presentation/support'
labels = ['High card','One pair','Two pairs','Three of a kind','Straight','Flush','Full house','Four of a kind','Straight flush','Royal flush']
counts = collections.Counter()
training = []
with zipfile.ZipFile(ROOT/'poker+hand.zip') as archive:
    for name in ['poker-hand-training-true.data','poker-hand-testing.data']:
        rows = list(csv.reader(archive.read(name).decode().splitlines()))
        counts.update(int(r[-1]) for r in rows)
        if 'training' in name: training = [[int(v) for v in r] for r in rows]
assert sum(counts.values()) == 1025010
keys = [tuple(sorted((r[i]-1)*13+r[i+1]-1 for i in range(0,10,2))) for r in training]
assert len(keys)-len(set(keys)) == 112
assert all(len(set(k)) == 5 for k in keys)
assert all(1<=r[i]<=4 and 1<=r[i+1]<=13 for r in training for i in range(0,10,2))
assert all(0<=r[-1]<=9 for r in training)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':15,'axes.spines.top':False,'axes.spines.right':False})
red,orange,gray = '#7c180b','#b66b26','#b5aaa0'
def save(fig, name):
    fig.savefig(OUT/name,dpi=170,facecolor='white',bbox_inches='tight'); plt.close(fig)
fig, ax=plt.subplots(figsize=(15,5.7))
y=list(range(10)); ax.barh(y,[counts[i] for i in y],color=[red,orange]+[gray]*8)
ax.set_yticks(y,labels); ax.invert_yaxis(); ax.set_xscale('log'); ax.set_xlim(1,1700000)
for i in y: ax.text(counts[i]*1.13,i,f'{counts[i]:,}',va='center',fontsize=13)
ax.set_xlabel('Number of records (logarithmic scale)'); ax.grid(axis='x',alpha=.15); ax.set_axisbelow(True)
fig.tight_layout(); save(fig,'class_distribution.png')
fig,axes=plt.subplots(1,2,figsize=(15,5.4))
models=['Majority baseline','Decision tree','Random forest']; acc=[49.96,22.57,60.56]; f1=[.0666,.0837,.1194]
for ax,values,title,limit,fmt in [(axes[0],acc,'Validation accuracy (%)',100,lambda v:f'{v:.2f}%'),(axes[1],f1,'Validation macro F1 (0–1)',.15,lambda v:f'{v:.4f}')]:
    ax.barh(models,values,color=[gray,orange,red]); ax.invert_yaxis(); ax.set_xlim(0,limit)
    for i,v in enumerate(values): ax.text(v+limit*.015,i,fmt(v),va='center',fontsize=15)
    ax.set_xlabel(title); ax.grid(axis='x',alpha=.15); ax.set_axisbelow(True)
fig.tight_layout(w_pad=3); save(fig,'validation_comparison.png')
fig,ax=plt.subplots(figsize=(15,5.7))
recall=[87.7,39.5]+[0]*8; support=[2488,2109,241,102,19,11,7,1,1,1]
ax.barh(y,recall,color=[red,orange]+[gray]*8); ax.set_yticks(y,[f'{n}  (n={s:,})' for n,s in zip(labels,support)]); ax.invert_yaxis();ax.set_xlim(0,103)
for i,v in enumerate(recall): ax.text(v+1.3,i,f'{v:.1f}%',va='center',fontsize=13)
ax.set_xlabel('Recall: percentage of actual hands correctly identified'); ax.grid(axis='x',alpha=.15);ax.set_axisbelow(True)
fig.tight_layout();save(fig,'validation_recall.png')

# Each original slide remains; seven additions are inserted in the narrative.
slides=[]
def add(title,speaker,seconds,script,source,original=None,kind=None,body=None,subtitle=None):
    slides.append(dict(title=title,speaker=speaker,seconds=seconds,script=script,source=source,original=original,kind=kind,body=body,subtitle=subtitle))
a='poker_hand_analysis.ipynb, saved descriptive outputs'
m='poker_hand_model_training.ipynb, saved code and validation outputs'
add('Poker Hand Classification','Francisco',20,
"Hello, we are Francisco Gutierrez and Lilian Kim. Our project asks how well classification models recognize five-card poker hands, especially when some categories are much more common than others. I will cover the data and modeling setup, and Lilian will explain the results and what they mean.",m,original=1)
add('Table of Contents','Francisco',15,
"We will follow the analysis from the research question through data preparation, exploration, model selection, and evaluation. We will show short code excerpts along the way, then close with limitations and recommendations.",m,original=2)
add('Introduction','Francisco',35,
"Our experience with statistics has often centered on medical research. Poker gives us a different setting with clear rules and known labels. The task is to classify a supplied hand into one of ten categories. We are not predicting future cards or an opponent's hidden cards. Because rules determine the correct category, this is also a useful way to examine what a statistical model actually learns. Our main question is how performance differs between common and rare hands.",a,original=3)
add('What does one record contain?','Francisco',30,
"Each hand has ten inputs: a suit and a rank for each of five cards. The target is a separate category code. In this example, two cards have rank ten, so the correct category is one pair. Suit numbers identify categories, not strength. We keep the target out of the inputs. The raw representation also gives each card a position, which matters later when we discuss limitations.",m,kind='data',subtitle='Five cards → ten input values → one category label',body='Card          1        2        3        4        5\nSuit          1        2        3        4        1\nRank         10       10        2        7       13\n\nCLASS = 1  →  One pair (two tens)\n\nSuits: 1=hearts, 2=spades, 3=diamonds, 4=clubs\nRanks: Ace=1, Jack=11, Queen=12, King=13')
add('Data Loading and Preparation','Francisco',40,
"The supplied files contain twenty-five thousand and ten training records and one million test records. Training records pass checks for missing values, valid codes, and repeated cards within a hand. We also identify the same five cards even when their order changes. Removing one hundred and twelve repeated hands leaves twenty-four thousand eight hundred and ninety-eight distinct development hands. We split these into nineteen thousand nine hundred and eighteen training hands and four thousand nine hundred and eighty validation hands. The supplied test file stays separate from fitting and model selection.",m,original=4)
add('Code: prevent the same hand crossing the split','Francisco',35,
"This excerpt shows the essential preparation steps. The helper creates a key for the five-card set, ignoring order. We keep the first occurrence, separate the inputs from the target, and make an eighty-twenty stratified split with a fixed random seed. Stratification approximately preserves the category proportions. The full notebook also checks label conflicts and verifies that training and validation keys do not overlap. This prevents identical-card-set leakage, although it does not group hands related by renaming suits.",m,kind='code',subtitle='Excerpt from the training notebook; validation helpers are defined there.',body='train_keys = unordered_hand_keys(train_data)\nkeep = ~train_keys.duplicated()\ndevelopment = train_data.loc[keep].copy()\nX_development = development[FEATURE_COLUMNS]\ny_development = development["CLASS"]\n\nX_train, X_validation, y_train, y_validation = train_test_split(\n    X_development, y_development,\n    test_size=0.20, stratify=y_development, random_state=42,\n)')
add('Exploratory Data Analysis','Francisco',25,
"The main exploratory finding is severe class imbalance. High card represents about fifty percent of the combined files, and one pair represents about forty-two percent. Together, they account for more than ninety-two percent of records. These are descriptive frequencies across both supplied files, not held-out model results. We disclose that the test file was included in that earlier descriptive exploration.",a,original=5)
add('Most records belong to just two categories','Francisco',30,
"The logarithmic axis makes the rare categories visible. It changes the spacing, not the counts. There are over five hundred thousand high-card records but only eight royal-flush records in the combined files. This means a model can score reasonably well on accuracy while missing uncommon hands. We therefore need a measure that gives each category equal weight, and we need to inspect how many examples support each score.",a,kind='chart',body='class_distribution.png',subtitle='Combined supplied files • 1,025,010 records • descriptive analysis only')
add('Model Selection','Francisco',40,
"We compare three candidates on the same validation split: a majority baseline, a depth-limited decision tree, and a random forest with two hundred trees. The baseline always predicts high card. The learned models use one-hot encoded suits and ranks, with the encoder fitted only on training data. Class weighting increases the influence of uncommon categories but does not create more examples. We select using macro F1, the average F1 across all ten categories, and also report accuracy and class-level results. Lilian will now explain the implementation and findings.",m,original=6)
add('Code: fit the encoder and classifier together','Lilian',35,
"Thank you, Francisco. This pipeline keeps preprocessing and the classifier together. Calling fit on the training split learns both the encoder and the forest. We then predict the separate validation inputs. The macro F1 calculation includes all ten labels, so categories with no successful predictions still count. These are the forest settings used in the saved notebook. The other candidates use the same split and evaluation procedure, allowing a consistent comparison.",m,kind='code',subtitle='Notebook excerpt • 200 trees • fixed seed • preprocessing fitted on training only',body='model = make_pipeline(\n    OneHotEncoder(handle_unknown="ignore"),\n    RandomForestClassifier(n_estimators=200,\n        class_weight="balanced_subsample", random_state=42, n_jobs=-1),\n)\nmodel.fit(X_train, y_train)\nprediction = model.predict(X_validation)\nscore = f1_score(y_validation, prediction, labels=list(range(10)),\n                 average="macro", zero_division=0)')
add('Model Analysis','Lilian',30,
"The random forest has the highest validation macro F1 among these candidates, so the notebook selects it. Its validation accuracy is sixty point five six percent, while macro F1 is only zero point one one nine four. Training accuracy is one hundred percent. That large training-to-validation gap suggests overfitting. Selection here means the strongest of these three candidates on this one split; it does not establish a reliable classifier across all categories.",m,original=7)
add('Validation Results','Lilian',25,
"The table shows why both metrics matter. The decision tree has lower accuracy than the majority baseline but a higher macro F1. The forest leads on both measures. Its accuracy exceeds the baseline by ten point six percentage points. All of these numbers come from the four thousand nine hundred and eighty validation hands. The notebook has not run the optional final test evaluation.",m,original=8)
add('The forest improves accuracy, but macro F1 stays low','Lilian',25,
"The two panels summarize the same comparison with different metrics. The accuracy panel uses a zero-to-one-hundred-percent scale. Macro F1 is on a separate zero-to-one scale, with the axis zoomed to zero point one five so the differences are readable. The forest improves over the baseline, but its low macro F1 indicates that the improvement does not extend evenly across the ten categories. A higher overall score is only part of the story.",m,kind='chart',body='validation_comparison.png',subtitle='Same validation split • n=4,980 • separate metric scales • no final test results')
add('Where the Model Struggles','Lilian',25,
"The class-level results explain the weak macro F1. The forest correctly identifies about eighty-eight percent of high-card hands, but only about forty percent of one-pair hands. It has zero recall for the eight remaining categories on this validation split. Even the notebook's example pair of tens is predicted as high card. That example illustrates an error; the class-level evaluation provides the broader evidence.",m,original=9)
add('Recall reveals which hands are missed','Lilian',30,
"Recall asks what fraction of actual hands in a category the model finds. The labels also show support, the number of validation examples. Two pairs has two hundred and forty-one examples with zero recalled, so the failures extend beyond just the rarest hands. In contrast, each of the three rarest categories has only one validation example. Their observed zero recall is real for this split, but one example cannot tell us their population performance reliably.",m,kind='chart',body='validation_recall.png',subtitle='Selected random forest • normalized within each true category • support shown as n')
add('Limitations','Lilian',35,
"There are several limits to the claim. This is one validation split, and we have not quantified variability across repeated evaluations. The same split guides selection and supplies the reported comparison. The rarest categories have tiny support. Inputs retain card positions, so changing card order may change a prediction. Deduplication removes identical card sets, but does not group suit-renamed equivalents. We also disclose the earlier descriptive exploration of both supplied files. Final testing and development-to-test overlap reporting remain pending.",m,original=10)
add('Recommendations','Lilian',30,
"Our next experiments should improve representation and evaluation. We can compare consistent card ordering with order-independent features, while explaining when those features encode poker rules directly. A correct rule-based evaluator is a useful reference. We should repeat validation where rare-class counts allow it, then lock the model and procedure before final testing. The final evaluation should report performance on the supplied test file and separately on hands absent from development. These are proposed next steps, not completed results.",m,original=11)
add('Conclusion','Lilian',25,
"Our answer is qualified: the random forest improves validation accuracy over a majority baseline, but the current representation does not support reliable classification across all ten categories. Low macro F1, zero recall outside the two most common classes, and the training-to-validation gap all limit the result. The project demonstrates why preparing data carefully and interpreting class-level metrics matter as much as reporting a single headline accuracy.",m,original=12)
add('Sources, speaking roles, and contribution record','Both',10,
"Francisco: Our code and saved outputs are documented in the two project notebooks.\nLilian: Before submission, we will confirm the contribution record and complete the required AI attribution. Thank you.", 'Local notebooks and README course-requirement summary; speaking roles are assigned here, actual coding/review roles remain to be confirmed.',kind='sources',subtitle='Speaking allocation is set; actual coding and review contributions need team confirmation.',body='Francisco Gutierrez: research question, data, preparation, EDA, model selection\nLilian Kim: implementation, validation results, errors, limitations, conclusions\n\nCoding / code review: add verified contributions and commit or review links.\n\nData: Cattral & Oppacher (2002), UCI Poker Hand. DOI: 10.24432/C5KW38\nEvidence: poker_hand_analysis.ipynb; poker_hand_model_training.ipynb\nAI disclosure: OpenAI Codex assisted with slide additions and speaker notes.\nReview and explain the content; complete the course-required attribution.')

# Plain rehearsal companion, including cues, timing, and traceable evidence.
lines=['# Two-speaker presentation notes','', 'Target: 9 minutes 40 seconds, including chart-reading pauses and handoff. Rehearse to stay within 8–10 minutes.', '', 'The charts and model metrics use local data and saved notebook outputs. No model was retrained and final testing was not run. Actual coding/review contributions must be confirmed by the team.', '']
for i,s in enumerate(slides,1):
    lines += [f'## {i}. {s["title"]}', '',f'**Speaker:** {s["speaker"]} · **Time:** {s["seconds"]} seconds','',s['script'],'',f'**Evidence:** {s["source"]}','']
seconds=sum(s['seconds'] for s in slides)
lines[2]=f'Target: {seconds//60} minutes {seconds%60} seconds, including chart-reading pauses and handoff. Rehearse to stay within 8–10 minutes.'
(OUT.parent/'two_speaker_notes.md').write_text('\n'.join(lines))
# Render code with preserved indentation; retain an editable text item beneath it.
for number, item in enumerate(slides, 1):
    if item['kind'] in ['data', 'code']:
        canvas = Image.new('RGBA', (3360, 1160), (0, 0, 0, 0))
        draw = ImageDraw.Draw(canvas)
        font = ImageFont.truetype('/System/Library/Fonts/Menlo.ttc', 64)
        draw.multiline_text((20, 20), item['body'], font=font, fill=(245,245,245,255), spacing=14)
        canvas.save(OUT/f'code-{number}.png')
(OUT/'slide_plan.json').write_text(json.dumps(slides,indent=2))
(OUT/'verified_data.json').write_text(json.dumps({'combined_counts':dict(counts),'training_records':len(training),'duplicates_removed':112,'source':'local ZIP and saved notebook outputs'},indent=2))

def q(s): return '"'+s.replace('\\','\\\\').replace('"','\\"').replace('\n','\\n')+'"'
# AppleScript supports literal newlines in strings; replace escaped newline below.
def aq(s): return q(s).replace('\\n','\n')
script=['tell application "/Volumes/formac2/Applications/Keynote Creator Studio.app"','tell front document', 'if (count of slides) is not 12 then error "Start from the original 12-slide backup before applying additions."']
# Write original notes before inserting; insert from the end to preserve indices.
for s in slides:
    if s['original']:
        note=f'SPEAKER: {s["speaker"]}\nTARGET: {s["seconds"]} seconds\n\n{s["script"]}\n\nEVIDENCE: {s["source"]}'
        script.append(f'set presenter notes of slide {s["original"]} to {aq(note)}')
for i,s in reversed(list(enumerate(slides,1))):
    note=f'SPEAKER: {s["speaker"]}\nTARGET: {s["seconds"]} seconds\n\n{s["script"]}\n\nEVIDENCE: {s["source"]}'
    if s['original']:
        continue
    # Create at end and move before the next original slide for stable insertion.
    script += ['set newSlide to make new slide at end of slides with properties {base layout:slide layout "Blank"}', 'tell newSlide']
    def text_item(text,x,y,w,h,size,color,font='Helvetica Neue'):
        script.extend([f'set box to make new text item with properties {{object text:{aq(text)}, position:{{{x}, {y}}}, width:{w}, height:{h}}}',f'set font of object text of box to {aq(font)}',f'set size of object text of box to {size}',f'set color of object text of box to {color}'])
    text_item(s['title'],100,70,1720,160,60,'{65535, 47000, 32000}')
    text_item(s['subtitle'],105,225,1710,85,28,'{52000, 52000, 52000}')
    if s['kind']=='chart':
        script.append(f'make new image with properties {{file:POSIX file {aq(str(OUT/s["body"]))}, position:{{110, 325}}, width:1700, height:646}}')
    else:
        size=34 if s['kind']=='data' else 29 if s['kind']=='sources' else 32
        text_item(s['body'],120,350,1680,580,size,'{62000, 62000, 62000}', 'Menlo' if s['kind'] in ['data','code'] else 'Helvetica Neue')
    if s['kind'] in ['data', 'code']:
        script.append('set opacity of box to 0')
        script.append(f'make new image with properties {{file:POSIX file {aq(str(OUT/f"code-{i}.png"))}, position:{{120, 350}}, width:1680, height:580}}')
    text_item('AAI 500  |  '+ ('Descriptive counts: local UCI files' if s['body']=='class_distribution.png' else 'Evidence: saved project notebooks')+'  |  '+str(i),105,1015,1710,40,21,'{47000, 47000, 47000}')
    script += [f'set presenter notes to {aq(note)}','end tell']
    nxt=next((t['original'] for t in slides[i:] if t['original']),None)
    if nxt: script.append(f'move newSlide to before slide {nxt}')
script += ['save','end tell','end tell']
(OUT/'apply_to_keynote.applescript').write_text('\n'.join(script))
print('Slides:',len(slides),'Total seconds:',seconds)
for who in ['Francisco','Lilian']:
 print(who, sum(s['seconds'] for s in slides if s['speaker']==who), 'seconds plus shared close;', sum(len(s['script'].split()) for s in slides if s['speaker']==who),'words')
