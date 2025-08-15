from nicegui import ui
from dataclasses import dataclass
from typing import Optional, List

CARD_WIDTH = 250
CARD_HEIGHT = 300

@dataclass
class VocabularyCard:
    german: str
    translation: str
    plural: Optional[str] = None  # Only for nouns


class VocabularyCardUi:
    GENDER_COLORS = {
        "der": "border-blue",
        "die": "border-red",
        "das": "border-green",
    }

    def __init__(self, card: VocabularyCard):
        self.card = card
        self.default_border = "border-green"
        self.card_width = CARD_WIDTH
        self.card_height = CARD_HEIGHT

    def _get_font_class(self, text: str, base="text-xl"):
        length = len(text)
        if length <= 10:
            return base
        elif length <= 20:
            return "text-lg"
        elif length <= 30:
            return "text-base"
        else:
            return "text-sm"

    def render(self):
        gender_class = self.default_border
        if self.card.plural:
            for gender, css_class in self.GENDER_COLORS.items():
                if self.card.german.lower().startswith(gender):
                    gender_class = css_class
                    break

        card_el = ui.card().classes(
            f"border-2 {gender_class}-100 hover:{gender_class}-500 "
            f"rounded-xl p-4 w-[{self.card_width}px] h-[{self.card_height}px] shadow-sm "
            "flex flex-col items-center justify-center gap-2 "
            "transition-all duration-200 hover:shadow-lg hover:-translate-y-0.5"
        )

        with card_el:
            ui.label(self.card.german).classes(
                f"{self._get_font_class(self.card.german)} font-bold text-center break-words"
            )

            if self.card.plural:
                ui.label(f"Plural: {self.card.plural}").classes(
                    f"{self._get_font_class(self.card.plural, base='text-sm')} text-gray-600 text-center break-words"
                )

            ui.label(self.card.translation).classes(
                f"{self._get_font_class(self.card.translation, base='text-base')} text-gray-800 text-center break-words"
            )

            ui.button(icon="volume_up", on_click=lambda: ui.notify(f"Pronouncing: {self.card.german}")) \
                .classes("bg-blue-100 hover:bg-blue-200 text-blue-600 rounded-full w-10 h-10 p-0")

        return card_el


class EndCardUi:
    def __init__(self):
        self.card_element = None

    def render(self):
        self.card_element = ui.card().classes(
                f"border-2 border-green-100 hover:border-green-500 "
                f"rounded-xl p-4 w-[{CARD_WIDTH}px] h-[{CARD_HEIGHT}px] shadow-sm "
                "flex flex-col items-center justify-center gap-2 "
                "transition-all duration-200 hover:shadow-lg hover:-translate-y-0.5"
            )
        self.card_element.style("margin:auto; display:flex; flex-direction:column; align-items:center; justify-content:center;")
        self.card_element.on('click', lambda: ui.notify("Go to next section"))

        with self.card_element:
            ui.label("🎉 The End 🎉").classes("text-xl font-bold text-center")
            ui.label("You've gone through all cards!").classes("text-gray-600 text-center")
        return self.card_element


# -------- Single Card Container with Navigation --------
class VocabularyCardContainer:
    def __init__(self, cards: List[VocabularyCard]):
        self.cards = cards
        self.index = 0
        self.card_element = None
        self.progress_container = None
        self.render_card()

    def render_card(self):
        # Remove previous elements
        if self.card_element:
            self.card_element.delete()
        if self.progress_container:
            self.progress_container.delete()

        # Render current card
        self.card_element = VocabularyCardUi(self.cards[self.index]).render()
        self.card_element.on('click', self.on_click)
        self.card_element.style("margin:auto; display:flex; flex-direction:column; align-items:center; justify-content:center;")

         # Progress row: centered text + progress bar
        with ui.column().classes("items-center mt-2 gap-2").style("align-self: center;") as self.progress_container:
            ui.label(f"{self.index + 1} / {len(self.cards)}").classes("text-gray-500 text-center")
            ui.linear_progress((self.index + 1) / len(self.cards), color='green', show_value=False)\
                .classes("w-[150px] h-2 rounded")

    def previous_card(self):
        if self.index > 0:
            self.index = self.index - 1
            self.render_card()

    def next_card(self):
        if self.index < len(self.cards) - 1:
            self.index = self.index + 1
            self.render_card()
        else:
            self.render_end_card()

    def render_end_card(self):
        # Remove previous elements
        if self.card_element:
            self.card_element.delete()
        if self.progress_container:
            self.progress_container.delete()

        self.end_card_element = EndCardUi().render()
        self.end_card_element.on('click', lambda: ui.notify("Go to next section"))



    def on_click(self, event):
        click_x = event.args['offsetX']
        if click_x < CARD_WIDTH / 2:
            self.previous_card()
        else:
            self.next_card()




# -------- Demo --------
def main():
    ui.label("Vocabulary Cards Demo").classes("text-2xl font-bold mb-4 text-center w-full")

    cards = [
        VocabularyCard(german="der Tisch", plural="die Tische", translation="the table"),
        VocabularyCard(german="laufen", translation="to run"),
        VocabularyCard(german="die Blume", plural="die Blumen", translation="the flower"),
        VocabularyCard(german="das Auto", plural="die Autos", translation="the car"),
        VocabularyCard(german="außergewöhnlichlangeswort", translation="extraordinarily long word"),
        VocabularyCard(german="der Hund und die Katze", plural="die Hunde und Katzen", translation="the dog and the cat")
    ]

    VocabularyCardContainer(cards)

    ui.run(title="German Vocabulary Cards", reload=False)


if __name__ == "__main__":
    main()
