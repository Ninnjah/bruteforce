# Bruteforce

![Banner](https://github.com/Ninnjah/bruteforce/blob/master/banner.JPG)

Simple bruteforce on python.
It's generate a password and compare this password with yours.
Bruteforce have 3 modes:
1. Generating password from letter
2. Generating password from letter and digits
3. Generating password from letter, digits and symbols

- Generate password
```python
while i < len(host):
    password = password + random.choice(charsn)
    i += 1
```
