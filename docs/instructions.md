## Instructions

Welcome to the **HackFu Online Challenge for 2018**. Captured by air pirates, you will need to use your wits and hackery skills to overcome a variety of complex challenges and avoid having to walk the plank! Do well, and great fortune awaits!

The various encrypted files in these challenges are locked using `AES-256-CBC` and `base64` encoding. You can decrypt them using `openssl`.

`openssl` can be used with command that looks like `openssl enc -aes-256-cbc -base64 -d -K <key_value> -iv <iv_value> -in <input_file> -out <output_file>`.

Once you unlock `challenges.zip.enc`, you will find 10 challenge folders. Each folder contains an instructions file, the files necessary for the challenge, and an encrypted solution file. The challenges range from simple logic problems to complex technical puzzles. You can do the challenges in any order you like, but the story makes much more sense in order of the challenges!

Solving each challenge will give you a passphrase, in the format `hackfu[a-z]+` (sometime passphrases may include uppercase letters -- _you should convert these to lowercase_), which can be used to decrypt the `solution.txt` file for that challenge. In addition to the second part of the story, this file will give you a challenge codename, a unique _UPPERCASE THREE-WORD PHRASE_, which can then be submitted on the challenge website (https://bronzefrog.mwrinfosecurity.com/submit), along with the email address you used to register and a detailed description of how you solved the challenge (_very important!_). Each submission will improve your standing on the HackFu Challenges leaderboard, and increase your chance to win an invite to one of MWR's HackFu events, held in the UK and South Africa.

The challenge will run from **23 April 2018** to **23 July 2018**.

## Thus ...

Just as a quick exercise, the rest of the introduction -- including instructions on how to decrypt the challenges and register online -- is encrypted in the block below. The passphrase is (_without the quotes_): "`hackfuchallenge2018`". All the passphrases you encounter will start with "`hackfu`". _Before attempting to decrypt the solution files for each challenge, convert all passphrases to lower case, with no punctuation and no spaces._

```
U2FsdGVkX1+WDgYAsg0pXZ+IeJViZaMLH/fLCPUT+a/gfrxqLMwXUIDp3KdpFFNn
a5WCHjD7bGp1dUbxtzZFie5UtKipDBcG9S0SOCtRX1InNISVHphXlnRvT1AnGfo3
ddKh4Y1xPJX/bfxZVXEyxC37l+w6GGFbAd/JOECLkJj6kBNkYjlRGSwniLYhcV+M
XIeH/4aNA+bnq5wzj0Se5PtTwlU22gJlj173xOlqJh2sxrtyhgrdYHH7QgqBhZs2
I3d2P2yS6PWu5AbV24j7uNzqMvOnUtiif6bL3nBArYkGZ1UdRK1PjTaNuXIXxM6R
IMQGsJeiyC7LMwBnYpjA3Jf9YAikho4c3tOLYumw4TMWb7Zy9UBp2fSWn+jN8SL6
1dy3h/2k6+hQiHncGQYqa2q09y/mshn+yS4wdpMhYBddkDl9AryavSVQMYF+sWdN
mG1NDXvQrb/b56bAkD9qgf6akpvdKLirsj8Y/xAWtMtIU53AUz/NX99hHxeYIPEh
bZgboI51rrMUdNG03H/kaVjN4axESPnnbjtH6gYLd0egF94HI2TS6RcUo+FrApo6
A2PZ1WbtXtK7qmlIHeMAW6UfKjysWnsIJRt2eFOBJiCEmhIiKyLaaRR0fcZERwji
QYwEE2eactTmaC3upv66d1KEI9JYkYsxttZMuwcFwd1nqAalZ6N4OhCtHeZU/ugM
T2qeSlaFZ7OeKnK1pa8DhcumeRtEpd4oGNsPSJ44hoBnOauB6WgXoX9RCDHSamrd
XCMrXerZvd2SRCs2vw/1ZLKFMREot9nq/hSYFvq6Gb6ZYKip0MBE7ZXQkLrLFFpg
L35FF7IvKO7HjDGs/dd1sB5/JXm1BzKnSav3HE8iA+2CzoAIPhc7O5K2wbeNNKD9
V68lgUtXvLBEvC4+QA3tdEiYn7YVE2L14cZQGs/d5zlJkUPbwlmhyssYyvaOzb8j
XmdtqCsgXF6RQGl8/VkB8kcdUqCSP/79Nbl2i9DCHqJ4gD+tTghd+p08T1LfOf1M
wkY65Ua23mHEO5BWR25maL9bAwO/hHop7IQHpQ5d8mYOgtKIVMWB/7XOapQ/folN
iMpyok3qySQhypygiOk80oapgtqxg8MfjDlQEUh43P5+uLKSr3H9UaVadTzGaQeE
oLu/GltMjtRmi8o3X/QKjexVc2DT6l6vEMX9iAzXy8tTh0q2Cfx34b0AOf2SuQgo
CjhHdRIUR31fz5goM26rQYhgXsK56PjwaqWar+EQICnliw14WC40PFvrxhnzcHYl
q01x0egsGnChbKqDHugYn/7BTGugPsGezjkbG3pLS1QfNDS8c7okFwETFu5g16VP
```

## Explanation

The above text is encrypted using AES-256-CBC with base64 input, we use `openssl` with the following command `openssl enc -aes-256-cbc -base64 -d -pass pass:hackfuchallenge2018 -in code.enc -out code.out`, where `code.enc` is the ciphertext (copy-and-paste the text above into a separate file) and `code.out` is the resulting plaintext.

The result is shown as follows

>Ah, good, at least we know you can decrypt stuff. You can decrypt the challenges themselves with the passphrase "hackfutrueplacesneveraredownonanymap".<br>
If you would like to register for the HackFu Online Challenge 2018 now, you can do so. Please send us an email with the following:<br>
Subject: Hackfu Online Challenge 2018 - Registration<br>
Email address: bronzefrog@mwrinfosecurity.com<br>
Body: Tell us who you are and where you are from (country). Also tell us what you are currently doing (Student / Developer / Scientist / Lab Rat / Dictator / Dr Evil etc.) and provide us with a user handle we can assign to you and use to publish your progess on our leaderboard at https://bronzefrog.mwrinfosecurity.com<br>
If you're interested in an internship and/or permanent position at MWR InfoSecurity, feel free to indicate as such and include your CV with your email.<br>
We will post occasional hints where necessary here, at our own discretion }:-]<br>
https://twitter.com/mwrinfosecurity<br>
Good luck, sky pirate!

Now, you can decrypt all the challenges using `openssl enc -aes-256-cbc -base64 -d -pass pass:hackfutrueplacesneveraredownonanymap -in challenges.zip.enc -out challenges.zip`. Then, use your favorite tool to unzip the file.
