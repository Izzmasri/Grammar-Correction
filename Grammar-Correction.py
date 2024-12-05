from textblob import TextBlob

def correcr_grammar(text):
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    return corrected_text

while True:  
    try:
        text = input("Enter your Sentence: ")
        if text == correcr_grammar(text):
            print("Your Sentence is correct")
        else:
            corrected_text = correcr_grammar(text)
            print("Corrected: {}".format(corrected_text))
        print("\n Enter Ctrl + C to exit")
    except KeyboardInterrupt:  
        print("\nExiting the program.")
        break
