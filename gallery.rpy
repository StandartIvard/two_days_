#init python:
#   g = Gallery() # переменная, которая принимает значение Галереи
#   g.locked_button = "" # для закрытых (не открытых) картинок (картинка когда закрыта)
#   g.button('') # кнопка, когда открыта
#   g.condition("") # при каком условии откроется картинка
#   g.image("") # картинка при открытии 


###########################

screen Gallery():
    tag menu
    add "."

    grid 2 5: # первый параметр отвечает за горизонталь
        xfill True # равномерное расположение по x горизонтали
        yfill True # равномерное расположение по y вертикали

    add g.make_button("# прописываем параметры, сами картинки","#их превью, маленькая картинка в самой игре внутри grid", xalign=0.5, yalign=0.5) #для центрирования, hover_border="#границы картинки при наведении")
