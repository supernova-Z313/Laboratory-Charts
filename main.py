import matplotlib.pyplot as plt
import numpy as np
import os


class Matplot:
    def __init__(self, data: list = None):
        try:
            import matplotlib.pyplot as plt
            import numpy as np
        except ImportError:
            print("Import Error:  \n\tNeed Matplot and Numpy library for this Program.\n\t"
                  "Use this commands on terminal to solve this problem:\n\t\t> pip3 install matplotlib\n\t\t &"
                  "\n\t\t> pip3 install numpy")

        if data is None:
            self.data = [0, 0]
        else:
            self.data = data

    # ====================================================================
    def set_data(self, **kwarg):
        self.data.clear()
        if kwarg.get("Liner"):
            x_points = np.array(kwarg["Liner"][0])
            y_points = np.array(kwarg["Liner"][1])
            self.data.append([x_points, y_points])
            print("The data is set")
        elif kwarg.get("Sin"):
            print("The data is set")
        elif kwarg.get("ASinH"):
            print("The data is set")
        elif kwarg.get("Log"):
            print("The data is set")
        elif kwarg.get("X^1/2"):
            print("This function is not yet available.\nData could not be set.")
        else:
            print("The desired function was not recognized.\nData could not be set.")
        # use ifs for multidata

    # ====================================================================
    def set_multi_data(self):
        pass

    # ====================================================================
    def plot(self, clear: bool = True, grid: bool = True, dots: str = "-", ls: str = "-", **kwargs):
        fig = plt.figure(clear=clear)
        ax0 = fig.subplots(1, 1)
        if kwargs.get("title"):
            ax0.set_title(kwargs["title"])
        if kwargs.get("x_label"):
            ax0.set_xlabel(kwargs["x_label"])
        if kwargs.get("y_label"):
            ax0.set_ylabel(kwargs["y_label"])
        if kwargs.get("x_scale"):
            ax0.set_xscale(kwargs["x_scale"])
        if kwargs.get("y_scale"):
            ax0.set_yscale(kwargs["y_scale"])
        if grid:
            ax0.grid()
        if kwargs.get("plot_arg"):
            ax0.plot(self.data[0][0], self.data[0][1], dots, ls=ls, lw=2, *kwargs["plot_arg"])
        else:
            ax0.plot(self.data[0][0], self.data[0][1], dots, ls=ls, lw=2)  # , color="green"

    # ====================================================================
    def multi_plot(self, ):
        pass

    # ====================================================================
    @staticmethod
    def show():
        plt.show()


# ====================================================================
def main():
    print("Hello Welcome to lab:")
    print("Select the desired option: \n(1)data entry\t(2)Plot Data\t(3)Draw the result\n(0)Exit")
    command = int(input())
    os.system("clear")
    test = Matplot()
    while command != 0:
        if command == 1:
            print("(1)Do you want to enter data manually?\n(2)or import from (CSV) file?")
            command = int(input())
            if command == 1:
                os.system("clear")
                print("Select the final chart type:\n(1)Linear graph\t(2)Sine graph\n(3)Log chart\t(4)Radical diagram\n"
                      "(5)ASinH graph")
                command = int(input())
                os.system("clear")
                if command == 1:
                    print("Enter the length of the graph points separated by a space. (like: 1 2 3)")
                    xs = list(map(float, input().split()))
                    os.system("clear")
                    print("Enter the width of the graph points separated by a space.")
                    ys = list(map(float, input().split()))
                    os.system("clear")
                    test.set_data(Liner=[xs, ys])
                elif command == 2:
                    pass
                elif command == 3:
                    pass
                elif command == 4:
                    pass
                elif command == 5:
                    pass
            elif command == 2:
                pass
        elif command == 2:
            print("enter the title of graph:")
            tit = input()
            os.system("clear")
            test.plot(clear=True, dots="o", title=tit)
        elif command == 3:
            test.show()
        os.system("clear")
        print("Select the desired option: \n(1)data entry\t(2)Plot Data\t(3)Draw the result\n(0)Exit")
        command = int(input())
        os.system("clear")


# ====================================================================
# Run the program if not imported
if __name__ == "__main__":
    main()
