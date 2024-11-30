import re

text = input("Enter a text: ")
# Add spaces between letters and numbers
formatted_text = re.sub(r"([a-zA-Z])([0-9])", r"\1 \2", text)
# Add spaces between numbers and letters
formatted_text = re.sub(r"([0-9])([a-zA-Z])", r"\1 \2", formatted_text)
# Add spaces for specific units or symbols
formatted_text = re.sub(r"ms", r"ms ", formatted_text)
formatted_text = re.sub(r"%", r" % ", formatted_text)
formatted_text = re.sub(r"MB", r" MB ", formatted_text)
formatted_text = re.sub(r"Complexity", r"", formatted_text)
formatted_text = re.sub(r"Analyze", r"", formatted_text)
# Remove multiple spaces
formatted_text = re.sub(r"\s+", " ", formatted_text).strip()



print(formatted_text)

# text = input("Enter a text: ")

# one_liner = " ".join(word for word in text.split() if word.lower() != "complexity" and word.lower() != "analyze")
# print(one_liner)