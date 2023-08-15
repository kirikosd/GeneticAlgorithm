import gen_alg

solution, generation, temp = gen_alg.run()

if temp:
    print(f"Solution:{solution}\nGeneration:{generation}")
else:
    print("The generation limit was reached before a perfect solution was found")
