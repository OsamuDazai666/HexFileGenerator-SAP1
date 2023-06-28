#importing the module
import customtkinter
from CTkMessagebox import CTkMessagebox

instruction_options = ["Null", "LDA", "ADD", "SUB", "JMP", "OUT", "HLT"]

location_options = ["Null", '0H', '1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', '11H', '12H', '13H', '14H', '15H']

def checksum(str_bytes):
    """ Calculates the Checksum for the hex-file"""
    decimals = []
    for byte in str_bytes:
        try:
            decimals.append(int(byte, 16))
        except ValueError:
            show_error()
    decimal_sum = sum(decimals)
    ones_complement = hex(decimal_sum ^ 0xFF)
    ones_complement_decimal = int(ones_complement, 16)
    twos_complement = hex(ones_complement_decimal + 1)

    string_two_complement = str(twos_complement) 
    check_sum = string_two_complement[-2] + string_two_complement[-1]

    return check_sum.upper()

def show_error():
    CTkMessagebox(title="Error", message="you have left a data field empty", icon="cancel")


def hex_file_generator(root):

    def generate_file():
        #list of instruction
        instructions = [i0.get(), i1.get(), i2.get(), i3.get(), i4.get(), i5.get(), i6.get(), i7.get(), i8.get(), i9.get(), i10.get(), i11.get(), i12.get(), i13.get(), i14.get(), i15.get()]
        #list of locations
        locations = [loc0.get(), loc1.get(), loc2.get(), loc3.get(), loc4.get(), loc5.get(), loc6.get(), loc7.get(), loc8.get(), loc9.get(), loc10.get(), loc11.get(), loc12.get(), loc13.get(), loc14.get(), loc15.get()]
        
        # text to add in the hex-file
        file_txt = ':10000000'
        
        list_for_checksum = ['10']
        #checking the instruction
        for i in range(len(instructions)):
            split_loc = locations[i].split('H')
            loc = split_loc[0]
            one_byte = ''

            if  loc == '10':
                loc = 'A'
            elif loc == '11':
                loc = 'B'
            elif loc == '12':
                loc = 'C'
            elif loc == '13':
                loc = 'D'
            elif loc == '14':
                loc = 'E'
            elif loc == '15':
                loc = 'F'
              
            if instructions[i] == 'LDA':
                one_byte += ('0' + loc )
            elif instructions[i] == 'ADD':
                one_byte += ('1' + loc )
            elif instructions[i] == 'SUB':
                one_byte += ('2' + loc )
            elif instructions[i] == 'JMP':
                one_byte += ('3' + loc )
            elif instructions[i] == 'OUT':
                one_byte += ('EF')
            elif instructions[i] == 'HLT':
                one_byte += ('FF')
            elif loc.lower() != 'null':
                one_byte += (loc)
            elif instructions[i].lower() == 'null':
                one_byte += ('FF')

            if len(one_byte) == 1:
                one_byte = '0' + one_byte

            file_txt += one_byte
            # the list to give to checksum function
            list_for_checksum.append(one_byte)

        
        file_txt = file_txt + checksum(list_for_checksum) + '\n'

        # generating the file
        with open('hex-file.hex', 'w') as file:
                file.writelines(file_txt)
                file.writelines(':00000001FF')
            
                
    def reset():
        i0.set('Null')
        i1.set('Null')
        i2.set('Null')
        i3.set('Null')
        
        i4.set('Null')
        i5.set('Null')
        i6.set('Null')
        i7.set('Null')
        
        i8.set('Null')
        i9.set('Null')
        i10.set('Null')
        i11.set('Null')
        
        i12.set('Null')
        i13.set('Null')
        i14.set('Null')
        i15.set('Null')

        loc0.set('Null')
        loc1.set('Null')
        loc2.set('Null')
        loc3.set('Null')
        
        loc4.set('Null')
        loc5.set('Null')
        loc6.set('Null')
        loc7.set('Null')
        
        loc8.set('Null')
        loc9.set('Null')
        loc10.set('Null')
        loc11.set('Null')
        
        loc12.set('Null')
        loc13.set('Null')
        loc14.set('Null')
        loc15.set('Null')


    # All the instruction drop downs
    label_instruction = customtkinter.CTkLabel(master=root, text="Instruction")
    label_instruction.grid(column=1, row=0, padx=20, pady=5)

    i0 = customtkinter.StringVar(value="Null")  
    i0 = customtkinter.CTkComboBox(master=root, values=instruction_options, variable=i0)
    i0.grid(column=1, row=1, padx=20, pady=10)

    i1 = customtkinter.StringVar(value="Null")  
    i1 = customtkinter.CTkComboBox(master=root, values=instruction_options, variable=i1)
    i1.grid(column=1, row=2, padx=20, pady=10)

    i2 = customtkinter.StringVar(value="Null")  
    i2 = customtkinter.CTkComboBox(master=root, values=instruction_options, variable=i2)
    i2.grid(column=1, row=3, padx=20, pady=10)

    i3 = customtkinter.StringVar(value="Null")  
    i3 = customtkinter.CTkComboBox(master=root, values=instruction_options, variable=i3)
    i3.grid(column=1, row=4, padx=20, pady=10)

    i4 = customtkinter.StringVar(value="Null")  
    i4 = customtkinter.CTkComboBox(master=root, values=instruction_options, variable=i4)
    i4.grid(column=1, row=5, padx=20, pady=10)

    i5 = customtkinter.StringVar(value="Null")  
    i5 = customtkinter.CTkComboBox(master=root, values=instruction_options, variable=i5)
    i5.grid(column=1, row=6, padx=20, pady=10)

    i6 = customtkinter.StringVar(value="Null")  
    i6 = customtkinter.CTkComboBox(master=root, values=instruction_options, variable=i6)
    i6.grid(column=1, row=7, padx=20, pady=10)

    i7 = customtkinter.StringVar(value="Null")  
    i7 = customtkinter.CTkComboBox(master=root, values=instruction_options, variable=i7)
    i7.grid(column=1, row=8, padx=20, pady=10)

    i8 = customtkinter.StringVar(value="Null")  
    i8 = customtkinter.CTkComboBox(master=root, values=instruction_options, variable=i8)
    i8.grid(column=1, row=9, padx=20, pady=10)

    i9 = customtkinter.StringVar(value="Null")  
    i9 = customtkinter.CTkComboBox(master=root, values=instruction_options, variable=i9)
    i9.grid(column=1, row=10, padx=20, pady=10)

    i10 = customtkinter.StringVar(value="Null")  
    i10 = customtkinter.CTkComboBox(master=root, values=instruction_options, variable=i10)
    i10.grid(column=1, row=11, padx=20, pady=10)

    i11 = customtkinter.StringVar(value="Null")  
    i11 = customtkinter.CTkComboBox(master=root, values=instruction_options, variable=i11)
    i11.grid(column=1, row=12, padx=20, pady=10)

    i12 = customtkinter.StringVar(value="Null")  
    i12 = customtkinter.CTkComboBox(master=root, values=instruction_options, variable=i12)
    i12.grid(column=1, row=13, padx=20, pady=10)

    i13 = customtkinter.StringVar(value="Null")  
    i13 = customtkinter.CTkComboBox(master=root, values=instruction_options, variable=i13)
    i13.grid(column=1, row=14, padx=20, pady=10)

    i14 = customtkinter.StringVar(value="Null")  
    i14 = customtkinter.CTkComboBox(master=root, values=instruction_options, variable=i14)
    i14.grid(column=1, row=15, padx=20, pady=10)

    i15 = customtkinter.StringVar(value="Null")  
    i15 = customtkinter.CTkComboBox(master=root, values=instruction_options, variable=i15)
    i15.grid(column=1, row=16, padx=20, pady=10)

    # All the locations
    label_location = customtkinter.CTkLabel(master=root, text="Data")
    label_location.grid(column=2, row=0, padx=20, pady=5)

    loc0 = customtkinter.StringVar(value="Null")  
    loc0 = customtkinter.CTkComboBox(master=root, values=location_options, variable=loc0)
    loc0.grid(column=2, row=1, padx=20, pady=10)

    loc1 = customtkinter.StringVar(value="Null")  
    loc1 = customtkinter.CTkComboBox(master=root, values=location_options, variable=loc1)
    loc1.grid(column=2, row=2, padx=20, pady=10)

    loc2 = customtkinter.StringVar(value="Null")  
    loc2 = customtkinter.CTkComboBox(master=root, values=location_options, variable=loc2)
    loc2.grid(column=2, row=3, padx=20, pady=10)

    loc3 = customtkinter.StringVar(value="Null")  
    loc3 = customtkinter.CTkComboBox(master=root, values=location_options, variable=loc3)
    loc3.grid(column=2, row=4, padx=20, pady=10)

    loc4 = customtkinter.StringVar(value="Null")  
    loc4 = customtkinter.CTkComboBox(master=root, values=location_options, variable=loc4)
    loc4.grid(column=2, row=5, padx=20, pady=10)

    loc5 = customtkinter.StringVar(value="Null")  
    loc5 = customtkinter.CTkComboBox(master=root, values=location_options, variable=loc5)
    loc5.grid(column=2, row=6, padx=20, pady=10)

    loc6 = customtkinter.StringVar(value="Null")  
    loc6 = customtkinter.CTkComboBox(master=root, values=location_options, variable=loc6)
    loc6.grid(column=2, row=7, padx=20, pady=10)

    loc7 = customtkinter.StringVar(value="Null")  
    loc7 = customtkinter.CTkComboBox(master=root, values=location_options, variable=loc7)
    loc7.grid(column=2, row=8, padx=20, pady=10)

    loc8 = customtkinter.StringVar(value="Null")  
    loc8 = customtkinter.CTkComboBox(master=root, values=location_options, variable=loc8)
    loc8.grid(column=2, row=9, padx=20, pady=10)

    loc9 = customtkinter.StringVar(value="Null")  
    loc9 = customtkinter.CTkComboBox(master=root, values=location_options, variable=loc9)
    loc9.grid(column=2, row=10, padx=20, pady=10)

    loc10 = customtkinter.StringVar(value="Null")  
    loc10 = customtkinter.CTkComboBox(master=root, values=location_options, variable=loc10)
    loc10.grid(column=2, row=11, padx=20, pady=10)

    loc11 = customtkinter.StringVar(value="Null")  
    loc11 = customtkinter.CTkComboBox(master=root, values=location_options, variable=loc11)
    loc11.grid(column=2, row=12, padx=20, pady=10)

    loc12 = customtkinter.StringVar(value="Null")  
    loc12 = customtkinter.CTkComboBox(master=root, values=location_options, variable=loc12)
    loc12.grid(column=2, row=13, padx=20, pady=10)

    loc13 = customtkinter.StringVar(value="Null")  
    loc13 = customtkinter.CTkComboBox(master=root, values=location_options, variable=loc13)
    loc13.grid(column=2, row=14, padx=20, pady=10)

    loc14 = customtkinter.StringVar(value="Null")  
    loc14 = customtkinter.CTkComboBox(master=root, values=location_options, variable=loc14)
    loc14.grid(column=2, row=15, padx=20, pady=10)

    loc15 = customtkinter.StringVar(value="Null")  
    loc15 = customtkinter.CTkComboBox(master=root, values=location_options, variable=loc15)
    loc15.grid(column=2, row=16, padx=20, pady=10)


    #locations labels
    label_Sr = customtkinter.CTkLabel(master=root, text="loc No.")
    label_Sr.grid(column=0, row=0, padx=20, pady=5)

    label0 = customtkinter.CTkLabel(master=root, text="0H")
    label0.grid(column=0, row=1, padx=20, pady=10)

    label1 = customtkinter.CTkLabel(master=root, text="1H")
    label1.grid(column=0, row=2, padx=20, pady=10)

    label2 = customtkinter.CTkLabel(master=root, text="2H")
    label2.grid(column=0, row=3, padx=20, pady=10)

    label3 = customtkinter.CTkLabel(master=root, text="3H")
    label3.grid(column=0, row=4, padx=20, pady=10)

    label4 = customtkinter.CTkLabel(master=root, text="4H")
    label4.grid(column=0, row=5, padx=20, pady=10)

    label5 = customtkinter.CTkLabel(master=root, text="5H")
    label5.grid(column=0, row=6, padx=20, pady=10)

    label6 = customtkinter.CTkLabel(master=root, text="6H")
    label6.grid(column=0, row=7, padx=20, pady=10)

    label7 = customtkinter.CTkLabel(master=root, text="7H")
    label7.grid(column=0, row=8, padx=20, pady=10)

    label8 = customtkinter.CTkLabel(master=root, text="8H")
    label8.grid(column=0, row=9, padx=20, pady=10)

    label9 = customtkinter.CTkLabel(master=root, text="9H")
    label9.grid(column=0, row=10, padx=20, pady=10)

    label10 = customtkinter.CTkLabel(master=root, text="10H")
    label10.grid(column=0, row=11, padx=20, pady=10)

    label11 = customtkinter.CTkLabel(master=root, text="11H")
    label11.grid(column=0, row=12, padx=20, pady=10)

    label12 = customtkinter.CTkLabel(master=root, text="12H")
    label12.grid(column=0, row=13, padx=20, pady=10)

    label13 = customtkinter.CTkLabel(master=root, text="13H")
    label13.grid(column=0, row=14, padx=20, pady=10)

    label14 = customtkinter.CTkLabel(master=root, text="14H")
    label14.grid(column=0, row=15, padx=20, pady=10)

    label15 = customtkinter.CTkLabel(master=root, text="15H")
    label15.grid(column=0, row=16, padx=20, pady=10)


    # f1ile generator button
    btn_Generate_File = customtkinter.CTkButton(master=root, text="Generate File", command=generate_file, width=220)
    btn_Generate_File.grid(columnspan=2, row=17, pady=10)
    
    btn_Reset = customtkinter.CTkButton(master=root, text="Reset", command=reset)
    btn_Reset.grid(column=2, row=17, pady=10)




#setting the default apperance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


#making the root
root = customtkinter.CTk()
root.title("Hex-File Generator")
root.geometry("450x650")

# call the hexfile generator from 

canvas = customtkinter.CTkScrollableFrame(root)
canvas.pack(expand=True, fill='both')



hex_file_generator(root=canvas)

#mainloop
root.mainloop()