from tkinter import*
from cell import Cell
import settings
import frameval

 
root = Tk()

root.configure(bg="black")
root.geometry(f'{settings.width}x{settings.height}')
root.title("Minesweeper")
root.resizable(False,False)

top_frame = Frame(
    root,
    bg = 'black', 
    width =settings.width,
    height=frameval.height_prct(25)
)
top_frame.place(x=0,y=0)

game_title=Label(
    top_frame,
    bg='black',
    fg='white',
    text='MINESWEEPER GAME',
    font=('Aerial',25)
)

game_title.place(
    x=frameval.width_prct(25),y=0
)

left_frame= Frame(
    root,
    bg = 'black',
      width =frameval.width_prct(25),
      height=frameval.height_prct(75)
)
left_frame.place( x=0,y=frameval.height_prct(25))

centre_frame = Frame( 
    root,
    bg='black',
    width=frameval.width_prct(75),
    height=frameval.height_prct(75)
)
centre_frame.place(
    x=frameval.width_prct(25),
    y=frameval.height_prct(25)
)

for x in range(settings.grid_size):
    for y in range(settings.grid_size):
        c=Cell(x,y)
        c.create_btn_object(centre_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(
    x=0,y=0
)
Cell.randomize_mines()
#run the window
root.mainloop()