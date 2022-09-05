
import sys
def currentFile():
    with open("Aregzip.txt", "r") as f:
        file_text = [row.strip() for row in f.readlines()]

        splitted_list = []
        k = 0
        counter = 1
        step = "!"
    
        for i in range(len(file_text)):
            splitted_list.extend(file_text[i].split())

        for i in range(len(splitted_list)):
            for j in range(i + 1, len(splitted_list)):
                if splitted_list[j] == splitted_list[i][-2:]:
                    splitted_list[j] = splitted_list[i][:-2]
            if splitted_list[i][-1] == step:
                splitted_list[i] = splitted_list[i][:-2]            

        with open("decompress.txt", "w") as file:
            for i in range(len(splitted_list)):
                file.write(splitted_list[i] + " ")            




def myFile():
    with open(sys.argv[1], "r") as f:
        file_text = [row.strip() for row in f.readlines()]

        splitted_list = []
        k = 0
        counter = 1
        step = "!"
    
        for i in range(len(file_text)):
            splitted_list.extend(file_text[i].split())

        list_copy = splitted_list[:]    
       
        for i in range(len(splitted_list)):
            for j in range(i + 1, len(splitted_list)):
                if len(splitted_list[i]) > 2:
                    if splitted_list[j] == splitted_list[i]:
                        splitted_list[j] = f"{counter}" + step

            if len(splitted_list[i]) > 1 and list_copy.count(splitted_list[i]) > 1:
                splitted_list[i] = splitted_list[i] + f"{counter}" + step
        
            counter += 1
            with open("Aregzip.txt", "w") as file:
                for i in range(len(splitted_list)):
                    file.write(splitted_list[i] + " ")               
            

    





    
   

    

           



           
        


