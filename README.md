# Offline OCR for Industrial / Stenciled Text #

📖 Overview

This project implements a fully offline Optical Character Recognition (OCR) system designed specifically for industrial and military-style stencil text extraction.

The system is built to handle:

Faded paint

Low contrast

Surface damage

Broken stencil characters

Uneven lighting

The architecture prioritizes robustness and offline deployability over cloud-dependent solutions.

🎯 Objective

To design an OCR pipeline that:

Works completely offline

Does not rely on internet APIs

Extracts structured text from industrial boxes

Produces clean, digital output

🧠 System Architecture

The OCR pipeline consists of:

Advanced image preprocessing

Text detection (EasyOCR CRAFT-based detector)

Text recognition (EasyOCR recognition head)

Post-processing and structured reconstruction

🔍 Why EasyOCR?

EasyOCR was selected because:

Fully offline capability

CRAFT-based text detection

Deep learning-based recognition

Robust multi-language support

Easy integration into deployment pipelines

Unlike cloud OCR APIs, EasyOCR:

Requires no internet

Ensures data privacy

Supports industrial edge deployment

🔬 Why CRAFT Text Detector?

CRAFT (Character Region Awareness for Text Detection) was chosen because:

Detects individual character regions

Handles irregular text layouts

Robust against distortions

Performs well on stencil-style fonts

Industrial stencil text often contains broken strokes and non-uniform spacing. CRAFT’s character-level detection makes it well-suited for such scenarios.

🛠 Preprocessing Strategy

Industrial stencil text poses unique challenges:

Faded paint

Background noise

Broken characters

Low contrast

To address these:

CLAHE (Contrast Limited Adaptive Histogram Equalization)

Adaptive thresholding

Morphological closing

Multi-scale detection

This improves character continuity and enhances readability before recognition.

🧠 Why No Cloud-Based OCR?

The system was intentionally designed to:

Avoid internet dependency

Maintain data confidentiality

Support military/industrial environments

Ensure deterministic offline performance

All model weights are stored locally and loaded using strict offline mode.

📦 Structured Output

The OCR system produces:

Bounding boxes

Cleaned uppercase text

Confidence scores

Line-level reconstruction

Output format is structured JSON for integration with downstream systems.

🏭 Industrial Suitability

100% offline

No runtime downloads

Edge-device compatible

Modular and extensible

Suitable for logistics, warehousing, defense labeling systems

🚧 Challenges Faced

Domain gap between stencil fonts and standard OCR training data

Broken character strokes

Low-contrast backgrounds

Overlapping detections

Offline model packaging

🔮 Possible Improvements

Fine-tuning OCR on synthetic stencil dataset

Custom CRNN trained on military fonts

Semantic correction using domain-specific language models

Improved line grouping using clustering methods
