score = 0
prize = 0

questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Actor", "Astronaut", "Plumber", 1],
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Lisbon", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 1],
    ["Who invented the light bulb?", "Albert Einstein", "Thomas Edison", "Isaac Newton", "Nikola Tesla", 1],
    ["Which language is used to create web pages?", "Python", "HTML", "C++", "Java", 1],
    ["How many continents are there?", "5", "6", "7", "8", 2],
    ["Which gas do plants absorb?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 2],
    ["What is the national animal of India?", "Lion", "Tiger", "Elephant", "Leopard", 1],
    ["Which country is known as the Land of the Rising Sun?", "China", "South Korea", "Japan", "Thailand", 2],
    ["Who painted the Mona Lisa?", "Picasso", "Leonardo da Vinci", "Van Gogh", "Michelangelo", 1],
    ["Which is the longest river in the world?", "Amazon", "Ganga", "Nile", "Yangtze", 2],
    ["What is the boiling point of water?", "90°C", "80°C", "100°C", "120°C", 2],
    ["Who wrote 'Romeo and Juliet'?", "Shakespeare", "Mark Twain", "J.K. Rowling", "Charles Dickens", 0],
    ["What is the currency of Japan?", "Yen", "Won", "Dollar", "Peso", 0],
    ["Which is the smallest prime number?", "0", "1", "2", "3", 2]
]

prizes = [100000, 200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000,
          1100000, 1200000, 1300000, 1400000, 1500000]

for i, que in enumerate(questions):
    print(f"\nQuestion {i + 1}: {que[0]}")
    print(f"  1. A: {que[1]}")
    print(f"  2. B: {que[2]}")
    print(f"  3. C: {que[3]}")
    print(f"  4. D: {que[4]}")

    try:
        a = int(input("\nEnter your option:\nA press 1\nB press 2\nC press 3\nD press 4\nYour answer: ")) - 1
        if a == que[5]:
            score += 1
            prize += prizes[i]
            print("✅ Correct answer!")
        else:
            print("❌ Wrong answer.")
    except:
        print("⚠️ Invalid input. Skipping this question.")

print(f"\n🎉 Your final score is {score} and you won a total prize of ₹{prize}")
