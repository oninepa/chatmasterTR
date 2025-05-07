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
        self.paned_window = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill="both", expand=True)

        # 왼쪽 프레임
        self.left_frame = ttk.Frame(self.paned_window, width=450, padding="15")
        self.paned_window.add(self.left_frame, weight=0)

        # 오른쪽 프레임
        self.right_paned = ttk.PanedWindow(self.paned_window, orient=tk.VERTICAL)
        self.paned_window.add(self.right_paned, weight=1)

        # 오른쪽 상단/하단 프레임
        self.right_top = ttk.Frame(self.right_paned, padding="15")
        self.right_bottom = ttk.Frame(self.right_paned, padding="15")
        self.right_paned.add(self.right_top, weight=0)
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
        self.ai_combo = ttk.Combobox(select_frame, values=["GPT-4", "DeepSeek"], width=15)
        self.ai_combo.pack(side="left", padx=5)
        self.ai_combo.set("GPT-4")

        # 대화방
        ttk.Label(self.chat_frame, text="대화방", font=('맑은 고딕', 12)).pack(anchor="w")
        self.conversation_text = tk.Text(self.chat_frame, wrap="word", height=20)
        self.conversation_text.pack(fill="both", expand=True, pady=(5, 10))

        # 저장 준비 영역으로 보내기 버튼
        self.send_to_prep = ttk.Button(self.chat_frame, text="저장 준비 영역으로 보내기")
        self.send_to_prep.pack(fill="x", pady=(0, 10))

        # 입력창 및 전송 버튼
        input_frame = ttk.Frame(self.chat_frame)
        input_frame.pack(fill="x")
        
        self.input_entry = ttk.Entry(input_frame)
        self.input_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        self.send_button = ttk.Button(input_frame, text="전송")
        self.send_button.pack(side="right")

    def create_settings_tab(self):
        # Firebase 설정
        firebase_frame = ttk.LabelFrame(self.settings_frame, text="Firebase", padding=10)
        firebase_frame.pack(fill="x", pady=5)

        ttk.Label(firebase_frame, text="서비스 계정 키 파일 경로:").pack(anchor="w")
        ttk.Entry(firebase_frame).pack(fill="x", pady=(0, 5))
        ttk.Label(firebase_frame, text="데이터베이스 URL:").pack(anchor="w")
        ttk.Entry(firebase_frame).pack(fill="x", pady=(0, 5))
        ttk.Button(firebase_frame, text="Firebase 연결").pack(anchor="w")

        # Supabase 설정
        supabase_frame = ttk.LabelFrame(self.settings_frame, text="Supabase", padding=10)
        supabase_frame.pack(fill="x", pady=5)

        ttk.Label(supabase_frame, text="URL:").pack(anchor="w")
        ttk.Entry(supabase_frame).pack(fill="x", pady=(0, 5))
        ttk.Label(supabase_frame, text="Anon Key:").pack(anchor="w")
        ttk.Entry(supabase_frame).pack(fill="x", pady=(0, 5))
        ttk.Label(supabase_frame, text="Service Key:").pack(anchor="w")
        ttk.Entry(supabase_frame).pack(fill="x", pady=(0, 5))
        ttk.Button(supabase_frame, text="Supabase 연결").pack(anchor="w")

        # MEGA 설정
        mega_frame = ttk.LabelFrame(self.settings_frame, text="MEGA", padding=10)
        mega_frame.pack(fill="x", pady=5)

        ttk.Label(mega_frame, text="로그인 이메일:").pack(anchor="w")
        ttk.Entry(mega_frame).pack(fill="x", pady=(0, 5))
        ttk.Label(mega_frame, text="비밀번호:").pack(anchor="w")
        ttk.Entry(mega_frame, show="*").pack(fill="x", pady=(0, 5))
        ttk.Button(mega_frame, text="MEGA 연결").pack(anchor="w")

    def create_right_panel(self):
        # 오른쪽 패널의 크기와 간격 조정
        self.right_paned.pane(self.right_top, minsize=200, padx=10, pady=10)
        self.right_paned.pane(self.right_bottom, minsize=200, padx=10, pady=10)
                     # 새 대화 업로드 준비
        upload_frame = ttk.LabelFrame(self.right_top, text="1. 새 대화 업로드 준비", padding=10)
        upload_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        ttk.Label(upload_frame, text="주제:").pack(anchor="w", pady=(10, 5))
        self.topic_entry = ttk.Entry(upload_frame)
        self.topic_entry.pack(fill="x")

        self.save_prep_text = tk.Text(upload_frame, wrap="word", height=10)
        self.save_prep_text.pack(fill="both", expand=True, pady=10)

        ttk.Button(upload_frame, text="업로드 (저장소로)").pack(anchor="e")

        # 대화 검색 및 선택
        search_frame = ttk.LabelFrame(self.right_bottom, text="2. 대화 검색 및 선택", padding=10)
        search_frame.pack(fill="both", expand=True, padx=5, pady=5)

        search_controls = ttk.Frame(search_frame)
        search_controls.pack(fill="x", pady=(0, 10))

        ttk.Label(search_controls, text="저장소 선택:").pack(side="left")
        self.storage_select = ttk.Combobox(search_controls, values=["Firebase"], width=15)
        self.storage_select.pack(side="left", padx=5)
        self.storage_select.set("Firebase")

        ttk.Label(search_controls, text="키워드 검색:").pack(side="left", padx=(10, 0))
        self.keyword_entry = ttk.Entry(search_controls, width=20)
        self.keyword_entry.pack(side="left", padx=5)

        # 대화 목록 Treeview
        self.conversation_tree = ttk.Treeview(search_frame, columns=("date", "model", "topic"), show="headings")
        self.conversation_tree.heading("date", text="날짜")
        self.conversation_tree.heading("model", text="AI 모델")
        self.conversation_tree.heading("topic", text="주제/미리보기")
        self.conversation_tree.pack(fill="both", expand=True, pady=10)

        # 다운로드 대화 준비
        download_frame = ttk.LabelFrame(self.right_bottom, text="3. 다운로드 대화 준비", padding=10)
        download_frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.preview_text = tk.Text(download_frame, wrap="word", height=10)
        self.preview_text.pack(fill="both", expand=True, pady=10)

        # 하단 버튼들
        button_frame = ttk.Frame(download_frame)
        button_frame.pack(fill="x")

        ttk.Button(button_frame, text="업데이트 저장").pack(side="left", padx=2)
        ttk.Button(button_frame, text="복사하기").pack(side="left", padx=2)
        ttk.Button(button_frame, text="내보내기").pack(side="left", padx=2)
        ttk.Button(button_frame, text="대화에 삽입").pack(side="left", padx=2)