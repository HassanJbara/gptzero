# GPTZero

GPTZero is an AI model with some mathematical formulation to determine if a particular text fed to it is written by AI or a human being.
This repository is a fork of the open-source implementation of GPTZero, refactored as a Python package.

## Installation

```bash
pip install gptzero@git+https://github.com/HassanJbara/gptzero
```

## Usage

### Script

```bash
python main.py
```

#### Code

```python
from gptzero import GPTZero

zero_gpt = GPTZero()
text = "I love you"

zero_gpt.get_score(text)
```  
