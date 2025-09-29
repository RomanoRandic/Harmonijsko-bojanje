import tkinter as tk
from tkinter import filedialog, messagebox
import math


def dodaj_vrh(L, boje, Susjedi, n, susjedi_boje):
    global min_rj
    global Lista_boja
    global Graf
    if min_rj is not None and boje >= min_rj:
        return
    if len(L) >= n:
        min_rj = boje
        Lista_boja = L
        return

    for i in range(1, boje + 1):
        bool1 = True
        for j in Graf[len(L)]:
            if j in susjedi_boje[i - 1]:
                bool1 = False
                break
            if j > len(L):
                continue
            if i in Susjedi[L[j - 1] - 1]:
                bool1 = False
                break

        if not bool1:
            continue
        M = L.copy()
        Susjedi2 = Susjedi.copy()
        M.append(i)

        for k in Graf[len(L)]:
            susjedi_boje[i - 1].append(k)
        for j in Graf[len(L)]:
            if j > len(L):
                continue
            Susjedi2[i - 1].append(L[j - 1])
            Susjedi2[L[j - 1] - 1].append(i)
        dodaj_vrh(M, boje, Susjedi2, n, susjedi_boje)

    boje += 1
    M = L.copy()
    Susjedi2 = Susjedi.copy()
    M.append(boje)
    Susjedi2.append([])
    Susjedi2[-1].append(len(Susjedi2))

    for j in Graf[len(L)]:
        susjedi_boje[boje - 1].append(j)
    if len(L) > 0:
        for j in Graf[len(L)]:
            if j > len(L):
                continue
            Susjedi2[boje - 1].append(L[j - 1])
            Susjedi2[L[j - 1] - 1].append(boje)
    dodaj_vrh(M, boje, Susjedi2, n, susjedi_boje)
    return


class DotConnectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dot Connector")

        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        self.dots = []
        self.dot_objects = {}
        self.connections = []
        self.selected_dot = None

        self.canvas.bind("<Button-1>", self.place_dot)
        self.canvas.bind("<Button-3>", self.connect_dot)
        self.highlight = None

        self.compute_button = tk.Button(
            root,
            text="Compute harmonic index and draw colors",
            command=self.compute_and_draw,
        )
        self.compute_button.pack()

        self.import_button = tk.Button(root, text="Import Graph", command=self.import_graph)
        self.import_button.pack()

        self.clear_button = tk.Button(root, text="Clear Canvas", command=self.clear_canvas)
        self.clear_button.pack()

        self.show_info_window()

    def show_info_window(self):
        info_window = tk.Toplevel(self.root)
        info_window.title("How to Use Dot Connector")
        info_window.geometry("400x300")

        info_text = (
            "Welcome to the Dot Connector App!\n\n"
            "- Left-click anywhere on the canvas to place a dot.\n"
            "- Right-click on a dot to select it, then right-click on another dot to create a connection.\n"
            "- Click 'Compute harmonic index and draw colors' to calculate and color the graph.\n"
            "- Click 'Import graph' to import a graph as a .txt adjacency list.\n"
            "- Click 'Clear canvas' to erase all dots and connections."
        )

        label = tk.Label(info_window, text=info_text, wraplength=380, justify="left")
        label.pack(pady=20)

        close_button = tk.Button(info_window, text="Close", command=info_window.destroy)
        close_button.pack(pady=10)

    def place_dot(self, event):
        x, y = event.x, event.y
        dot_id = len(self.dots) + 1
        self.dots.append((x, y, dot_id))
        dot_object = self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")
        self.canvas.create_text(x, y - 10, text=str(dot_id), fill="blue")
        self.dot_objects[dot_id] = dot_object

    def connect_dot(self, event):
        clicked_dot = self.get_nearest_dot(event.x, event.y)
        if clicked_dot is None:
            return
        if self.selected_dot is None:
            self.selected_dot = clicked_dot
            x, y, dot_id = self.selected_dot
            self.highlight = self.canvas.create_oval(
                x - 6, y - 6, x + 6, y + 6, outline="red", width=2
            )
        else:
            x1, y1, dot_id1 = self.selected_dot
            x2, y2, dot_id2 = clicked_dot
            if self.selected_dot != clicked_dot:
                self.canvas.create_line(x1, y1, x2, y2, fill="black")
                self.connections.append((dot_id1, dot_id2))
            self.selected_dot = None
            self.canvas.delete(self.highlight)

    def get_nearest_dot(self, x, y):
        for dot in self.dots:
            dot_x, dot_y, dot_id = dot
            if abs(dot_x - x) <= 5 and abs(dot_y - y) <= 5:
                return dot
        return None

    def import_graph(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not file_path:
            return

        try:
            with open(file_path, "r") as file:
                adjacency_list = [list(map(int, line.split())) for line in file]
            self.create_dots_from_graph(adjacency_list)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to import graph: {e}")

    def create_dots_from_graph(self, adjacency_list):
        self.dots.clear()
        self.connections.clear()
        self.canvas.delete("all")

        num_nodes = len(adjacency_list)
        radius = min(self.canvas.winfo_width(), self.canvas.winfo_height()) // 3
        center_x, center_y = self.canvas.winfo_width() // 2, self.canvas.winfo_height() // 2

        for i in range(num_nodes):
            angle = 2 * math.pi * i / num_nodes
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            self.place_dot_circle(x, y, i + 1)

        for i, neighbors in enumerate(adjacency_list, start=1):
            for neighbor in neighbors:
                if (i, neighbor) not in self.connections and (neighbor, i) not in self.connections:
                    self.connect_dots_by_ids(i, neighbor)

    def place_dot_circle(self, x, y, dot_id):
        self.dots.append((x, y, dot_id))
        dot_object = self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")
        self.canvas.create_text(x, y - 10, text=str(dot_id), fill="blue")
        self.dot_objects[dot_id] = dot_object

    def connect_dots_by_ids(self, id1, id2):
        dot1 = self.dots[id1 - 1]
        dot2 = self.dots[id2 - 1]
        x1, y1, _ = dot1
        x2, y2, _ = dot2
        self.canvas.create_line(x1, y1, x2, y2, fill="black")
        self.connections.append((id1, id2))

    def compute_and_draw(self):
        num_nodes = len(self.dots)
        global Graf
        Graf = self.generate_graph(self.connections, num_nodes)

        global min_rj
        global Lista_boja
        global susjedi_boje

        min_rj = None
        Lista_boja = []
        susjedi_boje = [[] for _ in range(len(Graf))]
        dodaj_vrh([], 0, [], len(Graf), susjedi_boje)

        self.display_harmonic_index(min_rj)
        self.execute_coloring(Lista_boja)

    def display_harmonic_index(self, harmonic_index):
        info_window = tk.Toplevel(self.root)
        info_window.title("Harmonic Chromatic Index")
        label = tk.Label(
            info_window,
            text=f"Harmonic Chromatic Index: {harmonic_index}",
            font=("Arial", 14),
        )
        label.pack(pady=20)
        close_button = tk.Button(info_window, text="Close", command=info_window.destroy)
        close_button.pack(pady=10)

    def execute_coloring(self, color_assignment):
        colors = [
            "red",
            "green",
            "blue",
            "yellow",
            "purple",
            "orange",
            "pink",
            "cyan",
            "lime",
        ]

        for dot_id, color_idx in enumerate(color_assignment, start=1):
            color = colors[(color_idx - 1) % len(colors)]
            self.canvas.itemconfig(self.dot_objects[dot_id], fill=color)

    def generate_graph(self, connections, num_nodes):
        graph = [[] for _ in range(num_nodes)]
        for dot1, dot2 in connections:
            graph[dot1 - 1].append(dot2)
            graph[dot2 - 1].append(dot1)
        return graph

    def clear_canvas(self):
        self.canvas.delete("all")
        self.dots.clear()
        self.connections.clear()
        self.dot_objects.clear()


root = tk.Tk()
app = DotConnectorApp(root)
root.mainloop()
