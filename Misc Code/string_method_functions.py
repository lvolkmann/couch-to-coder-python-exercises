def redact_after_count(text :str, count:int) ->str:
    words = text.split()
    word_count = len(words)
    first_half = ""
    current_count = 0
    
    while current_count < count:
        first_half += words[current_count]

    second_half = "XXXXX" * (word_count-count)

    return first_half + second_half

def redact_after_symbol(text:str, symbol:str) ->str:

    r_start = text.find(symbol)
    r_len = len(text) - r_start
    to_redact = text[r_start:]
    return text.replace(to_redact, "X"*r_len)

def numeric_scraper(text:str) -> list:

    num_lst = []

    cur_num = ""
    string = False
    
    for char in text:

        #on a string
        if string:
            if char.isdigit():
                cur_num += char
            else:
                num_lst.append(int(cur_num))
                cur_num = ""
                string = False
                
        #looking for a string
        else:
            if char.isdigit():
                cur_num += char
                string = True
    #last string
    if string:
        num_lst.append(int(cur_num))
        
    return num_lst


            
            
        
        
