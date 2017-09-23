from rhymeless import Rhymeless
poem_generator = Rhymeless()
book = open("source_text.txt", "r")
lines = []
for line in book:
    lines.append(line)
 
book = "".join(lines)

poem_generator.train(book)
poem = poem_generator.generate_poem()

print poem

text_file = open("../poem_output.html", "w")
text_file.write(poem)
text_file.close()