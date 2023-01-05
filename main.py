import matplotlib.pyplot as plt
import numpy as np


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
    test = Matplot()
    test.set_data(Liner=[[1, 2, 5], [3, 6, 8]])
    test.plot(clear=True, dots="o", title="hello")
    test.show()


# ====================================================================
# Run the program if not imported
if __name__ == "__main__":
    main()
