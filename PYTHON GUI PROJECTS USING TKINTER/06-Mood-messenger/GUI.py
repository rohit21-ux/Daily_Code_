import tkinter as tk
import random

MOODS = {
    "happy": {
        "emoji": "😄",
        "label": "Happy",
        "color": "#F59E0B",
        "bg": "#FFFBEB",
        "btn_hover": "#D97706",
        "quotes": [
            "Keep smiling — your vibe is contagious!",
            "Happiness looks good on you. Ride this wave!",
            "You're on fire today. Don't let anyone dim your light.",
            "Good vibes only — and you're the source.",
            "Today is a great day to have a great day.",
            "Your energy is a gift. Share it generously.",
        ],
    },
    "neutral": {
        "emoji": "😐",
        "label": "Neutral",
        "color": "#6366F1",
        "bg": "#EEF2FF",
        "btn_hover": "#4F46E5",
        "quotes": [
            "Not every day has to be amazing. Steady is underrated.",
            "A calm sea makes a skilled sailor. You're learning.",
            "Even a gray sky has its own quiet beauty.",
            "Neutral is just energy waiting to find its direction.",
            "Sometimes 'meh' is just your brain taking a breather.",
            "Peace and stillness are their own kind of strength.",
        ],
    },
    "sad": {
        "emoji": "😢",
        "label": "Sad",
        "color": "#3B82F6",
        "bg": "#EFF6FF",
        "btn_hover": "#2563EB",
        "quotes": [
            "It's okay not to be okay. You won't feel this way forever.",
            "Even the darkest night will end, and the sun will rise.",
            "You are allowed to be both a masterpiece and a work in progress.",
            "Crying is just your soul taking a shower. You'll feel cleaner soon.",
            "Every storm runs out of rain. Hang in there.",
            "Be gentle with yourself — you're doing the best you can.",
        ],
    },
}

BG_MAIN = "#0F172A"
BG_CARD = "#1E293B"
BG_CARD2 = "#334155"
TEXT_PRIMARY = "#F1F5F9"
TEXT_SECONDARY = "#94A3B8"
TEXT_MUTED = "#64748B"
ACCENT = "#6366F1"
RADIUS = 12
FONT_FAMILY = "Segoe UI"


class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, emoji, color, hover_color, command=None, width=180, height=64, **kwargs):
        super().__init__(parent, width=width, height=height,
                         bg=BG_CARD, highlightthickness=0, **kwargs)
        self.command = command
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.emoji = emoji
        self.w = width
        self.h = height
        self._draw(color)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<Button-1>", self._on_click)
        self.bind("<ButtonRelease-1>", self._on_release)

    def _rounded_rect(self, x1, y1, x2, y2, r, **kwargs):
        points = [
            x1 + r, y1,
            x2 - r, y1,
            x2, y1,
            x2, y1 + r,
            x2, y2 - r,
            x2, y2,
            x2 - r, y2,
            x1 + r, y2,
            x1, y2,
            x1, y2 - r,
            x1, y1 + r,
            x1, y1,
        ]
        return self.create_polygon(points, smooth=True, **kwargs)

    def _draw(self, fill_color):
        self.delete("all")
        self._rounded_rect(2, 2, self.w - 2, self.h - 2, 10,
                            fill=fill_color, outline="", tags="btn")
        self.create_text(self.w // 2, self.h // 2 - 8,
                         text=self.emoji, font=(FONT_FAMILY, 18),
                         fill="white", tags="btn")
        self.create_text(self.w // 2, self.h // 2 + 14,
                         text=self.text, font=(FONT_FAMILY, 11, "bold"),
                         fill="white", tags="btn")

    def _on_enter(self, e=None):
        self._draw(self.hover_color)
        self.config(cursor="hand2")

    def _on_leave(self, e=None):
        self._draw(self.color)
        self.config(cursor="")

    def _on_click(self, e=None):
        self._draw(BG_CARD2)
        if self.command:
            self.after(80, lambda: self.command())

    def _on_release(self, e=None):
        self._draw(self.color)


class VibeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("✨ Vibe Console")
        self.geometry("520x640")
        self.resizable(False, False)
        self.configure(bg=BG_MAIN)
        try:
            self.iconbitmap("")
        except Exception:
            pass

        self._current_mood = None
        self._build_ui()
        self._center_window()

    def _center_window(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        self.geometry(f"{w}x{h}+{(sw - w) // 2}+{(sh - h) // 2}")

    def _build_ui(self):
        outer = tk.Frame(self, bg=BG_MAIN)
        outer.pack(fill="both", expand=True, padx=28, pady=28)

        header = tk.Frame(outer, bg=BG_MAIN)
        header.pack(fill="x", pady=(0, 20))

        tk.Label(header, text="✨  Vibe Console",
                 font=(FONT_FAMILY, 22, "bold"),
                 fg=TEXT_PRIMARY, bg=BG_MAIN).pack()
        tk.Label(header, text="How are you feeling right now?",
                 font=(FONT_FAMILY, 11),
                 fg=TEXT_SECONDARY, bg=BG_MAIN).pack(pady=(4, 0))

        divider = tk.Frame(outer, bg=BG_CARD2, height=1)
        divider.pack(fill="x", pady=(0, 24))

        mood_card = tk.Frame(outer, bg=BG_CARD, pady=20, padx=20)
        mood_card.pack(fill="x")
        self._draw_card_border(mood_card)

        tk.Label(mood_card, text="S E L E C T   Y O U R   M O O D",
                 font=(FONT_FAMILY, 9, "bold"),
                 fg=TEXT_MUTED, bg=BG_CARD).pack(pady=(0, 16))

        btn_row = tk.Frame(mood_card, bg=BG_CARD)
        btn_row.pack()

        for key, data in MOODS.items():
            btn = RoundedButton(
                btn_row,
                text=data["label"],
                emoji=data["emoji"],
                color=data["color"],
                hover_color=data["btn_hover"],
                command=lambda k=key: self._pick_mood(k),
                width=130,
                height=70,
            )
            btn.pack(side="left", padx=8)

        tk.Frame(outer, bg=BG_MAIN, height=20).pack()

        self.quote_frame = tk.Frame(outer, bg=BG_CARD, pady=28, padx=24)
        self.quote_frame.pack(fill="x")

        self.mood_badge = tk.Label(self.quote_frame, text="",
                                   font=(FONT_FAMILY, 10, "bold"),
                                   fg=TEXT_MUTED, bg=BG_CARD)
        self.mood_badge.pack()

        self.quote_emoji = tk.Label(self.quote_frame, text="",
                                    font=(FONT_FAMILY, 36),
                                    bg=BG_CARD)
        self.quote_emoji.pack(pady=(10, 6))

        self.quote_text = tk.Label(self.quote_frame,
                                   text="Pick a mood above to get your vibe check ✨",
                                   font=(FONT_FAMILY, 13, "italic"),
                                   fg=TEXT_SECONDARY, bg=BG_CARD,
                                   wraplength=400,
                                   justify="center")
        self.quote_text.pack(pady=(0, 14))

        self.refresh_btn = tk.Button(self.quote_frame,
                                     text="↻  Another Quote",
                                     font=(FONT_FAMILY, 10, "bold"),
                                     fg="white", bg=ACCENT,
                                     activebackground="#4F46E5",
                                     activeforeground="white",
                                     bd=0, padx=20, pady=8,
                                     cursor="hand2",
                                     command=self._refresh_quote,
                                     state="disabled",
                                     relief="flat")
        self.refresh_btn.pack()

        tk.Frame(outer, bg=BG_MAIN, height=16).pack()

        footer = tk.Label(outer,
                          text="Made with ♥  |  Stay true to your vibe",
                          font=(FONT_FAMILY, 9),
                          fg=TEXT_MUTED, bg=BG_MAIN)
        footer.pack(side="bottom")

    def _draw_card_border(self, widget):
        pass

    def _pick_mood(self, mood_key):
        self._current_mood = mood_key
        self._show_quote(mood_key)
        self.refresh_btn.config(state="normal")

    def _show_quote(self, mood_key):
        data = MOODS[mood_key]
        quote = random.choice(data["quotes"])

        self.quote_frame.config(bg=data["bg"])
        self.mood_badge.config(
            text=f"MOOD: {data['label'].upper()}",
            fg=data["color"],
            bg=data["bg"]
        )
        self.quote_emoji.config(text=data["emoji"], bg=data["bg"])
        self.quote_text.config(
            text=f'"{quote}"',
            fg="#1E293B",
            bg=data["bg"],
            font=(FONT_FAMILY, 13, "italic")
        )
        self.refresh_btn.config(bg=data["color"],
                                activebackground=data["btn_hover"])

        self._animate_quote()

    def _animate_quote(self):
        self.quote_text.config(fg="#CBD5E1")
        self._fade_in(0)

    def _fade_in(self, step):
        colors = [
            "#CBD5E1", "#94A3B8", "#64748B", "#475569",
            "#334155", "#1E293B"
        ]
        if self._current_mood:
            data = MOODS[self._current_mood]
            target = "#1E293B"
        else:
            target = "#1E293B"

        if step < len(colors):
            self.quote_text.config(fg=colors[step])
            self.after(40, lambda: self._fade_in(step + 1))
        else:
            self.quote_text.config(fg=target)

    def _refresh_quote(self):
        if self._current_mood:
            self._show_quote(self._current_mood)


if __name__ == "__main__":
    app = VibeApp()
    app.mainloop()
