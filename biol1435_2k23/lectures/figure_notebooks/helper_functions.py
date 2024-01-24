# Import modules. 
from typing import Optional, Dict, List, Union
import numpy as np
import toyplot


# WF plot function from one of many AWESOME resources produced by Dr. Eaton.
class WrightFisherPlot:
    def __init__(self, time=20, popsize=20, width: int=500, height: int=500, seed: Optional[int]=None):
        self.rng: np.random.Generator = np.random.default_rng(seed)
        self.grid: np.ndarray = np.arange(popsize * 2 * time).reshape((time, popsize * 2))
        self.edges: np.ndarray = None
        self.canvas: toyplot.Canvas = toyplot.Canvas(width=width, height=height)
        self.axes: toyplot.coordinates.Cartesian = None
        self._setup_axes()
        self.marks: Dict[str, 'toyplot.Mark'] = {}

        # get node coordinates
        ys, xs = np.where(self.grid > -1)
        self.coords = np.column_stack([xs, ys])

    def _setup_axes(self):
        # setup the canvas and axes
        self.axes = self.canvas.cartesian(xshow=False, ylabel="Time (generations ago)", margin=70, padding=25)
        self.axes.y.ticks.labels.style["font-size"] = 14
        self.axes.y.label.style["font-size"] = 16
        self.axes.y.label.offset = 30
        self.axes.y.ticks.locator = toyplot.locator.Extended()
        self.axes.y.ticks.show = True

    def add_haploids(self, **kwargs):
        """Add circle marks for gene copies."""
        style = {
            "marker": "o", 
            "color": "white", #toyplot.color.Palette()[1]
            "size": self.canvas.width / self.grid.shape[1] / 7.5,
            "mstyle": {"stroke": "black", "stroke-opacity": 0.75, "stroke-width": 1.5},
        }
        style.update(kwargs)
        self.marks['haploids'] = self.axes.scatterplot(
            self.coords[:, 0], self.coords[:, 1], 
            **style,
        );

    def add_diploids(self):
        """Adds a rectangle around pairs of gene copies to represent a diploid individual."""
        self.marks['diploids'] = self.axes.rectangle(
            self.coords[:, 0][::2] - 0.25,
            self.coords[:, 0][::2] + 1.25, 
            self.coords[:, 1][::2] - 0.25,
            self.coords[:, 1][::2] + 0.25,
            style={"fill": "lightgrey", "stroke": "grey", "stroke-opacity": 0.75, "stroke-width": 1.5},
        );

    def add_lines(self, sort: bool=True, **kwargs):
        """Adds lines from gene copies to randomly sampled parent gene copies each generation.
        """
        # iterate over each generation adding pairs of node indices
        for gen in range(0, self.grid.shape[0] - 1):
            # children idxs span from left to right
            lower_idxs = self.grid[gen]

            # randomly sample parent idxs (some have many children, some none)
            upper_idxs = self.rng.choice(self.grid[gen + 1], size=self.grid[gen + 1].size, replace=True)

            # get sorting index for the upper idxs
            if sort:
                order = np.argsort(upper_idxs)
            else:
                order = np.arange(upper_idxs.size)

            # update array of edges
            iedges = np.column_stack([lower_idxs, upper_idxs[order]])
            if self.edges is not None:
                self.edges = np.concatenate([self.edges, iedges])
            else:
                self.edges = iedges

        # style the graph
        style = {"vlshow": False, "ecolor": "black", "ewidth": 1.5, 'vsize': 0, 'estyle': {}}
        style.update(kwargs)

        # add graph lines from lower_idxs to upper_idxs, using coordinates for all
        self.marks['genealogy'] = self.axes.graph(
            self.edges,
            vcoordinates=self.coords[sorted(np.unique(self.edges))],
            **style,
        );

    def add_sampled_lines(self, samples: Union[int, List[int]], **kwargs):
        """Add sampled genealogy lines from N random samples, or a list of sampled indices."""   
        if isinstance(samples, int):
            nsample = min(samples, self.grid.shape[0])
            samples = list(self.rng.choice(self.grid[0], size=samples, replace=False))          

        # base styles for the graph
        style = {"vlshow": False, "ecolor": toyplot.color.Palette()[0], "ewidth": 2, 'vsize': 0, 'estyle': {}}
        style.update(kwargs)

        # get selected edges to show
        tracked = samples.copy()
        for e in self.edges:
            if e[0] in tracked:
                tracked.append(e[1])

        # subset the edges to graph
        mask = np.isin(self.edges[:, 0], tracked)
        edges = self.edges[mask]

        # apply unique color to coalescent events
        if 'vcolor' not in style:
            vcolors = []
            vmarkers = []
            for v in sorted(np.unique(edges)):
                if sum(edges[:, 1] == v) > 1:
                    vcolors.append('yellow')
                    vmarkers.append("s")
                else:
                    vcolors.append('black')
                    vmarkers.append("o")
            style.update({
                'vcolor': vcolors,
                'vstyle': {'stroke': 'black', 'stroke-width': 2},
                'vmarker': vmarkers,
            })

        # add graph lines from lower_idxs to upper_idxs, using coordinates for all
        self.marks['genealogy'] = self.axes.graph(
            edges,
            vcoordinates=self.coords[sorted(np.unique(edges))],
            **style,
        );