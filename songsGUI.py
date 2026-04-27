import tkinter as tk
from songsController import SongsController
from woodBackground import WoodBackgroundManager


class SongsTab:
    """Songs tab with wooden background."""

    def __init__(self, parent):
        self.controller = SongsController()
        self.frame = tk.Frame(parent, bg="#f5f5f5")
        self.links_frame = None
        self.status_var = tk.StringVar(value="")
        self.background_manager = WoodBackgroundManager(
            self.frame,
            image_name=self.controller.get_background_image_path(),
        )
        self._build_layout()

    def _build_layout(self):
        self.background_manager.apply()

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=2)
        self.frame.grid_columnconfigure(1, weight=3)

        left_frame = tk.Frame(self.frame, bg="white", relief=tk.SUNKEN, bd=1)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=(20, 10), pady=20)

        right_frame = tk.Frame(self.frame, bg="white", relief=tk.SUNKEN, bd=1)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=(10, 20), pady=20)

        songs_title = tk.Label(
            left_frame,
            text=self.controller.get_list_title(),
            font=("Arial", 14, "bold"),
            bg="white",
            fg="#111111",
        )
        songs_title.pack(anchor="w", padx=12, pady=(12, 8))

        list_container = tk.Frame(left_frame, bg="white")
        list_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        list_container.grid_rowconfigure(0, weight=1)
        list_container.grid_columnconfigure(0, weight=1)

        list_canvas = tk.Canvas(list_container, bg="white", highlightthickness=0)
        list_canvas.grid(row=0, column=0, sticky="nsew")

        scrollbar = tk.Scrollbar(list_container, orient="vertical", command=list_canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        list_canvas.configure(yscrollcommand=scrollbar.set)

        self.links_frame = tk.Frame(list_canvas, bg="white")
        links_window = list_canvas.create_window((0, 0), window=self.links_frame, anchor="nw")

        # These two functions keep the canvas scroll area in sync with its contents.
        # _sync_scroll_region: updates the scrollable area whenever a new link is added.
        # _sync_inner_width: stretches the inner frame to always fill the canvas width.
        def _sync_scroll_region(_event):
            list_canvas.configure(scrollregion=list_canvas.bbox("all"))

        def _sync_inner_width(event):
            list_canvas.itemconfigure(links_window, width=event.width)

        self.links_frame.bind("<Configure>", _sync_scroll_region)
        list_canvas.bind("<Configure>", _sync_inner_width)

        def _on_mousewheel(event):
            list_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        list_canvas.bind("<MouseWheel>", _on_mousewheel)
        self.links_frame.bind("<MouseWheel>", _on_mousewheel)
        self._list_canvas = list_canvas
        self._on_mousewheel = _on_mousewheel

        for song_title, url in self.controller.get_song_tutorials():
            self._add_song_link_label(song_title, url)

        right_label = tk.Label(
            right_frame,
            text="Add Song Tutorial",
            font=("Arial", 14),
            bg="white",
            fg="#444444",
        )
        right_label.pack(pady=(20, 10))

        form_frame = tk.Frame(right_frame, bg="white")
        form_frame.pack(fill="x", padx=16, pady=(0, 10))

        name_label = tk.Label(form_frame, text="Song Name", font=("Arial", 10, "bold"), bg="white", fg="#222222")
        name_label.pack(anchor="w")
        self.name_entry = tk.Entry(form_frame, font=("Arial", 11))
        self.name_entry.pack(fill="x", pady=(4, 10))

        author_label = tk.Label(form_frame, text="Author", font=("Arial", 10, "bold"), bg="white", fg="#222222")
        author_label.pack(anchor="w")
        self.author_entry = tk.Entry(form_frame, font=("Arial", 11))
        self.author_entry.pack(fill="x", pady=(4, 10))

        url_label = tk.Label(form_frame, text="Tutorial URL", font=("Arial", 10, "bold"), bg="white", fg="#222222")
        url_label.pack(anchor="w")
        self.url_entry = tk.Entry(form_frame, font=("Arial", 11))
        self.url_entry.pack(fill="x", pady=(4, 12))

        add_button = tk.Button(
            form_frame,
            text="Add to Songs List",
            font=("Arial", 11, "bold"),
            bg="#2f6f44",
            fg="white",
            activebackground="#245837",
            activeforeground="white",
            relief=tk.FLAT,
            padx=10,
            pady=6,
            command=self._handle_add_song,
        )
        add_button.pack(anchor="w")

        status_label = tk.Label(
            form_frame,
            textvariable=self.status_var,
            font=("Arial", 10),
            bg="white",
            fg="#444444",
            justify="left",
            wraplength=380,
        )
        status_label.pack(anchor="w", pady=(10, 0))

        helper_label = tk.Label(
            right_frame,
            text=self.controller.get_empty_state_text(),
            font=("Arial", 10),
            bg="white",
            fg="#666666",
            justify="left",
            wraplength=380,
        )
        helper_label.pack(anchor="w", padx=16, pady=(6, 0))

    def _add_song_link_label(self, song_title, url):
        if not self.links_frame:
            return

        link_label = tk.Label(
            self.links_frame,
            text=song_title,
            font=("Arial", 11, "underline"),
            fg="#1f4fbf",
            bg="white",
            cursor="hand2",
            justify="left",
            anchor="w",
            wraplength=420,
        )
        link_label.pack(fill="x", padx=6, pady=(4, 2), anchor="w")
        link_label.bind("<Button-1>", lambda _event, target=url: self.controller.open_song_link(target))
        if hasattr(self, "_on_mousewheel"):
            link_label.bind("<MouseWheel>", self._on_mousewheel)

    def _handle_add_song(self):
        result = self.controller.add_song_tutorial(
            song_name=self.name_entry.get(),
            author_name=self.author_entry.get(),
            url=self.url_entry.get(),
        )

        self.status_var.set(result["message"])
        if result["success"]:
            song_title, song_url = result["song"]
            self._add_song_link_label(song_title, song_url)
            self.name_entry.delete(0, tk.END)
            self.author_entry.delete(0, tk.END)
            self.url_entry.delete(0, tk.END)

    def close(self):
        if self.controller:
            self.controller.close()
