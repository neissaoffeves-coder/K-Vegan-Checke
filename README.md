# K-Vegan-Checke
# 🇰🇷 K-Vegan Checker: AI-Powered Ingredient Analysis (Apple M4)

This project is a high-precision, local AI expert system designed to help vegan consumers navigate the South Korean food market. Using **Google Gemma 2** and the **Apple M4 chip**, it analyzes complex Korean ingredient lists to detect hidden animal products and factory cross-contamination.

## 🌟 Overview
The Korean food market often uses seafood-based seasonings, bone broths, and hidden animal additives that standard translation tools fail to identify. This project uses **Prompt Engineering** and **Local LLM inference** to provide a 100% private and accurate dietary assistant.

## 🛠 Tech Stack
- **AI Model:** Google Gemma 2 (Instruct)
- **Hardware:** Apple M4 Silicon (MacBook Pro/Air)
- **Environment:** LM Studio / Local Inference
- **Logic:** Custom-engineered "Knowledge-Injected" System Prompt

## 🧠 Key Features
- **Deep Ingredient Analysis:** Scans for over 50+ specific Korean terms for meat, seafood, dairy, and animal-derived additives.
- **Factory Trace Detection:** Automatically identifies "Traces" warnings (*제조시설 / 같은 제조*) to alert users of potential cross-contamination.
- **M4 Optimized:** Designed for the high-speed unified memory of Apple M4, ensuring sub-second analysis.
- **Privacy First:** 100% offline. No image or text data ever leaves your device.

## 📁 Repository Structure
- `system_prompt.txt`: The core "brain" of the project. Contains the exhaustive Korean-English dictionary and decision logic.
- `README.md`: Project documentation.
- `[YOUR_STUDENT_ID].pdf`: The full academic report.

## 🚀 How to Use
1. **Setup:** Install [LM Studio](https://lmstudio.ai/) on your Mac M4.
2. **Model:** Download the **Gemma 2 9B (Instruct)** model.
3. **Configure:** Copy the contents of `system_prompt.txt` into the "System Prompt" field in LM Studio.
4. **Parameters:** Set `Temperature` to **0.1** for factual accuracy.
5. **Analyze:** Copy Korean text from an image (using macOS Live Text) or provide a photo. The AI will output a strict ✅, ❌, or ⚠️ status.

## 📝 Example Output
> **Input:** 원재료명: 밀가루, 설탕, 멸치액젓, 소금.
> 
> **Output:** 
> ❌ NOT VEGAN
> Cause: contains anchovy fish sauce (멸치액젓)
