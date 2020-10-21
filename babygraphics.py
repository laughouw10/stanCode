"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    # total width divided the number of years, then times the order of the x location

    x_location = int((width / len(YEARS)) * int(year_index))
    return x_location



def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """

    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################

    # use get_x_coordinate to get the x coordinate, which can be used in for loop, for the fixed line

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE),
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE), width=LINE_WIDTH)
    for i in range(len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i),
                           GRAPH_MARGIN_SIZE - 30,
                           GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i),
                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE + 35, width=LINE_WIDTH)
        canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i) + TEXT_DX,
                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)



def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    global next_rank
    draw_fixed_lines(canvas)        # draw the fixed background grid


    # Write your code below this line
    #################################

    # set a x distance and y distance
    # set the y coordinate when the rank is out of 1000
    # nested for to loop every names and every years
    # set rank, next_rank; year, next_year to create line
    # assign 1001 to the rank or next_rank if the rank is out of 1000
    # then create line for four diff situations: combinations of rank < 1000 and rank > 1000
    # create text for year, after the for loop, finish with the final text
    # use %4 to loop colors

    x_dis = int((CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) / 12)
    y_dis = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000
    y_small = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
    print(7)

    for i in range(len(lookup_names)):
        name = lookup_names[i]
        print(6)

        for j in range(len(YEARS)-1):

            year = YEARS[j]

            if str(year) in name_data[name]:
                rank = int(name_data[name][str(year)])
                print('a')
            else:
                rank = 1001
                print('b')

            next_year = YEARS[j+1]

            if str(next_year) in name_data[name]:
                next_rank = int(name_data[name][str(next_year)])
                print('c')
            else:
                next_rank = 1001
                print('d')

            if rank > 1000 and next_rank > 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * x_dis, y_small,
                                   GRAPH_MARGIN_SIZE + (j+1) * x_dis, y_small, fill=COLORS[i % 4], width=LINE_WIDTH)
                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + j * x_dis, y_small,
                                   text=name + ' *', fill=COLORS[i % 4], anchor=tkinter.SW)
                print(1)

            elif rank > 1000 and next_rank < 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * x_dis, y_small,
                                   GRAPH_MARGIN_SIZE + (j + 1) * x_dis, GRAPH_MARGIN_SIZE + next_rank * y_dis,
                                   fill=COLORS[i % 4], width=LINE_WIDTH)
                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + j * x_dis, y_small,
                                   text=name + ' *', fill=COLORS[i % 4], anchor=tkinter.SW)
                print(2)

            elif rank < 1000 and next_rank > 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * x_dis, GRAPH_MARGIN_SIZE + rank * y_dis,
                                   GRAPH_MARGIN_SIZE + (j + 1) * x_dis, y_small, fill=COLORS[i % 4], width=LINE_WIDTH)
                name_str = ""
                name_str = str(name) + str(rank)
                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + j * x_dis, GRAPH_MARGIN_SIZE + rank * y_dis,
                                   text=name_str, fill=COLORS[i % 4], anchor=tkinter.SW)
                print(3)

            else:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * x_dis, GRAPH_MARGIN_SIZE + rank * y_dis,
                                   GRAPH_MARGIN_SIZE + (j + 1) * x_dis, GRAPH_MARGIN_SIZE + next_rank * y_dis,
                                   fill=COLORS[i % 4], width=LINE_WIDTH)
                name_str = ""
                name_str = str(name) + str(rank)
                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + j * x_dis, GRAPH_MARGIN_SIZE + rank * y_dis,
                                   text=name_str, fill=COLORS[i % 4], anchor=tkinter.SW)
                print(4)
        if next_rank > 1000:
            canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + (j+1) * x_dis, y_small,
                               text=name + ' *', fill=COLORS[i % 4], anchor=tkinter.SW)
        else:
            name_str = ""
            name_str = str(name) + str(next_rank)
            canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + (j+1) * x_dis, GRAPH_MARGIN_SIZE + next_rank * y_dis,
                               text=name_str, fill=COLORS[i % 4], anchor=tkinter.SW)






                # main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
