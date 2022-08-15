let_freq = {}
for num in range(97, 123):
    key = chr(num)
    let_freq[key] = 0

with open('words.txt', 'r') as f:
    all_words = f.readlines()

counter = 1
for word in all_words:
    for index in range(0, 5):
        letter = word[index]
        let_freq[letter] += 1
    print(f'Words checked: {counter}')
    counter += 1

print(let_freq)

scores = {}
for a in range(26):
    greatest = 0
    for i in let_freq:
        if let_freq[i] > greatest:
            let = i
            greatest = let_freq[i]
    scores[let] = greatest / 1000
    del let_freq[let]

print(scores)
