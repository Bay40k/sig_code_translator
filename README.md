# Pharmaceutical Signa Translator
Simple script for converting sigs to English and back

# signa `[sig´nah]` (*L.*)
1. mark or write; abbreviated S. or sig. in prescriptions, followed by the signature.
2. *verb.* (used imperatively, in prescriptions) mark; write; label.

> The "Sig" is the directions to follow by the provider to the patient for a given medication. Below are listed the most common abbreviations that are used in the Sig. "Sig" is an abbreviation for the Latin word "signetur," which means "let it be labeled." 

Source: https://denalirx.com/sig-explanations/

### Usage:
```commandline
git clone https://github.com/Bay40k/sig_code_translator
python -m sig_code_translator
```

###### Example output:
```text
Sig Code Translator
(square brackets denote default option)
1. [To English], 2. To Sig: 
Enter pharmacy sig: tk 2 t d prn
TAKE 2 TABLET DAILY AS NEEDED

1. [To English], 2. To Sig: 2
Enter instructions: take 1 capsule daily as needed for pain
TK 1 C D PRF P
```

### Embedding:

```python
import sig_code_translator

# Inputs are case insensitive
print(sig_code_translator.from_sig("tk 2 t d prn"))
# Output: TAKE 2 TABLET DAILY AS NEEDED

print(sig_code_translator.to_sig("take 1 capsule daily as needed for pain"))
# Output: TK 1 C D PRF P
```
