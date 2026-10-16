#!/bin/bash
set -e

if [ ! -f "data/trained_model.pkl" ]; then
    python train.py
fi

streamlit run app.py --server.port 8501 --server.address 0.0.0.0
