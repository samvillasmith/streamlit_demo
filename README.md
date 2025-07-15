# streamlit\_demo

> A compact Streamlit demo with interactive widgets, basic plotting, and clean Python code. Useful for getting familiar with Streamlit's building blocks.

---

## 📁 Folder Structure

```text
streamlit_demo/
├── app.py              # main dashboard – text, chart, and interactivity
├── widgets.py          # reusable Streamlit widgets (input forms, sliders)
├── classification.py   # iris classifier with sliders + sklearn RandomForest
├── requirements.txt    # streamlit + pandas + scikit-learn
```

---

## 🚀 Getting Started

```bash
# clone the repo
git clone https://github.com/samvillasmith/streamlit_demo.git && cd streamlit_demo

# create virtual environment
python -m venv .venv && source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate                               # Windows

# install dependencies
pip install -r requirements.txt

# launch any Streamlit app
streamlit run app.py
streamlit run classification.py
streamlit run widgets.py
```

---

## 🎯 What's Inside

* `app.py` — Demonstrates layout, markdown, data input/output, and basic plotting.
* `classification.py` — A simple classifier using scikit-learn on the Iris dataset with interactive sliders.
* `widgets.py` — Modular input forms and slider functions for reuse.

---

## 📝 License

MIT – use, learn, fork.

<sub>Last updated: July 15, 2025</sub>
---
