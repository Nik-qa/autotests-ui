from elements.base_element import BaseElement


class Image(BaseElement):
    @property
    def text(self) -> str:
        return "image"