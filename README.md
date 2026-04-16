# 🐍 CodeAlpha Python Internship

## Overview

This repository contains all four Python Development internship tasks for **CodeAlpha**. Each task is implemented as a standalone Python script featuring clean input/output, input validation, error handling, and modular code structure.

**Libraries used:** `random`, `os`, `re`, `shutil`, `csv`, `datetime`

---

## Tasks

### Task 1 — Hangman Game

**Objective:** Build an interactive word-guessing game played entirely in the console.

**Approach:**
- Randomly selects a word from a predefined list of 5 words
- Displays blanks for each letter and reveals correct guesses
- Tracks guessed letters and remaining attempts (limit: 6 incorrect guesses)
- Handles invalid input (non-letters, repeated guesses, multi-character entries)

**Key Concepts Used:** `random`, `while` loop, `if-else`, strings, lists

---

### Task 2 — Stock Portfolio Tracker

**Objective:** Build a console-based stock tracker that calculates total investment value.

**Approach:**
- User inputs stock symbols and quantities interactively
- Uses a hardcoded price dictionary (7 stocks: AAPL, TSLA, GOOGL, AMZN, MSFT, META, NFLX)
- Displays a formatted summary table with per-stock value and grand total
- Optionally exports the portfolio to a `.csv` file

**Key Concepts Used:** `dict`, `input/output`, arithmetic, `csv` file handling

---

### Task 3 — Task Automation Scripts

**Objective:** Automate two small, real-life repetitive file management tasks.

**Approach:**
- **Tool 1 — Move JPG Files:** Scans the current working directory and moves all `.jpg` files into a `jpg_images/` subfolder using `os` and `shutil`
- **Tool 2 — Extract Emails:** Reads a user-specified `.txt` file, extracts all unique email addresses using `re.findall()`, and saves results to `extracted_emails.txt`
- Both tools are accessible through a simple numbered menu

**Key Concepts Used:** `os`, `shutil`, `re`, file handling

---

### Task 4 — Rule-Based Chatbot

**Objective:** Build a simple conversational chatbot that responds to common user inputs.

**Approach:**
- Matches user input against keywords (greetings, questions, farewells, jokes, etc.)
- Returns randomized replies to avoid repetitive responses
- Includes a live date/time feature using `datetime`
- Exits gracefully when user types `bye` or `quit`

**Key Concepts Used:** `if-elif`, functions, loops, `input/output`, `random`, `datetime`

---

## Results Summary

| Task   | Project                  | Key Feature                        | Concepts                        |
|--------|--------------------------|------------------------------------|---------------------------------|
| Task 1 | Hangman Game             | 6-attempt word guessing game       | random, loops, strings, lists   |
| Task 2 | Stock Portfolio Tracker  | Investment calculator + CSV export | dict, arithmetic, file handling |
| Task 3 | Task Automation Scripts  | JPG mover + Email extractor        | os, shutil, re, file handling   |
| Task 4 | Rule-Based Chatbot       | Keyword-based conversational bot   | if-elif, functions, loops       |

---
