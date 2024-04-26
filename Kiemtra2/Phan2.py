from turtle import *
color = ['blue', 'red', 'green']
a = int(input('Input position: '))
print(f'Color at position {a} : {color[a]}')
b = input('Item to delete: ')
color.remove(b)
print(str(color))

# for i in range (len((color))) :
#     pencolor(color[i])
#     forward(50)
#     up()                     

# mainloop()
