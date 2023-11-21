"""Class Writing Practice"""

from __future__ import annotations

__author__ = "730659395"


class ChristmasTreeFarm:
    plots: list[int]
    
    def __init__(self, plots: int, initial_planting: int) -> None:
        self.plots: list[int] = []
        for tree in range(0, initial_planting):
            self.plots.append(1)
        for tree in range(0, (plots - initial_planting)):
            self.plots.append(0)
    
    def plant(self, plot_idx: int) -> None:
        self.plots[plot_idx] = 1
    
    def growth(self) -> None:
        for i in range(0, len(self.plots)):
            if self.plots[i] != 0:
                self.plots[i] += 1

    def harvest(self, replant: bool) -> int:
        replant_count: int = 0
        for i in range(0, len(self.plots)):
            if self.plots[i] >= 5 and replant is True:
                self.plots[i] = 1
                replant_count += 1
            if self.plots[i] >= 5 and replant is False:
                self.plots[i] = 0
                replant_count += 1
        return replant_count

    def __add__(self, rhs: ChristmasTreeFarm) -> ChristmasTreeFarm:
        size: int = len(self.plots) + len(rhs.plots)
        treecount: int = 0
        for i in range(0, len(self.plots)):
            if self.plots[i] > 0:
                treecount += 1
        for i in range(0, len(rhs.plots)):
            if rhs.plots[i] > 0:
                treecount += 1
        print(size, treecount)
        return ChristmasTreeFarm(size, treecount)