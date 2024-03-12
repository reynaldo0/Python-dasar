# bentuk standar fungsi 
'''
Studi Kasus 
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi("ucup")
'''

# Penggunaan type hints

def fungsi_int(arg:int) ->int:
    # FUNGSI DENGAN HINTS INTEGER
    output = 10**arg
    return output

hasil = fungsi_int(2)
print(hasil)

def fungsi_bool(arg:bool)->bool:
    # FUNGSI DENGAN HINTS BOOLEAN
    output = 10//arg
    return output

hasil = fungsi_bool(2.5)
print(hasil)

def display(arg:str):
    print(arg)

display("ucup")
