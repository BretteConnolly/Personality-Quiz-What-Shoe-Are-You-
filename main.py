def main():
    print("What Shoe Are You? \n A series of multiple choice " 
          "questions will follow. Please respond with the uppercase letter "   
          "of the answer choice (no punctuation).")
    print()
    # Quiz_results starts as an empty list. It will store the quiztaker's answer choices.
    quiz_results = []
  
    # For a benchmark, the quiztaker is asked which type of shoe they 
    # like best, and this shoe is their benchmark result.
    # At the end of the quiz, their result is compared to their benchmark
    # result, and the answer to each question is evaluated to see whether
    # it matches the benchmark result. Questions with answers that match the
    # benchmark result are considered more valid.
    benchmark = input("What is your favorite type of shoe? " 
      "A. Brogues or pumps " 
      "B. Boat shoes or flats "
      "C. Canvas sneakers " 
      "D. Sneakers " 
      "E. Sandals ")
    benchmark = benchmark.upper()
          
    answer1 = input("It's the weekend! What do you want to do? " 
                    "A. Go to a museum "
                    "B. Spend time with family " 
                    "C. Party! " 
                    "D. Go on a trip " 
                    "E. Kick back and relax ")
    #Lowercase answers are corrected with the .upper method.
    quiz_results.append(answer1.upper())   
    print ("\n")
        
    answer2 = input("What matters most to you when you put together an outfit? "
                    "A. Will it impress others? " 
                    "B. Is it classic? " 
                    "C. Is it creative? "
                    "D. Is it me? "
                    "E. Is it comfortable? ")
    quiz_results.append(answer2.upper())
    print ("\n")
        
    answer3 = input("Which statement describes you best? " 
                    "A. I demand a lot of myself. " 
                    "B. I am happiest when I'm helping someone. "
                    "C. I am always hungry for more knowledge. " 
                    "D. I don't depend on anyone but myself. " 
                    "E. I never feel too emotional. ")
    quiz_results.append(answer3.upper()) 
    print ("\n")
        
    answer4 = input("Where would you like to live? " 
                    "A. The most upscale area I can afford " 
                    "B. Close to family "
                    "C. In an area with a lot of culture " 
                    "D. In a big city " 
                    "E. Somewhere quiet ")
    quiz_results.append(answer4.upper())  
    print ("\n")
        
    answer5 = input("What makes you happiest? "
                    "A. Doing something exceptionally well "
                    "B. Being with others " 
                    "C. Creating something " 
                    "D. Doing whatever I want! "
                    "E. Enjoying the present moment ")
    quiz_results.append(answer5.upper())      
    print ("\n")
        
    answer6 = input("How would you describe your personal style? " 
                    "A. Planned and perfected " 
                    "B. Conservative and classic "
                    "C. Imaginative " 
                    "D. Comfortable "
                    "E. Relaxed ")
    quiz_results.append(answer6.upper()) 
    print ("\n")
        
    answer7 = input("Which statement do you agree with most? "
                    "A. I don't shirk my duties. "
                    "B. I make people feel at ease. " 
                    "C. I have a great imagination. "
                    "D. I am happy without close relationships. "
                    "E. I don't have to be perfect. ")
    quiz_results.append(answer7.upper())
    print ("\n")
        
    # The user's result is calculated based on which letter they
    # answered the most.
    A = 0
    B = 0                  
    C = 0
    D = 0
    E = 0
    for answer in quiz_results:
      if answer == "A":
        A += 1
      elif answer == "B":
        B += 1
      elif answer == "C":
        C += 1
      elif answer == "D":
        D += 1
      else:
        E += 1

    result = max(A, B, C, D, E)
    print(result)
    print(benchmark)
    if result == A:
      print("Brogues and Pumps \n You always look amazing, and you're"
                                  " someone who takes great care in their"
                                  " appearance. You demand a lot of yourself, "
                                  "always striving to meet your own high" 
                                  " standards. You thrive on intimate" 
                                  " supportive relationships that are stable" 
                                  " and long-lasting.")
      # Match each result to the benchmark to see if the quiz result reflects the user's true shoe preference.
      if benchmark == "A":
        print("Result matches true preference!")
    elif result == B:
      print("Boat Shoes and Flats \n Your shoes are comfortable and"
                              " they're not flashy or ostentatious. You've got"
                              " nothing to prove. You are compassionate,"
                              " friendly, generous, and modest. You can often"
                              " be found where you're needed, helping friends,"
                              " loved ones, and others in need.")
      if benchmark == "B":
        print("Result matches true preference!")
      
    elif result == C:
      print("Canvas Sneakers \n You're creative and curious! Your"
                          " comfortable yet quirky shoes go with your"
                          " inquisitive nature and your search for knowledge"
                          " and understanding. You're always open to trying new"
                          " things.")
      if benchmark == "C":
        print("Result matches true preference!")
      
    elif result == D:
      print("Sneakers \n Independent and self-sufficient, you"
                          " don't depend on anyone else to get what you want."
                          " Your shoes reflect your self-reliant nature --"
                          " -- you wear what's right for you and don't need to"
                          " impress others with fancy shoes.")
      if benchmark == "D":
        print("Result matches true preference!")
      
    else:
      print("Sandals \n Your feet are firmly on the ground:"
                          " you are perpetually calm and even-tempered. You"
                          " don't let your emotions get the better of you! You"
                          " help others work through their problems by staying"
                          " grounded and thoughtful.")
      if benchmark == "E":
        print("Result matches true preference!")

    # Evaluate which questions had answers that matched the user's true preference. These are considered more valid questions. 
    index = 1
    for answer in quiz_results:
      print(index)
      if answer == benchmark:
        print("Match")
      else:
        print("Not a Match")
      index += 1


if __name__ == "__main__":
    main()