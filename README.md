# similarity
Uses embeddings to determine similar results.

Usage:

```python
sentences = {
  'You are awesome!': 1,
  'You aren't so great.': 0,
  'Hmm, I don't know': 0,
  'Oh yeah nice work!': 1,
  ...
}

from similarity import similar
sim = similar(sentences)

tests = [
  "Whoa! Never thought of that before! Cool!",
  "Nah, this is not it..."
]

for i in tests:
    print(i)
    out = sim.similar(i, max=1) # max is amount of results returned
    if out[0] == 1:
        print("Positive!")
    else:
        print("Negative!")
    print()
```
