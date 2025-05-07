import tkinter as tk
from tkinter import ttk
from gui import ChatManagerGUI

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatManagerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatManagerGUI(root)
    root.mainloop()

class ChatManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI 대화 관리자")
        self.root.geometry("1200x800")

        # 스타일 설정
        self.style = ttk.Style()
        self.style.configure("TButton", font=('맑은 고딕', 12))

        # PanedWindow 설정
        self.paned_window = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill="both", expand=True)

        # 왼쪽 프레임
        self.left_frame = ttk.Frame(self.paned_window, width=450, padding="15")
        self.paned_window.add(self.left_frame, weight=0)

        # 오른쪽 프레임
        self.right_frame = ttk.Frame(self.paned_window, padding="15")
        self.paned_window.add(self.right_frame, weight=1)

        # 기본 UI 구성
        self.create_ui()

    def create_ui(self):
        # 대화방 UI 구성
        ttk.Label(self.left_frame, text="대화방", font=('맑은 고딕', 14, 'bold')).pack(anchor="w")
        self.conversation_text = tk.Text(self.left_frame, wrap="word", state="disabled", font=('맑은 고딕', 12))
        self.conversation_text.pack(fill="both", expand=True)

        # 입력창 및 버튼
        input_frame = ttk.Frame(self.left_frame)
        input_frame.pack(fill="x", pady=(10, 0))

        self.input_entry = ttk.Entry(input_frame, font=('맑은 고딕', 12))
        self.input_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))

        self.send_button = ttk.Button(input_frame, text="전송", command=self.send_message)
        self.send_button.pack(side="left")

    def send_message(self):
        message = self.input_entry.get()
        if message:
            self.conversation_text.config(state="normal")
            self.conversation_text.insert("end", f"User: {message}\n")
            self.conversation_text.config(state="disabled")
            self.input_entry.delete(0, "end")
            pyperclip.copy(message)  # 입력된 메시지를 클립보드에 복사

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatManagerGUI(root)
    root.mainloop()