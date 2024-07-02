import aspose.pdf as ap
from datetime import date
import tkinter as tk

# Load the PDF document




#REPLACE TEXT-----------------------------------------------------------------------------
def replace(lines_list):
    document = ap.Document("OriginalFile.pdf")
    j = 1
    # Instantiate a TextFragmentAbsorber object
    for i in range(0,9):
        txtAbsorber = ap.text.TextFragmentAbsorber("Producto" + str(j))
        # Search text
        document.pages.accept(txtAbsorber)
        # Get reference to the found text fragments
        textFragmentCollection = txtAbsorber.text_fragments
        # Parse all the searched text fragments and replace text
        for txtFragment in textFragmentCollection:
            txtFragment.text = variables[i].get()
        j += 1
        
    #about images
    mainImage = ""
    if "Arroz de pollo" in lines_list:
        mainImage = "arroz"
    elif "Pechuga a la plancha en chimichurri" in lines_list:
        mainImage = "pollochi"   
    elif "Espagueti napolitano" in lines_list:
        mainImage = "spaghetti"   
    elif "Frijoles" in lines_list:
        mainImage = "frijol"
    elif "Sopa de ajiaco" in lines_list:
        mainImage = "sopa"
    elif "Sopa de colicero" in lines_list:
        mainImage = "sopa"
    elif "Garbanzos" in lines_list:
        mainImage = "garbanzo"
    elif "Lentejas" in lines_list:
        mainImage = "lenteja"
    elif "Lentejas criollas" in lines_list:
        mainImage = "lenteja"
    elif "Sopa de conchas" in lines_list:
        mainImage = "sopaconcha"
    elif "Sopa de verduras" in lines_list:
        mainImage = "sopaverdura"
    elif "Pechua a la plancha en chimichurri" in lines_list:
        mainImage = "pollochi"
        
        
    image_file="C:/Users/YourUser/Desktop/" + str(mainImage) + ".png"
    document.pages[1].add_image(image_file, ap.Rectangle(100, 480, 1200, -100, True))
        
    today_date = date.today()
    print("Done!")
    # Save the updated PDF
    document.save("MenuAlmuerzo" + str(today_date) + ".pdf")





def on_button_click():
    # This function will be called when the button is clicked
    input_text = text_box.get("1.0", "end-1c")  # Get the text from the text box
    lines = input_text.split('\n')  # Split the text into lines
    lines_list = [line.strip() for line in lines if line.strip()]
    for i, line in enumerate(lines):
        if line.strip():  # Skip empty lines
            variables[i].set(line)
    replace(lines_list)





#INTERFASE-----------------------------------------------------------------------------------------------------------
# Create the main application window
app = tk.Tk()
app.title("Save Text in Different Variables")

# Create a text box that allows multiple lines
text_box = tk.Text(app, height=15, width=40)
text_box.pack(padx=10, pady=20)

# Create a button
button = tk.Button(app, text="Save Lines", command=on_button_click)
button.pack(pady=10)

# Create variables to store each line of text
num_lines = 9  # Set the number of lines you want to handle
variables = [tk.StringVar() for _ in range(num_lines)]

# Display the variables (optional)
for i, var in enumerate(variables):
    label = tk.Label(app, text=f"Variable {i + 1}:")
    label.pack()
    entry = tk.Entry(app, textvariable=var, state='readonly')
    entry.pack()

# Start the Tkinter event loop
app.mainloop()


