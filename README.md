## NATO Phonetic Alphabet Converter - How it works

This program converts any name into **NATO phonetic code words** (Alpha, Bravo, Charlie, etc.).

### What is used

- `pandas` module: to read the CSV file
- Dictionary comprehension: to create letter-to-code mapping
- `try/except`: to handle invalid input
- Recursion: to ask again if input is wrong

### How it works

1. Reads `nato_phonetic_alphabet.csv` which contains letters and their code words
2. Creates a dictionary like: `{"A": "Alpha", "B": "Bravo", ...}`
3. Asks user to enter a name
4. Converts each letter to its NATO code word
5. Prints the result as a list

### Example

**Input:**
```
Enter your name: John
```

**Output:**
```
['Juliett', 'Oscar', 'Hotel', 'November']
```

### Error handling

- Only letters are allowed
- Numbers and symbols will show an error message
- Program asks for input again

### File format (CSV)

| letter | code |
|--------|------|
| A | Alpha |
| B | Bravo |
| C | Charlie |
| ... | ... |

---

