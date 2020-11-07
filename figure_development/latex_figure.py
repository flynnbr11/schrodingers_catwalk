r"""
Module to gather together functionality to make tidy figures suitable for direct import to Latex projects. 

Inspired by and building on (stealing from) 
    https://jwalton.info/Embed-Publication-Matplotlib-Latex/. 

This class ensures the figures are the right size for the page, 
    and generates aesthetic width/height ratios for any number of subplots.
It also sets text to match the size and font of Latex, with functionality to specify any aspect. 

"""

import numpy as np

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

class LatexFigure():
    def __init__(
        self,
        width='thesis',
        fraction=1, 
        square_plot=False, 
        use_gridspec=False, 
        auto_gridspec=None, 
        gridspec_layout=(1,1),
        gridspec_params={},
        font_scale=1,
        rc_params={},
        plot_style='default',
        legend_axis=None
    ):
        r"""
        Wrapper around matplotlib functionality to produce Latex-compatible figures. 

        :param str/float width: 
            if 'thesis' or 'beamer', uses default width, 
            else if a float, specifies the width of the target page
        :param float fraction: fraction of the page's width to occupy
        :param bool use_gridspec: whether to use GridSpec to generate a 
            grid of axes
        :param int auto_gridspec: 
            if not None, the number of subplots to layout in a square grid
        :param tuple gridspec_layout: 
            (num_rows, num_cols) to use in GridSpec grid
        :param dict gridspec_params: 
            key/value pairs to pass to grid spec object, 
            e.g. {"wspace" : 0.25}
        :param float font_scale: scale to multiply default font sizes by
        :param dict rc_params: 
            key/value pairs to alter any functionality of the rcParams as in plt.rcParams.update(),
            e.g. {"axes.labelsize": 10}
        :param str plot_style: 
            matplotlib style from 
            https://matplotlib.org/devdocs/gallery/style_sheets/style_sheets_reference.html
        """

        plt.style.use(plot_style)
        
        if width == 'thesis':
            self.width_pt = 448
        elif width == 'beamer':
            self.width_pt = 307.28987
        else:
            self.width_pt = width
        self.fraction = fraction
        self.font_scale = font_scale
        self.specific_rc_params = rc_params
        self.square_plot = square_plot
        
        # Setup gridspec 
        self.use_gridspec = use_gridspec
        if self.use_gridspec and auto_gridspec is not None :
            # auto_gridspec is num subplots to draw
            ncols = int(np.ceil(np.sqrt(auto_gridspec)))
            nrows = int(np.ceil(auto_gridspec / ncols))
            self.gridspec_layout = (nrows, ncols)
        else:
            self.gridspec_layout = gridspec_layout
        if 'width_ratios' in gridspec_params:
            self.width_ratios = gridspec_params['width_ratios']
        else:
            self.width_ratios = [1] * self.gridspec_layout[1]
        if 'height_ratios' in gridspec_params:
            self.height_ratios = gridspec_params['height_ratios']
        else:
            self.height_ratios = [1] * self.gridspec_layout[0]
        
        # Setup figure
        self.size = self.set_size(
            width_pt = self.width_pt, 
            fraction = self.fraction,
            subplots = self.gridspec_layout
        )
        self.set_fonts()
        
        # Produce figure object
        if self.use_gridspec: 
            self.num_rows = self.gridspec_layout[0]
            self.num_cols = self.gridspec_layout[1]
            self.gridspec_axes = {}
            # TODO pass in wspace and other GS params
            self.fig = plt.figure(
                figsize = self.size
            )

            self.gs = GridSpec(
                nrows=self.num_rows,
                ncols=self.num_cols,
                figure=self.fig, 
                **gridspec_params
            )
            self.row = 0
            self.col = 0 # because first call adds 1 to self.col and want to start at 0

            if legend_axis is not None:
                self.legend_ax = self.new_axis(force_position=legend_axis)
                self.legend_grid_pos = legend_axis
        else:
            self.fig, self.ax = plt.subplots(1, 1, figsize=self.size)
                        
    def set_fonts(
        self, 
    ):
        r"""
        Tell matplotlib to use custom font parameters. 
        """

        self.font_default = int(11*self.font_scale) # set as same size as the doc font
        self.font_small = int(8*self.font_scale)
        self.font_medium = int(10*self.font_scale)
        self.font_large = int(14*self.font_scale)
        
        self.rc_params = {
            # Use LaTeX to write all text
            "pgf.texsystem": "pdflatex",
            "text.usetex": True,
            "font.family": "serif",
            "font.weight" : "normal",
            'pgf.rcfonts': False,

            # Match font sizes
            "font.size": self.font_default,
            "axes.titlesize": self.font_medium,
            "axes.labelsize": self.font_default,
            # Make the legend/label fonts a little smaller
            "legend.fontsize": self.font_small,
            "xtick.labelsize": self.font_small,
            "ytick.labelsize": self.font_small,
            # Legend
            "legend.fontsize" : self.font_medium, 
            "figure.titlesize" : self.font_default,
            # Plot
            "lines.markersize" : 5,
            
            # Format of figure
            "savefig.format" : "pdf"
        }
        self.rc_params.update(self.specific_rc_params)

        # Update font etc via matplotlib
        plt.rcParams.update(self.rc_params)        
        
    def set_size(self, width_pt, fraction=1, subplots=(1, 1)):
        """
        Set figure dimensions to avoid scaling in LaTeX.

        :param float width_pt:
            Document width in points, or string of predined document type
        :param float fraction:
            Fraction of the width which you wish the figure to occupy
        :param tuple subplots: 
            The number of rows and columns of subplots.
        :return tuple fig_dim:
            Dimensions of figure in inches
        """

        # TODO if height exceeds length of A4 page (or maximum set somehow), scale down
        # TODO account for the width ratios of the gridspec layout -- don't use full ratio in s[0]/s[1] in fig_height_in if some are shorter

        # Width of figure (in pts)
        fig_width_pt = width_pt * fraction
        # Convert from pt to inches
        inches_per_pt = 1 / 72.27

        # Golden ratio to set aesthetic figure height
        # https://disq.us/p/2940ij3
        golden_ratio = (5**.5 - 1) / 2
        if self.square_plot:
            self.width_to_height = 1
        else:
            # The "golden ratio" for aesthetcis
            self.width_to_height = 0.5*(1 + np.sqrt(5))

        # Ratio of subplots sizes
        self.total_width = sum(self.width_ratios) * self.width_to_height
        self.total_height = sum(self.height_ratios) 
        self.geometry_ratio = self.total_width/self.total_height       

        # Figure width/height in inches
        # We know the total width in inches, so must get the height in inches
        # -> height_inches/width_inches = total_height/total_width
        fig_width_in = fig_width_pt * inches_per_pt
        fig_height_in = (fig_width_in/self.total_width) * self.total_height

        return (fig_width_in, fig_height_in)

    def new_axis(self, force_position=None, ax_params={}):
        r""" 
        Get an ax object to plot on. 
        If using grid spec, finds the next available ax. 
        All axes are stored in self.gridspec_axes for later access.

        :param dict ax_params: 
            parameters to pass to add_subplot method, 
            e.g. {'sharex' : ax1}
        :returns ax: matplotlib ax object
        """

        if self.use_gridspec:
            if force_position is not None:
                grid_position = force_position
            else:
                while (self.row, self.col) in self.gridspec_axes:
                    self.col += 1
                    if self.col == self.num_cols:
                        self.col = 0
                        self.row += 1
                grid_position = (self.row, self.col)

            self.ax = self.fig.add_subplot(
                self.gs[grid_position],
                **ax_params
            )
            self.gridspec_axes[grid_position] = self.ax

        
        # set background to white # TODO make this optional
        self.ax.set_facecolor('white')
        return self.ax 
    
    def show(self):
        r"""
        Display the figure in an interactive environment. 
        """
        from IPython.display import display
        # self.set_fonts()
        display(self.fig)
        
    def save(
        self, 
        save_to_file, 
        file_format='pdf'
    ):
        r"""
        Save figure.

        :param path save_to_file: 
            path where the figure will save. 
            If a filetype is not included in the suffix, 
            default format used from self.rc_params.
        """
        self.fig.savefig(
            save_to_file, 
            # format=file_format, 
            bbox_inches='tight'
        )
        

def test_load():
    print("Hello world")