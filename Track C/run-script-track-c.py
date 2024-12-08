#!/bin/bash

{
    # Create and activate virtual environment
    python -m venv venv
    source venv/bin/activate

    # Install required packages
    pip install torch pandas numpy scikit-learn gensim tqdm

    echo '========== Starting Multilingual Emotion Detection =========='
    python multilingual_emotion.py submission.csv

    # Deactivate virtual environment
    deactivate

} 2>&1 | tee run_log.txt  # record all outputs