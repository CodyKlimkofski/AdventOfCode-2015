class WrappingPaperEstimator:

    def get_dimensions_from_text(self, text):
        dimensions = text.strip().split('x')
        l = int(dimensions[0])
        w = int(dimensions[1])
        h = int(dimensions[2])
        return l, w, h

    def get_side_sizes(self, l, w, h):
        return l * w, w * h, h * l
    
    def get_side_perimeters(self, l, w, h):
        perim1 = 2 * (l + w)
        perim2 = 2 * (w + h)
        perim3 = 2 * (h + l)
        return perim1, perim2, perim3
    
    def get_lowest_side_size(self, l, w, h):
        return min(self.get_side_sizes(l, w, h))
    
    def get_lowest_perimeter(self, l, w, h):
        return min(self.get_side_perimeters(l, w, h))
    
    def get_cubic_volume(self, l, w, h):
        return l * w * h
    
    def estimate_wrapping_paper(self, text):
        l, w, h = self.get_dimensions_from_text(text)
        side1, side2, side3 = self.get_side_sizes(l, w, h)
        total_area = (2 * side1) + (2 * side2) + (2 * side3)
        slack = self.get_lowest_side_size(l, w, h)
        return total_area + slack
    
    def estimate_ribbon_length(self, text):
        l, w, h = self.get_dimensions_from_text(text)
        perimeter = self.get_lowest_perimeter(l, w, h)
        bow = self.get_cubic_volume(l, w, h)
        return perimeter + bow

