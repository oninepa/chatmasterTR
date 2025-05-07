import tkinter as tk
from tkinter import ttk
import pyperclip

class ChatManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI 대화 관리자")
        self.root.geometry("1200x800")
        self.setup_styles()
        self.create_main_layout()

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.configure("TButton", font=('맑은 고딕', 12))
        self.style.configure("TLabel", font=('맑은 고딕', 10))
        self.style.configure("TEntry", font=('맑은 고딕', 10))
        self.style.configure("TText", font=('맑은 고딕', 10))

    def create_main_layout(self):
        # PanedWindow 설정
        self.main_paned = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.main_paned.pack(fill="both", expand=True)

        # 왼쪽 프레임
        self.left_frame = ttk.Frame(self.main_paned, width=600, padding="10")
        self.main_paned.add(self.left_frame, weight=1)

        # 오른쪽 프레임
        self.right_paned = ttk.PanedWindow(self.main_paned, orient=tk.VERTICAL)
        self.main_paned.add(self.right_paned, weight=1)

        # 오른쪽 상단/하단 프레임
        self.right_top = ttk.Frame(self.right_paned, padding="10")
        self.right_middle = ttk.Frame(self.right_paned, padding="10")
        self.right_bottom = ttk.Frame(self.right_paned, padding="10")
        self.right_paned.add(self.right_top, weight=1)
        self.right_paned.add(self.right_middle, weight=1)
        self.right_paned.add(self.right_bottom, weight=1)

        # 기본 UI 구성
        self.create_left_panel()
        self.create_right_panel()

    def create_left_panel(self):
        # Notebook 생성
        self.notebook = ttk.Notebook(self.left_frame)
        self.notebook.pack(fill="both", expand=True)

        # 대화 탭
        self.chat_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.chat_frame, text="대화")

        # 설정 탭
        self.settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.settings_frame, text="설정")

        # 대화 탭 구성
        self.create_chat_tab()
        self.create_settings_tab()

    def create_chat_tab(self):
        # 저장소 및 AI 모델 선택
        select_frame = ttk.Frame(self.chat_frame)
        select_frame.pack(fill="x", pady=(0, 10))

        ttk.Label(select_frame, text="저장소 (대화 저장용):").pack(side="left")
        self.storage_combo = ttk.Combobox(select_frame, values=["Firebase", "Supabase", "MEGA"], width=15)
        self.storage_combo.pack(side="left", padx=5)
        self.storage_combo.set("Firebase")

        # 상태 표시등
        self.status_canvas = tk.Canvas(select_frame, width=15, height=15)
        self.status_canvas.pack(side="left", padx=5)
        self.status_canvas.create_oval(2, 2, 13, 13, fill="red")

        ttk.Label(select_frame, text="AI 모델:").pack(side="left", padx=(10, 0))
        self.ai_combo = ttk.Combobox(select_frame, values=["GPT-4", "DeepSeek", "Claude", "Baidu", "Grok"], width=15)
        self.ai_combo.pack(side="left", padx=5)
        self.ai_combo.set("GPT-4")

        # 대화방
        ttk.Label(self.chat_frame, text="대화방", font=('맑은 고딕', 12)).pack(anchor="w")
        self.conversation_text = tk.Text(self.chat_frame, wrap="word", height=20)
        self.conversation_text.pack(fill="both", expand=True, pady=(5, 10))

        # 입력창 및 전송 버튼
        input_frame = ttk.Frame(self.chat_frame)
        input_frame.pack(fill="x")
        
        self.input_entry = ttk.Entry(input_frame)
        self.input_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        self.send_button = ttk.Button(input_frame, text="전송")
        self.send_button.pack(side="right")

    def create_settings_tab(self):
        # AI 모델 설정 프레임
        ai_frame = ttk.LabelFrame(self.settings_frame, text="AI 모델 설정", padding=10)
        ai_frame.pack(fill="x", pady=5)

        # AI 모델 선택
        ttk.Label(ai_frame, text="AI 모델:").pack(anchor="w")
        self.ai_model_combo = ttk.Combobox(ai_frame, values=["GPT-4", "DeepSeek", "Claude", "Baidu", "Grok"], width=15)
        self.ai_model_combo.pack(anchor="w", pady=(0, 5))
        self.ai_model_combo.set("GPT-4")

        # API 키 입력
        ttk.Label(ai_frame, text="API Key:").pack(anchor="w")
        self.api_key_entry = ttk.Entry(ai_frame)
        self.api_key_entry.pack(fill="x", pady=(0, 5))

        # Secret Key 입력
        ttk.Label(ai_frame, text="Secret Key:").pack(anchor="w")
        self.secret_key_entry = ttk.Entry(ai_frame, show="*")
        self.secret_key_entry.pack(fill="x", pady=(0, 5))

        # 저장소 설정 프레임
        storage_frame = ttk.LabelFrame(self.settings_frame, text="저장소 설정", padding=10)
        storage_frame.pack(fill="x", pady=5)

        # 저장소 선택
        ttk.Label(storage_frame, text="저장소:").pack(anchor="w")
        self.storage_combo = ttk.Combobox(storage_frame, values=["Firebase", "Supabase", "MEGA"], width=15)
        self.storage_combo.pack(anchor="w", pady=(0, 5))
        self.storage_combo.set("Firebase")

        # 저장소 연결 정보 입력
        ttk.Label(storage_frame, text="연결 정보:").pack(anchor="w")
        self.storage_info_entry = ttk.Entry(storage_frame)
        self.storage_info_entry.pack(fill="x", pady=(0, 5))

    def create_right_panel(self):
        # 오른쪽 상단 패널에 버튼 추가
        ttk.Button(self.right_top, text="버튼 1", command=self.button1_click).pack(pady=5)
        ttk.Button(self.right_top, text="버튼 2", command=self.button2_click).pack(pady=5)

        # 오른쪽 중간 패널에 입력 필드 추가
        ttk.Label(self.right_middle, text="입력 필드:").pack()
        self.right_middle_entry = ttk.Entry(self.right_middle)
        self.right_middle_entry.pack(pady=5)

        # 오른쪽 하단 패널에 텍스트 박스 추가
        self.right_bottom_text = tk.Text(self.right_bottom, wrap="word", height=10)
        self.right_bottom_text.pack(fill="both", expand=True, pady=5)

    def button1_click(self):
        self.right_bottom_text.insert("end", "버튼 1 클릭\n")

    def button2_click(self):
        self.right_bottom_text.insert("end", "버튼 2 클릭\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatManagerGUI(root)
    root.mainloop()