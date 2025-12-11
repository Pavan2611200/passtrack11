# passtrack11
# Password Brute Force Simulator (Python)

This project is a **simple brute-force password guessing simulator** created for learning purposes.  
It shows how a computer can try every possible combination of letters and numbers to guess a password.

⚠️ **Important:**  
This project is only for **educational and fun practice**.  
Never use brute force against real accounts, websites, or personal data.  


## 🚀 Features
- Tries all combinations of characters (a–z, A–Z, 0–9)
- Uses `itertools.product` to generate combinations efficiently
- Works for any small password (1–length of password)
- Shows each guess in real time
- Helps beginners understand:
  - loops  
  - combinations  
  - brute-force search  
  - Python string handling  

---

## 📌 How It Works
1. You enter a password.
2. The script generates combinations of characters:
   - a, b, c ... z  
   - A, B, C ... Z  
   - 0, 1, 2 ... 9  
3. It compares each generated string with your password.
4. When both match → it prints:
