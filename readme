# K-Vegan Checker v5 🌱

Hey! So this is my upgraded vegan ingredient checker. The original version (v4) used Gemma 2 locally on my Mac, which worked pretty well, but it had a major annoying problem: you had to manually copy-paste ingredient lists. Standing in a Korean supermarket trying to copy text from a label is... not fun.

This version adds vision stuff (Vision Transformers, CLIP, BLIP-2) so you can just take a photo of the label and it analyzes it directly. No manual typing.

## What does it do?

- Takes an image of a food label (or raw ingredient text if you're lazy)
- Detects Korean non-vegan ingredients (meat, seafood, dairy, weird additives)
- Checks for manufacturing warnings (like "may contain milk" stuff)
- Tells you: ✅ VEGAN, ❌ NOT VEGAN, or ⚠️ MAYBE (traces)
- Runs locally on your Mac = privacy, no cloud BS

## Quick Start

### You need:
- Python 3.9 or newer
- A Mac with reasonable specs (M1/M2/M3/M4 ideally, but CPU works too—slower)
- Like 12GB of disk space for the AI models

### Setup (takes ~5 min):

```bash
# Create a folder
mkdir k-vegan && cd k-vegan

# Make a virtual environment (keeps things clean)
python3 -m venv venv
source venv/bin/activate

# Install stuff
pip install --upgrade pip
pip install torch torchvision transformers Pillow numpy
```

### First time only: Download the models

```bash
python3 << 'PYTHON'
print("Downloading models... this takes a few minutes")
from transformers import CLIPModel, CLIPProcessor, Blip2ForConditionalGeneration, Blip2Processor

CLIPModel.from_pretrained('openai/clip-vit-base-patch32')
CLIPProcessor.from_pretrained('openai/clip-vit-base-patch32')
print("✅ CLIP done")

Blip2ForConditionalGeneration.from_pretrained('Salesforce/blip2-flan-t5-xl', torch_dtype='float16')
Blip2Processor.from_pretrained('Salesforce/blip2-flan-t5-xl')
print("✅ BLIP-2 done")
PYTHON
```

### Use it:

**Option 1: Text** (fastest)
```bash
python k_vegan_clip_blip.py "밀가루, 설탕, 멸치액젓, 소금"
```

Output:
```
❌ NOT VEGAN
Cause: Contains 멸치액젓
```

**Option 2: Image** (cooler)
```bash
python k_vegan_clip_blip.py food_label.jpg
```

Takes a few seconds, then tells you what's in it.

## How it actually works

Three stages:

**1. You give it input** → Text or a photo

**2. CLIP analyzes it** → Compares the image against ingredient keywords (anchovy, pork, dairy, etc.) using a shared semantic space. Scores how likely each ingredient is present.

**3. BLIP-2 explains it** → Generates a Korean description of what ingredients it sees, then cross-checks against the dictionary.

Result: ✅/❌/⚠️

## What it detects

- **Meat:** beef, pork, chicken, bacon, ham, meat broth, bone stock
- **Seafood:** anchovy, anchovy sauce (멸치액젓—super common), shrimp, squid, crab, oyster, fish sauce, salted seafood pastes
- **Dairy:** milk, butter, cheese, cream, eggs
- **Weird stuff:** honey, gelatin, collagen, carmine (red dye from bugs)

Plus it flags "may contain" warnings if you care about traces.

## Important stuff

- **Privacy:** Everything runs on your Mac. Nothing leaves your computer. Not even telemetry.
- **Speed:** Text analysis is instant (<100ms). Images take 3-5 seconds (includes AI thinking).
- **Accuracy:** On my test cases, it got everything right. But it's not perfect—new brands, weird regional ingredients might confuse it.
- **Offline:** After downloading models, you don't need internet.

## Limitations

- If the label is blurry/glared, the AI might miss stuff
- Only knows ~40 common non-vegan Korean ingredients—doesn't know every brand-specific thing
- Manufacturing warnings are just rule-based (looking for keywords), so false positives/negatives possible
- The ingredient dictionary is static (not updating in real-time)

## If something breaks

### "Out of memory"
```bash
# Use CPU instead (slower but works)
python k_vegan_clip_blip.py image.jpg --device cpu
```

### "Models won't download"
Make sure you have internet and HuggingFace access isn't blocked. If stuck:
```bash
huggingface-cli login
```

### It's slow
- First run loads models from disk (~5 min total)
- Subsequent runs are cached (much faster)
- Images on M1/M2 are slow; M4 is way faster
- If you're on Intel Mac + CPU, yeah it's gonna be slow

## File structure

```
k-vegan-checker/
├── k_vegan_clip_blip.py    # Main code
├── test_it.py              # Tests (run this to check if it works)
├── README.md               # This file
└── venv/                   # Virtual environment (auto-created)
```

## Papers I'm citing

If you care about the research:
- Vision Transformers (ViT): https://arxiv.org/abs/2010.11929
- CLIP: https://arxiv.org/abs/2103.00020
- BLIP-2: https://arxiv.org/abs/2301.12597
- OCR benchmarks: https://arxiv.org/abs/2510.03570
- Korean fine-tuning: https://arxiv.org/abs/2403.16444

## Future ideas

If I keep working on this:
- Mobile app (iOS/Android) so you can use it in actual supermarkets
- Community ingredient database (crowdsourced)
- Fine-tuning on Korean-specific food labels
- Better handling of ambiguous ingredients
- Maybe a website version

## Final note

This started because I got frustrated manually checking every Korean food ingredient in the supermarket. The AI is supposed to make life easier, not more complicated. If it's being annoying to set up, that's a bug on my end.

Good luck! 🌱
